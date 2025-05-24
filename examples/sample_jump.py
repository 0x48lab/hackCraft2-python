from py2hackCraft.modules import Player


player = Player("your name")
player.login("localhost", 25570)

hello = player.get_entity("hello")

for i in range(10):
    hello.add_force(0, 0.6, 0)
    hello.place_down()

player.logout()
