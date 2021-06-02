from kivymd.app import MDApp
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivy.lang import Builder
from kivy.uix.label import Label
from kivymd.uix.textfield import MDTextField

from association import screen_nav
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineListItem, TwoLineListItem
from kivymd.uix.button import MDFlatButton
import pyrebase
from datetime import datetime
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.tab import MDTabsBase

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
storage = firebase.storage()


def find_user(user):
    users = db.child("users").get()
    user_found = 0
    for i in users.each():
        if str(user) == str(i.key()):
            user_found += 1
    if user_found > 0:
        return 1
    else:
        return 0


def find_patient(user):
    users = db.child("patients").get()
    user_found = 0
    for i in users.each():
        if str(user) == str(i.key()):
            user_found += 1
    if user_found > 0:
        return 1
    else:
        return 0


def username_exist(user):
    users = db.child("users").get()
    user_found = 0
    for i in users.each():
        if str(user) == str(i.val()["Username"]):
            user_found += 1
    if user_found > 0:
        return 1
    else:
        return 0


def currentUser(username):
    user = db.child("users").get()
    for i in user.each():
        if i.val()['Username'] == str(username):
            return str(i.key())


def numbersonly(something):
    l = ['-', '+', '_', '!', '@', '#', '$', '%', '^', '*', '(', ')']
    flag = 0
    for i in range(0, len(something)):
        if something[i] in l:
            flag = 1
    if str(something).isupper() or str(something).islower() or flag == 1:
        return 0
    return 1


def grantAccess(username, password):
    users = db.child("users").get()
    grant_Access = 0
    for i in users.each():
        if (str(username) == str(i.val()['Username'])) and (str(password) == str(i.val()['pass'])):
            grant_Access = 1
        if (str(username) == str(i.val()['Username'])) and (str(password) != str(i.val()['pass'])):
            grant_Access = 0
    return grant_Access


def invalidForm():
    dialog = MDDialog(title='invalid Form')
    close_button = MDFlatButton(text='Close', on_release=dialog.dismiss())
    dialog.open()


def changedsucc():
    pop = MDDialog(title='Succeded!Password changed successfully')

    pop.open()


def invalidinFormation():
    pop = MDDialog(title='Succeded!Password changed successfully')
    pop.open()


def emptyfield():
    pop = MDDialog(title='Error!', text='Fill the field first')
    close_button = MDFlatButton(text='Close', on_release=pop.dismiss())
    pop.add_widget(close_button)
    pop.open()


def no_user():
    pop = MDDialog(title='Error!This user does not exist')

    pop.open()


class MenuScreen(Screen):
    pass


class DoctorLog(Screen):
    def home_button(self):
        self.manager.current = 'doctorlog'

    def Pprofile_btn(self):
        self.manager.current = 'pprofile'

    def patientDiagnosist_btn(self):
        self.manager.current = 'profileDR'

    def patientD_btn(self):
        self.manager.current = 'pprofile2'


    pass


