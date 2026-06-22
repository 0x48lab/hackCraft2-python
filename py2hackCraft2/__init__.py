"""py2hackCraft2 は py2hackCraft のエイリアスパッケージ。

配布パッケージ名（pip install 名）が ``py2hackCraft2`` のため、
``import py2hackCraft2`` や ``from py2hackCraft2.modules import ...`` を
期待する利用者が多い。実体は :mod:`py2hackCraft` パッケージであり、
ここではそのサブモジュールを ``py2hackCraft2`` 名前空間へ転送して、
pip 名と import 名のどちらでも動作するようにする。
"""
import sys as _sys

import py2hackCraft.modules as _modules
import py2hackCraft.material as _material

# from py2hackCraft2.modules import ... / from py2hackCraft2.material import ... を可能にする
_sys.modules[__name__ + ".modules"] = _modules
_sys.modules[__name__ + ".material"] = _material

# import py2hackCraft2; py2hackCraft2.Player のようなトップレベル参照にも対応
from py2hackCraft.modules import *  # noqa: F401,F403,E402
