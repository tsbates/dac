import whois
from twilio.rest import Client

# Twilio Configuration
# Enter your Twilio account details below. See https://www.twilio.com/console
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

# Enter your domain below
domain = 'DOMAINHERE'

def domain_lookup():
    try:
        w = whois.whois(domain)
        print("Checking domain: " + str(w.domain_name))
        print("Domain %s is registered!" % (domain))
        print("Checking expiration date on " + str(w.domain_name) + "...")
        print("Expiry date: " + str(w.expiration_date[0]))
    except:
        print("Domain %s is unregistered! Sending SMS" % (domain))
        message = client.messages \
        .create(
        body= domain + ' is not registered. Click the following link to register the domain: https://www.crazydomains.com.au/ ',
        # Enter your trial number below. See https://www.twilio.com/console for your trial number.
        from_='+XXXXXXXXXXX',
        # Enter your Verified Caller ID below. See https://www.twilio.com/console/phone-numbers/verified
        to='+XXXXXXXXXXX'
    )
 
if __name__ == '__main__':
    domain_lookup()
