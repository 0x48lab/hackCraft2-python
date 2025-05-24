from dataclasses import dataclass
from py2hackCraft.modules import Player, Entity, LocationFactory, Location
import time
import random

@dataclass
class Area:
    min_x: int
    min_y: int
    min_z: int
    max_x: int
    max_y: int
    max_z: int    
    def is_within_bounds(self, x, y, z):
        return (self.min_x <= x <= self.max_x and
                self.min_y <= y <= self.max_y and
                self.min_z <= z <= self.max_z)

tnt_locations = []
stage = None

# 特定の座標がTNTであるかチェックする関数
def isTntLocation(x, y, z):
    return (x, y, z) in tnt_locations

def createStage(entity: Entity):
    global stage
    location = entity.get_location()
    stage = Area(location.x, location.y, location.z, location.x + 10, location.y, location.z + 10)
    #　蓋
    for x in range(10):
        for y in range(10):
            sx = location.x + x
            sy = location.y
            sz = location.z + y + 1
            # 砂を設置
            loc = LocationFactory.absolute(sx, sy, sz)
            entity.place_at(loc)
            # 1ブロック下にランダムで"TNT"または"stone"を配置
            block_choice = random.choice(["tnt", "stone"])  # ランダムにブロックを選択
            loc = LocationFactory.absolute(sx, sy - 1, sz)
            entity.place_at(loc)  # 選択したブロックを1ブロック下に配置
            if block_choice == "tnt":
                tnt_locations.append((sx, sy, sz))

def onInteractEvent(entity, event):    
    if event.type == "block":
        if not stage.is_within_bounds(event.x, event.y, event.z):
            return
        
        if event.action == "right_click":
            if event.name == "red_sand":
                loc = LocationFactory.absolute(event.x, event.y, event.z)
                entity.place_at(loc)  # 砂を設置
            else:    
                loc = LocationFactory.absolute(event.x, event.y, event.z)
                entity.place_at(loc)  # 赤砂を設置
        else:
            if isTntLocation(event.x, event.y, event.z):
                loc = LocationFactory.absolute(event.x, event.y, event.z)
                entity.dig_at(loc)  # ブロックを破壊
                entity.execute_command("title masafumi_t title {\"text\":\"ちゅっどーーーん！\",\"color\":\"red\"}")
                entity.execute_command(f"summon creeper {event.x} {event.y} {event.z} {{Fuse:0,ExplosionRadius:3}}")
            else:    
                loc = LocationFactory.absolute(event.x, event.y, event.z)
                entity.dig_at(loc)  # ブロックを破壊

player = Player("your name")
player.login("localhost", 25570)

test = player.get_entity("hello")
print(test)

test.say("ステージをつくるー")
createStage(test)

# イベントハンドラの設定は現在のAPIではサポートされていないため、コメントアウト
# test.setOnInteractEvent(onInteractEvent)
test.execute_command("title masafumi_t title {\"text\":\"ゲームスタート！\",\"color\":\"green\"}")

quit = input("Press Enter to quit...")
player.logout()
