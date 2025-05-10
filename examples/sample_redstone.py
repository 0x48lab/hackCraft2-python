from py2hackCraft.modules import Player
import time

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

try:
    while True:
        hello.wait_for_redstone_change()    
        hello.up()
        hello.down()
        time.sleep(1)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
