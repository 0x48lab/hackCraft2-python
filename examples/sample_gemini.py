from py2hackCraft.modules import Player
import time
import google.generativeai as genai

genai.configure(api_key='<API KEY>')

model = genai.GenerativeModel('gemini-pro')

def onPlayerChat(entity, data):
    response = model.generate_content(f"これ「${data.message}」を牛の言葉で返事してください。")
    entity.say(response.text)


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
