from configparser import ConfigParser

import logging
logging.basicConfig(filename="banklog.log",format='%(asctime)s %(message)s',filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info('Creating a config parser object')
config=ConfigParser()
logger.info('Read the account details file')
parser=config.read("account.ini")
logger.info('Ask choice from the user')
ch=int(input("Enter the choice\n1-Generate new account\n2-Update existing account details\n3-Update a transaction for a customer\n"))

if(ch==1):
	logger.info('Choice is 1, so generating new account')
	iname=input("Enter the name of account holder:")
	iadd=input("Enter the address of the account holder:")
	iphn=input("Enter the phone number:")
	idob=input("Enter the DOB:")
	idep=input("Enter the amount to be deposited:")
	accnum=str(int(config.sections()[-1])+1)
	config.add_section(accnum)
	config.set(accnum,"Name",iname)
	config.set(accnum,"Address",iadd)
	config.set(accnum,"Phone",iphn)
	config.set(accnum,"DOB",idob)
	config.set(accnum,"Balance",idep)
	with open('account.ini','w') as f:
		config.write(f)
	logger.info('New account added')
	print("Account number is:",accnum)
elif(ch==2):
	logger.info('Choice is 2, so updating customer details')
	macc=input("Enter the account number to be updated with new details:")
	ch1=int(input("Enter the section to be updated\n1-Name\n2-Address\n3-Phone\n4-DOB\n"))
	if(ch1==1):
		print(config.get(macc,"Name"))
		newchg=input("Enter the modified input:")
		config.set(macc,"Name",newchg)
		with open('account.ini','w') as f:
			config.write(f)
		logger.info('Updated the name of account')
	elif(ch1==2):
		print(config.get(macc,"Address"))
		newchg=input("Enter the modified input:")
		config.set(macc,"Address",newchg)
		with open('account.ini','w') as f:
			config.write(f)
		logger.info('Updated the address of account')
	elif(ch1==3):
		print(config.get(macc,"Phone"))
		newchg=input("Enter the modified input:")
		config.set(macc,"Phone",newchg)
		with open('account.ini','w') as f:
			config.write(f)
		logger.info('Updated the Phone of account')
	elif(ch1==4):
		print(config.get(macc,"DOB"))
		newchg=input("Enter the modified input:")
		config.set(macc,"DOB",newchg)
		with open('account.ini','w') as f:
			config.write(f)
		logger.info('Updated the DOB of account')
	else:
		print("Enter the right option")
		logger.info('User failed entering the correct value')
elif(ch==3):
	logger.info('Selected transaction updation')
	macc=input("Enter the account number for updating transaction details:")
	amt=int(input("Enter the amount:"))
	ch2=int(input("Enter 1-Debit or 2-Credit:"))
	if(ch2==1):
		bal=config.get(macc,"Balance")
		amt=str(int(bal)-amt)
		config.set(macc,"Balance",amt)
		with open('account.ini','w') as f:
			config.write(f)

		print("Updated balance is:",config.get(macc,"Balance"))
	if(ch2==2):
		print(config.get(macc,"Balance"))
		amt=str(int(bal)+amt)
		config.set(macc,"Balance",amt)
		with open('account.ini','w') as f:
			config.write(f)

		print("Updated balance is:",config.get(macc,"Balance"))
else:
	print("Enter the right choice")

	
