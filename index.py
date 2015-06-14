import cherrypy
import smsbomber

class Site(object):
	@cherrypy.expose
	def index(self):
		return """
		<html>
			<head>
				<title>Home | SMS Bomber</title>
			</head>
			<body>
				<center>
					Welcome to robottom's SMS bomber!
					<br><br><br>
					<form method="post" action="spam">
						Email Username: <input type="text" name="emailUsername"><br>
						Email Password: <input type="password" name="emailPassword"><br>
						Target Number: <input type="text" name="targetNumber"><br>
						Target Carrier: <input type="text" name="targetCarrier"><br>
						Text To Spam: <input type="text" name="textToSpam"><br>
						Times To Spam: <input type="text" name="timesToSpam"><br><br>
						<button type="submit">SPAM!</button>
					</form>
				<center>
			</body>
		</html>
		"""

	@cherrypy.expose
	def spam(self, emailUsername, emailPassword, targetNumber, targetCarrier, textToSpam, timesToSpam):
		try:
			smsbomber.spam((emailUsername, emailPassword, targetNumber, targetCarrier, textToSpam, timesToSpam))
			return """
			<html>
				<head>
					<title>Spam Failed</title>
				</head>
				<body>
					<center>
						Successfully spammed {num} '{text}' {times} times!<br><br>
						<a href="index">Click here to go home.</a>
					</center>
				</body>
			</html>
			""".format(num=targetNumber, text=textToSpam, times=timesToSpam)
		except:
			return """
			<html>
				<head>
					<title>Spam Failed</title>
				</head>
				<body>
					<center>
						Spam attempt failed :(<br><br>
						<a href="index">Click here to go home.</a>
					</center>
				</body>
			</html>
			"""

if __name__ == "__main__":
	cherrypy.quickstart(Site())