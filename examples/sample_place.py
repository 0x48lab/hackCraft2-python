from py2hackCraft.modules import Player

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

for i in range(5):
    hello.place()
    hello.back()

player.logout()
