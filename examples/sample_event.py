from py2hackCraft.modules import Player, Volume, LocationFactory
import time
import json

try:
    player = Player("o2nerocha")
    player.login("localhost", 25570)

    test = player.get_entity("hello")
    test.set_event_area(Volume.local(10, 10, 10, -10, -10, -10))

    loc = LocationFactory.local(0, 0, 0)
    ret = test.is_event_area(loc)
    print(f"is_event_area ret: {ret}")

    print("イベントの待機を開始します（Ctrl+Cで終了）...")
    try:
        while True:
            try:
                value = test.get_event_message()
                if value is False:  # イベントがない場合
                    pass  # 何もしない
                else:  # イベントがある場合
                    print(f"イベントメッセージ: {value}")
            except Exception as e:
                print(f"イベントの処理中にエラーが発生: {e}")
            time.sleep(1)  # 1秒待機
            
    except KeyboardInterrupt:
        print("\n処理を終了します...")

except Exception as e:
    print(f"エラーが発生しました: {e}")
finally:
    player.logout()
