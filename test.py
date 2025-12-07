from py2hackCraft.modules import *
player = Player("o2nerocha")
player.login("localhost", 25570)

hello = player.get_entity("練習生５")

ret = hello.write_sign(["Line 1", "Line 2", "Line 3", "Line 4"])
print(ret)
ret = hello.read_sign()
print(ret)