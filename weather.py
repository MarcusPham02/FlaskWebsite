#import modules
import json
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import base64





Coin= os.getenv("API_Token")
Conversion= Coin.encode('utf-8')
Api_Key=str(base64.b64encode(Conversion), 'utf-8')
  


#def authorization():
    #return {'Authorization': 'Bearer ' + Token}







def GetWeather(lat,lon,Api_Key):
    ApiCall= requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={Api_Key}")

    print(ApiCall.json())
    
    
GetWeather("41.8755616",'-87.6244212',Api_Key)
    
    

    
    
   
    