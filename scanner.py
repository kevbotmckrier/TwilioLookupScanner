from twilio.rest.lookups import TwilioLookupsClient
from urllib.parse import quote

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = ""
auth_token  = ""
client = TwilioLookupsClient(account_sid, auth_token)

# Load the CSV file
CSVScanner = open("Your.file", "r")

stack = []

for line in CSVScanner:
    phoneNumber = str('+' + line).rstrip()
    #print(phoneNumber)
    try:
        number = client.phone_numbers.get(quote(phoneNumber), include_carrier_info=True)
    except:
        print("Error On Number: " + phoneNumber)
    #print(number.carrier['type'])
    #print(number.carrier['name'])

    try:
        processedNumber = phoneNumber +","+ number.carrier['type']  +","+ number.carrier['name']
        print(processedNumber)
        stack.append(processedNumber)
    except:
        print("Error on Processing Number: " + phoneNumber)
        stack.append("Error on Processing Number: " + phoneNumber)

#With the stack finished write it to a new CSV
f = open('Output.File', 'w')

for item in stack:
  f.write("%s\n" % item)

f.close()
