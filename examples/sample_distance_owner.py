from py2hackCraft.modules import Player
import time


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

try:
    while True:
        d = test.getDistanceTarget(player.uuid)
        print(d)
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
