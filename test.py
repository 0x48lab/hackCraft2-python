from py2hackCraft.modules import Player, Entity, Coordinates
player = Player("o2nerocha")
player.login("localhost", 25570)

hello = player.getEntity("maiko")

hello.digX(0, 0, 5)

