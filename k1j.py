def CountMessages():
	app.info("Messages", "Counting messaages")
	global userID_logged
	statement = f"SELECT COUNT(MessageID) from MessageTable WHERE UserID='{userID_logged}' ;"
	cur.execute(statement)
	rows = cur.fetchall()
	print(rows)
	if len(rows) == 0:  # An empty result evaluates to False.
		app.info("Messages", "You Have No Messages")
		TotalMessages.value = 0
	else:

		TotalMessages.value = rows[0][0]
		
#

def GetMessages():
	app.info("Messages", "Getting Your Messages")
	global userID_logged
	statement = f"SELECT * from MessageTable WHERE UserID='{userID_logged}' ;"
	cur.execute(statement)
	rows = cur.fetchall()
	print(rows)
	if len(rows) == 0:  # An empty result evaluates to False.
		app.info("Messages", "You Have No Messages")
	else:
		#PUT MESSAGES INTO LIST BOX
		for x in rows:
			ListboxM.append(x)
#
#
#
def LogInButton():
	global userID_logged
	statement = f"SELECT UserID, Username from UserTable WHERE Username='{UsernameLog.value}' AND UserPW = '{PasswordLog.value}';"
	print(statement)
	cur.execute(statement)
	rows = cur.fetchall()
	print(rows)
	if len(rows) != 1:  # An empty result evaluates to False.
		print("Login failed")
	else:
		#STORE THE USER THAT LOGS IN
		userID_logged = rows[0][0]
		print("Welcome")
		open_WindowM()
		close_WindowL()
