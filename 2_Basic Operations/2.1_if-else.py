# login program and indentation
# email -> meghadri@gmail.com
# password -> 1234

email = input('enter email')
password = input('enter password')

if email == 'meghadri@gmail.com' and password == '1234':
  print('Welcome')
elif email == 'meghadri@gmail.com' and password != '1234':
  # tell the user
  print('Incorrect password')
  password = input('enter password again')
  if password == '1234':
    print('Welcome,finally!')
  else:
    print('Fuck off hacker lol')
else:
  print('Not correct')
  
  
  


            