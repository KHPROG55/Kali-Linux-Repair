import os
def Edit_Sources_File():
	while True:
		os.system("clear")
		print("""
	1) Automatic
	2) Manual
	99) Back
		""")
		menu = input(">> ")
		if menu == "1":
			text= """deb http://http.kali.org/kali kali-rolling main contrib non-free
# For source package access, uncomment the following line
# deb-src http://http.kali.org/kali kali-rolling main contrib non-free"""
			file = open("/etc/apt/sources.list", "w")
			file.write(text)
			file.close
			print("Done, Thanks for using this tool, Enjoy :)")
			exit()
		elif menu == "2":
			select = input("Enter name of text editor (like leafpad or gedit or nano) : ")
			os.system(select + " /etc/apt/sources.list")
			print("Thanks for using this tool, Enjoy :)")
			exit()
		elif menu == "99":
			os.system("clear")
			main()
		else:
			continue
def Updating_System():
	while True:
		os.system("clear")
		print("""
	1) Update only
	2) Full Update (With upgrade)
	99) Back
		""")
		menu = input(">> ")
		if menu == "1":
			os.system("clear")
			os.system("apt-get update")
			exit()
		elif menu == "2":
			os.system("clear")
			os.system("apt-get update && apt-get -y full-upgrade")
			exit()
		elif menu == "99":
                        os.system("clear")
                        main()
		else:
			continue
def Fix_PGP_Error():
	key = input("Enter key here : ")
	os.system("apt-key adv --keyserver hkp://keys.gnupg.net --recv-keys " + key)
	print("Done, Thanks for using this tool, Enjoy :)")
	exit()
def VMware_Tools():
	os.system("apt -y install open-vm-tools-desktop fuse")
	Ask_Rebooting = input("Done, You need to reboot your system, reboot now? [y/n] ")
	if Ask_Rebooting == "y" or Ask_Rebooting == "yes" or Ask_Rebooting == "Y" or Ask_Rebooting == "Yes":
		os.system("reboot")
	else:
		print("Done, Thanks for using this tool, Enjoy :)")
		exit()
def Virtualbox_Tools():
	os.system("apt-get install -y virtualbox-guest-x11")
	Ask_Rebooting = input("Done, You need to reboot your system, reboot now? [y/n] ")
	if Ask_Rebooting == "y" or Ask_Rebooting == "yes" or Ask_Rebooting == "Y" or Ask_Rebooting == "Yes":
		os.system("reboot")
	else:
		print("Done, Thanks for using this tool, Enjoy :)")
		exit()
def main():
	while True:
		os.system("clear")
		print("""
	1) Edit sources.list
	2) Updating & Upgrading System
	3) Fix pgp error
	4) install VMware tools on kali (After Update)
	5) install Virtualbox tools on kali (After Update)
		""")
		menu = input(">> ")
		if menu == "1":
			Edit_Sources_File()
		elif menu == "2":
			Updating_System()
		elif menu == "3":
			Fix_PGP_Error()
		elif menu == "4":
			VMware_Tools()
		elif menu == "5":
			Virtualbox_Tools()
		else:
			continue
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("\nThanks for using this tools, Enjoy :)")
