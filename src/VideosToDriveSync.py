import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

import time

SCOPES = ["https://www.googleapis.com/auth/drive"]

# PATHS #
credentialsAndTokenPath = "/home/dotapie/CatMonitoring"
videosPath = "/home/dotapie/CatMonitoring/Videos"

while 1:
    print("Syncing ...")

    creds = None

    timeStamp = time.time()

    if os.path.exists(credentialsAndTokenPath + "/token.json"):
        creds = Credentials.from_authorized_user_file(credentialsAndTokenPath + "/token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentialsAndTokenPath + "/credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(credentialsAndTokenPath + '/token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build("drive", "v3", credentials=creds)

        response = service.files().list(
            q="name='CatMonitoring' and mimeType='application/vnd.google-apps.folder'",
            spaces='drive'
        ).execute()

        if not response['files']:
            file_metadata = {
                "name": "CatMonitoring",
                "mimeType": "application/vnd.google-apps.folder"
            }

            file = service.files().create(body=file_metadata, fields="id").execute()

            folder_id = file.get('id')
        else:
            folder_id = response['files'][0]['id']

        for file in os.listdir(videosPath):
            file_metadata = {
                "name": file,
                "parents": [folder_id]
            }

            media = MediaFileUpload(f"{videosPath}/{file}")
            upload_file = service.files().create(body=file_metadata,
                                                media_body = media,
                                                fields="id").execute()
            
            print("Synced up file: " + file)

            print("Deleting synced file ...")
            os.remove(f"{videosPath}/{file}")

    except HttpError as e:
        print("Error: " + str(e))
    
    print("Syncing done, goin to sleep ...")
    time.sleep(300 - (time.time() - timeStamp))