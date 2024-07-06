# from py2hackCraft.modules import Player

import sys
import os

# ../py2hackCraft ディレクトリのパスを取得して追加
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
py2hackCraft_dir = os.path.join(parent_dir, 'py2hackCraft')
sys.path.append(py2hackCraft_dir)
from modules import Player

player = Player("masafumi_t")
player.login("92.203.228.101", 25570)
hello = player.getEntity("hello")


while True:
    ret = hello.digUp()
    if(ret != True):
        break
