import requests
import json
import os
from dotenv import load_dotenv
import base64
from requests import post,get
load_dotenv()

#id and secret

client_id=os.getenv('client_id')
client_secret=os.getenv('client_secret')
print(client_id,client_secret)


#authentication

def get_token():
    auth_string= client_id + ':' + client_secret
    author_bytes= auth_string.encode('utf-8')
    author_base64=str(base64.b64encode(author_bytes), 'utf-8')
    Url="https://accounts.spotify.com/api/token"
    
    headers={
   'Authorization':'Basic ' + author_base64,
   "Content-Type": "application/x-www-form-urlencoded"}
    
    data= {'grant_type':'client_credentials'}
    result = post(Url,headers=headers,data=data)
    json_results = json.loads(result.content)
    token=json_results['access_token']
    return token


def header(token):
    return {'Authorization': 'Bearer ' + token}

def search(token, userinteraction):
    userinteraction= input('Who is your artist?')

    url= 'https://api.spotify.com/v1/search'
    headers= header(token)
    query= f'?q={userinteraction}&type=artist,track'
    querycombine= url + query
    result= get(querycombine,headers=headers)
    json_results = json.loads(result.content)
    print(json_results)
    


token= get_token
search(token,'Justin Bieber')
print((get_token))






#ask users input for what is your favorite playlist of Justin Bieber?
#then it will spit out the just amount of songs and songs from the playlist 
