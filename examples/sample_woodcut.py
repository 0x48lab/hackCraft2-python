from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

if(hello.is_blocked()):
    hello.harvest()
    hello.forward()
    while True:
        if(not hello.dig_up()):
            break
    hello.back()

player.logout()
