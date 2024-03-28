from py2hackCraft.modules import Player
import time

def onBlockBreak(player, block):
    print("example::onBlockBreak %s %d %d %d" %(block.name, block.x, block.y, block.z))

if __name__ == "__main__":
    player = Player("masafumi_t")
    player.login("localhost", 25570)

    test = player.getEntity("test")

    player.setOnBlockBreak(onBlockBreak)    

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Disconnecting...")

    player.logout()
