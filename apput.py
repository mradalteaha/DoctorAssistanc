import unittest
import pyrebase

import os
import sys
import time
import os.path as op
from functools import partial
from kivy.clock import Clock
from kivy.tests.common import GraphicUnitTest
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button

firebaseConfig = {
            'apiKey': "AIzaSyAxS1KDjH4OQrbw-k050yGJHQ8giCuyFDU",
            'authDomain': "project16-f346d.firebaseapp.com",
            'databaseURL': "https://project16-f346d-default-rtdb.firebaseio.com/",
            'projectId': "project16-f346d",
            'storageBucket': "project16-f346d.appspot.com",
            'messagingSenderId': "237946682699",
            'appId': "1:237946682699:web:59b0610e150f5c42b7bcce",
            'measurementId': "G-W8TSC422XT"}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()

class TestUser(unittest.TestCase):
    def test_userid(self):
        '''this test to check if  user id found in the data base'''
        from main import find_user
        self.assertEqual(1,find_user('209102250'),"User in the data base")
        self.assertEqual(0, find_user('1111111'),"User is not in the data base")

    def test_username(self):
        '''this test to check if  username exist  in the data base'''
        from main import username_exist
        self.assertEqual(1,username_exist('asd'),"user name exists in data base")
        self.assertEqual(0, username_exist('ZZZZZ'),"user name doesnt exist in data base")

    def test_granaccess(self):
        '''this test to check if  username and the password are correct and grant user acces'''
        from main import grantAccess
        self.assertEqual(1,grantAccess('asd','asd'),"Grant access")
        self.assertEqual(0, grantAccess('abd10', '6548'), "Wrong password")

    def test_currentuser(self):
        '''this test return the id of the current users'''
        from main import currentUser
        self.assertEqual('209102250',currentUser('asd'),"returned the username ")
        self.assertNotEqual('123456',currentUser('abd10'),"not the username of this id")


from kivy.tests.common import GraphicUnitTest, UnitTestTouch
from kivy.lang import Builder
from kivy.uix.textinput import TextInput


class TestGraphic(GraphicUnitTest):
    def test_testButton(self):
        def test_button(self):
            from kivy.uix.widget import Widget
            from kivy.uix.button import Button
            from kivy.graphics import  Color

            button = Button()
            r = self.render
            # create a root widget
            wid = Widget()
            with wid.canvas:
                Color(1, 1, 1, 1)
            wid.add_widget(button)
            button.bind(
                on_release=lambda instance: setattr(
                    instance, 'test_released', True
                )
            )
            self.assertTrue(button.test_released)

            '''r(wid)'''

if __name__ == '__main__':
    unittest.main()

