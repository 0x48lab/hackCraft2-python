from dataclasses import dataclass
from py2hackCraft.modules import Player, Entity
import time
import random


def onInteractEvent(entity, event):
    if( event.event == "kill"):
        if( event.type == "pet" or event.type == "player"):
            entity.executeCommand(f"entity here {event.name} 17 73 -23")

player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("hello")
test.setOnInteractEvent(onInteractEvent)


quit = input("Press Enter to quit...")
player.logout()
