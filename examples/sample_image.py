from py2hackCraft.modules import Player, LocationFactory
from PIL import Image

# 画像ファイルを開く
file = Image.open('creeper.png')

# 画像をRGBモードに変換
image = file.convert('RGB')


player = Player("your name")
player.login("localhost", 25570)

hello = player.get_entity("hello")

for y in range(image.height):
    for x in range(image.width):
        # 指定位置のピクセルのRGB値を取得
        rgb = image.getpixel((x, y))
        hex_color = "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])
        block = hello.get_block_by_color(hex_color)
        hello.place_at(LocationFactory.local(x, image.height-y + 1, 1), block.name)

player.logout()
