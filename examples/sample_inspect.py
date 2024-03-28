from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")

ret = test.inspectDown()
test.say(f"これは{ret.name}です。")

player.logout()
