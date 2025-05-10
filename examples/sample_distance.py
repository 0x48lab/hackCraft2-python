from py2hackCraft.modules import Player
import time


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

try:
    while True:
        d = hello.get_distance()
        print(d)
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
