#import twilio
import apscheduler

from twilio.rest import Client
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import time
from apscheduler.schedulers.blocking import BlockingScheduler
# app = Flask(__name__)
# @app.route("/sms", methods=['GET', 'POST'])
# def sms_reply():
#     resp = MessagingResponse()
#     resp.message("The robots are coming? head for the hills")
#     return str(resp)
# if __name__ == "__main__":
#     app.run(debug=True)

account_sid = 'AC727c2031e9ee30abad130ffa8b993047'
auth_token = '42e746fc9e118181e55e7927f4dc6f45'
client = Client(account_sid, auth_token)


def send():
    count = 0
    while count <= 50:
        message = client.messages.create(
            # from_='whatsapp:+14155238886',
            # body='i just love coding',
            # to='whatsapp:+233275846911'
            from_='+12036337863',
            body='i just love coding',
            to='+233275846911'
        )
        print(message.sid)
        print(message.date_created)
        print(message.price)
        print(message.body)
        print(message.date_sent)
        print(message.feedback)
        print(message.fetch())
        print(message.TrafficType)
        print(message.status)
        time.sleep(0.1)
        count += 1
# 😂😂😂😂😂😂😂😂😂
send()


# Schedule job to be called every two hours
# try:
#     shed = BlockingScheduler()
#     shed.add_job(send, 'interval', seconds=2)
#     shed.start()
# except ConnectionError as e:
#     print("Please connect to the internet and try again: {}".format(e))

