from py2hackCraft.modules import Player
import time
import json

def onMessage(entity, event):
    print("Message from %s: %s" % (event.sender, event.message))
    entity.say("I got your message!")

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

hello.set_on_message(onMessage)

hello.send_message("hello", "hello")   

quit = input("Press Enter to quit...")
player.logout()
