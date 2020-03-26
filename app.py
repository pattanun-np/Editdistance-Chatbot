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
from textprocessing import find_distance
app = Flask(__name__)

line_bot_api = LineBotApi('6ZiODgd7zsp3v9Pn4fYiLIPE6Zu+EeVUpUfgae3MyuFuDaPNVo3e7ZHLfzLnk68Zw0YRhSYVN8SybOo/DuVdEmAPaLbQaKoIdqNCrLXNIlzC9mylS1UgrBgvDdY0hMv1OAlSp4JX1osyotbWwE2i1AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f2337591beeb37fbec2c0ff9bca05801')


@app.route("/webhook", methods=['POST'])
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
    reply_msg = find_distance(event)
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_msg))


if __name__ == "__main__":
    app.run()