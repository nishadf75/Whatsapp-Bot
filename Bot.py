# importing the library
import pywhatkit

#importing datetime to get current time
from datetime import datetime

# Getting Current time
now = datetime.now()
chour = now.strftime("%H")

'''
Getting the mobile number
Getting the message to be sent
Getting the hour at which msg must be delivered.
Getting the minue at which the message must be sent.
'''

mobile_num = input('Enter Mobile No of Receiver : ')
message_to_be_sent = input('Enter Message you wanna send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : '))

# sending the message.
pywhatkit.sendwhatmsg(mobile_num,message_to_be_sent,hour,minute)

#printing a short message on succesfully sending a message.
print('Message Delivered Succesfully...')
