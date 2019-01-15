

all_rsvps = []

class RsvpModel:
    def __init__(self):
        self.db = all_rsvps
    def create_rsvp(self, meetupId, topic, status):
        new_rsvp = {
            "meetupId": meetupId,
            "topic": topic,
            "status": status
        }
        rsvp = self.db.append(new_rsvp)

        return rsvp

