encryptprogram = input("If you wish to Encrypt a message, press the 'e' key. If you wish to decrypt a message, press the 'd' key. ")
if encrypt == ('e'):
      encrypt()
elif decrypt == ('d'):
  decrypt()
  
else:
  stop()

#while loop that controls the entire program goes here
encryption_program = True 
while encryption_program:

  LUT_encryption = dict()
  LUT_decryption = dict()

#encryption function goes here
def encrypt():
  n = input("Please enter the n value (P * Q):")
  e = input("Please enter the e value (smallest co-prime number between your P and Q values):")
  message = input("Please enter the message you wish to encrypt:")
  encrypted_message = ''
  encrypted_message2 = ''
for x in message:
    if x in LUT_encryption:
        message = LUT_encryption[x]

    else:
        numerize = ord(x)
        encrypt = pow(numerize, e, n)
        denumerize = chr(encrypt)
        message += denumerize
        LUT_encryption[x] = denumerize

print('encrypted_message')

#decryption function goes here
encrypted_message2 = input("Please enter the message you wish to decrypt.")
def decrypt():
  for t in encrypted_message2:
    if t in LUT_encryption:
      encrypted_message2 += LUT_encryption[t]
    else: 
          numerize = ord(t)
          decrypt = pow(numerize, e, n)
          encrypted_message += denumerize
          LUT_encryption[t] = denumerize

print('encrypted_message2')

#option to exit goes here
def stop():
    stop = input("Press S to stop, press C to continue")
    if stop == ('S'):
      encryption_program = False