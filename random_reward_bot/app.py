from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():

    in_msg = request.values.get('Body', '')

    resp = MessagingResponse()
    out_msg = resp.message()
    out_msg.body(in_msg)
    
    return str(resp)


if __name__ == '__main__':
    app.run()