class ProfileDR(Screen):
    def ID_btn(self):  ##checking the id number if it's valid and inserting it to the database
        if self.manager.screens[8].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[8].ids.idnum.text) != 9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[8].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='insert Id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[8].ids.idnum.text) == 1 and find_patient(
                self.manager.screens[8].ids.idnum.text) == 1:  # checking that the user doesn't exist before
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            print(self.manager.screens[8].ids)
            user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
            self.manager.screens[8].ids.name.text += ' ' + str(user.val()['Name'])
            self.manager.screens[8].ids.idnumb.text += ' ' + str(user.val()['IDnum'])
            self.manager.screens[8].ids.age.text += ' ' + str(user.val()['Age'])
            self.manager.screens[8].ids.gender.text += ' ' + str(user.val()['Gender'])
            self.manager.screens[8].ids.nationality.text += ' ' + str(user.val()['Origin'])
            self.manager.screens[8].ids.smoker.text += ' ' + str(user.val()['Smoker'])
            self.manager.screens[8].ids.bph.text += ' ' + str(user.val()['blood pressure history'])
            self.manager.screens[8].ids.diabetes.text += ' ' + str(user.val()['Diabetes in family'])
            self.manager.screens[8].ids.pregnant.text += ' ' + str(user.val()['Pregnant'])
            self.manager.screens[8].ids.wbc.text += ' ' + str(user.val()['wbc'])
            self.manager.screens[8].ids.fever.text += ' ' + str(user.val()['Fever'])
            self.manager.screens[8].ids.neutrophil.text += ' ' + str(user.val()['neutrophil'])
            self.manager.screens[8].ids.lymphocytes.text += ' ' + str(user.val()['lymphocytes'])
            self.manager.screens[8].ids.rbc.text += ' ' + str(user.val()['rbc'])
            self.manager.screens[8].ids.hct.text += ' ' + str(user.val()['hct'])
            self.manager.screens[8].ids.urea.text += ' ' + str(user.val()['urea'])
            self.manager.screens[8].ids.hemoglobin.text += ' ' + str(user.val()['hemoglobin'])
            self.manager.screens[8].ids.creatine.text += ' ' + str(user.val()['creatine'])
            self.manager.screens[8].ids.iron.text += ' ' + str(user.val()['iron'])
            self.manager.screens[8].ids.hdl.text += ' ' + str(user.val()['hdl'])
            self.manager.screens[8].ids.alp.text += ' ' + str(user.val()['alp'])

            self.diagnosist()
            self.printteatment()


        else:
            pop = MDDialog(title='Error!', text='This patient already existing')
            pop.open()

    def wbc_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['Age'])) >= 18:
            if int(str(user.val()['wbc'])) < 4500:
                self.manager.screens[8].ids.wbc.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "viruses").set("rest at home")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "immuneS fail").set("Antibiotics")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "cancer").set(".1")
            elif int(str(user.val()['wbc'])) > 11000:
                self.manager.screens[8].ids.wbc.text_color = (209, 10, 25, 1)
                if str(user.val()['Fever']) == "yes":
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "infection").set("Antibiotics")
                elif int(str(user.val()['wbc'])) > 20000:
                    d=db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "cancer").get()
                    newvalue=float(d.val())+0.2
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "cancer").set("0.1")
        elif int(str(user.val()['Age'])) >= 4 and int(str(user.val()['Age'])) <= 17:

            if int(str(user.val()['wbc'])) < 5500:
                self.manager.screens[8].ids.wbc.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "viruses").set("rest at home")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "immuneS fail").set("Antibiotics")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "cancer").set(".1")
            elif int(str(user.val()['wbc'])) > 15500:
                self.manager.screens[8].ids.wbc.text_color = (209, 10, 25, 1)
                if str(user.val()['Fever']) == "yes":
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "infection").set("Antibiotics")
                elif int(str(user.val()['wbc'])) > 22000:
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "cancer").set("0.1")

        elif int(str(user.val()['Age'])) >= 0 and int(str(user.val()['Age'])) <= 4:

            if int(str(user.val()['wbc'])) < 6000:
                self.manager.screens[8].ids.wbc.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "viruses").set("rest at home")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "immuneS fail").set("Antibiotics")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "cancer").set(".1")
            elif int(str(user.val()['wbc'])) > 17500:
                self.manager.screens[8].ids.wbc.text_color = (209, 10, 25, 1)
                if str(user.val()['Fever']) == "yes":
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "infection").set("Antibiotics")
                elif int(str(user.val()['wbc'])) > 23000:
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "cancer").set("0.1")

    def neutrophil_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['neutrophil'])) < 28:
            self.manager.screens[8].ids.neutrophil.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Blood Creation problems").set("1 table of 10mg B12 and 1 table 5mg folic acid once a day for month")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "infection").set("Antibiotics")
            d = db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "cancer").get()
            newvalue = float(d.val()) + 0.2
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "cancer").set(str(newvalue))
        elif int(str(user.val()['neutrophil'])) >54:
            self.manager.screens[8].ids.neutrophil.text_color = (209, 10, 25, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "infection").set("Antibiotics")
    def lymphocytes_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['neutrophil'])) < 36:
            self.manager.screens[8].ids.lymphocytes.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Blood Creation problems").set("1 table of 10mg B12 and 1 table 5mg folic acid once a day for month")
        elif int(str(user.val()['neutrophil'])) >54:
            self.manager.screens[8].ids.lymphocytes.text_color = (209, 10, 25, 1)
            d = db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "cancer").get()
            newvalue = float(d.val()) + 0.2
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "cancer").set(str(newvalue))
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "infection").set("Antibiotics")

    def rbc_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if float(str(user.val()['rbc'])) < 4.5:
            self.manager.screens[8].ids.rbc.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "anemia").set("2 tables 10mg B12 once a day for month")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "bleeding").set("direct immediately to hospital")
        elif float(str(user.val()['rbc'])) >6:
            self.manager.screens[8].ids.rbc.text_color = (209, 10, 25, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Blood Creation problems").set("1 table of 10mg B12 and 1 table 5mg folic acid once a day for month")
            if str(user.val()['Smoker']) == 'yes':
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "smoking").set("stop smoking")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "lungs disease").set("stop smoking/direct to rontgen photo")

    def hct_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if str(user.val()['Gender']) == "Male":
            if int(str(user.val()['hct'])) < 37:
                self.manager.screens[8].ids.hct.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "anemia").set("2 tables 10mg B12 once a day for month")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "bleeding").set("direct immediately to hospital")
            elif int(str(user.val()['hct'])) >54:
                self.manager.screens[8].ids.hct.text_color = (209, 10, 25, 1)
                if str(user.val()['Smoker']) == 'yes':
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "smoking").set("stop smoking")

        elif str(user.val()['Gender']) == "Female":

            if int(str(user.val()['hct'])) < 33:
                self.manager.screens[8].ids.hct.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "anemia").set("2 tables 10mg B12 once a day for month")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "bleeding").set("direct immediately to hospital")
            elif int(str(user.val()['hct'])) >47:
                self.manager.screens[8].ids.hct.text_color = (209, 10, 25, 1)
                if str(user.val()['Smoker']) == 'yes':
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "smoking").set("stop smoking")

    def urea_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if str(user.val()['Origin']) == "2":
            if str(user.val()['Pregnant'])== "yes":
                if int(str(user.val()['urea'])) < 14:
                    self.manager.screens[8].ids.urea.text_color = (210, 210, 10, 1)
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "malnutrition").set("direct to nutritionist")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "liver problem").set("direct to liver specialist")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "pregnancy may cause lower urine ").set("no worries")

            elif str(user.val()['Pregnant'])== "no":
                if int(str(user.val()['urea'])) < 17:
                    self.manager.screens[8].ids.urea.text_color = (210, 210, 10, 1)
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "malnutrition").set("direct to nutritionist")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "liver problem").set("direct to liver specialist")


            elif int(str(user.val()['urea'])) >47:
                self.manager.screens[8].ids.urea.text_color = (209, 10, 25, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "Kidney problem").set("balance sugar in blood")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "dehydration").set("rest and consume more water")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "over consume protein").set("direct to nutritionist")

        elif str(user.val()['Origin']) != "2":

            if int(str(user.val()['urea'])) < 17:
                self.manager.screens[8].ids.urea.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "anemia").set("2 tables 10mg B12 once a day for month")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "bleeding").set("direct immediately to hospital")
            elif int(str(user.val()['urea'])) >43:
                self.manager.screens[8].ids.urea.text_color = (209, 10, 25, 1)
                if str(user.val()['Smoker']) == 'yes':
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "Kidney problem").set("balance sugar in blood")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "dehydration").set("rest and consume more water")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "over consume protein").set("direct to nutritionist")

    def hemoglobin_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['Age'])) >= 18:
            if str(user.val()['Gender']) == "Male":
                if float(str(user.val()['hemoglobin'])) < 12:
                    self.manager.screens[8].ids.hemoglobin.text_color = (210, 210, 10, 1)
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "anemia").set("2 tables 10mg B12 once a day for month")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "hemotology disorder").set("hormon ingection to improve rbc creation")
                elif float(str(user.val()['hemoglobin'])) > 18:
                    self.manager.screens[8].ids.hemoglobin.text_color = (209, 10, 25, 1)
            elif str(user.val()['Gender']) == "Female":
                if float(str(user.val()['hemoglobin'])) < 12:
                    self.manager.screens[8].ids.hemoglobin.text_color = (210, 210, 10, 1)
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "anemia").set("2 tables 10mg B12 once a day for month")
                    db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                        "hemotology disorder").set("hormon ingection to improve rbc creation")
                elif float(str(user.val()['hemoglobin'])) > 16:
                    self.manager.screens[8].ids.hemoglobin.text_color = (209, 10, 25, 1)

        elif int(str(user.val()['Age'])) <= 17:
            if float(str(user.val()['hemoglobin'])) < 11.5:
                self.manager.screens[8].ids.hemoglobin.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "anemia").set("2 tables 10mg B12 once a day for month")
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "hemotology disorder").set("hormon ingection to improve rbc creation")
            elif float(str(user.val()['hemoglobin'])) > 15.5:
                self.manager.screens[8].ids.hemoglobin.text_color = (209, 10, 25, 1)

    def creatine_test(self):

        result="none"

        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['Age'])) >= 18 and int(str(user.val()['Age'])) <= 59:
            if float(str(user.val()['creatine'])) <0.6:
                result = 'low'
            elif float(str(user.val()['creatine'])) >1:
                result ='high'
        elif int(str(user.val()['Age'])) >= 3 and int(str(user.val()['Age'])) <= 17:
            if float(str(user.val()['creatine'])) <0.5:
                result = 'low'
            elif float(str(user.val()['creatine'])) >1:
                result ='high'
        elif int(str(user.val()['Age'])) <= 60:
            if float(str(user.val()['creatine'])) <0.6:
                result = 'low'
            elif float(str(user.val()['creatine'])) >1.2:
                result ='high'


        if result == 'high':
            self.manager.screens[8].ids.creatine.text_color = (209, 10, 25, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "over consuming meat").set("direct to nutritionist")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "muscle problems").set("2 tables 5mg korkom , altman c3 once a day for month")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Kidney problem").set("balance sugar in blood")

        elif result == 'low' :
            self.manager.screens[8].ids.creatine.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "low protein consumption").set("direct to nutritionist")

    def iron_test(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if str(user.val()['Gender']) == 'Female':
            if int(str(user.val()['iron'])) < 48:
                self.manager.screens[8].ids.lymphocytes.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "Insufficient iron consumption ").set("Direct to nutritionist ")
            elif int(str(user.val()['neutrophil'])) >128:
                self.manager.screens[8].ids.lymphocytes.text_color = (209, 10, 25, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "iron poisoning").set("Direct immediately to hospital")
        elif str(user.val()['Gender']) == 'Male':
            if int(str(user.val()['iron'])) < 60:
                self.manager.screens[8].ids.lymphocytes.text_color = (210, 210, 10, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "Insufficient iron consumption ").set("2 tables 10mg B12 a day for month ")
            elif int(str(user.val()['neutrophil'])) >160:
                self.manager.screens[8].ids.lymphocytes.text_color = (209, 10, 25, 1)
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "iron poisoning").set("Direct immediately to hospital")

    def hdl_test(self):
        result="none"

        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['Origin'])) == 3:
            if str(user.val()['Gender']) == 'Female':
                if int(str(user.val()['hdl'])) <41:
                    result = 'low'
                elif float(str(user.val()['hdl'])) >99:
                    result ='high'

            elif str(user.val()['Gender']) == 'Male':
                if int(str(user.val()['hdl'])) <35:
                    result = 'low'
                elif float(str(user.val()['hdl'])) >74:
                    result ='high'

        elif int(str(user.val()['Origin'])) != 3:
            if str(user.val()['Gender']) == 'Female':
                if int(str(user.val()['hdl'])) <34:
                    result = 'low'
                elif float(str(user.val()['hdl'])) >82:
                    result ='high'

            elif str(user.val()['Gender']) == 'Male':
                if int(str(user.val()['hdl'])) <29:
                    result = 'low'
                elif float(str(user.val()['hdl'])) >62:
                    result ='high'


        if result == 'high':
            self.manager.screens[8].ids.hdl.text_color = (209, 10, 25, 1)

        elif result == 'low':
            self.manager.screens[8].ids.hdl.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Heart problems").set("direct to nutritionist")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Hyperlipidemia").set("direct to nutritionist + 1 table 5mg semovel a day for a week")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Diabetes").set("insulin injections ")

    def alp_test(self):

        result="none"
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        if int(str(user.val()['Origin'])) == 2:
            if int(str(user.val()['alp'])) <60:
                result = 'low'
            elif float(str(user.val()['alp'])) >120:
                result ='high'


        elif int(str(user.val()['Origin'])) != 2:
            if int(str(user.val()['alp'])) < 30:
                result = 'low'
            elif float(str(user.val()['alp'])) > 90:
                result = 'high'


        if result == 'high':
            self.manager.screens[8].ids.alp.text_color = (209, 10, 25, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "liver problem").set("direct to liver specialist")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "biliary tract problem").set("direct to liver specialist")
            if str(user.val()['Gender']) =="Female":
                db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                    "Pregnancy").set("Patient might be pregnant")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "over work thyroid").set("patient should take Propylthiouracil")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "Using multiple medecines ").set("Direct to the family doctor")
        elif result == 'low':
            self.manager.screens[8].ids.alp.text_color = (210, 210, 10, 1)
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "malnutrition").set("direct to nutritionist")
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "lack of vitamines C B6 B12 Folic acid").set("direct to make blood test")

    def diagnosist(self):
        user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
        db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child("").set("")
        db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
            "cancer").set("0")

        self.wbc_test()
        self.neutrophil_test()
        self.lymphocytes_test()
        self.rbc_test()
        self.hct_test()
        self.urea_test()
        self.hemoglobin_test()
        self.creatine_test()
        self.iron_test()
        self.hdl_test()
        self.alp_test()

        if str(user.val()['Origin']) == '1':
            self.manager.screens[8].ids.nationality.text='Nationality:'+' Israelian'
        elif str(user.val()['Origin']) == '2':
            self.manager.screens[8].ids.nationality.text='Nationality:'+'Easten'
        elif str(user.val()['Origin']) == '3':
            self.manager.screens[8].ids.nationality.text='Nationality:'+'Ethiupian'

    def printteatment(self):

        diseases = db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").get()

        if float(diseases.val()['cancer']) >=0.2:
            db.child("patients").child(self.manager.screens[8].ids.idnum.text).child("diseases").child(
                "cancer").set("Enterctinib")

        self.manager.screens[8].ids.treat.text+=" \n"
        counter=0
        for i in diseases.each():
            self.manager.screens[8].ids.treat.text+=" "+str(i.key())+": "+str(i.val())+", "
            counter+=1
            print("counter")
            if ((int(counter)) % 4) == 0:
                self.manager.screens[8].ids.treat.text += " \n"












    pass


