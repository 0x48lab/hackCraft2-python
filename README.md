# py2hackCraft2

Python client library for hackCraft2

## 概要

py2hackCraft2は、hackCraft2にPythonから接続して命令を送るためのライブラリです。

hackCraft2はMinecraft Java Editionのサーバープラグインで、このプラグインを導入することで、Minecraft上でプログラミングが可能になります。hackCraft2の詳細については、[hackCraft2のダウンロードページ](https://github.com/yokmama/8x9Craft-download)をご参照ください。

Minecraftについての詳細は、インターネットで検索していただければと思います。

py2hackCraft2を使用することで、hackCraft2が導入されたMinecraftサーバーに対して、Pythonから直接命令を送ることができます。

## ドキュメント

詳細なAPIリファレンスと使用例は[ドキュメント](https://0x48lab.github.io/hackCraft2-python/)を参照してください。

## インストール方法

```bash
pip install py2hackCraft2
```

## 使用方法

```python
from py2hackCraft2.modules import Player, Volume, LocationFactory

# プレイヤーの接続
player = Player("your_name")
player.login("localhost", 25570)

# エンティティの取得と操作
entity = player.get_entity("entity_name")
entity.set_event_area(Volume.local(10, 10, 10, -10, -10, -10))

# その他の操作...
```

### セキュア(wss)接続（Colab / リモート）

Google Colab などから、HTTPS 公開トンネル（Cloudflare 等）越しに動いているサーバーへ接続する場合は `secure=True` を指定します。`port` を省略すると標準TLSポート(443)を使用します。

```python
# 公開サーバーへ wss 接続
player.login("your-tunnel.example.com", secure=True)

# 自己署名証明書や自前トンネルで証明書検証を無効化する場合（自己責任）
player.login("self-hosted.example.com", secure=True, verify_ssl=False)
```

ローカルサーバーへは従来どおり `player.login("localhost", 25570)` で接続できます（後方互換）。

## ライセンス

MIT License