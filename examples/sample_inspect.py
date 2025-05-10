from py2hackCraft.modules import Player


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

ret = hello.inspect_down()
hello.say(f"これは{ret.name}です。")

player.logout()
