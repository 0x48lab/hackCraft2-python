"""US2: 後方互換の回帰テスト。

既存の login(host, port)（非secure）が従来どおり ws:// URL を構築し、
sslopt が None（証明書設定の影響なし）であることを検証する。
"""
import json

import pytest

import py2hackCraft.modules as modules
from py2hackCraft.modules import Player


class _FakeWS:
    last_url = None
    last_sslopt = "UNSET"

    def __init__(self, url, on_message=None, on_error=None, on_close=None):
        _FakeWS.last_url = url
        self.url = url
        self.on_open = None
        self._on_message = on_message

    def run_forever(self, sslopt=None, **kwargs):
        _FakeWS.last_sslopt = sslopt
        if self.on_open:
            self.on_open(self)

    def send(self, message):
        self._on_message(self, json.dumps({
            "type": "logged",
            "data": {"playerUUID": "uuid-xyz", "world": "world"},
        }))

    def close(self):
        pass


@pytest.fixture
def patched(monkeypatch):
    _FakeWS.last_url = None
    _FakeWS.last_sslopt = "UNSET"
    monkeypatch.setattr(modules.websocket, "WebSocketApp", _FakeWS)

    def sync_run_forever(self):
        self.thread.start()
        self.thread.join()
    monkeypatch.setattr(modules._WebSocketClient, "_run_forever", sync_run_forever)
    return _FakeWS


def test_legacy_login_builds_plain_ws_url(patched):
    # 既存の呼び出し方法（位置引数 host, port）が従来どおり動作すること
    player = Player("tester")
    player.login("localhost", 25570)
    assert patched.last_url == "ws://localhost:25570/ws"
    # 非secure では sslopt は None（verify_ssl フラグの影響を受けない）
    assert patched.last_sslopt is None
    assert player.uuid == "uuid-xyz"
