import os
from  flask import Flask
from app.api.v1.views.question_record_views import v1_questions_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1_questions_blueprint)
    return app