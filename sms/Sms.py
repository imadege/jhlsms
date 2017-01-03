from twilio.rest import TwilioRestClient
from django.conf import settings

class SendMessage():
    """""
        Will use these class to send sms/ check status and queue sending sms
    """
    Gateways = ["twilio"]
    gateway = ""
    number = ""
    message = ""

    def __init__(self,gateway,number,message):
        self.number = number
        self.message = message
        if gateway not in self.Gateways:
            "Liase with Mosoti to handle expections"
            raise  ValueError("wrong in on sms Gateyway, Currently available are twilio")
        else:
            self.gateway = gateway


    def send(self):
        if self.gateway is "twilio":
            self.twilio_gateway()
            return "Yes we can send"
        else:
            raise ValueError("We cannot send Message now ")


    def twilio_gateway(self):
        """Handle twilio sms sending """
        account_sid = settings.TWILIO_SID
        account_token = settings.TWILIO_TOKEN
        client = TwilioRestClient(account_sid, account_token)
        client.messages.create(
            to = self.number,
            body = self.message,
            from_="+16178602872",
        )

    def tuma_gateway(self):
        return  True

    def queue_send(selfS):
        return  False