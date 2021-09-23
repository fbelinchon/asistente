import requests
import json





api_address='http://localhost:5005/webhooks/rest/webhook'


def rasa(message):
    
    data=jsonMessage(message)
    json_data = requests.post(url=api_address, data = jsonMessage(message)).json()
    #print(json_data[0]['text'])
    text1=[resp["text"] for resp in json_data if "text" in resp.keys()] 
    print(text1)
    return text1

def jsonMessage(message):
    print(bytes(message,'iso-8859-1').decode('latin1'))
    json_text='{"sender": "test_user","message": "'+ message+'"}'
    return json_text.encode('utf-8')



