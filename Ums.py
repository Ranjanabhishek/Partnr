import requests
from Redis import redis
import json
from django.http import HttpResponse
import uuid


class Ums:
    def register(self, user_name, email, phone):
        id = uuid()
        
        #assuming we have a db connection and we are saving data in db 
        db.save(user_name, email, phone)


    def login(self, user_details):
        user_id = user_details.get('id')
        #can call redis if session is stored else fallback on db
        response = {}

        session_id = redis(user_id)
        if session_id:
            response['session_id'] = session_id
            response['status'] = 200
            return HttpResponse(json.dumps(response), content_type="application/json")
        else:
            #fallback on db 
            return HttpResponse(json.dumps(response), content_type="application/json")
        response['session_id'] = None
        response['status'] = 400
        return HttpResponse(json.dumps(response), content_type="application/json")
    
    def generate_passoword(self, user_name, email):
        pass
    
    def forgot_password(self, user_name, email):
        pass
        

