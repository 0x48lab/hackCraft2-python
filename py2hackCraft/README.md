## 概要

**py2hackCraft2**はhackCraft2にpythonから接続し命令をするためのライブラリです。  
hackCraft2がどういうものかについて、くわしくはhackCraft2のダウンロードページを参考していただくとして、  
簡単に説明をするとhackCraft2はMinecraft java editionのサーバープラグインです。  
このプラグインを導入すると、Minecraft上でプログラミングができるようになります。  
Minecraftについて何かについてくわしくはインターネットで検索をして調べてください。  
hackCraft2を導入されたMinecraftサーバーに**py2hackCraft2**をつかえばPythonから命令をすることができます。

次に、**py2hackCraft2**のインストール方法、それから利用方法を説明します。


## インストール方法

次のコマンドを実行して、プロジェクトをローカルマシンにセットアップします：

```bash
python3 -m pip install py2hackCraft2
```

## 利用方法

以下のコードはシンプルなコードで、ペットをその場でくるくる回らせるように命令するプログラムです。

```python
from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

for i in range(5):
    hello.forward()
    hello.turn_right()

player.logout()
```

