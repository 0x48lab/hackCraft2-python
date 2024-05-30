from dataclasses import dataclass
from py2hackCraft.modules import Player, Entity, Coordinates
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
    location = entity.getLocation()
    stage = Area(location.x, location.y, location.z, location.x + 10, location.y, location.z + 10)
    #　蓋
    for x in range(10):
        for y in range(10):
            sx = location.x + x
            sy = location.y
            sz = location.z + y + 1
            entity.setBlock(Coordinates.world, sx, sy, sz, "sand")
            # 1ブロック下にランダムで"TNT"または"stone"を配置
            block_choice = random.choice(["TNT", "stone"])  # ランダムにブロックを選択
            entity.setBlock(Coordinates.world, sx, sy - 1, sz, block_choice)  # 選択したブロックを1ブロック下に配置
            if block_choice == "TNT":
                tnt_locations.append((sx, sy, sz))

def onInteractEvent(entity, event):    
    if( event.type == "block"):
        if(stage.is_within_bounds(event.x, event.y, event.z) == False):
            return
        
        if( event.action == "right_click"):
            if(event.name == "red_sand"):
                entity.setBlock(Coordinates.world, event.x, event.y, event.z, "sand")
            else:    
                entity.setBlock(Coordinates.world,event.x, event.y, event.z, "red_sand")
        else:
            if(isTntLocation(event.x, event.y, event.z)):
                entity.setBlock(Coordinates.world,event.x, event.y, event.z, "air")
                entity.executeCommand("title masafumi_t title {\"text\":\"ちゅっどーーーん！\",\"color\":\"red\"}")
                entity.executeCommand(f"summon creeper {event.x} {event.x} {event.x} {{Fuse:0,ExplosionRadius:3}}")
                #entity.getWorld().createExplosion(block.x, block.y, block.z, 4.0)
            else:    
                entity.setBlock(Coordinates.world,event.x, event.y, event.z, "air")

player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("hello")
print(test)

test.say("ステージをつくるー")
createStage(test)

test.setOnInteractEvent(onInteractEvent)
test.executeCommand("title masafumi_t title {\"text\":\"ゲームスタート！\",\"color\":\"green\"}")

quit = input("Press Enter to quit...")
player.logout()
