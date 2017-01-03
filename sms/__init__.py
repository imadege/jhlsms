from sms.Sms import SendMessage


def send(gateway,number,message):
    s = SendMessage(gateway,number,message)
    s.send()
    return True