# print('Hello Rucha')
# print('o----')
# print(' ||||')
# print('*' * 10)

# patientName='John Smith'
# print(patientName[-3])
# age=20
# Is_new_patient=True
# print(patientName,age,patientName + ' is a new patient')

# Birthyear =input('Birth Year  : ')
# print(type(Birthyear))
# age= 2026 - int(Birthyear)
# print(type(age))
# print(age)

# weight_in_pounds=input('Weight in pounds : ')
# weight_in_kgs = int(weight_in_pounds) *0.45
# print(weight_in_kgs)

# firstname='Rucha'
# lastname='Marathe'

# msg=f'{firstname} {lastname} is a coder'
# print(msg.find('r'))
# print(msg.replace('Rucha', 'Pooja'))
# print('Marathe' in msg)
# print('Rucha' in msg)

# expected_balance = 5000
# actual_balance = 3200
# assert actual_balance == expected_balance
# print("Test Success")

# is_hot = False
# is_cold =False
# if is_hot:
#     print('Its a hot day') 
#     print('Drink plenty of water')
# elif is_cold:
#     print('Its a cold day')
#     print('Wear warm clothes')
# else:
#     print('Its a lovely day')

# is_price=1000000
# is_good_credit=False
# if is_good_credit:
#     down_payment=0.1*is_price
# else:  down_payment=0.2*is_price
# print(f'Down payment : ${down_payment}')

# weight= input('Enter your weight')
# unit= input('(L)bs or (K)kgs : ')
# if unit.upper() == 'L':
#     converted_weight = int(weight) * 0.45
#     print(f'You are {converted_weight} kgs')
# elif unit.upper() == 'K':
#     converted_weight = int(weight) / 0.45
#     print(f'You are {converted_weight} lbs')

command=""
while True:
    command = input('> ')
    if command.lower() == 'start':
        print('Car started...Ready to go!')
    elif command.lower() == 'stop':
        print('Car stopped.')
    elif command.lower() == 'help':
        print(""start - to start the car
stop - to stop the car""  )
else:   
         print('Sorry, I dont understand that')
        
    