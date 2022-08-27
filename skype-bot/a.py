import os
email = os.environ['EMAIL']
password = os.environ['PASSWORD']
# print(email, password) # debugging only

from skpy import Skype, SkypeChats
sk = Skype(email, password) # connect to Skype

# Docs: https://skpy.t.allofti.me/reference/api.html#skpy.event.SkypeEvent

# WORKS MAGICALLY: Prints the groups's ids as well, YO!!
skc = SkypeChats(sk)
# print(skc.recent())

import os.path

# Docs: https://pypi.org/project/SkPy/

# Works
# for i in sk.contacts:
# 	print(i)
# 	print()


# sk.user # you
# sk.contacts # your contacts
# sk.chats # your conversations

# Not working
# print(sk.user)

# print(sk)
# for i in sk.chats:
# 	print(i)
# 	print()

# WORKS MAGICALLY (It waits for one latest message to arrive and print its details)
# print(sk.getEvents())

# WORKS MAGICALLY TO SEND MESSAGES TO GROUPS
######## liveId of a group looks like: 19:43fa5ab68e7448f185e03d35c68d95cb@thread.skype    , TIP: Get live id by using `print(skc.recent())`
myGroup = skc.chat("19:43fa5ab68e7448f185e03d35c68d95cb@thread.skype")
# print(myGroup) # To debug, prints None if no group found, else prints whole lots of details about the group.
myGroup.sendMsg("Hahakaaal...")
# WORK MAGICALLY TO SEND IMAGES TO ANY SKYYPE GROUP
# with open("/home/array/Documents/profile-round.png", "rb") as f:
with open("./images/start1.gif", "rb") as f:
	myGroup.sendFile(f, "myFile.gif", image=True)



##### WORK MAGICALLY
##### liveId of Alex : live:slxv21
# alex = sk.contacts["live:slxv21"]
# print(alex)
# alex.chat.sendMsg("welcom to bot world")

# WORKS MAGICALLY TO SEND FILES (atleast images are tested)
# with open("/home/array/Documents/profile-round.png", "rb") as f:
# 	alex.chat.sendFile(f, "myFile.png", image=True)

# WORKS MAGICALLY
# group = sk.chats.create(["live:slxv21", "live:.cid.a0d2a22cb000856c"])

# ch = sk.chats.create(["joe.4", "daisy.5"]) # new group conversation
# ch = sk.contacts["sahilrajput03"].chat # 1-to-1 conversation
# ch.sendMsg("content") # plain-text message

# #### Other bad stuff
# Finding group id via tough way (i.e., tracking http request in web.skype.com)
# 19%3A56abae838aa34f87a46401d2d7ca425f%40thread.skype
# Decoded above url via: https://meyerweb.com/eric/tools/dencoder/
# 19:56abae838aa34f87a46401d2d7ca425f@thread.skype