from py2hackCraft.modules import Player
from PIL import Image

# 画像ファイルを開く
file = Image.open('creeper.png')

# 画像をRGBモードに変換
image = file.convert('RGB')


player = Player("masafumi_t")
player.login("localhost", 25570)

test = player.getEntity("test")
world = test.getWorld()
location = test.getLocation()

for y in range(image.height):
    for x in range(image.width):
        # 指定位置のピクセルのRGB値を取得
        rgb = image.getpixel((x, y))
        hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        px = location.x + x
        py = location.y + (image.height-y + 1)
        pz = location.z + 1
        block = world.getBlockByColor(hex_color)
        world.setBlock(px, py, pz, block.name)
