import smtplib

def query():
	username = input("Gmail Username: ")
	password = input("Gmail Password: ")
	number = input("Target Phone Number: ")
	carrier = input("Target Phone Carrier: ")
	text = input("Text to Spam: ")
	times = int(input("Times to Spam: "))
	return (username, password, number, carrier, text, times)

def generateEmail(number, carrier):
	gateways = {"alltel": "@text.wireless.alltel.com", "att": "@txt.att.net", "boost": "@myboostmobile.com", "cricket": "@sms.mycricket.com", "sprint": "@messaging.sprintpcs.com", "tmobile": "@tmomail.net", "usc": "@email.uscc.net", "verizon": "@vtext.com", "virgin": "@vmobl.com"}
	carrier = carrier.lower()
	if(carrier == "at&t"):
		carrier = "att"
	if(carrier == "boostmobile" or carrier == "boost mobile"):
		carrier = "boost"
	if(carrier == "t-mobile"):
		carrier = "tmobile"
	if(carrier == "us cellular" or carrier == "uscellular"):
		carrier = "usc"
	if(carrier == "virgin mobile"):
		carrier = "virgin"
	if(carrier not in gateways.keys() and "@" not in carrier):
		raise KeyError("Carrier not found.")
	else:
		return "{num}{carrier}".format(num=number, carrier=gateways[carrier])

def spam(info):
	try:
		username, password, number, carrier, text, times = info
		email = smtplib.SMTP("smtp.gmail.com", 587)
		email.ehlo()
		email.starttls()
		email.login(username, password)
		for time in range(times):
			email.sendmail(text, generateEmail(number, carrier), text)
		email.quit()
		print("'{text}' was successfully sent to {number} {times} times!".format(text=text, number=number, times=times))
	except KeyError:
		print("Carrier not found. Try again.")

if __name__ == "__main__":
	spam(query())