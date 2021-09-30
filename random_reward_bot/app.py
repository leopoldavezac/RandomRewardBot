from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

from rewards import get_reward

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():

    in_msg_str = request.values.get('Body', '').lower()

    reward = get_reward(win_type_nm=in_msg_str)

    resp = MessagingResponse()
    resp_msg = resp.message()
    resp_msg.body(reward)
    
    return str(resp)


if __name__ == '__main__':
    app.run()