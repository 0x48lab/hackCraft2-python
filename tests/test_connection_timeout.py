"""接続確立タイムアウトの単体テスト（FR-005: 無限待機しない）。

実接続せず、connected が True にならない状況で _wait_for_connection が
短時間で ConnectionTimeoutError を送出することを検証する。
"""
import time

import pytest

from py2hackCraft.modules import _WebSocketClient, ConnectionTimeoutError


def test_wait_for_connection_times_out_when_never_connected():
    client = _WebSocketClient()
    client.url = "wss://unreachable.example.com:443/ws"
    # connected は False のまま（接続成立しないケース）
    start = time.monotonic()
    with pytest.raises(ConnectionTimeoutError):
        client._wait_for_connection(timeout=0.3)
    elapsed = time.monotonic() - start
    # 上限時間付近で速やかに失敗すること（無限待機しない）
    assert elapsed < 5


def test_wait_for_connection_returns_immediately_when_connected():
    client = _WebSocketClient()
    client.connected = True
    # 既に接続済みなら即座に戻る（例外なし）
    client._wait_for_connection(timeout=0.3)
