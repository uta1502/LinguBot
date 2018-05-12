#!/usr/bin/env python

#Python libraries that we need to import for our bot
import random
from flask import Flask, request
from pymessenger.bot import Bot
import sys
import audio_to_text as a2t
from googletrans import Translator

app = Flask(__name__)
ACCESS_TOKEN = 'EAAU3ZCNLnRqIBAOEEZA1JZB550HYVAlhkGlBdxjajgwPFvZA8t4ZAqjKUxQ1Uxu5rqx3Ca57xQRLEilBNPeegWVB7VONE5nZBtDAkYlM2lBUpXmi2C6xO4UMBrDklccA5QqaukvvOIv54DWlEJUEvksPkapBefEJRMIwde5hQpoQZDZD'
VERIFY_TOKEN = 'chatTranslator'
bot = Bot(ACCESS_TOKEN)
PORT_NUM = int(sys.argv[1])
SRC_LANG = 'en'
DEST_LANG = 'el' # 'fr'

#We will receive messages that Facebook sends our bot at this endpoint 
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    print('Method: ' + str(request.method))
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook.""" 
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    #if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                msg = message.get('message')
                if msg:
                    #Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    print('The message received is: ')
                    print(msg)
                    if msg.get('text') == '&start-translate':
                        # set a flag in the database
                        # response_sent_text = get_message()
                        response_sent_text = 'Starting translation. All audio attachments\
                                                will now be converted from speech to text'
                        send_message(recipient_id, response_sent_text)
                    #if user sends us a GIF, photo,video, or any other non-text item
                    attachments = msg.get('attachments')
                    if attachments:
                        attch = attachments[0]
                        attch_type = attch.get('type')
                        if attch_type == 'audio':
                            url = attch['payload']['url']
                            response = a2t.convert_audio_from_url(url)
                            translator = Translator()
                            converted_response = \
                                translator.translate(response, dest=DEST_LANG, src=SRC_LANG)
                            send_message(recipient_id, converted_response.text)
    return "Message Processed"

def verify_fb_token(token_sent):
    #take token sent by facebook and verify it matches the verify token you sent
    #if they match, allow the request, else return an error 
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'
 
 
#chooses a random message to send to the user
def get_message():
    sample_responses = ["You are stunning!", "We're proud of you.", "Keep on being you!", "We're greatful to know you :)"]
    # return selected item to the user
    return random.choice(sample_responses)
 
#uses PyMessenger to send response to user
def send_message(recipient_id, response):
    #sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"
 
if __name__ == "__main__":
    app.run(port=PORT_NUM, use_reloader=True)
