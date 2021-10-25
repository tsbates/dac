# dac
Domain Availability Checker (DAC) is a simple python script to confirm the availability of a domain name.

Uses twilio.com's free account API to send an SMS to a mobile number when a domain is available.

## Configuration/install
Enter your Twilio credentials (and source phone number) and populate the domain you want to lookup.

## Usage
> python dac.py
> 
> Checking domain: TSBATES.COM
> 
> Domain tsbates.com is registered!
> 
> Checking expiration date on TSBATES.COM...
> 
> Expiry date: 2026-08-16 14:15:29
