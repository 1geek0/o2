from __future__ import print_function
import httplib2
import os
import base64
from apiclient import discovery
import oauth2client
from oauth2client import client
from oauth2client import tools
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from email.parser import Parser
from email.parser import HeaderParser
import quopri
import requests
import mmap
import urllib3.contrib.pyopenssl
urllib3.contrib.pyopenssl.inject_into_urllib3()

urlSet = set()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
		if tag == 'a':
			for attr in attrs:
				# print "     attr:", attr
				link = attr[1]
				if link.startswith('http://mandrillapp.com/track/click/30146609/oneplus.net'):
					urlSet.add(link)
				elif link.startswith('http://mandrillapp.com/track/click/30146609/invites'):
					urlSet.add(link)

parser = MyHTMLParser()
toTH = []
parser = MyHTMLParser()
f = open('b.json', 'a+')
try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret_542287787593-eqc0mv6kscvv1e3s8399t62mi1hn7qre.apps.googleusercontent.com.json'
APPLICATION_NAME = 'My Project'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'gmail-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
	noTh = 0
	credentials = get_credentials()
	http = credentials.authorize(httplib2.Http())
	service = discovery.build('gmail', 'v1', http=http)
	results = service.users().labels().list(userId='me').execute()
	res = service.users().threads().list(userId='me').execute()
	labels = results.get('labels', [])
	threads = res.get('threads', [])
	'You&#39;re on the list! Thanks for your interest'
	if not threads:
		print('No threads found.')
	else:
		print('Threads: ')
		print(len(threads))
		for thread in threads:
			if thread['snippet'] == 'Confirm your email You&#39;re almost there! Please go to the following address to confirm your':
				toTH.append(thread)
				print('Thread No: ' + str(len(toTH)))
				mainThread = service.users().threads().get(userId='me', id=thread['id']).execute()
				messages = mainThread['messages']
				x = 1
				l = 0
				ln = len(messages)
				print(len(messages))
				while x<len(messages):
					
					#print(x)
					print(str(x) + "/" + str(ln))
					s = messages[ln - x]
					msg_id = s['id']
					message = service.users().messages().get(userId='me', id=msg_id,format='raw').execute()
					t = '''http://mandrillapp.com/track/click/30146609/invites.=oneplus.net?p=3DeyJzIjoiNmhDWi05enhTMlRmcjB1eUxMMmJXUUhNOGhVIiwidiI6MSwicCI=6IntcInVcIjozMDE0NjYwOSxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL2ludml0ZX=Mub25lcGx1cy5uZXRcXFwvY29uZmlybVxcXC9BMEE1NDJFNUY1NjAwRUZDRUU3N0QxOUI5OTQ3N=TkzRFwiLFwiaWRcIjpcImE1N2Q3N2VlNmQzYzQ0NTM4MDI5MDFjZTIzNWNiYmFjXCIsXCJ1cmxf=aWRzXCI6W1wiMjViZGM4MThhNGE2Mjg5ZDc0Mjg5MjI3ZmJiZmFjZjU5MDRhZDZiMlwiXX0ifQ'''
					a = t.replace('=','')
					r = a.index('?p')
					u = a.replace('?p', '?p=')
					
					# print('Message snippet: %s' % message['snippet'])
					msg_str = base64.urlsafe_b64decode(message['raw'].encode(encoding='UTF-8', errors='strict'))
					fg = Parser()
					
					ll = HeaderParser()
					gfs = ll.parsestr(msg_str)
					fin_parsed = quopri.decodestring(msg_str)
					
					parser.feed(fin_parsed)
					x += 1
			elif thread['snippet'] == 'You&#39;re on the list! Thanks for your interest in the OnePlus 2! You&#39;ll be notified once you':
				toTH.append(thread)
				print('Thread No: ' + str(len(toTH)))
				mainThread = service.users().threads().get(userId='me', id=thread['id']).execute()
				messages = mainThread['messages']
				x = 1
				l = 0
				ln = len(messages)
				print(len(messages))
				while x<len(messages):
					
					#print(x)
					print(str(x) + "/" + str(ln))
					s = messages[ln - x]
					msg_id = s['id']
					message = service.users().messages().get(userId='me', id=msg_id,format='raw').execute()
					t = '''http://mandrillapp.com/track/click/30146609/invites.=oneplus.net?p=3DeyJzIjoiNmhDWi05enhTMlRmcjB1eUxMMmJXUUhNOGhVIiwidiI6MSwicCI=6IntcInVcIjozMDE0NjYwOSxcInZcIjoxLFwidXJsXCI6XCJodHRwczpcXFwvXFxcL2ludml0ZX=Mub25lcGx1cy5uZXRcXFwvY29uZmlybVxcXC9BMEE1NDJFNUY1NjAwRUZDRUU3N0QxOUI5OTQ3N=TkzRFwiLFwiaWRcIjpcImE1N2Q3N2VlNmQzYzQ0NTM4MDI5MDFjZTIzNWNiYmFjXCIsXCJ1cmxf=aWRzXCI6W1wiMjViZGM4MThhNGE2Mjg5ZDc0Mjg5MjI3ZmJiZmFjZjU5MDRhZDZiMlwiXX0ifQ'''
					a = t.replace('=','')
					r = a.index('?p')
					u = a.replace('?p', '?p=')
					
					# print('Message snippet: %s' % message['snippet'])
					msg_str = base64.urlsafe_b64decode(message['raw'].encode(encoding='UTF-8', errors='strict'))
					fg = Parser()
					
					ll = HeaderParser()
					gfs = ll.parsestr(msg_str)
					fin_parsed = quopri.decodestring(msg_str)
					x += 1
					parser.feed(fin_parsed)
	c = 0
	urlList = list(urlSet)
	print(len(urlList))
	m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
	op = requests.get(urlList[len(urlList)-1])
	for item in urlList:
		print(item, file = f)
		if m.find(item) != -1:
			fg = 0
		else:
			res = requests.get(item)
			c += 1
			print(c)
				# print(str(s), file = f)
				# 
				# print(len(messages), file = f)
	"""Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """


if __name__ == '__main__':
    main()