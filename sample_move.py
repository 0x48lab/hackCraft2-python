from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")
al = player.getEntity("al")
hello = player.getEntity("hello")
aiueo = player.getEntity("aiueo")
for i in range(10):
    test.move(5.0)
    al.move(5.0)
    hello.move(5.0)
    aiueo.move(5.0)


player.logout()
