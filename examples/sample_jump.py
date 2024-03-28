from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

for i in range(10):
    test.jump()
    test.placeDown()

player.logout()
