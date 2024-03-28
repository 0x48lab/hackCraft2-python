from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

ret = test.getLocation()
test.forward()
test.forward()
test.teleport(ret.x, ret.y, ret.z)

player.logout()
