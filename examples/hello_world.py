from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.get_entity("hello")
test.say("こんにちは")

player.logout()
