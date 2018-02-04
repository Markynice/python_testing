import imaplib
import email

user = 'aily.teamqa@gmail.com'
password = 'Asdf123$%^'

con = imaplib.IMAP4_SSL('imap.gmail.com')
con.login(user,password)

con.list()

#result, data = connect.fetch(b'3','(RFC822)')