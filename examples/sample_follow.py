from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

while True:
    test.lookAtTarget(player.uuid)
    test.move(1.0)