import json

import pytest
import requests

@pytest.fixture
def logged_session():
    session = requests.Session()

    def log_request_and_response(response,*args,**kwargs):
        request = response.request
        print('\n===========Request ========')
        print(f"{request.method} {request.url}")
        print('Headers:')
        for key,value in request.headers.items():
            print(f"{key}: {value}")
        if request.body:
            if 'application/json' in request.headers.get['Content-Type','']:
                body = json.loads(request.body)
            else:
                body = request.body
            print('Body:')
            print(body)
        else:
            print('Body: None')

        print('\n===========Response ========')
        print(f"Status code: {response.status_code}")
        print('Headers:')
        for key,value in response.headers.items():
            print(f"{key}: {value}")
        print('Body:')
        print(response.text)

    session.hooks['response'].append(log_request_and_response)
    return session