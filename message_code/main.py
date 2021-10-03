from twilio.rest import Client
import keys

client = Client(keys.account_sid , keys.auth_token)

message = client.messages.create(
    body="Hi This is Spandan",
    from_=keys.phone_number,
    to=keys.target_number
)
print(message.body)