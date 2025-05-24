from py2hackCraft.modules import Player


player = Player("your name")
player.login("localhost", 25570)

hello = player.get_entity("hello")

for i in range(5):
    hello.forward()
    hello.turn_right()

player.logout()
