from distutils.util import split_quoted


spamWords = ['buy now','order now','subscribe now']

email = input('Enter your email:')
spam = False

if 'buy now' in email or 'order now' in email or 'subscribe now' in email:
    spam = True

print("Spam is", spam)