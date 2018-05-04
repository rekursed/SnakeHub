import pytest
from mixer.backend.django import mixer

# We need to do this so that writing to the DB is possible in our tests.
pytestmark = pytest.mark.django_db


def test_message_type():
    instance = schema.MessageType()
    assert instance

def test_resolve_all_messages():
    msg = mixer.blend('simple_app.Message')
    q = schema.Query()
    id = to_global_id('MessageType' , msg.pk)
    res = q.resolve_messages({'id':id},None,None)

    assert res = msg , 'Should Retrun All Messages'
