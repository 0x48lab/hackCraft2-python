from py2hackCraft.modules import Player, Entity
from py2hackCraft.material import Items, Blocks

def plant(entity: Entity):
    block = entity.inspect_down()
    if block.name != Blocks.FARMLAND:
        entity.select_item(0)
        entity.use_item_down()
    entity.select_item(1)
    entity.use_item_down()


def farming(entity: Entity):
    block = entity.inspect()
    if block.name == Blocks.AIR:
        plant(entity)
    elif block.name == Blocks.WHEAT and block.data == 7:    
        entity.harvest()
        plant(entity)


player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")
hello.set_item(0, Items.DIAMOND_HOE)
hello.set_item(1, Blocks.WHEAT_SEEDS)

home = hello.get_location()
for x in range(5):
    hello.forward()
    farming(hello)
hello.teleport(home)    

player.logout()


