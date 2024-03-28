from py2hackCraft.modules import Player
from openai import OpenAI
import time

# APIキーを設定
openai = OpenAI(api_key='your api token')

def onPlayerChat(entity, data):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "あなたはマイクラの世界に詳しい鶏です。鶏の言葉で返事してください。"},
            {"role": "user", "content": data.message},
        ]
    )
    text = response.choices[0].message.content.strip()
    entity.say(text)

if __name__ == "__main__":
    player = Player("masafumi_t")
    player.login("localhost", 25570)

    test = player.getEntity("test")

    test.setOnPlayerChat(onPlayerChat)
    try:
        test.say("なにか手伝えることはありますか？")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("Disconnecting...")

    player.logout()
