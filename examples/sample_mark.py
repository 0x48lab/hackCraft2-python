from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

ret = hello.get_location()
hello.forward()
hello.forward()
hello.teleport(ret)

player.logout()
