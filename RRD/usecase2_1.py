# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 20:08:13 2019

@author: Rachita.Pabreja
"""
from __future__ import print_function
import pickle
import os.path
import sys
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import base64
from email.mime.text import MIMEText

def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject
  return {'raw': base64.urlsafe_b64encode(message.as_string().encode('UTF-8')).decode('ascii')}


def send_message(argv):
    ##msg = create_message('rkpabreja@gmail.com','rachit.pabreja@saggezza.com','Test','Test123')
    msg = create_message(argv[0],argv[1],argv[2],argv[3])
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
     
    service = build('gmail', 'v1', credentials=creds)
    service.users().messages().send(userId='me', body=msg).execute()

if __name__ == '__main__':
    send_message(sys.argv[1:])
