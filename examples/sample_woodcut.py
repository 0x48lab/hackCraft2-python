from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

if(test.isBlocked()):
    test.dig()
    test.forward()
    while True:
        if(not test.digUp()):
            break
    test.back()

player.logout()
