"""US1: secure(wss) ログインの統合テスト。

実サーバーには接続せず、websocket.WebSocketApp と run_forever を monkeypatch して、
login(secure=True) が wss URL を構築し sslopt を run_forever に渡すことを検証する。
"""
import json
import ssl

import pytest

import py2hackCraft.modules as modules
from py2hackCraft.modules import Player


class _FakeWS:
    """WebSocketApp の差し替え。run_forever の sslopt を記録し、接続成立させる。"""

    last_url = None
    last_sslopt = "UNSET"

    def __init__(self, url, on_message=None, on_error=None, on_close=None):
        _FakeWS.last_url = url
        self.url = url
        self.on_open = None
        self._on_message = on_message

    def run_forever(self, sslopt=None, **kwargs):
        # connect() が functools.partial(run_forever, sslopt=...) で渡す sslopt を記録
        _FakeWS.last_sslopt = sslopt
        # 接続成立を通知（on_open → _WebSocketClient.connected = True）
        if self.on_open:
            self.on_open(self)

    def send(self, message):
        # login 送信に対して logged 応答を即返してフローを進める
        self._on_message(self, json.dumps({
            "type": "logged",
            "data": {"playerUUID": "uuid-123", "world": "world"},
        }))

    def close(self):
        pass


@pytest.fixture
def patched(monkeypatch):
    _FakeWS.last_url = None
    _FakeWS.last_sslopt = "UNSET"
    monkeypatch.setattr(modules.websocket, "WebSocketApp", _FakeWS)

    # スレッド起動を同期実行に置き換え（partial(run_forever, sslopt=...) をその場で実行）
    def sync_run_forever(self):
        self.thread.start()
        self.thread.join()
    monkeypatch.setattr(modules._WebSocketClient, "_run_forever", sync_run_forever)
    return _FakeWS


def test_secure_login_builds_wss_url_and_passes_sslopt(patched):
    player = Player("tester")
    player.login("example.com", secure=True)
    assert patched.last_url == "wss://example.com:443/ws"
    # verify_ssl 既定(True) → sslopt は None（既定検証）
    assert patched.last_sslopt is None
    assert player.uuid == "uuid-123"


def test_secure_login_verify_ssl_false_disables_cert_check(patched):
    player = Player("tester")
    player.login("example.com", secure=True, verify_ssl=False)
    assert patched.last_url == "wss://example.com:443/ws"
    assert patched.last_sslopt == {"cert_reqs": ssl.CERT_NONE}
