from datetime import datetime


class MeetupRecord:
    """ Creates the meetup record model """
    def __init__(self, *args):
        self.all_meetup_records = []

    def create_meetup(self, meetupId, createdOn, location, images, happeningOn, tags):
        """ Adds a new question to the all_question_records list """
        self.meetupId = meetupId
        self.createdOn = datetime.now()
        self.location = location
        self.images = images
        self.happeningOn = happeningOn
        self.tags = tags

        new_meetup = {
            "meetupId": meetupId,
            "createdOn": createdOn,
            "location": location,
            "images": images,
            "happeningOn": happeningOn,
            "Tags": tags

        }
        self.all_meetup_records.append(new_meetup)