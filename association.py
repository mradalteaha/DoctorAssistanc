screen_nav = """

ScreenManager:
    MenuScreen:
    RegiWindo:
    Loginwindo:
    DoctorLog:
    MyProfile:
    PassReset:
    CreatePatientProfile:
    AddPatientTests:
    StreamPatientDiagnosis:
   




<MenuScreen>:
    name:'menu'

    MDRectangleFlatButton:
        text:'Log In'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint:0.5,0.2
        on_release:
            root.manager.current='Login'
    MDRectangleFlatButton:
        text:'Sign Up'
        pos_hint:{'center_x':0.5,'center_y':0.2}
        size_hint:0.5,0.2
        on_release:
            root.manager.current='Register'
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        title: 'Welcome to Doctor associate app'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'doc.png'


                MDLabel:
                    text:'  Welcome '
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Log in'
                            on_press:
                                root.manager.current='Login'
                            IconLeftWidget:
                                icon:'login'
                              
                        OneLineIconListItem:
                            text:'Sign Up'
                            on_press:
                                root.manager.current='Register'
                            IconLeftWidget:
                                icon:'face-woman'
 



<RegiWindo>
    name:'Register'
    id_box:idnum
    fullname_box:f_name
    dob:date
    username_box:username
    password_box:pass_word

    MDToolbar:
        title: 'Register'
        elevation: 10
        pos_hint: {'top': 1}
    MDTextField:
        hint_text:"ID number"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
        id:idnum
        multiline:False
    MDTextField:
        hint_text:"Full Name"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:f_name
        multiline:False
    MDTextField:
        hint_text:"date of birth(dd/mm/yyyy)"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:date
        multiline:False
    MDTextField:
        hint_text:"Username"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
        id:username
        multiline:False
    MDTextField:
        hint_text:"Password"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300
        id:pass_word
        password:True
        multiline:False
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':0.3,'center_y':0.2} 
        width:300
        on_release:
            root.regibtn()
    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'center_x':0.8,'center_y':0.2} 
        width:300
        on_release:
            root.manager.current='menu'

<Loginwindo>
    name:'Login'
    username_box:username
    password_box:pass_word
    id:container
    MDToolbar:
        title: 'Log In'
        elevation: 10
        pos_hint: {'top': 1}

    MDTextField:
        hint_text:"Username"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
        id:username
        multiline:False
    MDTextField:
        hint_text:"Password"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:pass_word
        password:True
        multiline:False

    MDTextField:
        hint_text:"ID number"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:idnum
        max_text_length:9
        multiline:False    

    MDRectangleFlatButton:
        text:'Log In'
        pos_hint:{'center_x':0.3,'center_y':0.4} 
        width:300
        on_release:
            root.logbtn()

    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'center_x':0.8,'center_y':0.3} 
        width:300
        on_release:
            root.manager.current='menu'    
    MDRectangleFlatButton:
        text:'Reset Password'
        pos_hint:{'center_x':0.8,'center_y':0.2} 
        width:300
        on_release:
            root.manager.current='Preset'


<DoctorLog>
    name:'doctorlog'
    id:currentuser

    MDRectangleFlatButton:
        text:'Create patient profile'
        pos_hint:{'center_x':0.9,'top':0.8}
        size_hint:0.2,0.2
        on_release:
            root.Pprofile_btn()
 

    MDRectangleFlatButton:
        id:patientdiagnosist
        text:'Add Patient tests'
        pos_hint:{'center_x':0.9,'top':0.6}
        size_hint:0.2,0.2
        on_release:
            root.patientD_btn()
            
    MDRectangleFlatButton:
        text:'Patient Diagnosis'
        pos_hint:{'center_x':0.9,'top':0.4}
        size_hint:0.2,0.2
        on_release:
            root.patientDiagnosist_btn()


       


    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:managertoolbar
                        title: 'Welcome Doctor'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'doc.png'


                MDLabel:   
                    text:'  Welcome'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                               
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'





<MyProfile>
    name:"myprofile"      
    MDToolbar:
        id:thisUser
        title: 'My Profile'
        elevation: 10
        pos_hint: {'top': 1}
    MDLabel:
        id:name
        text:
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:300
    MDLabel:
        id:username
        text:
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
    MDLabel:
        id:idnum
        text:
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
    MDLabel:
        id:dob
        text:
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
    MDLabel:
        id:subt
        text:
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:300

    MDRectangleFlatButton:
        text:'Change'
        pos_hint:{'center_x':0.8,'center_y':0.7} 
        width:300
        on_release:
            root.manager.current='chname'

    MDRectangleFlatButton:
        text:'Change'
        pos_hint:{'center_x':0.8,'center_y':0.4} 
        width:300
        on_release:
            root.manager.current='chdob'              


    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation:'vertical'
                    MDToolbar:
                        id:test
                        title: 'My Profile'
                        left_action_items:[["menu",lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:8
                    Widget:          
        MDNavigationDrawer:
            id: nav_drawer

            BoxLayout:
                orientation:'vertical'

                spacing: '8dp'
                padding: '8dp'
                Image:
                    source:'doc.png'


                MDLabel:
                    text:'  Welcome'
                    font_style:'Caption'
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:
                    MDList:
                        OneLineIconListItem:
                            text:'Profile'
                            on_release:
                                root.manager.current='myprofile'             
                            IconLeftWidget:
                                icon:'face-profile'

                        OneLineIconListItem:
                            text:'Home Page'
                            on_press:
                                root.home_button()
                            IconLeftWidget:
                                icon:'home'                                 
                        OneLineIconListItem:
                            text:'Log Out'
                            on_press:
                                root.manager.current='menu'
                            IconLeftWidget:
                                icon:'logout'
                                
                                
                                
<PassReset>
    name:'Preset'
    MDToolbar:
        title: 'Password Reset'
        elevation: 10
        pos_hint: {'top': 1}        
    MDTextField:
        hint_text:"Enter User ID number"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:300
        id:IDnum
        multiline:False
    MDTextField:
        hint_text:"Enter User Date of Birth"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:300
        id:dob
        multiline:False
    MDTextField:
        hint_text:"Enter New Password"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:300
        id:newpass
        password:True
        multiline:False

    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'center_x':0.3,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.resetPass()

    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'center_x':0.6,'center_y':0.2} 
        size_hint:0.2,0.2
        on_release:
            root.manager.current='menu'        
                                 

<CreatePatientProfile>
    name:'pprofile'
    
    MDToolbar:
        title: 'Create Patient Profile'
        elevation: 10
        pos_hint: {'top': 1}
       
    MDTextField:
        hint_text:"Enter Patient name"
        pos_hint:{'center_x':0.1,'center_y':0.7}
        size_hint_x:None
        width:150
        length:100
        id:pname
        multiline:False
    MDLabel:
        id:pnamecheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.7}
        size_hint:0.08,0.05
        on_release:
            root.patientname_btn()
    MDTextField:
        hint_text:"Enter patient ID"
        pos_hint:{'center_x':0.1,'center_y':0.8}
        size_hint_x:None
        width:150
        length:100
        max_text_length:9
        id:idnum
        multiline:False
        
    MDLabel:
        id:idnumcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.8}
        size_hint:0.08,0.05
        on_release:
            root.patientId_btn()
    MDTextField:
        hint_text:"Enter Patient Age"
        pos_hint:{'center_x':0.1,'center_y':0.6}
        size_hint_x:None
        width:150
        length:100
        max_text_length:2
        id:age
        multiline:False
        
    MDLabel:
        id:agecheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.6}
        size_hint:0.08,0.05
        on_release:
            root.patientAge_btn()
    MDTextField:
        hint_text:"Smoker? (Yes/NO)"
        pos_hint:{'center_x':0.1,'center_y':0.5}
        size_hint_x:None
        width:150
        length:100
        max_text_length:3
        id:smoker
        multiline:False
    MDLabel:
        id:smokercheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.5}
        size_hint:0.08,0.05
        on_release:
            root.patientSmoker_btn()
    MDTextField:
        hint_text:"Diabets in family? (Yes/NO)"
        pos_hint:{'center_x':0.1,'center_y':0.4}
        size_hint_x:None
        width:150
        length:100
        max_text_length:3
        id:diabetes
        multiline:False
        
    MDLabel:
        id:diabetescheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.3,'center_y':0.4}
        size_hint:0.08,0.05
        on_release:
            root.patientDiabetes_btn()
    MDTextField:
        hint_text:"blood pressure history? (Yes/NO)"
        pos_hint:{'center_x':0.1,'center_y':0.3}
        size_hint_x:None
        width:150
        length:100
        max_text_length:3
        id:bph
        multiline:False
    MDLabel:
        id:bphcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.35,'center_y':0.3}
        size_hint:0.08,0.05
        on_release:
            root.patientbph_btn()

    MDTextField:
        hint_text:"origin:1-israelian,2-eastern,3-ethupia"
        pos_hint:{'center_x':0.1,'center_y':0.2}
        size_hint_x:None
        width:150
        length:200
        max_text_length:1
        id:origin
        multiline:False
    MDLabel:
        id:origincheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.4,'center_y':0.2}
        size_hint:0.08,0.05
        on_release:
            root.patientorigin_btn()

    MDTextField:
        hint_text:"do u have fever(Yes,No)"
        pos_hint:{'center_x':0.5,'center_y':0.8}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:fever
        multiline:False
    MDLabel:
        id:fevercheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.8}
        size_hint:0.08,0.05
        on_release:
            root.patientfever_btn()

    MDTextField:
        hint_text:"Gender(Male,Female)"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:150
        length:200
        max_text_length:5
        id:gender
        multiline:False
    MDLabel:
        id:gendercheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.7}
        size_hint:0.08,0.05
        on_release:
            root.patientGender_btn()
    MDTextField:
        hint_text:"pregnant?(Yes/No)"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:pregnant
        multiline:False
    MDLabel:
        id:pregnantcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.6}
        size_hint:0.08,0.05
        on_release:
            root.patientPregnant_btn()



                                                  
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'x':0.3,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.confirm_button()
    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'x':0.5,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.cancel_button()  


<AddPatientTests>
    name:'pprofile2'
    
    MDToolbar:
        title: 'Patient Examination'
        elevation: 10
        pos_hint: {'top': 1}
    MDTextField:
        hint_text:"Enter patient ID"
        pos_hint:{'center_x':0.4,'center_y':0.8}
        size_hint_x:None
        width:150
        length:100
        max_text_length:9
        id:idnum
  
        multiline:False
    MDLabel:
        id:idcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.65,'center_y':0.8}
        size_hint:0.08,0.05
        on_release:
            root.ID_btn()       
    MDTextField:
        hint_text:"White blood cells"
        pos_hint:{'center_x':0.1,'center_y':0.7}
        size_hint_x:None
        width:150
        length:100
        id:wbc
        max_text_len:5
        multiline:False
    MDLabel:
        id:wbccheck
        text:'0'    
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.7}
        size_hint:0.08,0.05
        on_release:
            root.wbc_btn()
    MDTextField:
        hint_text:"Neutrophil"
        pos_hint:{'center_x':0.1,'center_y':0.6}
        size_hint_x:None
        width:150
        length:100
        max_text_length:2
        id:neutrophil
        multiline:False
        

    MDLabel:
        id:neutrophilcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.6}
        size_hint:0.08,0.05
        on_release:
            root.neutrophil_btn()
    MDTextField:
        hint_text:"Lymphocytes"
        pos_hint:{'center_x':0.1,'center_y':0.5}
        size_hint_x:None
        width:150
        length:100
        max_text_length:2
        id:lymphocytes
        multiline:False
    MDLabel:
        id:lymphocytescheck
        text:'0'        
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.5}
        size_hint:0.08,0.05
        on_release:
            root.lymphocytes_btn()
    MDTextField:
        hint_text:"Red Blood Cells"
        pos_hint:{'center_x':0.1,'center_y':0.4}
        size_hint_x:None
        width:150
        length:100
        max_text_length:3
        id:rbc
        multiline:False
    MDLabel:
        id:rbccheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.4}
        size_hint:0.08,0.05
        on_release:
            root.rbc_btn()
    MDTextField:
        hint_text:"HCT"
        pos_hint:{'center_x':0.1,'center_y':0.3}
        size_hint_x:None
        width:150
        length:100
        max_text_length:2
        id:hct
        multiline:False
    MDLabel:
        id:hctcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.3}
        size_hint:0.08,0.05
        on_release:
            root.hct_btn()
    MDTextField:
        hint_text:"Urea"
        pos_hint:{'center_x':0.1,'center_y':0.2}
        size_hint_x:None
        width:150
        length:100
        max_text_length:2
        id:urea
        multiline:False
        
    MDLabel:
        id:ureacheck
        text:'0'
        
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.25,'center_y':0.2}
        size_hint:0.08,0.05
        on_release:
            root.urea_btn()

    MDTextField:
        hint_text:"Hemoglobin"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:hemoglobin
        multiline:False
    MDLabel:
        id:hemoglobincheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.7}
        size_hint:0.08,0.05
        on_release:
            root.hemoglobin_btn()
    MDTextField:
        hint_text:"Creatine"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:creatine
        multiline:False
    MDLabel:
        id:creatinecheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.6}
        size_hint:0.08,0.05
        on_release:
            root.creatine_btn()

    MDTextField:
        hint_text:"Iron"
        pos_hint:{'center_x':0.5,'center_y':0.5}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:iron
        multiline:False
    MDLabel:
        id:ironcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.5}
        size_hint:0.08,0.05
        on_release:
            root.iron_btn()

    MDTextField:
        hint_text:"High Density Lipoprotein"
        pos_hint:{'center_x':0.5,'center_y':0.4}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:hdl
        multiline:False
    MDLabel:
        id:hdlcheck
        text:'0'
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.4}
        size_hint:0.08,0.05
        on_release:
            root.hdl_btn()

    MDTextField:
        hint_text:"Alkaline phosphatase"
        pos_hint:{'center_x':0.5,'center_y':0.3}
        size_hint_x:None
        width:150
        length:200
        max_text_length:3
        id:alp
        multiline:False
    MDLabel:
        id:alpcheck
        text:'0'    
    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.7,'center_y':0.3}
        size_hint:0.08,0.05
        on_release:
            root.alp_btn()



                                                  
    MDRectangleFlatButton:
        text:'Confirm'
        pos_hint:{'x':0.3,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.confirm_btn()
            

    MDRectangleFlatButton:
        text:'Cancel'
        pos_hint:{'x':0.5,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.cancel_btn()  


<StreamPatientDiagnosis>
    name:'profileDR'
    MDToolbar:
        title: 'Patient Diagnosist and treatment'
        elevation: 10
        pos_hint: {'top': 1} 
    MDTextField:
        hint_text:"Enter patient ID"
        pos_hint:{'center_x':0.4,'center_y':0.85}
        size_hint_x:None
        width:150
        length:100
        max_text_length:9
        id:idnum
  
        multiline:False

    MDRectangleFlatButton:
        text:'Check'
        pos_hint:{'center_x':0.65,'center_y':0.85}
        size_hint:0.08,0.05
        on_release:
            root.ID_btn()       
    
    MDLabel:
        id:name
        text:'Name:'
        pos_hint:{'center_x':0.2,'center_y':0.75}
        size_hint_x:None
        width:300   
    MDLabel:
        id:idnumb
        text:'ID:'
        pos_hint:{'center_x':0.2,'center_y':0.7}
        size_hint_x:None
        width:300      
    MDLabel:
        id:age
        text:'Age:'
        pos_hint:{'center_x':0.2,'center_y':0.65}
        size_hint_x:None
        width:300      
    MDLabel:
        id:gender
        text:'Gender:'
        pos_hint:{'center_x':0.2,'center_y':0.6}
        size_hint_x:None
        width:300   
    MDLabel:
        id:nationality
        text:'Nationality:'
        pos_hint:{'center_x':0.2,'center_y':0.55}
        size_hint_x:None
        width:300      

    MDLabel:
        id:smoker
        text:'Smoker:'
        pos_hint:{'center_x':0.45,'center_y':0.75}
        size_hint_x:None
        width:300      

    MDLabel:
        id:bph
        text:'Blood pressure:'
        pos_hint:{'center_x':0.45,'center_y':0.7}
        size_hint_x:None
        width:300      

    MDLabel:
        id:diabetes
        text:'Diabetes:'
        pos_hint:{'center_x':0.45,'center_y':0.65}
        size_hint_x:None
        width:300      

    MDLabel:
        id:pregnant
        text:'Pregnant:'
        pos_hint:{'center_x':0.45,'center_y':0.6}
        size_hint_x:None
        
        width:300      
    MDLabel:
        id:wbc
        text:'WBC:'
        pos_hint:{'center_x':0.45,'center_y':0.55}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300     
    MDLabel:
        id:neutrophil
        text:'Neutrophil:'
        pos_hint:{'center_x':0.75,'center_y':0.75}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:fever
        text:'Fever:'
        pos_hint:{'center_x':0.75,'center_y':0.7}
        size_hint_x:None
        width:300      
    MDLabel:
        id:lymphocytes
        text:'Lymphocytes:'
        pos_hint:{'center_x':0.75,'center_y':0.65}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300     
    MDLabel:
        id:rbc
        text:'RBC:'
        pos_hint:{'center_x':0.75,'center_y':0.6}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:hct
        text:'HCT:'
        pos_hint:{'center_x':0.75,'center_y':0.55}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:urea
        text:'Urea:'
        pos_hint:{'center_x':1,'center_y':0.8}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:hemoglobin
        text:'Hemoglobin:'
        pos_hint:{'center_x':1,'center_y':0.75}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:creatine
        text:'Creatine:'
        pos_hint:{'center_x':1,'center_y':0.7}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:iron
        text:'Iron:'
        pos_hint:{'center_x':1,'center_y':0.65}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300      

    MDLabel:
        id:hdl
        text:'HDL:'
        pos_hint:{'center_x':1,'center_y':0.6}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300
    MDLabel:
        id:alp
        text:'AlP:'
        pos_hint:{'center_x':1,'center_y':0.55}
        size_hint_x:None
        theme_text_color:'Custom'
        width:300
               
    MDLabel:
        id:treat
        text:'Diagnosist & Treatment:'
        pos_hint:{'center_x':0.5,'center_y':0.25}
        size_hint_x:None
        width:700
        length:300
                


                                                     
    MDRectangleFlatButton:
        text:'Save'
        pos_hint:{'x':0.3,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.SaveToFile_btn()
            

    MDRectangleFlatButton:
        text:'Back'
        pos_hint:{'x':0.5,'y':0.0} 
        size_hint:0.2,0.1
        on_release:
            root.cancel_btn()  
            
            
            
"""