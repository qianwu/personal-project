'''I will use this file to upload the pronunciation file with google drive api
'''


import os
import logging
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive.metadata.readonly"]
class GoogleDriveStorage:
    def __init__(self, credentials_path):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.creds = None
        self.service = None
        self.abs_p = os.path.dirname(os.path.abspath(__file__))
        self.token_path = self.abs_p + "/token.json"
        self.credentials_path = credentials_path
        self.authenticate()
        self.create_service()

    def authenticate(self):
        if os.path.exists(self.token_path):
            self.creds = Credentials.from_authorized_user_file(self.token_path)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_path, SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open(self.token_path, "w") as token:
                token.write(self.creds.to_json())

    def create_service(self):
        self.service = build("drive", "v3", credentials=self.creds)

    def upload_file(self, file_path, file_name):
        file_metadata = {
            "name": file_name,
            "mimeType": "audio/mp3"
        }
        media = MediaFileUpload(file_path, mimetype="audio/mp3")
        file = self.service.files().create(body=file_metadata, media_body=media, fields="id").execute()
        self.logger.info("File ID: %s" % file.get("id"))

    def delete_file(self, file_id):
        try:
            self.service.files().delete(fileId=file_id).execute()
            self.logger.info("File ID: %s has been deleted" % file_id)
        except HttpError as e:
            self.logger.error("An error occurred: %s" % e)

    def download_file(self, file_id, file_name):
        request = self.service.files().get_media(fileId=file_id)
        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            self.logger.info("Download %d%%." % int(status.progress() * 100))
        with open(file_name, "wb") as f:
            f.write(fh.getvalue())
        self.logger.info("File ID: %s has been downloaded" % file_id)