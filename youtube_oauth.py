# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    credentials = None

    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"

    if os.path.exists('token.json'):
        try:
            credentials = Credentials.from_authorized_user_file('token.json', scopes)
            credentials.refresh(Request())
        except google.auth.exceptions.RefreshError as error:
            # if refresh token fails, reset creds to none.
            credentials = None
            print(f'Refresh token expired requesting authorization again: {error}')

    # If there are no valid credentials then we will go through the login flow.
    if not credentials or not credentials.valid:
        client_secrets_file = "client_secret_682810262156-60cjmqf560vmn44rglnu40smvh9ddcit.apps.googleusercontent.com.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()

        with open('token.json', 'w') as token:
            token.write(credentials.to_json())

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    # request = youtube.channels().list(
    #     part="snippet,contentDetails,statistics",
    #     mine=True
    # )

    request = youtube.playlists().list(
        part="snippet",
        mine=True
    )


    response = request.execute()

    print(response)

#def main():
#    youtube = youtubAuth()

if __name__ == "__main__":
    main()