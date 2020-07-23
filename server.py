from bot import chad_bot
import requests
import json
 
dog_url='https://dog.ceo/api/breeds/image/random'

update_id= None
bot = chad_bot()
def make_reply(msg):
    if msg == '/hi':
        reply= "hi there, I am a Bot created by Abhishek Singh(asrgabreo on gitHub , give a star if you like it) follow my creator on instragram @its.abhishek.asr"
    elif msg == '/doggo':
        r = requests.get(dog_url)
        json_parse = json.loads(r.text)
        reply= json_parse["message"]
        return reply
    elif msg == '/start' or '/help':
        reply = '''
        Hi!!! I am a bot created by Abhishek Singh ( github:https://github.com/asrgabreo ).
        Currently you can use following commands:
            - /help - list  all the commands.
            - /hi - A hello greeting.
            - /doggo - I will send you a random image of a dog with the breed type <3.
            '''

    else:
        reply= None
    return reply

while True:
    print ("...")
    updates=bot.get_updates(offset=update_id)
    updates= updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message= item["message"]["text"]
            except:
                message = None
            from_=item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply,from_)


