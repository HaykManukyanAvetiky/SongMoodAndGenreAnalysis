from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import random


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
# DEVELOPER_KEY = 'REPLACE_ME'
# https://www.youtube.com/results?search_query=sad+songs

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="D:/env_vars/My First Project-cd8411264b7e.json"

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

youtube = build(serviceName=YOUTUBE_API_SERVICE_NAME, version=YOUTUBE_API_VERSION)



def youtube_search(query):
    search_response = youtube.search().list(
                                            part='id,snippet',
                                            q=query,
                                            maxResults=50,
                                            type = 'video'
                                            ).execute()
    choice = search_response['items'][random.randint(1,50)]
    
    return choice['snippet']['title'], 'https://www.youtube.com/watch?v=' + choice['id']['videoId']



if __name__ == '__main__':
  while True:
      query = input("tell me your mood >>>")
      if query == 'quit' :
          print('goodby...')
          break
      try:
          title, url = youtube_search(query)
      except HttpError as e:
          print('An HTTP error %d occurred:\n%s' % (e.resp.status, e.content))
      print('title: '+ title)
      print('url:   '+ url)