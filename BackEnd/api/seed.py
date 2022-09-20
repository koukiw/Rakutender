from utils.auth import get_digest
from utils.db import session

from models.category import Category
from models.event import Event
from models.user import User
from models.participant import Participant

category = Category()
user = User()
event = Event()
participant = Participant()

category.id = "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
category.name = "dinner"
session.add(category)

user.id = "550e8400-e29b-41d4-a716-446655440000"
user.username = "wakabayashi"
user.digest = get_digest("password")
session.add(user)

event.id = "A0EEBC99-9C0B-4EF8-BB6D-6BB9BD380A11"
event.name = "testパーティー"
event.created_user_id = "550e8400-e29b-41d4-a716-446655440000"
event.category_id = "a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11"
session.add(event)
session.commit()

participant.id = "550e8400-e29b-41d4-a716-446655441111"
participant.user_id = "550e8400-e29b-41d4-a716-446655440000"
participant.event_id = "A0EEBC99-9C0B-4EF8-BB6D-6BB9BD380A11"
session.add(participant)

session.commit()
