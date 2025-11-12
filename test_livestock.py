"""
Livestock APIのテストコード例
"""
from py2hackCraft.modules import Player

# プレイヤーでログイン
player = Player("masafumi_t")
player.login("localhost", 25570)

# ペットを取得
pet = player.get_entity("my_pet")

# 近くの牛を数える
cow_count = pet.livestock_count_nearby("COW", 50)
print(f"近くに{cow_count}頭の牛がいます")

# 最も近い牛を取得
nearest_cow = pet.livestock_get_nearest_uuid("COW", 50)
if nearest_cow:
    print(f"最も近い牛: {nearest_cow}")
    
    # 牛を誘導（ペットから前方10ブロック）
    pet.livestock_herd(nearest_cow, 10, 0, 0, "^", 1.0)
    print("牛を誘導しました")

# 近くの羊を全て探す
sheep_list = pet.livestock_find_nearby("SHEEP", 30)
print(f"{len(sheep_list)}頭の羊を見つけました")

for sheep in sheep_list:
    print(f"  - {sheep['animalType']}: 距離{sheep['distance']:.1f}m, 体力{sheep['health']}/{sheep['maxHealth']}")

# すべての牛を集める
herded = pet.livestock_herd_all_nearby("COW", 50, 0, 0, 10, "~", 1.5)
print(f"{herded}頭の牛を集めました")

player.logout()
