import requests

sender = input("Selamat datang Artourist . . .\n")
bot_message=""
while bot_message != "keluar":
    message = input()
    print("mengirim pesan . . .")
    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"sender": sender, "message": message})
    print("Bot membalas, ", end=' ')
    for i in r.json():
        bot_message = i['text']
        print(bot_message)


# from PIL import Image
# from io import BytesIO

# bot_message = ""
# url = "https://blog.reservasi.com/wp-content/uploads/2016/09/candi-prambanan-reservasi.jpg"

# while bot_message != "bye":
#     message = input("ada yang bisa dibantu?\n")
#     print("mengirimkan pesan . . .")
#     r = requests.post('https://828f-182-2-36-215.ngrok.io/webhooks/rest/webhook', json={"sender": sender, "message": message})
#     response = requests.get(url)
#     img = Image.open(BytesIO(response.content))
#     print("Bot membalas, ", end=' ')
#     for i in r.json():
#         bot_message = i['text']
#         # print(f"{i['text']}")
#         print(bot_message)
