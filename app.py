from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app =  Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"
@app.route("/sms", methods=['POST']) 

def sms_rly():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    If msg == "I love you ":
       Print ("I love you banggaru ")

    # Create reply
    resp = MessagingResponse()
    resp.message(msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
