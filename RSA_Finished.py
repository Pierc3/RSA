LUT_encryption = dict()
LUT_decryption = dict()
## Private Key
d = 9883
#while loop that controls the entire program goes here
program_on = True 
while program_on: 
  encrypted_message = ''
  option = input('Type "1" to encrypt a message, type "2" to decrypt:')
  if option == '1':
      ## encryption function goes here

      n = int(input('Please enter n value (P * Q):'))
      e = int(input('Please enter e value (smallest co-prime number between your P and Q values):'))
      message = input('Now enter the message you wish to encrypt:')
      for x in message:
          if x in LUT_encryption:
              encrypted_message += LUT_encryption[x]
      
          else:
              numerize = ord(x)
              encrypt = pow(numerize, e, n)
              denumerize = chr(encrypt)
              encrypted_message += denumerize
              LUT_encryption[x] = denumerize
      print ('Your message: ', encrypted_message)
  
  elif option == '2': 
    ## decryption function goes here
    decrypted_message = ''
    n = int(input('Please enter n value (P * Q):'))
    d = int(input('Please enter your decryption key:'))

    decrypt_message = input('Please enter the message you wish to decrypt:')
    
    for t in decrypt_message:
     if t in LUT_decryption:
      decrypted_message += LUT_encryption[t]
     else: 
          numerize = ord(t)
          decrypt = pow(numerize, d, n)
          denumerize = chr(decrypt)
          decrypted_message += denumerize
          LUT_encryption[t] = denumerize
          
    print ('Decrypted message: ', decrypted_message)
  
  ##option to exit goes here
  stop = input('Press "s" to stop, press "c" to continue')
  if stop == 's':
    program_on = False
    print ('Restart the program to use again')