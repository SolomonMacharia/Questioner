import os
from  flask import Flask
from app.api.v1.views.question_record_views import v1_questions_blueprint
from app.api.v1.views.meetup_record_views import v1_meetup_blueprint
from app.api.v1.views.rsvp_views import v1_rsvp_blueprint
from app.api.v1.views.user_record_views import v1_user_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(v1_questions_blueprint)
    app.register_blueprint(v1_meetup_blueprint)
    app.register_blueprint(v1_rsvp_blueprint)
    app.register_blueprint(v1_user_blueprint)
    
    return app