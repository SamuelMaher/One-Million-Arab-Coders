from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC2b133fa711e34622d5b83921d915c4bb"
# Your Auth Token from twilio.com/console
auth_token  = "faa4904814ea98e13092b384ae4860ae"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="++201282255084", 
    from_="+14084264974",
    body="I Love You Mariomty so Much")

print(message.sid)
