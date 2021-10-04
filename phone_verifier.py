import phonenumbers
from phonenumbers import geocoder

phone = input('Enter phone number in format of +551140028922: ')
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))
