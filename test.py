from py2hackCraft.modules import Player, Entity, LocationFactory
player = Player("o2nerocha")
player.login("localhost", 25570)

hello = player.get_entity("hello")

hello.teleport(LocationFactory.absolute(276, 62, 92))

