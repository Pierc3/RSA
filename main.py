
decrypted_message = ''

LUT_encryption = dict()
LUT_decryption = dict()

#while loop that controls the entire program goes here
program_on = True 
while program_on: 


  option = input('Type "1" to encrypt a message, type "2" to decrypt:')
  if option == '1':
      ## encryption function goes here
      encrypted_message = ''
      n = int(input('Please enter n value (P * Q):'))
      e = int(input('Please enter e value (smallest co-prime number between your P and Q values):'))
      message = input('Now enter the message you wish to encrypt:')
      for x in message:
          if x in LUT_encryption:
              message = LUT_encryption[x]
      
          else:
              numerize = ord(x)
              encrypt = pow(numerize, e, n)
              denumerize = chr(encrypt)
              message += str(numerize)
              LUT_encryption[x] = numerize
      print ('Your message: ', encrypted_message)


  elif option == '2': 
    ## decryption function goes here
    d = int(input('Please enter d value:'))
    n = int(input('Please enter n value (P * Q):'))
    decrypt_message = input('Please enter the message you wish to decrypt:')
    
    for t in encrypted_message:
     if t in LUT_encryption:
      decrypted_message == LUT_encryption[t]

     else: 
          numerize and [t]
          decrypt = pow(numerize, e, n)
          encrypted_message += denumerize
          LUT_encryption[t]
    print ('Decrypted message: ',decrypted_message)
  
  ##option to exit goes here
  stop = input('Press "s" to stop, press "c" to continue')
  if stop == 's':
    program_on = False
    print ('Restart the program to use again')
  