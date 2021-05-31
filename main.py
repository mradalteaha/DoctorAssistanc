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
    users=db.child("patients").get()
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
    l=['-','+','_','!','@','#','$','%','^','*','(',')']
    flag=0
    for i in range(0,len(something)):
        if something[i] in l:
            flag=1
    if str(something).isupper() or str(something).islower() or flag==1:
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
    pop = MDDialog(title='Error!',text='Fill the field first')
    close_button = MDFlatButton(text='Close', on_release=pop.dismiss())
    pop.add_widget(close_button)
    pop.open()

def no_user():
    pop = MDDialog(title='Error!This user does not exist')

    pop.open()


def diagnosist(patient):
    diagno=''
    patient=db.child("patients").child("patient").get()




    return diagno

class MenuScreen(Screen):
    pass


class DoctorLog(Screen):
    def home_button(self):
        self.manager.current = 'doctorlog'
    def Pprofile_btn(self):
        self.manager.current = 'pprofile'
    def patientD_btn(self):
        self.manager.current = 'pprofile2'
    pass

    def patientDialog_btn(self):
        self.manager.current = 'pprofile2'
    pass

class ProfileDR(Screen):
    def ID_btn(self):##checking the id number if it's valid and inserting it to the database
        if self.manager.screens[8].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[8].ids.idnum.text) !=9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[8].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='insert Id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[8].ids.idnum.text) == 1 and find_patient(self.manager.screens[8].ids.idnum.text) == 1:#checking that the user doesn't exist before
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            print(self.manager.screens[8].ids)
            user = db.child("patients").child(self.manager.screens[8].ids.idnum.text).get()
            self.manager.screens[8].ids.name.text+=' '+str(user.val()['Name'])
            self.manager.screens[8].ids.idnumb.text += ' ' + str(user.val()['IDnum'])
            self.manager.screens[8].ids.age.text += ' ' + str(user.val()['Age'])
            self.manager.screens[8].ids.nationality.text += ' ' + str(user.val()['Origin'])
            self.manager.screens[8].ids.smoker.text += ' ' + str(user.val()['Smoker'])
            self.manager.screens[8].ids.bph.text += ' ' + str(user.val()['blood pressure history'])
            self.manager.screens[8].ids.diabetes.text += ' ' + str(user.val()['Diabetes in family'])
            self.manager.screens[8].ids.wbc.text += ' ' + str(user.val()['wbc'])
            self.manager.screens[8].ids.neutrophil.text += ' ' + str(user.val()['neutrophil'])
            self.manager.screens[8].ids.lymphocytes.text += ' ' + str(user.val()['lymphocytes'])
            self.manager.screens[8].ids.rbc.text += ' ' + str(user.val()['rbc'])
            self.manager.screens[8].ids.hct.text += ' ' + str(user.val()['hct'])
            self.manager.screens[8].ids.urea.text += ' ' + str(user.val()['urea'])
            self.manager.screens[8].ids.hemoglobin.text += ' ' + str(user.val()['hemoglobin'])
            self.manager.screens[8].ids.creatine.text += ' ' + str(user.val()['creatine'])
            self.manager.screens[8].ids.iron.text += ' ' + str(user.val()['iron'])
            self.manager.screens[8].ids.hdl.text += ' ' + str(user.val()['hdl'])


        else:
            pop = MDDialog(title='Error!', text='This patient already existing')
            pop.open()


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

        if self.manager.screens[6].ids.pname.text == '':#name input
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        else:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Name").set(self.manager.screens[6].ids.pname.text)
            self.manager.screens[6].ids.pnamecheck.text='1'

    def patientId_btn(self):##checking the id number if it's valid and inserting it to the database
        if self.manager.screens[6].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[6].ids.idnum.text) !=9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='insert Id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.idnum.text) == 1 and find_patient(self.manager.screens[6].ids.idnum.text) == 0:#checking that the user doesn't exist before
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("IDnum").set(self.manager.screens[6].ids.idnum.text)
            self.manager.screens[6].ids.idnumcheck.text ='1'
        else:
            pop = MDDialog(title='Error!', text='This patient already existing')
            pop.open()


    def patientAge_btn(self):
        if self.manager.screens[6].ids.age.text == '':#checking that it's not empty input
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif numbersonly(self.manager.screens[6].ids.age.text) == 0:
            pop = MDDialog(title='Error!', text='please insert numbers only')
            pop.open()
        elif int(self.manager.screens[6].ids.age.text) <0 or int(self.manager.screens[6].ids.age.text) >200 or len(self.manager.screens[6].ids.age.text) >3 :
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) ==1:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Age").set(self.manager.screens[6].ids.age.text)
            self.manager.screens[6].ids.agecheck.text='1'
        else:
            pop = MDDialog(title='Error!', text='check the ID first')
            pop.open()
    def patientSmoker_btn(self):
        if self.manager.screens[6].ids.smoker.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.smoker.text =="yes" or self.manager.screens[6].ids.smoker.text =="no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Smoker").set(self.manager.screens[6].ids.smoker.text)
            self.manager.screens[6].ids.smokercheck.text='1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def patientDiabetes_btn(self):
        if self.manager.screens[6].ids.diabetes.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.diabetes.text =="yes" or self.manager.screens[6].ids.diabetes.text =="no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Diabetes in family").set(self.manager.screens[6].ids.diabetes.text)
            self.manager.screens[6].ids.diabetescheck.text='1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
    def patientbph_btn(self):
        if self.manager.screens[6].ids.bph.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.bph.text =="yes" or self.manager.screens[6].ids.bph.text =="no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("blood pressure history").set(self.manager.screens[6].ids.bph.text)
            self.manager.screens[6].ids.bphcheck.text='1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
    def patientfever_btn(self):
        if self.manager.screens[6].ids.fever.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif self.manager.screens[6].ids.fever.text =="yes" or self.manager.screens[6].ids.fever.text =="no":
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Fever").set(self.manager.screens[6].ids.fever.text)
            self.manager.screens[6].ids.fevercheck.text='1'
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
        elif int(self.manager.screens[6].ids.origin.text)>3 or int(self.manager.screens[6].ids.origin.text) <1:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the id number first')
            pop.open()
        elif int(self.manager.screens[6].ids.origin.text)<=3 or int(self.manager.screens[6].ids.origin.text) >0:
            pop = MDDialog(title='Pass!', text='valid input')
            pop.open()
            db.child("patients").child(self.manager.screens[6].ids.idnum.text).child("Origin").set(
                self.manager.screens[6].ids.origin.text)
            self.manager.screens[6].ids.origincheck.text='1'
        else:
            pop = MDDialog(title='Error!', text='Invalid input')
            pop.open()

    def confirm_button(self):


        if int(self.manager.screens[6].ids.idnumcheck.text) !=1:
            pop = MDDialog(title='Error!', text='check the patient ID input')
            pop.open()
        elif int(self.manager.screens[6].ids.pnamecheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient name input !')
            pop.open()
        elif int(self.manager.screens[6].ids.agecheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient Age input !')
            pop.open()
        elif int(self.manager.screens[6].ids.smokercheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient smoker input!')
            pop.open()
        elif int(self.manager.screens[6].ids.diabetescheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient diabetes input !')
            pop.open()
        elif int(self.manager.screens[6].ids.bphcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient blood pressure input !')
            pop.open()
        elif int(self.manager.screens[6].ids.origincheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient origin input !')
            pop.open()
        elif int(self.manager.screens[6].ids.fevercheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the patient origin input !')
            pop.open()
        elif int(self.manager.screens[6].ids.idnumcheck.text) and int(self.manager.screens[6].ids.pnamecheck.text) and int(self.manager.screens[6].ids.agecheck.text) and int(self.manager.screens[6].ids.smokercheck.text) and int(self.manager.screens[6].ids.diabetescheck.text) and int(self.manager.screens[6].ids.bphcheck.text) and int(self.manager.screens[6].ids.origincheck.text):
            pop = MDDialog(title='Success!', text='The patient profile has been created !')
            pop.open()
            self.manager.screens[6].ids.pname.text = ''
            self.manager.screens[6].ids.idnum.text = ''
            self.manager.screens[6].ids.age.text = ''
            self.manager.screens[6].ids.smoker.text = ''
            self.manager.screens[6].ids.diabetes.text = ''
            self.manager.screens[6].ids.bph.text = ''
            self.manager.screens[6].ids.origin.text = ''
            self.manager.screens[6].ids.fever.text = ''
            self.manager.screens[6].ids.fevercheck.text='0'
            self.manager.screens[6].ids.idnumcheck.text='0'
            self.manager.screens[6].ids.pnamecheck.text='0'
            self.manager.screens[6].ids.agecheck.text='0'
            self.manager.screens[6].ids.smokercheck.text='0'
            self.manager.screens[6].ids.diabetescheck.text='0'
            self.manager.screens[6].ids.bphcheck.text='0'
            self.manager.screens[6].ids.origincheck.text='0'
            self.manager.current = 'doctorlog'


    pass

class PProfile2(Screen):

    def ID_btn(self):
        if self.manager.screens[7].ids.idnum.text == '':
            pop = MDDialog(title='Error!', text='Fill the field first')
            pop.open()

        elif len(self.manager.screens[7].ids.idnum.text) !=9:
            pop = MDDialog(title='Error!', text='invalid ID number')
            pop.open()
        elif numbersonly(self.manager.screens[7].ids.idnum.text) == 0:
            pop = MDDialog(title='Error!', text='Insert id with numbers only')
            pop.open()
        elif numbersonly(self.manager.screens[7].ids.idnum.text) == 1 and find_patient(self.manager.screens[7].ids.idnum.text) == 1:#checking that the user doesn't exist before
            pop = MDDialog(title='success!', text='Fill the Patient result now')
            pop.open()
            self.manager.screens[7].ids.idcheck.text='1'
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
        elif int(self.manager.screens[7].ids.wbc.text) <0 or int(self.manager.screens[7].ids.wbc.text)>50000:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("wbc").set(
                self.manager.screens[7].ids.wbc.text)
            self.manager.screens[7].ids.wbccheck.text='1'
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
        elif int(self.manager.screens[7].ids.neutrophil.text) <0 or int(self.manager.screens[7].ids.neutrophil.text)>100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("neutrophil").set(
                self.manager.screens[7].ids.neutrophil.text)
            self.manager.screens[7].ids.neutrophilcheck.text='1'
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
        elif int(self.manager.screens[7].ids.lymphocytes.text) <0 or int(self.manager.screens[7].ids.lymphocytes.text)>100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("lymphocytes").set(
                self.manager.screens[7].ids.lymphocytes.text)
            self.manager.screens[7].ids.lymphocytescheck.text='1'
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
        elif float(self.manager.screens[7].ids.rbc.text) <0 or float(self.manager.screens[7].ids.rbc.text)>10:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("rbc").set(
                self.manager.screens[7].ids.rbc.text)
            self.manager.screens[7].ids.rbccheck.text='1'
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
        elif int(self.manager.screens[7].ids.hct.text) <0 or int(self.manager.screens[7].ids.hct.text)>100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hct").set(
                self.manager.screens[7].ids.hct.text)
            self.manager.screens[7].ids.hctcheck.text='1'
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
        elif int(self.manager.screens[7].ids.urea.text) <0 or int(self.manager.screens[7].ids.urea.text)>100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("urea").set(
                self.manager.screens[7].ids.urea.text)
            self.manager.screens[7].ids.ureacheck.text='1'
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
        elif float(self.manager.screens[7].ids.hemoglobin.text) <0 or float(self.manager.screens[7].ids.hemoglobin.text)>50:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hemoglobin").set(
                self.manager.screens[7].ids.hemoglobin.text)
            self.manager.screens[7].ids.hemoglobincheck.text='1'
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
        elif float(self.manager.screens[7].ids.creatine.text) <0 or float(self.manager.screens[7].ids.creatine.text)>5:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("creatine").set(
                self.manager.screens[7].ids.creatine.text)
            self.manager.screens[7].ids.creatinecheck.text='1'
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
        elif float(self.manager.screens[7].ids.iron.text) <0 or float(self.manager.screens[7].ids.iron.text)>400:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("iron").set(
                self.manager.screens[7].ids.iron.text)
            self.manager.screens[7].ids.ironcheck.text='1'
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
        elif float(self.manager.screens[7].ids.hdl.text) <0 or float(self.manager.screens[7].ids.hdl.text)>100:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("hdl").set(
                self.manager.screens[7].ids.hdl.text)
            self.manager.screens[7].ids.hdlcheck.text='1'
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
        elif float(self.manager.screens[7].ids.alp.text) <0 or float(self.manager.screens[7].ids.alp.text)>200:
            pop = MDDialog(title='Error!', text='input out of possible range ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) == 1:
            db.child("patients").child(self.manager.screens[7].ids.idnum.text).child("alp").set(
                self.manager.screens[7].ids.alp.text)
            self.manager.screens[7].ids.alpcheck.text='1'
            pop = MDDialog(title='Success!', text='alp has been added to the patient profile ')
            pop.open()
        else:
            pop = MDDialog(title='Error!', text='check the ID field first ')
            pop.open()



    def confirm_btn(self):
        if int(self.manager.screens[7].ids.idcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the ID field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.wbccheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the wbc field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.neutrophilcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the neutrophil field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.rbccheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the rbc field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hctcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the hct field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.ureacheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the urea field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hemoglobincheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the hemoglobin field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.creatinecheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the creatine field please ')
            pop.open()

        elif int(self.manager.screens[7].ids.ironcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the iron field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.hdlcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the hdl field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.alpcheck.text)!=1:
            pop = MDDialog(title='Error!', text='check the alp field please ')
            pop.open()
        elif int(self.manager.screens[7].ids.idcheck.text) and int(self.manager.screens[7].ids.wbccheck.text) and\
                int(self.manager.screens[7].ids.neutrophilcheck.text) and int(self.manager.screens[7].ids.rbccheck.text)\
                and int(self.manager.screens[7].ids.hctcheck.text) and int(self.manager.screens[7].ids.ureacheck.text) and\
                int(self.manager.screens[7].ids.hemoglobincheck.text) and int(self.manager.screens[7].ids.creatinecheck.text) and\
                int(self.manager.screens[7].ids.ironcheck.text) and int(self.manager.screens[7].ids.hdlcheck.text) and int(self.manager.screens[7].ids.alpcheck.text):
            self.manager.screens[7].ids.idcheck.text='0'
            self.manager.screens[7].ids.wbccheck.text='0'
            self.manager.screens[7].ids.neutrophilcheck.text='0'
            self.manager.screens[7].ids.rbccheck.text='0'
            self.manager.screens[7].ids.hctcheck.text='0'
            self.manager.screens[7].ids.ureacheck.text='0'
            self.manager.screens[7].ids.hemoglobincheck.text='0'
            self.manager.screens[7].ids.creatinecheck.text='0'
            self.manager.screens[7].ids.ironcheck.text='0'
            self.manager.screens[7].ids.hdlcheck.text='0'
            self.manager.screens[7].ids.alpcheck.text='0'

            self.manager.screens[7].ids.id.text=''
            self.manager.screens[7].ids.wbc.text=''
            self.manager.screens[7].ids.neutrophil.text=''
            self.manager.screens[7].ids.rbc.text=''
            self.manager.screens[7].ids.hct.text=''
            self.manager.screens[7].ids.urea.text=''
            self.manager.screens[7].ids.hemoglobin.text=''
            self.manager.screens[7].ids.creatine.text=''
            self.manager.screens[7].ids.iron.text=''
            self.manager.screens[7].ids.hdl.text=''
            self.manager.screens[7].ids.alp.text=''
            self.manager.current = 'doctorlog'






    def cancel_btn(self):
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

        self.manager.screens[7].ids.id.text = ''
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


class ManagClass(Screen):
    menu = ObjectProperty(None)

    def build(self):

        daylist = ["sunday", "monday", "tuesday", "wednesday", "thursday"]
        timelist = ["8:00", "8:45", "9:30", "10:15", "11:30", "12:45", "13:30"]
        for i in daylist:
            items = OneLineListItem(text=str(i))
            items.bind(on_release=self.manager.screens[16].set_itemday)
            self.manager.screens[16].ids.menuday.add_widget(items)

        for i in timelist:
            items = OneLineListItem(text=str(i))
            items.bind(on_release=self.manager.screens[16].set_itemtime)
            self.manager.screens[16].ids.menutime.add_widget(items)

    def set_itemtime(self, text_of_the_option):
        self.manager.screens[16].ids.timepicked.text = text_of_the_option.text

    def set_itemday(self, text_of_the_option):
        self.manager.screens[16].ids.daypicked.text = text_of_the_option.text

    def data_submit(self):
        teachersub = db.child("users").child(self.manager.screens[16].ids.idt.text).get()

        db.child("Class").child(self.manager.screens[16].ids.classid.text).child("Schedule").child(
            str(self.manager.screens[16].ids.daypicked.text)).child(
            str(self.manager.screens[16].ids.timepicked.text)).set(teachersub.val()['Subject'])

    pass





class clsspress(Screen):
    tnow = datetime.now()

    def build(self):
        students = db.child("Class").child("11").child("Students").get()

        for sub in students.each():
            stud = db.child('users').child(sub.key()).get()
            items = OneLineListItem(text=str(stud.val()['Username']))
            items.bind(on_release=self.manager.screens[20].present)
            self.manager.screens[20].ids.studlist.add_widget(items)

    def present(self, text):
        thisuser = db.child("users").get()
        for u in thisuser.each():
            if u.val()["Username"] == str(text.text):
                db.child("users").child(str(u.key())).child("present").child(
                    self.tnow.strftime("%d,%m,%Y, %H:%M:%S")).set("checked")

    def home_button(self):
        self.manager.screens[20].ids.studlist.clear_widgets()
        self.manager.current = 'teacherlog'

    pass





class Doctor(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Blue'
        screen = Builder.load_string(screen_nav)
        return screen

    def navigation_draw(self):
        print("navigation")


Doctor().run()
