import spotipy
import requests
CLIENT_ID="b17aa41ea56f4d8e931b210c3a766e70"
CLIENT_SECRET="18563009e3fc439fa5f0bc18224f57a6"

AUTH_URL='https://accounts.spotify.com/api/token'
auth_response= requests.post(AUTH_URL,{
  'client_id':CLIENT_ID,
  'grant_type':'client_credentials',
  'client_secret': CLIENT_SECRET
})
print(auth_response.status_code)
auth_response_data=auth_response.json()
#auth_response_data
print(auth_response_data)
access_token=auth_response_data['access_token']
headers={
  'Authorization': 'Bearer{token}'.format(token=access_token)
}
BASE_URL='https://api.spotify.com/v1/'
track_id = '1XeExJaUcQYYBcFVuil3fP'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()


