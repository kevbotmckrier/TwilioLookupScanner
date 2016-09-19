from twilio.rest.lookups import TwilioLookupsClient
from urllib.parse import quote
import requests

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = input("Account SID?")
auth_token  = input("Auth Token?")
addon = input("Addon? (leave blank for none)")

client = TwilioLookupsClient(account_sid, auth_token)

# Load the CSV file
CSVScanner = open("Input.csv", "r")

stack = []

for line in CSVScanner:
    if(line.startswith('+')):
        phoneNumber = line.rstrip()
    else:
        phoneNumber = str('+' + line).rstrip()
    #print(phoneNumber)
    try:
        if(addon):
            number = client.phone_numbers.get(quote(phoneNumber), include_carrier_info=True, addOns='whitepages_pro_caller_identity')
        else:
            number = requests.get('https://lookups.twilio.com/v1/PhoneNumbers/' + quote(phoneNumber) + '?Type=carrier&AddOns=' + addon, auth=(account_sid,auth_token)).json()
        
    except Exception as e:
        print("Error On Number: " + phoneNumber)
        print(e)

    try:
        print(number['add_ons']['results'])
        processedNumber = phoneNumber +"|"+ number['carrier']['type']  +"|"+ number['carrier']['name'] + "|" + str(number['add_ons'])
        print(processedNumber)
        stack.append(processedNumber)
    except Exception as e:
        print(e)
        # print("Error on Processing Number: " + phoneNumber)
        stack.append("Error on Processing Number: " + phoneNumber)

#With the stack finished write it to a new CSV
f = open('Output.txt', 'w')

for item in stack:
  f.write("%s\n" % item)

f.close()
