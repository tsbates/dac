import whois
import traceback

def domain_lookup():
    input = raw_input("Enter a domain: ")
    w = whois.whois(input)
    print("Checking domain: " + str(w.domain_name))
    print("Expiry date: " + str(w.expiration_date)) # This prints Expiry date: [datetime.datetime(2021, 8, 16, 14, 15, 29)
    print(w.expiration_date[0]) # This prints 2021-08-16 14:15:29
    
try:
    domain_lookup()
except:
    print("Domain is not registered!")
