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

line_bot_api = LineBotApi('Yn1Vel28yNntbD8R/4ysvB2CAW3FJtBUXjpOE+23Jas2ZwXJ4oj9PnjJBNte0niSK3j57AX+YNCCVNSW8ZmM0Bb2su1e5euye92ni05tt2ZFRA9idHPZG359tWKrO80dm06iY8kzRKV402rpWryMQwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('48e2ec7d5bc3ed10c23864d35ae0c144')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()