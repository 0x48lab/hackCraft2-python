# from py2hackCraft.modules import Player

import sys
import os

# ../py2hackCraft ディレクトリのパスを取得して追加
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
py2hackCraft_dir = os.path.join(parent_dir, 'py2hackCraft')
sys.path.append(py2hackCraft_dir)
from modules import Player, Location


player = Player("masafumi_t")
player.login("192.168.11.34", 25570)
hello = player.getEntity("hello")

array = [
    [1, 1, 1, 1, 1,],
    [1, 0, 0, 0, 1,],
    [0, 0, 0, 0, 1,],
    [1, 0, 0, 0, 1,],
    [1, 1, 1, 1, 1,],
]
 
# 壁
for h in range(3):
    for i in range(len(array)):
        for j in range(len(array[i])):
            # 各要素に対して処理を行う
            if(array[i][j] == 1):
                # hello.digX("^", i, h, j+1)
                hello.placeX("^", i, h, j+1, "cobblestone")
# 屋根                
for i in range(len(array)):
    for j in range(len(array[i])):
        # hello.digX("^", i, 3, j+1)
        hello.placeX("^", i, 3, j+1, "cobblestone")
# ドア
        
hello.placeX("^", 2, 0, 1, "oak_door")