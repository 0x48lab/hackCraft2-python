from py2hackCraft.modules import Player
import time
import math

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

try:
    while True:
        # プレイヤーとの距離を取得
        distance = hello.get_distance_target(player.uuid)
        if distance > 0:
            # プレイヤーの方向を向く（簡易的な実装）
            # 南(0度)を向いてから、プレイヤーの方向に応じて回転
            hello.facing(0)  # 南を向く
            hello.add_force(0, 0, 0.3)  # 前方に移動
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()