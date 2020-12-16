from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app =  Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"
@app.route("/sms", methods=['POST'])

def mg():
    if msg == "I love you ":
        return "I love you too banggaru "
    else:
        return msg 

def sms_rly():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
  

    # Create reply
    resp = MessagingResponse()
    resp.message(mg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
