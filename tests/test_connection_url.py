"""build_ws_url / build_sslopt の純粋ロジック単体テスト（contracts/login-api.md 準拠）。

実 WebSocket 接続を行わず、URL と TLS オプションの組み立てのみを検証する。
"""
import ssl

from py2hackCraft.modules import build_ws_url, build_sslopt


class TestBuildWsUrl:
    def test_local_non_secure(self):
        assert build_ws_url("localhost", 25570, False) == "ws://localhost:25570/ws"

    def test_secure_default_tls_port(self):
        # secure かつ port 省略(None) → 標準TLSポート 443
        assert build_ws_url("example.com", None, True) == "wss://example.com:443/ws"

    def test_secure_custom_port(self):
        assert build_ws_url("example.com", 8443, True) == "wss://example.com:8443/ws"


class TestBuildSslopt:
    def test_non_secure_returns_none(self):
        assert build_sslopt(False, True) is None

    def test_secure_verify_returns_none(self):
        # 既定検証は websocket-client の既定挙動に委ねる → None
        assert build_sslopt(True, True) is None

    def test_secure_no_verify_disables_cert_check(self):
        assert build_sslopt(True, False) == {"cert_reqs": ssl.CERT_NONE}

    def test_non_secure_ignores_verify_flag(self):
        assert build_sslopt(False, False) is None
