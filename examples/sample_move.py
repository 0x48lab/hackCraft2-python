from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

for i in range(5):
    test.forward()
    test.turnRight()

player.logout()
