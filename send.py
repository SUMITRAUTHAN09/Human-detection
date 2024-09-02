from twilio.rest import Client

account_sid = 'AC8e6e948d69f4054f3bc93987a0b52fca'
auth_token = '4c4e25bc4243c0fb620c5cd3bd6c4cf2'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+17178975175',
  body='alert !',
  to='+918864854298'
)
def sendSms():
  print("someone is there!")
