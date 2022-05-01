from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from pprint import pprint
import email
import base64
from bs4 import BeautifulSoup

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)

        recent_emails = service.users().messages().list(userId='me', maxResults=3).execute()
        email_id = recent_emails['messages'][0]['id']

        results = service.users().messages().get(userId='me', id=email_id, format='raw').execute()
        message = results['raw']
        message_raw = base64.urlsafe_b64decode(message.encode('ASCII'))
        # print(type(message_raw))
        message_str = email.message_from_bytes(message_raw)

        content_types = message_str.get_content_maintype()

        if content_types == 'multipart':
            # part 1 is plain text, part 2 is html text
            part1, part2 = message_str.get_payload()
            soup = BeautifulSoup(part2.get_payload(), 'lxml') # we get an html string
            print(soup.a.text)
        else:
            print(message_str.get_payload())

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')


if __name__ == '__main__':
    main()