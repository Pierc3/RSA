#while loop that controls the entire program goes here


##option to encrypt a message goes here
e = input("Please enter the e value (smallest co-prime number between your P and Q values):")
n = input("Please enter the n value (P * Q):")

message = input("Please enter the message you wish to encrypt:")
encrypted_message = ''
encrypted_message2 = ''


LUT_encryption = dict()
LUT_decryption = dict()

for x in message:
    if x in LUT_encryption:
        encrypted_message += LUT_encryption[x]

    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt)
        encrypted_message += denumerize
        LUT_encryption[x] = denumerize

print encrypted_message


##option to decrypt a message goes here

for t in encrypted_message:
  if x in LUT_encryption:
    encrypted_message == LUT_encryption[x]
  else: 
        numerize and [x]
        decrypt = pow(numerize, e, n)
        encrypted_message += denumerize
        LUT_encryption[x]

print encrypted_message2



##option to exit goes here
#encryption function goes here
#decryption function goes here
