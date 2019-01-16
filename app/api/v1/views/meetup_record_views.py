from flask import jsonify, Blueprint, request, json
from ..models.meetup_record_models import MeetupRecord
from datetime import datetime
from uuid import uuid4

v1_meetup_blueprint = Blueprint('meetups', __name__, url_prefix='/api/v1')

meetup = MeetupRecord()

@v1_meetup_blueprint.route('/meetups', methods=['POST'])
def post_question():
    data = request.get_json()

    topic = data["topic"]
    images = data["images"]
    tags = data["tags"]
    location = data["location"]

    mtp = meetup.create_meetup(topic, location, images, tags )
    return jsonify({"status": 201, "data": mtp}),201

@v1_meetup_blueprint.route('/meetups/upcoming', methods=['GET'])
def get_all_meetups():
    return jsonify(meetup.all_meetup_records)

@v1_meetup_blueprint.route('/meetups/upcoming/<int:meetupId>', methods=['GET'])
def get_single_meetup(meetupId):
    singleMeetup = meetup.fetch_single_meetup(meetupId)
    return jsonify(singleMeetup)

@v1_meetup_blueprint.route('/meetups/delete/<int:meetupId>', methods=['DELETE'])
def delete_meetup(meetupId):
    Meetup = meetup.delete_meetup(meetupId)
    return jsonify({"status": 204, "Meetup": Meetup})
    