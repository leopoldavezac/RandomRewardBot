from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():

    in_msg_str = request.values.get('Body', '')

    resp = MessagingResponse()
    resp_msg = resp.message()
    resp_msg.body(in_msg_str)
    
    return str(resp)


if __name__ == '__main__':
    app.run()