from py2hackCraft.modules import Player, Entity, LocationFactory
player = Player("o2nerocha")
player.login("localhost", 25570)

hello = player.get_entity("test")

recip = [3,3,3,
         -1,4,-1,
         -1,4,-1]

ret = hello.craft(recip, 2, 11)
print(ret)