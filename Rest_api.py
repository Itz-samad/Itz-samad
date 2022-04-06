import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

for i in response.json()['items']:
    if i['answer_count'] == 0:
        print(i['title'])
        print(i['link'])
        
    else :
        print('skip')
    
    print('')
