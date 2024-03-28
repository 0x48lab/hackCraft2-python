from py2hackCraft.modules import Player
import time

def onMessage(entity, event):
    print("Message from %s: %s" % (event.sender, event.message))
    entity.say("I got your message!")

if __name__ == "__main__":
    player = Player("masafumi_t")
    player.login("localhost", 25570)

    test = player.getEntity("test")

    test.setOnMessage(onMessage)

    test.sendMessage("dog", "hello")   

    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Disconnecting...")

    player.logout()
