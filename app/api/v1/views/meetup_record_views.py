from flask import jsonify, Blueprint, request, json
from ..models.meetup_record_models import MeetupRecord
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = MeetupRecord()

@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def post_question():
    data = request.get_json()

    meetupId = len(meetup.all_meetup_records) + 1
    createdOn = datetime.now()
    location = data["location"]
    images = data["images"]
    happeningOn = data["happeningOn"]
    tags = data["tags"]

    meetup.create_meetup(meetupId, createdOn, location, images, happeningOn, tags )
    return jsonify({
        "status": 201,
        "data": [{
            "topic": "The topic",
            "location": "The venue",
            "happeningOn": "The meetup date.",
            "tags": ["tag1", "tag2", "tag3"]
        }]
    }), 201

@v1_meetup_blueprint.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    return jsonify(meetup.all_meetup_records)

@v1_meetup_blueprint.route('/meetups/upcoming/<int:meetupId>', methods=['GET'])
def get_single_meetup(meetupId):
    singleMeetup = meetup.fetch_single_meetup(meetupId)
    return jsonify(singleMeetup)