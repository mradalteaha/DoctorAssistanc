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
    'apiKey': "AIzaSyCVxh3zfkNPlbPTaUmhHgIRISlWl6l4qBY",
    'authDomain': "doctorassistance-bce5c.firebaseapp.com",
    'databaseURL': "https://doctorassistance-bce5c-default-rtdb.firebaseio.com",
    'projectId': "doctorassistance-bce5c",
    'storageBucket': "doctorassistance-bce5c.appspot.com",
    'messagingSenderId': "1046807573992",
    'appId': "1:1046807573992:web:bb926a9a210d49f2f4a05d",
    'measurementId': "G-77QNZ4D0VQ"}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()


class TestUser(unittest.TestCase):
    def test_userid(self):
        '''this test to check if  user id found in the data base'''
        from main import find_user
        self.assertEqual(1,find_user('123321123'),"User in the data base")
        self.assertEqual(0, find_user('1111111'),"User is not in the data base")

    def test_username(self):
        '''this test to check if  username exist  in the data base'''
        from main import username_exist
        self.assertEqual(1,username_exist('morad98'),"user name exists in data base")
        self.assertEqual(0, username_exist('ZZZZZ'),"user name doesnt exist in data base")

    def test_granaccess(self):
        '''this test to check if  username and the password are correct and grant user acces'''
        from main import grantAccess
        self.assertEqual(1,grantAccess('morad98','m@123456','123321123'),"Grant access")
        self.assertEqual(0, grantAccess('morad98', '6548','123321123'), "Wrong password")

    def test_password_check(self):
        '''this test to check if password is strong enough'''
        from main import password_check
        self.assertEqual(0,password_check('12345'),"password isn't long enough")
        self.assertEqual(0,password_check('1234547'),"password should have a character")
        self.assertEqual(0, password_check('1234547m'), "password should have a special character")
        self.assertEqual(1, password_check('123454@7m'), "good password")


if __name__ == '__main__':
    unittest.main()
