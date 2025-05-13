from py2hackCraft.modules import Player

def transfer_items(chest):
    """
    チェストとプレイヤーのインベントリ間でアイテムを移動するサンプル
    
    Args:
        chest: 開いているチェストのインベントリオブジェクト
    """
    try:
        # チェストから自分のインベントリにアイテムを取り出す
        # チェストのスロット0のアイテムを自分のスロット5に取り出す
        print("チェストからアイテムを取り出します...")
        chest.retrieve_from_self(0, 5)
        
        # 自分のインベントリからチェストにアイテムを格納する
        # 自分のスロット0のアイテムをチェストのスロット5に格納
        print("チェストにアイテムを格納します...")
        chest.store_to_self(0, 5)
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")

def main():
    try:
        player = Player("masafumi_t")
        player.login("localhost", 25570)

        hello = player.get_entity("hello")

        # チェストを開く（座標は適宜調整してください）
        print("チェストを開きます...")
        chest = hello.open_inventory(0, 0, 1)

        # アイテムの移動を実行
        transfer_items(chest)

    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        player.logout()

if __name__ == "__main__":
    main() 