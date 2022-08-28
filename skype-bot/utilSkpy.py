from time import time, ctime
from skpy import Skype, SkypeChats
import os
import random

email = os.environ['EMAIL']
password = os.environ['PASSWORD']
# print(email, password) # debugging only

# login usigng old SOAP
# sk = Skype(email, password)  # connect to Skype

# login using new live login for compartibility with manual login flows. Source: https://github.com/Terrance/SkPy/issues/65#issuecomment-683798844
sk = Skype()
sk.conn.liveLogin(email, password)

skc = SkypeChats(sk)

# Get group: "Totel - Deployment Logs"
myGroup = skc.chat("19:43fa5ab68e7448f185e03d35c68d95cb@thread.skype")


#
def getThought():
	return random.choice([
            "“The worst time is always the present.“ ~ Jean de La Fontaine",
            "“Don't be afraid of your worst times. If you learn from them, you'll look back on them as the best times.“ ~ Robert Kiyosaki",
            "“Sometimes life has a cruel sense of humor, giving you the thing you always wanted at the worst time possible.“ ~ Lisa Kleypas",
            "“It was the best of times, it was the worst of times.“ ~ Charles Dickens",
            "“The worst happens when you least expect it.” ― Dean Koontz"
	])


COMMON_MESSAGE = "=== BUILD NOTIFICATION ===\n"

current_DateTime = time()
print('\nToday is: ', ctime(current_DateTime))


def buildStarted():
	with open("./images/start1.gif", "rb") as f:
		myGroup.sendFile(f, "myFile.gif", image=True)
	myGroup.sendMsg(COMMON_MESSAGE)
	myGroup.sendMsg("Build started..")


def buildSuccessful():
	with open("./images/success1.gif", "rb") as f:
		myGroup.sendFile(f, "myFile.gif", image=True)
	myGroup.sendMsg(COMMON_MESSAGE)
	myGroup.sendMsg(
            "Build SUCCESSFULLY DEPLOYED. Deployed at: https://totel.herokuapp.com/")


def buildFailed():
	with open("./images/failure1.gif", "rb") as f:
		myGroup.sendFile(f, "myFile.gif", image=True)
	myGroup.sendMsg(COMMON_MESSAGE)
	myGroup.sendMsg("Ooops.. build failed.")
	myGroup.sendMsg(getThought())
