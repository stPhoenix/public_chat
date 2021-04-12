from django.test import TestCase
from api.models import Message

# Create your tests here.

def fill_chat():
    for i in range(1, 51):
            message = Message(author=f'author{i}@mail.com', text=f'text message {i}')
            message.save()

class TestMessages01List(TestCase):
    def setUp(self):
        fill_chat()

    def test_message_list(self):
        response = self.client.get('/api/messages/list/5')
        self.assertTrue(response.status_code == 200, response.status_code)
        self.assertContains(response, 'text message 50')


class TestMessages02Detail(TestCase):
    def setUp(self):
        fill_chat()

    def test_message_detail(self):
        #Improve for postgresql case - because every time TestCase destroyed it also destroys data in database, so new id for messages will start with 51
        response = self.client.get('/api/messages/single/65')
        self.assertTrue(response.status_code == 200, response.status_code)
        self.assertContains(response, 'text message 15')


class TestMessages03Create(TestCase):
    def test_message_create(self):
        response = self.client.post('/api/messages/add', {'author': 'user51@mail.com',
                                                          'text': 'text message 51'})
        self.assertTrue(response.status_code == 201, response.status_code)
        self.assertContains(response, 'text message 51', status_code=201)

    def test_wrong_email(self):
        response = self.client.post('/api/messages/add', {'author': 'user.mail.com',
                                                          'text': 'text message 51'})
        self.assertTrue(response.status_code == 400, response.status_code)
        self.assertContains(response, 'Enter a valid email address.', status_code=400)
    
    def test_empty_text(self):
        response = self.client.post('/api/messages/add', {'author': 'user.mail.com',
                                                          'text': ''})
        self.assertTrue(response.status_code == 400, response.status_code)
        self.assertContains(response, 'This field may not be blank.', status_code=400)
    
    def test_long_text(self):
        response = self.client.post('/api/messages/add', {'author': 'user.mail.com',
                                                          'text': 'a'*101})
        self.assertTrue(response.status_code == 400, response.status_code)
        self.assertContains(response, 'Ensure this field has no more than 100 characters.', status_code=400)
