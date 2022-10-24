from flask import Flask

api = Flask(__name__)

@api.route('/profile')
def my_profile():
    response_body = {
        "name": "Shahaf",
        "about" :"HelloWorld!"
    }

    return response_body