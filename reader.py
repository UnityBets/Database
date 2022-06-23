import urllib.request
print("Welcome to the UnityBets premeum member printer")
yesno=input("Want to showcase the premeum members? [Y/N]: ")
if yesno == "Y" or yesno == "y":
	print("Premeum members are {\n")
	page = urllib.request.urlopen('https://raw.githubusercontent.com/XPRSSN/test/main/1.dat')
	print(page.read())
	print("\n]\n")
	exit()
elif yesno == "N" or yesno == "n":
	print("Selected No.\nExiting")
else:
	print("Invalid answer.\nExiting")