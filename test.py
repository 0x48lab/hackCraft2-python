from py2hackCraft.modules import Player, Entity, Coordinates
player = Player("masafumi_t")
player.login("92.203.228.101", 25570)

hello = player.getEntity("hello")

while True:
    block = hello.findNearbyBlockX(0, 0, 0, "^", "water:0", 10)
    print(block)
    if block is None:
        break
    hello.placeX(block.x, block.y, block.z, "")

