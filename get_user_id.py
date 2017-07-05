import requests
from constants import APP_ACCESS_TOKEN,BASE_URL
def get_user_id(insta_username):
    #function logic
     requset_url=(BASE_URL+'user/search?q=&s')%(insta_username,APP_ACCESS_TOKEN)
     print'GET REQUEST url:&'%(requset_url)
     user_info=requests.get(requset_url).json()
     if user_info['meta']['code']==200:
         if len(user_info)['data']:
            return user_info['data'][0]['id']
         else:
              return None
     else:
         print'status code other then 200 recieved'
         exit()