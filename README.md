# TwilioLookupScanner

Batch processing file for Twilio Lookups, the script expects a single line CSV file of E164 numbers (+12122223344) style numbers which it will then look up against the Twilio Lookup service, exporting back the line type - Mobile, Landline and then Carrier  - Verizon, ATT etc. 

To run the script you need to input your AccountSid, AuthKey and location of the CSV File then run: 

python3 lookupScanner.py

