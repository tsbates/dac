import whois
import traceback
from twilio.rest import Client

# Twilio Configuration
# Enter your Twilio account details below. See https://www.twilio.com/console
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'edxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

# Enter your domain below
domain = 'example.com'

def domain_lookup():
    w = whois.whois(domain)
    print("Checking domain: " + str(w.domain_name[0]))
    print("Expiry date: " + str(w.expiration_date))
    
try:
    domain_lookup()
except:
    print('Domain is unregistered. Sending SMS')
    message = client.messages \
        .create(
        body= domain + ' is not registered. Click the following link to register the domain: https://www.crazydomains.com.au/ ',
        # Enter your trial number below. See https://www.twilio.com/console for your trial number.
        from_='+16xxxxxxxxx',
        # Enter your Verified Caller ID below. See https://www.twilio.com/console/phone-numbers/verified
        to='+61xxxxxxxxx'
    )
