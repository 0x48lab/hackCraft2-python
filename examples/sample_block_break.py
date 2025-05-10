from py2hackCraft.modules import Player, Block
import time

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

try:
    while True:
        block = hello.wait_for_block_break()    
        print("example::onBlockBreak %s %d %d %d" %(block.name, block.x, block.y, block.z))
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
