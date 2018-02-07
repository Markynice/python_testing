import imaplib
import email

user = 'aily.teamqa@gmail.com'
password = 'Asdf123$%^'

con = imaplib.IMAP4_SSL('imap.gmail.com',993)
print('Success')
con.login(user,password)
print('Success')

typ, data = con.search(None, 'All')
for num in data[0].split():
	typ, data = con.fetch(num, '(RFC822)')
	print('Message %s\n%s\n' % (num, data[0][1]))
con.close()
con.logout()


#result, data = connect.fetch(b'3','(RFC822)')