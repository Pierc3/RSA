#while loop that controls the entire program goes here


##option to encrypt a message goes here
e = raw_input("Please enter the E value (smallest co-prime number between your P and Q values):")
n = raw_input("Please enter the N value (P * Q):")
message = raw_input("Please enter the message you wish to encrypt:")
encrypted_message = ''

LUT_encryption = dict()
LUT_decryption = dict()

for x in message:
    if x in LUT_encryption:
        encrypted_message += LUT_encryption[x]
    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = unichr(encrypt)
        encrypted_message += denumerize
        LUT_encryption[x] = denumerize

print encrypted_message




##option to decrypt a message goes here
##option to exit goes here
#encryption function goes here
#decryption function goes here