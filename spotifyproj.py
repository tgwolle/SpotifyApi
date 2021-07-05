import spotipy
import requests
import sqlalchemy
from sqlalchemy import create_engine
import pandas


CLIENT_ID = "b17aa41ea56f4d8e931b210c3a766e70"
CLIENT_SECRET = "18563009e3fc439fa5f0bc18224f57a6"
AUTH_URL = "https://accounts.spotify.com/api/token"
auth_response = requests.post(AUTH_URL, {
  'client_id': CLIENT_ID,
  'grant_type': 'client_credentials',
  'client_secret': CLIENT_SECRET
})
# check if status code is 200
# print(auth_response.status_code)
auth_response_data = auth_response.json()


access_token = auth_response_data['access_token']
# reaching, but check if auth_response_data is not null
# print(auth_response_data)
headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '1ivUwqx8QXtteFsxAOF5X1'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
df = pandas.DataFrame(list(r.items()), columns = ['Feature', 'Score'])


engine = create_engine('mysql://root:codio@localhost/Spotify')

df.to_sql('Audio Features', con = engine, if_exists = 'replace', index = False)

# print(r)
# print(df)
