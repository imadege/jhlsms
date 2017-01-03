from sms.Sms import SendMessage


def send(gateway,number,message):
    s = SendMessage(gateway,number,message)
    return True