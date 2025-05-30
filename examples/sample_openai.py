from py2hackCraft.modules import Player
from openai import OpenAI
import time

# APIキーを設定
openai = OpenAI(api_key='your api token')

player = Player("your name")
player.login("localhost", 25570)

hello = player.get_entity("hello")
try:
    while True:
        hello.say("なにか手伝えることはありますか？")
        chat = hello.wait_for_player_chat()
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "あなたはマイクラの世界に詳しい鶏です。鶏の言葉で返事してください。"},
                {"role": "user", "content": chat.message},
            ]
        )
        text = response.choices[0].message.content.strip()
        hello.say(text)

except KeyboardInterrupt:
    print("Disconnecting...")

player.logout()
