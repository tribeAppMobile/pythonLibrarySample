from AccountManager import AccountManager
import getpass

ADM_USER = 'admin'
ADM_PWD = '123456'

# Init account and load from file if any
# Filename is 'accounts'
accountManager = AccountManager('accounts')
accountManager.loadAccount()

# User Menu
user_menu = '\n1. Add Account\n2. Edit Account\n3. Delete Account\n4. Account List\n5. Quit'

username = input('Username: ')
password = getpass.getpass()

# Check if the user is Administrator
choice = 0
if (username.lower() == ADM_USER and password == ADM_PWD):
	# Yes, he is administrator		
	while (choice != '5'):
		print(user_menu)
		choice = input('Input menu selection [1-5]: ')
		if (choice == '1'):
			# Add Account
			new_username = input('New username: ')
			new_password = getpass.getpass()
			fullName = input('Full Name: ')
			accountManager.addAccount(new_username, new_password, fullName)
			# Save the changes to file
			accountManager.saveAccount()
		elif (choice == '2'):
			# Edit account
			edit_username = input('Edit username: ')
			edit_password = getpass.getpass('Password [Press Enter to skip]: ')
			edit_name = input('Edit Name [Press Enter to skip]: ')
			if (accountManager.editAccount(edit_username, edit_password, edit_name)):
				print('Saved successfully')
				accountManager.saveAccount()
			else:
				print('Invalid username')
		elif (choice == '3'):
			# Delete account
			delete_username = input('Delete username: ')
			if (accountManager.deleteAccount(delete_username)):
				print('Account removed.')
				accountManager.saveAccount()
			else:
				print('Invalid username')

		elif (choice == '4'):
			# Print account list
			accountManager.printAccount()
# check in AccountManager for this username/password
else:
	account = accountManager.authenticate(username, password)
	if (account == None):
		print('Invalid username/password')
	else:
		print('Welcome to Library.')