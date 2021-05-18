import tweepy
import json 
from time import sleep

consumer_key = 'p7JHobPEgYm0333Mkdjm4UIJG'
consumer_secret = 'pcTi7UXiLRjSL3F2vtkwxfP4RIyUTEEiXncdwiuId8RvPnLXYW'
access_token = '2292310067-tkF3tw2KSJA4GUCCAimqYL4riyC5aDrgW68GqVs'
access_token_secret = 'Nha0gcESchEGYYTNPtIWYYoT7DULJlamlLkG464GcgsXP'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

usuarios = open("usuarios.txt","r",encoding="utf-8")
for usuario in usuarios:
    f = open("usuarios_extraidos.csv","a+",encoding="utf-8")
    f.write("Usuario " + usuario)
    for user in tweepy.Cursor(api.followers, screen_name=usuario).items():
        f.write(user.screen_name + '\n')
        print(user.screen_name)
        sleep(1)
    f.close()
usuarios.close()
