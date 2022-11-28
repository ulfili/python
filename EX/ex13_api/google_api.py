"""API."""
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import os

import googleapiclient.discovery



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://docs.google.com/spreadsheets/d/1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M']
SAMPLE_RANGE_NAME = 'A1:E4'


def get_links_from_spreadsheet(id: str, token_file_name: str) -> list:
    """Return a list of strings from the first column of a Google Spreadsheet with the given ID."""
    links_list = []
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token_file_name):
        creds = Credentials.from_authorized_user_file(token_file_name, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_file_name, 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=id,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')

        for row in values:
            links_list.append(row[0])
        return links_list
    except HttpError as err:
        print(err)


scopes = ["https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK"]


def extract_video_id_from_response(response):
    """Something."""
    pageToken = response.setdefault("nextPageToken", "None")
    print(pageToken)
    video_id_list = []
    items_list = response["items"]
    for item in items_list:
        # print(item)
        content = item["contentDetails"]
        video_id = content["videoId"]
        print("video id is: ", video_id)
        video_id_list.append(video_id)
    return video_id_list, pageToken


def get_links_from_playlist(link: str, developer_key: str) -> list:
    """
    Return a list of links to songs in the Youtube playlist with the given address.
    Example input
        get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                                'ThisIsNotARealKey_____ThisIsNotARealKey')

    Returns
        ['https://youtube.com/watch?v=r_It_X7v-1E', 'https://youtube.com/watch?v=U4ogK0MIzqk', ... and so on]
    """
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    last_index = link.index("=")
    playlist_id = link[last_index + 1:]
    print(playlist_id)
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)
    return_list = []
    request = youtube.playlistItems().list(
        part="contentDetails",
        # pageToken="EAAaBlBUOkNBVQ",
        playlistId=playlist_id
    )

    response = request.execute()
    print(response)
    new_video_id_list, pageToken = extract_video_id_from_response(response)
    print(new_video_id_list, pageToken)
    return_list.extend(new_video_id_list)
    while pageToken != "None":
        next_request = youtube.playlistItems().list(
        part="contentDetails",
        pageToken=pageToken,
        playlistId=playlist_id
        )
        response = next_request.execute()
        new_video_id_list, pageToken = extract_video_id_from_response(response)
        return_list.extend(new_video_id_list)
        print(new_video_id_list, pageToken)
    print(return_list)
    full_link_list = []
    youtube_link = "https://youtube.com/watch?v="
    for id in return_list:
        full_link = youtube_link + id
        full_link_list.append(full_link)
    return full_link_list


if __name__ == '__main__':
    # get_links_from_spreadsheet('1WrCzu4p5lFwPljqZ6tMQEJb2vSJQSGjyMsqcYt-yS4M', 'token.json')
    get_links_from_playlist('https://www.youtube.com/playlist?list=PLFt_AvWsXl0ehjAfLFsp1PGaatzAwo0uK',
                            "AIzaSyAS_HhoP6Vq1OOcsXwQ1sTVZS91DyEK9mc")
