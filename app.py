# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('c+dELRTkGtydoP0rLSbMU33NH0Vh4p4HOzHa/Ea1L+zLmXNWpQbcNb+pZPSD8S1zvTvDGtGo3knIQWinAYd7//5EZFshYAd4Sg73Ehw87b1IbKxmfBocdRr7EZsxY/lXTCNeYZlK4rhdKZlTylA22QdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('97526a60450cd91e1a2d318ca6646fb9') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    #text = event.message.text #message from user
    if event.message.text == "mbim":
    	line_bot_api.reply_message(event.reply_token, TextSendMessage(text='opo?')) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
