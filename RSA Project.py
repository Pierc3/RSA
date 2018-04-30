#while loop that controls the entire program goes here


##option to encrypt a message goes here
n = input("Please enter the n value (P * Q):")
e = input("Please enter the e value (smallest co-prime number between your P and Q values):")

message = input("Please enter the message you wish to encrypt:")
encrypted_message = ''
encrypted_message2 = ''


LUT_encryption = dict()
LUT_decryption = dict()

##option to decrypt a message goes here
##option to exit goes here
stop = input("Please enter 'stop' to exit the program.")
for input in stop:
  if input in stop:
    exit()
  else:
    break
  
#encryption function goes here
for x in message:
    if x in LUT_encryption:
        encrypted_message += LUT_encryption[x]

    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt)
        encrypted_message += denumerize
        LUT_encryption[x] = denumerize

print('encrypted_message')

#decryption function goes here
for t in encrypted_message:
  if t in LUT_encryption:
    encrypted_message == LUT_encryption[t]
  else: 
        numerize and [t]
        decrypt = pow(numerize, e, n)
        encrypted_message += denumerize
        LUT_encryption[t]

print('encrypted_message2')