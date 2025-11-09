クイックスタートガイド
===============

このガイドでは、py2hackCraftの基本的な使用方法を説明します。

基本的な使用方法
----------

サーバーに接続してエンティティと対話する簡単な例を示します：

.. code:: python
    :force:

    from py2hackCraft.modules import Player, Volume, LocationFactory

    # プレイヤーインスタンスを作成してサーバーに接続
    player = Player("your_name")
    player.login("localhost", 25570)

    # エンティティを取得してイベントエリアを設定
    entity = player.get_entity("entity_name")
    entity.set_event_area(Volume.local(10, 10, 10, -10, -10, -10))

    # 位置がイベントエリア内かどうかを確認
    loc = LocationFactory.local(0, 0, 0)
    is_in_area = entity.is_event_area(loc)
    print(f"イベントエリア内: {is_in_area}")

    # イベントを待機
    while True:
        message = entity.get_event_message()
        if message is not False:  # イベントがある場合
            print(f"イベントを受信: {message}")

    # 終了時にログアウト
    player.logout()

一般的な操作
---------------

移動と位置指定
~~~~~~~~~~~~~~~~~~~~

.. code:: python
    :force:

    # 前進
    entity.forward(5)  # 5ブロック前進

    # 回転
    entity.turn_left()  # 左に回転
    entity.turn_right()  # 右に回転
    entity.turn(90)  # 90度回転

    # 特定の座標にテレポート
    loc = LocationFactory.absolute(100, 64, -200)
    entity.teleport(loc)

ブロック操作
~~~~~~~~~~~~~~

.. code:: python
    :force:

    # ブロックを設置
    # 前方に設置
    entity.place()

    # 上方に設置
    entity.place_up()

    # 特定の位置に設置
    loc = LocationFactory.local(0, 5, 0)

    entity.place_at(loc)

    # ブロックを破壊
    # 前方のブロックを破壊
    entity.dig()

    # 上方のブロックを破壊
    entity.dig_up()

    # 特定の位置のブロックを破壊
    # 絶対座標(100, 64, -200)のブロックを壊す
    loc = LocationFactory.absolute(100, 64, -200)

    entity.dig_at(loc)

    # ブロックの調査
    # 前方のブロックを調査
    block = entity.inspect()

    print(f"ブロックの種類: {block.name}")

イベント処理
~~~~~~~~~~~~

.. code:: python
    :force:

    # イベントメッセージの送信
    entity.send_message("target_entity", "こんにちは！")

    # イベントメッセージの受信
    while True:
        message = entity.get_event_message()
        if message is not False:  # イベントがある場合
            print(f"イベントを受信: {message}")

より詳細な例とAPIリファレンスについては、:doc:`api_reference` セクションを参照してください。 