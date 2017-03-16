from twilio.rest import TwilioRestClient
from django.conf import settings

#from AfricasTalkingGateway import AfricasTalkingGateway, AfricasTalkingGatewayException
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)

import  requests

class SendMessage():
    """""
        Will use these class to send sms/ check status and queue sending sms
    """
    Gateways = ["twilio","africastalking","mtech"]
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
        elif self.gateway is "africastalking":
            self.africas_talking_gateway()
            #raise ValueError("Not Supported")
        elif self.gateway is "mtech":
            self.mtech_gateway()
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

    def africas_talking_gateway(self):
        """Handle smss sending for africa"""
        africa_talking_username = settings.AFRICA_TALKING_USERNAME
        afirca_talking_apiky = settings.AFRICA_TALKING_APIKEY
        to = "+254724454978"
        message = self.message
        gateway = AfricasTalkingGateway(africa_talking_username,afirca_talking_apiky)
        try:
            # Thats it, hit send and we'll take care of the rest.
            results = gateway.sendMessage(to, message)
        except AfricasTalkingGatewayException as e:
            print ('Encountered an error while sending: %s' % str(e))



    """mtech ssms"""
    def mtech_gateway(self):
        user = settings.MTECH_USER
        password = settings.MTECH_PASS
        code = settings.MTECH_SHORT_CODE
        payload = {'user':user, 'pass': 'password','shortCode':code,'MSISDN':self.number,'MESSAGE':self.message}
        r = requests.get('http://ke.mtechcomm.com/bulkAPIV2/', params = payload)
        return r


    def tuma_gateway(self):
        return  True

    def queue_send(selfS):
        return  False