"""Testing for the methods applied to the entries"""
from tests.base import BaseTestClass

import json


class TestEntryCase(BaseTestClass):
    """Class testing for entry test cases"""


    def test_post_entry(self):
        """Test for posting an entry"""

        # Correct entry data format
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        response = self.client.post('/api/v1/entries',
                                    data=json.dumps(self.entry_contents),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)} )
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Entry created successfully')


    def test_post_entry_no_title(self):
        # No title
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        response = self.client.post('/api/v1/entries',
                                    data=json.dumps(self.entry_no_title),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)} )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Title is required')


    def test_post_entry_no_description(self):
        # No description
        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        response = self.client.post('/api/v1/entries',
                                    data=json.dumps(self.entry_no_description),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Description is required')

        

    def test_get_all_entries(self):
        """Test for viewing all user entries"""

        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                            data=json.dumps(self.entry_contents),
                            content_type='application/json',
                            headers={"Authorization":"Bearer {}".format(token)} )
        response = self.client.get('/api/v1/entries',
                                    data=json.dumps(self.entry_contents),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'All entries found successfully')


    def test_get_single_entry(self):
        """Test for viewing a single entry"""

        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                            data=json.dumps(self.entry_contents),
                            content_type='application/json',
                            headers={"Authorization":"Bearer {}".format(token)} )
        response = self.client.get('/api/v1/entries/1',
                                    data=json.dumps(self.entry_contents),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Entry retrieved successfully')


    def test_update_entry(self):
        """Test for updating an entry"""

        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                            data=json.dumps(self.entry_contents),
                            content_type='application/json',
                            headers={"Authorization":"Bearer {}".format(token)} )
        response = self.client.put('/api/v1/entries/1',
                                    data=json.dumps({'title':'My Name', 'description':'You know who I am son'}),
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Entry updated successfully')

    
    def test_delete_entry(self):
        """Test for deleting an entry"""

        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                            data=json.dumps(self.entry_contents),
                            content_type='application/json',
                            headers={"Authorization":"Bearer {}".format(token)} )
        response = self.client.delete('/api/v1/entries/1',
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)} )
        self.assertEqual(response.status_code, 204)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Entry deleted successfully')

    
    def test_delete_entry_non_existent(self):
        """Test for deleting an entry"""

        self.signup_user()
        login = self.login_user()
        token = json.loads(login.data.decode("UTF-8"))['token']
        self.client.post('/api/v1/entries',
                            data=json.dumps(self.entry_contents),
                            content_type='application/json',
                            headers={"Authorization":"Bearer {}".format(token)} )
        response = self.client.delete('/api/v1/entries/5',
                                    content_type='application/json',
                                    headers={"Authorization":"Bearer {}".format(token)} )
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data())
        self.assertEqual(data['message'], 'Entry not found.')