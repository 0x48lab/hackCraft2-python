from py2hackCraft.modules import Player
import time

def onRedstoneChange(entity, data):
    entity.up()
    entity.down()
    print("example::onRedstoneChange %s %s" %(data.oldCurrent, data.newCurrent))

if __name__ == "__main__":
    player = Player("masafumi_t")
    player.login("localhost", 25570)

    test = player.getEntity("test")

    test.setOnRedstoneChange(onRedstoneChange)    

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Disconnecting...")

    player.logout()