class PProfile(Screen):

    def cancel_button(self):
        self.manager.screens[6].ids.pname.text = ''
        self.manager.screens[6].ids.idnum.text = ''
        self.manager.screens[6].ids.age.text = ''
        self.manager.screens[6].ids.smoker.text = ''
        self.manager.screens[6].ids.diabetes.text = ''
        self.manager.screens[6].ids.bph.text = ''
        self.manager.screens[6].ids.origin.text = ''
        self.manager.screens[6].ids.idnumcheck.text = '0'
        self.manager.screens[6].ids.pnamecheck.text = '0'
        self.manager.screens[6].ids.agecheck.text = '0'
        self.manager.screens[6].ids.smokercheck.text = '0'
        self.manager.screens[6].ids.diabetescheck.text = '0'
        self.manager.screens[6].ids.bphcheck.text = '0'
        self.manager.screens[6].ids.origincheck.text = '0'
        self.manager.current = 'doctorlog'

    def patientname_btn(self):

        if self.manager.screens[6].ids.pname.text == '':  # name input
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        else:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Name").set(
                self.manager.screens[6].ids.pname.text)
            self.manager.screens[6].ids.pnamecheck.text = '1'

    def patientId_btn(self):  ##checking the id number if it's valid and inserting it to the database
        if self.manager.screens[6].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[6].ids.idnum.text) != 9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='insert Id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.idnum.text) == 1 and find_patient(
                self.manager.screens[6].ids.idnum.text) == 0:  # checking that the user doesn't exist before
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("IDnum").set(
                self.manager.screens[6].ids.idnum.text)
            self.manager.screens[6].ids.idnumcheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='This patient already existing')
            pop.open()

    def patientAge_btn(self):
        if self.manager.screens[6].ids.age.text == '':  # checking that it's not empty input
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.age.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif int(self.manager.screens[6].ids.age.text) < 0 or int(self.manager.screens[6].ids.age.text) > 200 or len(
                self.manager.screens[6].ids.age.text) > 3:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) == 1:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Age").set(
                self.manager.screens[6].ids.age.text)
            self.manager.screens[6].ids.agecheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='check the ID first')
            pop.open()

    def patientSmoker_btn(self):
        if self.manager.screens[6].ids.smoker.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.smoker.text == "yes" or self.manager.screens[6].ids.smoker.text == "no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Smoker").set(
                self.manager.screens[6].ids.smoker.text)
            self.manager.screens[6].ids.smokercheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientDiabetes_btn(self):
        if self.manager.screens[6].ids.diabetes.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.diabetes.text == "yes" or self.manager.screens[6].ids.diabetes.text == "no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Diabetes in family").set(
                self.manager.screens[6].ids.diabetes.text)
            self.manager.screens[6].ids.diabetescheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientbph_btn(self):
        if self.manager.screens[6].ids.bph.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.bph.text == "yes" or self.manager.screens[6].ids.bph.text == "no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("blood pressure history").set(
                self.manager.screens[6].ids.bph.text)
            self.manager.screens[6].ids.bphcheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientfever_btn(self):
        if self.manager.screens[6].ids.fever.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.fever.text == "yes" or self.manager.screens[6].ids.fever.text == "no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Fever").set(
                self.manager.screens[6].ids.fever.text)
            self.manager.screens[6].ids.fevercheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientGender_btn(self):
        if self.manager.screens[6].ids.gender.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif str(self.manager.screens[6].ids.gender.text).islower() == str("Female").islower() or str(
                self.manager.screens[6].ids.gender.text).islower() == str("Male").islower():
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Gender").set(
                self.manager.screens[6].ids.gender.text)
            self.manager.screens[6].ids.gendercheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientorigin_btn(self):
        if self.manager.screens[6].ids.origin.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()


        elif numbersonly(self.manager.screens[6].ids.origin.text) == 0:
            pop = MDDialog(title='Error!', text='please choose number for choice 1-israelian 2-ethiopian 3-eastern')
            pop.open()
        elif int(self.manager.screens[6].ids.origin.text) > 3 or int(self.manager.screens[6].ids.origin.text) < 1:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif int(self.manager.screens[6].ids.origin.text) <= 3 or int(self.manager.screens[6].ids.origin.text) > 0:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Origin").set(
                self.manager.screens[6].ids.origin.text)
            self.manager.screens[6].ids.origincheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientPregnant_btn(self):
        if self.manager.screens[6].ids.pregnant.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif int(self.manager.screens[6].ids.gendercheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif str(self.manager.screens[6].ids.gender.text) == "Male" and self.manager.screens[6].ids.pregnant.text == "yes":
            pop = MDDialog(title='Error!', text='Male can not be pregnant')
            pop.open()
        elif self.manager.screens[6].ids.pregnant.text == "yes" or self.manager.screens[6].ids.pregnant.text == "no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Pregnant").set(
                self.manager.screens[6].ids.pregnant.text)
            self.manager.screens[6].ids.pregnantcheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def confirm_button(self):

        if int(self.manager.screens[6].ids.idnumcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient ID input')
            pop.open()
        elif int(self.manager.screens[6].ids.pnamecheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient name input !')
            pop.open()
        elif int(self.manager.screens[6].ids.agecheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient Age input !')
            pop.open()
        elif int(self.manager.screens[6].ids.smokercheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient smoker input!')
            pop.open()
        elif int(self.manager.screens[6].ids.diabetescheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient diabetes input !')
            pop.open()
        elif int(self.manager.screens[6].ids.bphcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient blood pressure input !')
            pop.open()
        elif int(self.manager.screens[6].ids.origincheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient origin input !')
            pop.open()
        elif int(self.manager.screens[6].ids.fevercheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient fever input !')
            pop.open()
        elif int(self.manager.screens[6].ids.gendercheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient gender input !')
            pop.open()
        elif int(self.manager.screens[6].ids.pregnantcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the patient pregnant input !')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) and int(
                self.manager.screens[6].ids.pnamecheck.text) and int(self.manager.screens[6].ids.agecheck.text) and int(
                self.manager.screens[6].ids.smokercheck.text) and int(
                self.manager.screens[6].ids.diabetescheck.text) and int(
                self.manager.screens[6].ids.bphcheck.text) and int(self.manager.screens[6].ids.origincheck.text):
            pop = MDDialog(title='Success!', text='The patient profile has been created !')
            pop.open()
            self.manager.screens[6].ids.pname.text = ''
            self.manager.screens[6].ids.idnum.text = ''
            self.manager.screens[6].ids.age.text = ''
            self.manager.screens[6].ids.smoker.text = ''
            self.manager.screens[6].ids.diabetes.text = ''
            self.manager.screens[6].ids.bph.text = ''
            self.manager.screens[6].ids.origin.text = ''
            self.manager.screens[6].ids.gender.text = ''
            self.manager.screens[6].ids.gendercheck.text = '0'
            self.manager.screens[6].ids.fever.text = ''
            self.manager.screens[6].ids.pregnant.text = ''
            self.manager.screens[6].ids.pregnantcheck.text = '0'
            self.manager.screens[6].ids.fevercheck.text = '0'
            self.manager.screens[6].ids.idnumcheck.text = '0'
            self.manager.screens[6].ids.pnamecheck.text = '0'
            self.manager.screens[6].ids.agecheck.text = '0'
            self.manager.screens[6].ids.smokercheck.text = '0'
            self.manager.screens[6].ids.diabetescheck.text = '0'
            self.manager.screens[6].ids.bphcheck.text = '0'
            self.manager.screens[6].ids.origincheck.text = '0'
            self.manager.current = 'doctorlog'

    pass


class PProfile2(Screen):

    def ID_btn(self):
        if self.manager.screens[7].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[7].ids.idnum.text) != 9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[7].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='Insert id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[7].ids.idnum.text) == 1 and find_patient(
                self.manager.screens[7].ids.idnum.text) == 1:  # checking that the user doesn't exist before
            pop = MDDialog(title='success!', text='Fill the Patient result now')
            pop.open()
            self.manager.screens[7].ids.idcheck.text = '1'
        else:
            pop = MDDialog(title='Error!', text='There is no Patient profile associated with this Id number')
            pop.open()

    def wbc_btn(self):
        if self.manager.screens[7].ids.wbc.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.wbc.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif int(self.manager.screens[7].ids.wbc.text) < 0 or int(self.manager.screens[7].ids.wbc.text) > 50000:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("wbc").set(
                self.manager.screens[7].ids.wbc.text)
            self.manager.screens[7].ids.wbccheck.text = '1'
            pop = MDDialog(title='Success!', text='wbc has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def neutrophil_btn(self):
        if self.manager.screens[7].ids.neutrophil.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.neutrophil.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive numbers only')
            pop.open()
        elif int(self.manager.screens[7].ids.neutrophil.text) < 0 or int(
                self.manager.screens[7].ids.neutrophil.text) > 100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("neutrophil").set(
                self.manager.screens[7].ids.neutrophil.text)
            self.manager.screens[7].ids.neutrophilcheck.text = '1'
            pop = MDDialog(title='Success!', text='neutrophil has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def lymphocytes_btn(self):
        if self.manager.screens[7].ids.lymphocytes.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.lymphocytes.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive numbers only')
            pop.open()
        elif int(self.manager.screens[7].ids.lymphocytes.text) < 0 or int(
                self.manager.screens[7].ids.lymphocytes.text) > 100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("lymphocytes").set(
                self.manager.screens[7].ids.lymphocytes.text)
            self.manager.screens[7].ids.lymphocytescheck.text = '1'
            pop = MDDialog(title='Success!', text='lymphocytes has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def rbc_btn(self):
        if self.manager.screens[7].ids.rbc.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.rbc.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.rbc.text) < 0 or float(self.manager.screens[7].ids.rbc.text) > 10:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("rbc").set(
                self.manager.screens[7].ids.rbc.text)
            self.manager.screens[7].ids.rbccheck.text = '1'
            pop = MDDialog(title='Success!', text='rbc has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def hct_btn(self):
        if self.manager.screens[7].ids.hct.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.hct.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive numbers only')
            pop.open()
        elif int(self.manager.screens[7].ids.hct.text) < 0 or int(self.manager.screens[7].ids.hct.text) > 100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hct").set(
                self.manager.screens[7].ids.hct.text)
            self.manager.screens[7].ids.hctcheck.text = '1'
            pop = MDDialog(title='Success!', text='hct has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def urea_btn(self):

        if self.manager.screens[7].ids.urea.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.urea.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive  numbers only')
            pop.open()
        elif int(self.manager.screens[7].ids.urea.text) < 0 or int(self.manager.screens[7].ids.urea.text) > 100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("urea").set(
                self.manager.screens[7].ids.urea.text)
            self.manager.screens[7].ids.ureacheck.text = '1'
            pop = MDDialog(title='Success!', text='urea has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def hemoglobin_btn(self):

        if self.manager.screens[7].ids.hemoglobin.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.hemoglobin.text) == 0:
            pop = MDDialog(title='Error!', text='please insert positive numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.hemoglobin.text) < 0 or float(
                self.manager.screens[7].ids.hemoglobin.text) > 50:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hemoglobin").set(
                self.manager.screens[7].ids.hemoglobin.text)
            self.manager.screens[7].ids.hemoglobincheck.text = '1'
            pop = MDDialog(title='Success!', text='hemoglobin has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def creatine_btn(self):

        if self.manager.screens[7].ids.creatine.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.creatine.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.creatine.text) < 0 or float(
                self.manager.screens[7].ids.creatine.text) > 5:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("creatine").set(
                self.manager.screens[7].ids.creatine.text)
            self.manager.screens[7].ids.creatinecheck.text = '1'
            pop = MDDialog(title='Success!', text='creatine has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def iron_btn(self):

        if self.manager.screens[7].ids.iron.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.iron.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.iron.text) < 0 or float(self.manager.screens[7].ids.iron.text) > 400:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("iron").set(
                self.manager.screens[7].ids.iron.text)
            self.manager.screens[7].ids.ironcheck.text = '1'
            pop = MDDialog(title='Success!', text='iron has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def hdl_btn(self):

        if self.manager.screens[7].ids.hdl.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.hdl.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.hdl.text) < 0 or float(self.manager.screens[7].ids.hdl.text) > 100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hdl").set(
                self.manager.screens[7].ids.hdl.text)
            self.manager.screens[7].ids.hdlcheck.text = '1'
            pop = MDDialog(title='Success!', text='hdl has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def alp_btn(self):
        if self.manager.screens[7].ids.alp.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif numbersonly(self.manager.screens[7].ids.alp.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif float(self.manager.screens[7].ids.alp.text) < 0 or float(self.manager.screens[7].ids.alp.text) > 300:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("alp").set(
                self.manager.screens[7].ids.alp.text)
            self.manager.screens[7].ids.alpcheck.text = '1'
            pop = MDDialog(title='Success!', text='alp has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()

    def confirm_btn(self):
        if int(self.manager.screens[7].ids.idcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the ID field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.wbccheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the wbc field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.neutrophilcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the neutrophil field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.rbccheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the rbc field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hctcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the hct field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.ureacheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the urea field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hemoglobincheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the hemoglobin field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.creatinecheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the creatine field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.ironcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the iron field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hdlcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the hdl field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.alpcheck.text) != 1:
            pop = MDDialog(title='Error!', text='check the alp field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) and int(self.manager.screens[7].ids.wbccheck.text) and \
                int(self.manager.screens[7].ids.neutrophilcheck.text) and int(self.manager.screens[7].ids.rbccheck.text) \
                and int(self.manager.screens[7].ids.hctcheck.text) and int(
            self.manager.screens[7].ids.ureacheck.text) and \
                int(self.manager.screens[7].ids.hemoglobincheck.text) and int(
            self.manager.screens[7].ids.creatinecheck.text) and \
                int(self.manager.screens[7].ids.ironcheck.text) and int(
            self.manager.screens[7].ids.hdlcheck.text) and int(self.manager.screens[7].ids.alpcheck.text):
            self.manager.screens[7].ids.idcheck.text = '0'
            self.manager.screens[7].ids.wbccheck.text = '0'
            self.manager.screens[7].ids.neutrophilcheck.text = '0'
            self.manager.screens[7].ids.rbccheck.text = '0'
            self.manager.screens[7].ids.hctcheck.text = '0'
            self.manager.screens[7].ids.ureacheck.text = '0'
            self.manager.screens[7].ids.hemoglobincheck.text = '0'
            self.manager.screens[7].ids.creatinecheck.text = '0'
            self.manager.screens[7].ids.ironcheck.text = '0'
            self.manager.screens[7].ids.hdlcheck.text = '0'
            self.manager.screens[7].ids.alpcheck.text = '0'

            self.manager.screens[7].ids.idnum.text = ''
            self.manager.screens[7].ids.wbc.text = ''
            self.manager.screens[7].ids.neutrophil.text = ''
            self.manager.screens[7].ids.rbc.text = ''
            self.manager.screens[7].ids.hct.text = ''
            self.manager.screens[7].ids.urea.text = ''
            self.manager.screens[7].ids.hemoglobin.text = ''
            self.manager.screens[7].ids.creatine.text = ''
            self.manager.screens[7].ids.iron.text = ''
            self.manager.screens[7].ids.hdl.text = ''
            self.manager.screens[7].ids.alp.text = ''
            self.manager.current = 'doctorlog'

    def cancel_btn(self):
        self.manager.screens[7].ids.idcheck.text = '0'
        self.manager.screens[7].ids.wbccheck.text = '0'
        self.manager.screens[7].ids.neutrophilcheck.text = '0'
        self.manager.screens[7].ids.lymphocytescheck.text = '0'
        self.manager.screens[7].ids.rbccheck.text = '0'
        self.manager.screens[7].ids.hctcheck.text = '0'
        self.manager.screens[7].ids.ureacheck.text = '0'
        self.manager.screens[7].ids.hemoglobincheck.text = '0'
        self.manager.screens[7].ids.creatinecheck.text = '0'
        self.manager.screens[7].ids.ironcheck.text = '0'
        self.manager.screens[7].ids.hdlcheck.text = '0'
        self.manager.screens[7].ids.alpcheck.text = '0'

        self.manager.screens[7].ids.idnum.text = ''
        self.manager.screens[7].ids.wbc.text = ''
        self.manager.screens[7].ids.neutrophil.text = ''
        self.manager.screens[7].ids.lymphocytes.text = ''
        self.manager.screens[7].ids.rbc.text = ''
        self.manager.screens[7].ids.hct.text = ''
        self.manager.screens[7].ids.urea.text = ''
        self.manager.screens[7].ids.hemoglobin.text = ''
        self.manager.screens[7].ids.creatine.text = ''
        self.manager.screens[7].ids.iron.text = ''
        self.manager.screens[7].ids.hdl.text = ''
        self.manager.screens[7].ids.alp.text = ''
        self.manager.current = 'doctorlog'

    pass


class MyProfile(Screen):
    def build(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        user = db.child("users").child(user_key).get()
        self.manager.screens[7].ids.thisUser
        self.manager.screens[7].ids.name.text = 'Name:' + ' ' + user.val()['Name']
        self.manager.screens[7].ids.username.text = 'Username:' + ' ' + user.val()['Username']
        self.manager.screens[7].ids.idnum.text = 'ID Number:' + ' ' + user.val()['IDnum']
        self.manager.screens[7].ids.dob.text = 'Date of Birth:' + ' ' + user.val()['DOB']
        self.manager.screens[7].ids.subt.text = 'Title:' + ' ' + user.val()['Title']

    def home_button(self):
        user_key = currentUser(str(self.manager.screens[2].ids.username.text))
        user = db.child("users").child(user_key).get()

        logto = 0
        if str('Teacher') == str(user.val()['Title']):
            logto = 1
        if str('Manager') == str(user.val()['Title']):
            logto = 2
        if logto == 1:
            self.manager.current = 'teacherlog'

        if logto == 2:
            self.manager.current = 'mangerlog'

    def change_dob_D(self):
        dialog = MDDialog(title='Change date of birth', text='test', size_hint=(0.5, 0.5))
        ##dialog.open()

    pass


##login window properties
class RegiWindo(Screen):
    id_box = ObjectProperty(None)
    fullname_box = ObjectProperty(None)
    dob = ObjectProperty(None)
    username_box = ObjectProperty(None)
    password_box = ObjectProperty(None)

    def regibtn(self):

        if self.id_box.text != '' and self.fullname_box.text != '' and self.dob.text != '' and self.username_box.text != '' and self.password_box.text != '':
            if find_user(str(self.id_box.text)) == 0 and username_exist(self.ids.username.text) == 0:
                users_data = {'Name': self.fullname_box.text, 'IDnum': self.id_box.text,
                              'Username': self.username_box.text, 'DOB': self.dob.text, 'pass': self.password_box.text
                    , 'Class': '11',
                              'Title': str('Student')}
                db.child("users").child(str(self.id_box.text)).set(users_data)
                if str(self.id_box.text) == ("315198564"):
                    db.child("users").child("315198564").update({'Title': 'Manager'})
                print("account created successfully")
            else:
                self.sameuser()

        else:
            self.empty()

    def empty(self):
        dialog = MDDialog(title='you forgot to fill one of the boxes')
        dialog.open()

    def sameuser(self):
        dialog = MDDialog(title='you enterd an Existing ID or Username')
        dialog.open()

    pass


class PassReset(Screen):
    def resetPass(self):
        if find_user(str(self.ids.IDnum.text)) == 0:
            no_user()
        else:
            users = db.child("users").get()
            for i in users.each():
                if (str(self.ids.IDnum.text) == str(i.val()['IDnum'])) and (
                        str(self.ids.dob.text) == str(i.val()['DOB'])):
                    db.child("users").child(str(self.ids.IDnum.text)).update({'pass': str(self.ids.newpass.text)})
                    changedsucc()
                    self.manager.current = 'menu'

    pass


class Loginwindo(Screen):
    username_box = ObjectProperty(None)
    password_box = ObjectProperty(None)

    def logbtn(self):

        logto = 0

        if grantAccess(str(self.username_box.text), str(self.password_box.text)) == 1:

            user_key = currentUser(str(self.username_box.text))
            user = db.child("users").child(user_key).get()
            ###init Tool bar names in whole logging in##
            self.manager.screens[3].ids.managertoolbar.title = 'Welcome' + ' ' + user.val()['Name']

            self.manager.screens[4].ids.teachername.title = 'Welcome' + ' ' + user.val()['Name']

            ###Page 9 change name ###
            self.manager.screens[9].ids.username.text = user.val()['Username']

            ###Page 10 change DOB ###
            self.manager.screens[10].ids.username.text = user.val()['Username']
            ###page 11 Student page ###
            self.manager.screens[11].ids.studenttoolbar.title = 'Welcome' + ' ' + user.val()['Name']
            self.manager.screens[11].ids.username.text = user.val()['Username']

            db.child("Online").child(self.username_box.text).set("ok")

            if str('Teacher') == str(user.val()['Title']):
                logto = 1
            if str('Manager') == str(user.val()['Title']):
                logto = 2

            if logto == 2:
                self.manager.current = 'mangerlog'


        else:
            self.invalid()

    def invalid(self):
        dialog = MDDialog(title='Wrong Username or password')
        dialog.open()

    pass


###if grantAccess(str(self.username_box.text), str(self.password_box.text)) == 0:

class reportprob(Screen):
    msgtxt = ObjectProperty(None)
    emailtxt = ObjectProperty(None)
    tnow = datetime.now()

    def printtxt(self):
        email = str(self.emailtxt.text)
        data = {'report': self.msgtxt.text, 'Email': self.emailtxt.text,
                'Date': self.tnow.strftime("%m/%d/%Y, %H:%M:%S")}
        db.child('Report').child(email.split("@")[0]).set(data)

    pass







class Doctor(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_nav)
        return screen

    def navigation_draw(self):
        print("navigation")


Doctor().run()
