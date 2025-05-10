from py2hackCraft.modules import Player, Inventory

def bubbleSort(chest: Inventory):
    n = chest.size
    # 配列の全要素をチェック
    for i in range(n-1):
        # 最後尾の要素から順にチェック
        for j in range(0, n-i-1):
            # 隣接要素を比較し、順序が逆なら交換
            item1 = chest.get_item(j)
            item2 = chest.get_item(j+1)
            if item1.amount < item2.amount:
                chest.swap_items(j+1, j)

player = Player("masafumi_t")
player.login("localhost", 25570)

hello = player.get_entity("hello")

chest = hello.open_inventory(0,0,1)
bubbleSort(chest)

player.logout()
