from py2hackCraft.modules import Player
from py2hackCraft.material import Blocks


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

test.setItem(0, Blocks.STONE)
test.holdItem(0)

for i in range(5):
    test.place()
    test.up()
    test.forward()

player.logout()
