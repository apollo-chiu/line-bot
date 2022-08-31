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
    msg_in = event.message.text
    msg_reply = '尚未建立資料'

    if '順宏' in msg_in:
        msg_reply = '順宏交通有限公司,聯絡人:雪碧,電話:(02)2608-9268,地址:南勢倉_新北市林口區南勢村10鄰31之21號,太平倉_新北市林口區太平里6鄰10-10號'
    elif '瀚文' in msg_in:
        msg_reply = '瀚文紙(企)業股份有限公司,聯絡人:陳伊柔,電話:(02)2759-6116,地址:台北市信義區松德路171號20樓'

    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text))
        TextSendMessage(text=msg_reply))

if __name__ == "__main__":
    app.run()