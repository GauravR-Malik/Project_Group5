# Question 1 for Python Project: Course PROG 101 @ Saras AI Institute
# Submitted by Group 5 (Gaurav R Malik and Lakshya Manchanda)

# Defining the empty dictionary to store user data and defining the attributes
user_data = {}
attributes = ['password','first_name','last_name', 'age']

# Defining the startup menu. This is displayed initially when the code is run.
print('Menu:')
print('1. Signup')
print('2. Sign-in')
print('3. Exit')
print('')
print('Choose an option (1,2 or 3):')
option = input()

# Defining the while loop to keep the application running
while(option != '3'):

    
    # Condition for Option 1: Signup
    if option == '1':
        
        print('Enter your email ID:')
        username = input()

        if (username in user_data.keys()):
            print('Email ID already exists. Please use a different one.')
            print('')
            print('Menu:')
            print('1. Signup with different email ID')
            print('2. Sign-in')
            print('3. Exit')
            print('')
            print('Choose an option (1,2 or 3):')
            option = input()
        
        else:
            data = []
            print('Enter your password:')  
            password = input()
            data.append(password)
            print('Enter your first name:')
            first_name = input()
            data.append(first_name)
            print('Enter your last name:')
            last_name = input()
            data.append(last_name)
            print('Enter your age:')
            age = input()
            data.append(age)
            user_data[username] = dict(zip(attributes,data))
            print('Registration Successful!')
            print('')

            print('Menu:')
            print('1. Back to Signup for new user')
            print('2. Sign-in')
            print('3. Exit')
            print('')
            print('Choose an option (1,2 or 3):')
            option = input()

    
    # Condition for Option 2: Sign-in
    if option == '2':
        print('Enter your email ID:')
        username = input()
        print('Enter your password:')
        password = input()

        if (username in user_data.keys() and password == user_data[username]['password']):
            print('Login Successful!')
            print('Welcome ' + user_data[username]['first_name'] + ' ' + user_data[username]['last_name'] + '!')
            print('')
            print('Press 3 to sign out and exit')
            print('Press 2 to sign in as different user')
            print('Press 1 to signup as a new user')
            option = input()

        else:
            print('Invalid email ID or password.')
            print('')
            print('Menu:')
            print('1. Signup as a new user')
            print('2. Sign-in for another attempt')
            print('3. Exit')
            print('')
            print('Choose an option (1,2 or 3):')
            option = input()
    
    else:
        valid = ['1','2','3']
        if option not in valid:
            print('The input seems to be invalid... Please check at your end and try again...')
    

# Condition for option 3: Exit
if option == '3':
    print('Exiting the application. Goodbye!')
    print('')
