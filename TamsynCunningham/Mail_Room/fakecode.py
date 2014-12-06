
def MailRoom():
	print "What would you like to do?"
	print "Please select an option"
	print "1: Make a Report"
	print "2: Send a Thank You"
	print "3: Exit"
	path = input("Select 1, 2, or 3")
	while path == 1:
		Reporter()
		continue
	while path == 2:
		Thanker():
		continue
	while path == 3:
		break

def Reporter():
	print {donor}{donation}
	#this should line up in coloumns

def Namer():
	Full_Name = raw_input("Please provide Donor name   ")
	while Full_Name == "exit":
		break
	while Full_Name == "list":
		print {donors}
		Full_Name = raw_input("Please provide Donor name  ")

	while Full_Name is not on {donors}:
		{donors}.ammend(Full_Name)
	Insert_Name = Full_Name
	#easier to call a new thing than keep returning 

def Donationer():
	Donation_Amount = raw_input("Please provide Donation Amount")
	while Donation_Amount != a float:
		print "Please enter a numeric value"
		Donation_Amount = raw_input("Please provide Donation Amount")
	{donation}.ammend(Donation_Amount)
	Donation_Insert = Donation_Amount

{donors} #list of donors
{donation} #dictionary key is donor name value is donation Amount

