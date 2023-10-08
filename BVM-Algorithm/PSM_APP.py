import xlwt
from PIL import ImageGrab
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
Window.maximize()
import time
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton
# from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDRoundFlatIconButton
from kivy.uix.slider import Slider
from kivymd.uix.label import MDLabel
import os
from pyzbar.pyzbar import decode
import xlwt as xw
import xlrd
from datetime import datetime
import mysql.connector
from xlwt import Workbook
from kivy.properties import ObjectProperty
from kivy.properties import NumericProperty
import numpy as np
cam = False
#import sqlite3
import mysql.connector
from time import *
screen_helper = """

<TooltipMDIconButton@MDIconButton+MDTooltip>
#: import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManager:
    transition: FadeTransition()
    WelcomeScreen:
    StandbyScreen:
    NewScreen:
    FirstScreen:
    LoginUserScreen:
    RegisterUserScreen:
    CameraScreen:
    HelpScreen:


<Content>
    orientation: "vertical"
    spacing: "5dp"
    size_hint_y: None
    height: "300dp"

    MDLabel: 
        text: "This app is developed by Kandolo Jire Christian and Georgina Mampuru"
        color: 0, 0.1, 0.5, 1.0
        # size_hint: (1,1)
        pos_hint: {'center_x':0.53,'center_y':0.8}
        font_name: "ultra"
        # color:13, 27, 186
        font_size: "18sp"
        multiline: True
        bold: True
        
    MDLabel:
        text: "Phone number\\nTel: +27814042723/+27606883521\\nEmail: 218049862@mycput.ac.za/216001579@mycput.ac.za"
        id: email
        color: 0, 0.1, 0.5, 1.0
        # size_hint: (1,1)
        pos_hint: {'center_x':0.53,'center_y':0.4}
        font_name: "Roboto"
        font_size: "18sp"
        # color:13, 27, 186
        multiline: True
        bold: True 
<Explain>
    orientation: "vertical"
    spacing: "5dp"
    size_hint_y: None
    height: "300dp"

    MDLabel: 
        text: "This device   an automated bag valve mask ventilator developped for monitoring covid-19 patient "
        color: 0, 0.1, 0.5, 1.0
        # size_hint: (1,1)
        pos_hint: {'center_x':0.53,'center_y':0.8}
        font_name: "ultra"
        # color:13, 27, 186
        font_size: "18sp"
        multiline: True
        bold: True

<WelcomeScreen>:
    name: 'welcome'

    FloatLayout:
        orientation: 'vertical'
        canvas.before:

            Color:
                rgba: 1, 1, 1, 1  
            Rectangle:
                pos: self.pos
                size: self.size
        Image:
            id: imageView
            source: 'medin.png'
            pos_hint: {'center_x':0.8,'center_y':0.4}
            # size_hint_y: 1.2
            size_hint: (0.6,0.6)
            # width: 100
            allow_stretch: True
        Image:
            id: imageView
            source: 'merseta.jpg'
            pos_hint: {'center_x':0.3,'center_y':0.43}
            # size_hint_y: 0.5
            size_hint: (0.4,0.4)
            # width:50
            allow_stretch: True
    
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: " Automated Bag Valve  Mask Ventilator"
                pos_hint: {'center_x':0.72,'center_y':0.8}
                color:0, 0, 0
                # mode: "fill"
                font_size: "40sp"
                font_name: "Ultra"
                bold: True

<StandbyScreen>:
    name: 'standby'
    FloatLayout:
        orientation: 'vertical'
        canvas.before:

            Color:
                rgba: 0, 0.04, 0.15, 0.83  
            Rectangle:
                pos: self.pos
                size: self.size

        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "STANDBY MODE"
                pos_hint: {'center_x':0.77,'center_y':0.9}
                color:0, 0, 0
                # mode: "fill"
                font_size: "80sp"
                font_name: "Ultra"
                bold: True
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "STANDBY MODE"
                pos_hint: {'center_x':0.77,'center_y':0.9}
                color:0, 0, 0
                # mode: "fill"
                font_size: "80sp"
                font_name: "Ultra"
                bold: True
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "UserName"
                pos_hint: {'center_x':0.95,'center_y':0.5}
                color:0, 0, 0
                # mode: "fill"
                font_size: "30sp"
                font_name: "Ultra"
                bold: True
                spacing :20
        FloatLayout:
            orientation: 'vertical'    
            spacing :20

            MDLabel:
                multiline: True
                text: "Password"
                pos_hint: {'center_x':0.95,'center_y':0.35}
                color:0, 0, 0
                # mode: "fill"
                font_size: "30sp"
                font_name: "Ultra"
                bold: True  
            MDTextFieldRound:
            
                icon_left: "account-check"
                hint_text: "Username"
                foreground_color: 1, 0, 1, 1
                spacing :20
                size_hint:(0.15,0.05)
                padding_x: 20
                # pos_hint: {"center_x": 0.5}
                pos_hint: {'center_x':0.5,'center_y':0.45}
            MDTextFieldRound:
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                foreground_color: 1, 0, 1, 1
                hint_text: "Password"
                size_hint:(0.15,0.05)
                # padding_x: 20
                # pos_hint: {"center_x": 0.5}
                pos_hint: {'center_x':0.5,'center_y':0.3}
            MDRoundFlatButton:
                text: 'Login'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                md_bg_color: app.theme_cls.primary_color 
                pos_hint: {"center_x": 0.5}
                spacing:0
                # padding:50
                on_press: root.proceed()
                pos_hint: {'center_x':0.45,'center_y':0.1}
            MDRoundFlatButton:
                text: 'Register new user'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                md_bg_color: app.theme_cls.primary_color 
                on_press: root.go()
                pos_hint: {'center_x':0.6,'center_y':0.1}
                
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color 
            Rectangle:
                pos: self.pos
                size: self.size
        # MDToolbar:
        #     # title: "Tools"
        #     # size_hint: (0.1,1)
        #     height: '40'
        #     color:13, 27, 186
        #     # pos_hint: {'center_x':0.5,'center_y':0.96}
        #     md_bg_color: 0.1, 0.4, 0.5, 0.9
        #     left_action_items: [["about.PNG", lambda x: app.about()], ["alpha-f-box-outline",lambda x: root.first()],\
        #    ["account-plus",lambda x: root.add_user()],["account-check",lambda x: register_user()],\
        # #    ["camera",lambda x: root.camera()],["alpha-h-box",lambda x: root.help(),"alpha-h-box",lambda x: root.help(),]] 
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1,0.05)
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_dark
                Rectangle:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1,0.05)
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_dark
                Rectangle:
                    pos: self.pos
                    size: self.size            

            # TooltipMDIconButton:
            #     icon: "human-male"
            #     tooltip_text: "about app"
            #     pos_hint: {"center_x": .5, "center_y": .5}
            #     on_press: print("hello world")
            #     # md_bg_color:  app.theme_cls.primary_color 
            TooltipMDIconButton:
                icon: "information-variant"
                tooltip_text: "about the device"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.device()
                # md_bg_color:  app.theme_cls.primary_color 
            TooltipMDIconButton:
                icon: "chart-line"
                tooltip_text: "Record snapshot"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press:app.screengrab()
                # md_bg_color:  app.theme_cls.primary_color 
            TooltipMDIconButton:
                icon: "alpha-a-box"
                tooltip_text: "Patient Data"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: 
                # md_bg_color:  app.theme_cls.primary_color 
            TooltipMDIconButton:
                icon: "card-text-outline"
                tooltip_text: "user manual"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: 
                # md_bg_color:  app.theme_cls.primary_color
            TooltipMDIconButton:
                icon: "home"
                tooltip_text: "home"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: root.proceed()
                # md_bg_color:  app.theme_cls.primary_color 
        BoxLayout:
            orientation: 'vertical'
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_color 
                Rectangle:
                    pos: self.pos
                    size: self.size
            FloatLayout:
                MDRectangleFlatButton:
                    text: 'VISUALIZE '
                    # size_hint: (1,0.3)
                    text_color: 1, 1, 1, 1
                    font_name: "Ultra"
                    bold: True
                    md_bg_color:   0.1, 0.9, 0.5, 0.9
                    on_press: print("HI")
                    pos_hint: {'center_x':0.5,'center_y':0.9}
                MDLabel:
                    id: time
                    text: 
                    pos_hint: {'center_x':0.2,'center_y':0.9}
                    color:1, 1, 1
                    halign: 'center'
                    # mode: "fill"
                    font_size: "30sp"
                    font_name: "ultra"
                    bold: True
                MDFillRoundFlatButton:
                    text: 'proceed'
                    text_color: 1, 1, 1, 1
                    font_name: "Ultra"
                    bold: True
                    color :  0, 1, 0, 1
                    on_press: 
                    pos_hint: {'center_x':0.5,'center_y':0.6}  
                    
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1,0.05)
            canvas.before:
                Color:
                    rgba: app.theme_cls.primary_dark
                Rectangle:
                    pos: self.pos
                    size: self.size    
            TooltipMDIconButton:
                icon: "led-variant-off"
                tooltip_text: "turn off alarm"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.about()
                # md_bg_color:  app.theme_cls.primary_color 
                
        # FloatLayout:
        #     # cols: 1
        #     # id: grid
        #     # orientation: 'vertical'
        # 
        #     # spacing:[6,6]
        #     # padding: 6
        #     MDRectangleFlatButton:
        #         id: Generate
        #         text: 'Front panel'
        #         text_color: 1, 1, 1, 1
        #         font_name: "Ultra"
        #         bold: True
        #         on_press: root.label()
        #         pos_hint: {'center_x':0.5,'center_y':0.5}
<NewScreen>:
    name: 'new'
    FloatLayout:
        orientation: 'vertical'
        canvas.before:

            Color:
                rgba: 0, 0.04, 0.15, 0.83  
            Rectangle:
                pos: self.pos
                size: self.size

        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "new user"
                pos_hint: {'center_x':0.77,'center_y':0.9}
                color:0, 0, 0
                # mode: "fill"
                font_size: "80sp"
                font_name: "Ultra"
                bold: True
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "new user"
                pos_hint: {'center_x':0.77,'center_y':0.9}
                color:0, 0, 0
                # mode: "fill"
                font_size: "80sp"
                font_name: "Ultra"
                bold: True
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "UserName"
                pos_hint: {'center_x':0.95,'center_y':0.5}
                color:0, 0, 0
                # mode: "fill"
                font_size: "30sp"
                font_name: "Ultra"
                bold: True
                spacing :20
        FloatLayout:
            orientation: 'vertical'    
            spacing :20
            MDLabel:
                multiline: True
                text: "Password"
                pos_hint: {'center_x':0.95,'center_y':0.35}
                color:0, 0, 0
                # mode: "fill"
                font_size: "30sp"
                font_name: "Ultra"
                bold: True  
            MDTextFieldRound:
                id:word_label
                icon_left: "account-check"
                hint_text: "Username"
                foreground_color: 1, 0, 1, 1
                spacing :20
                size_hint:(0.15,0.05)
                padding_x: 20
                # pos_hint: {"center_x": 0.5}
                pos_hint: {'center_x':0.5,'center_y':0.45}
            MDTextFieldRound:
                id:word_input
                icon_left: 'key-variant'
                icon_right: 'eye-off'
                foreground_color: 1, 0, 1, 1
                hint_text: "Password"
                size_hint:(0.15,0.05)
                # padding_x: 20
                # pos_hint: {"center_x": 0.5}
                pos_hint: {'center_x':0.5,'center_y':0.3}
            MDRoundFlatButton:
                text: 'SAVE'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                md_bg_color: app.theme_cls.primary_color 
                on_press: app.submit()
                pos_hint: {'center_x':0.5,'center_y':0.1}
                
<LoginUserScreen>:
    name: 'login'
    BoxLayout:
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color 
            Rectangle:
                pos: self.pos
                size: self.size
        # cols: 1
        orientation: 'vertical'
        MDToolbar:
            # title: "Tools"
            # size_hint: (0.1,1)
            height: '40'
            # pos_hint: {'center_x':0.5,'center_y':0.96}
            md_bg_color: app.theme_cls.primary_dark
            left_action_items: [["alpha-a-box", lambda x: app.about(),"about the app"], ["alpha-m-box",lambda x: root.first(),"patient Monitoring"],\
           ["account-check",lambda x: root.register_user(),"register patient"],\
           ["alpha-h-box",lambda x: root.help(),"help"]] 

        FloatLayout:
            cols: 1
            id: grid
            # orientation: 'vertical'

            # spacing:[6,6]
            # padding: 6
            MDRectangleFlatButton:
                id: Generate
                text: 'Start here'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                on_press: root.label()
                pos_hint: {'center_x':0.5,'center_y':0.5}
                
<RegisterUserScreen>:
    name: 'register'
    BoxLayout:
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color 
            Rectangle:
                pos: self.pos
                size: self.size
        # cols: 1
        orientation: 'vertical'
        MDToolbar:
            # title: "Tools"
            # size_hint: (0.1,1)
            height: '40'
            # pos_hint: {'center_x':0.5,'center_y':0.96}
            md_bg_color: app.theme_cls.primary_dark
            left_action_items: [["alpha-a-box", lambda x: app.about(),"About the app"], ["alpha-m-box",lambda x: root.first(),"patient monitoring"],\
           ["account-check-outline",lambda x: root.register_user()],\
           ["cog-outline",lambda x: root.camera(),"configuration settings"],["alpha-h-box",lambda x: root.help()]] 
        FloatLayout:
            cols: 1
            id: grid
            orientation: 'vertical'

            spacing:[6,6]
            padding: 6
            MDRectangleFlatButton:
                id: Generate
                text: 'register patient'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                on_press: root.addDataToSheet()
                pos_hint: {'center_x':0.5,'center_y':0.90}
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "AGE"
                pos_hint: {'center_x':0.60,'center_y':0.85}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDTextFieldRound:
                id: age
                pos_hint: {'center_x':0.5,'center_y':0.85} 
                icon_left: "account-check"
                hint_text: "Age"
                foreground_color: 1, 0, 1, 1
                size_hint_x: None
                width: 800
                font_size: 20

        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "BMI"
                pos_hint: {'center_x':0.60,'center_y':0.75}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDTextFieldRound:
                id :bmi
                pos_hint: {'center_x':0.5,'center_y':0.85} 
                icon_left: "relative-scale"
                hint_text: "BMI"
                foreground_color: 1, 0, 1, 1
                size_hint_x: None
                width: 800
                font_size: 20
            #     icon_left: "account-check"
            #     hint_text: "Age"
            #     foreground_color: 1, 0, 1, 1
            #     size_hint_x: None
            #     width: 800
            #     font_size: 20
            #     size_hint:(0.15,0.08)
            #     pos_hint: {'center_x':0.5,'center_y':0.75}
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "INITIALS"
                pos_hint: {'center_x':0.60,'center_y':0.65}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDTextFieldRound:
                id: initials
                pos_hint: {'center_x':0.5,'center_y':0.85} 
                icon_left: "alphabet-aurebesh"
                hint_text: "Initials"
                foreground_color: 1, 0, 1, 1
                size_hint_x: None
                width: 800
                font_size: 20
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "GENDER"
                color:0, 0, 0
                pos_hint: {'center_x':0.60,'center_y':0.55}
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDTextFieldRound:
                id: gender
                icon_left: "gender-male-female-variant"
                hint_text: "Gender"
                foreground_color: 1, 0, 1, 1
                size_hint_x: None
                width: 800
                font_size: 20
                pos_hint: {'center_x':0.5,'center_y':0.55}
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            # MDLabel:
            #     multiline: True
            #     # text: "SUBMIT"
            #     pos_hint: {'center_x':0.60,'center_y':0.45}
            #     color:0, 0, 0
            #     # mode: "fill"
            #     font_size: "25sp"
            #     font_name: "Ultra"
            #     bold: True
            # MDTextFieldRound:
            #     icon_left: "gender-male-female-variant"
            #     hint_text: "Gender"
            #     size_hint:(0.15,0.08)
            #     foreground_color: 1, 0, 1, 1
            #     size_hint_x: None
            #     width: 800
            #     font_size: 20
            #     pos_hint: {'center_x':0.5,'center_y':0.45}    
        MDRoundFlatIconButton:
            text: "SUBMIT"
            text_color: 0,0 , 0, 1
            font_name: "Ultra"
            bold: True
            width:100
            # md_bg_color: app.theme_cls.primary_color 
            on_press: root.addDataToSheet()
            font_size: 15
            pos_hint: {"center_x": 0.5} 
<CameraScreen>:
    name: 'camera'
    BoxLayout:
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color 
            Rectangle:
                pos: self.pos
                size: self.size
        # cols: 1
        orientation: 'vertical'
        MDToolbar:
            # title: "Tools"
            # size_hint: (0.1,1)
            height: '40'
            # pos_hint: {'center_x':0.5,'center_y':0.96}
            md_bg_color: app.theme_cls.primary_dark
            left_action_items: [["alpha-a-box", lambda x: app.about(),"about the app"], ["alpha-m-box",lambda x: root.first(),"patient monitoring"],\
           ["account-check",lambda x: root.register_user(),"register patient"],\
           ["cog-outline",lambda x: root.camera()],["alpha-h-box",lambda x: root.help()]] 
        FloatLayout:
            cols: 1
            id: grid
            # orientation: 'vertical'

            # spacing:[6,6]
            # padding: 6
            MDRectangleFlatButton:
                id: initialize
                text: 'Configuration settings'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                on_press: root.label()
                pos_hint: {'center_x':0.5,'center_y':0.70}
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "TIDAL VOLUME"
                pos_hint: {'center_x':0.60,'center_y':0.70}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDSlider:
                min: 0
                ax: 100
                value: 40
                hint: True
                pos_hint: {'center_x':0.50,'center_y':0.80}
                color:0, 0, 0
                size_hint:(0.15,0.08)
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "I/E ratio"
                pos_hint: {'center_x':0.60,'center_y':0.65}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            #     icon_left: "square-alternate"
            #     hint_text: "Age"
            #     foreground_color: 1, 0, 1, 1
            #     size_hint_x: None
            #     width: 800
            #     font_size: 20
            #     size_hint:(0.15,0.08)
            #     pos_hint: {'center_x':0.5,'center_y':0.75}
            MDSlider:
                min: 0
                max: 100
                value: 40
                hint: True
                pos_hint: {'center_x':0.5,'center_y':0.70}
                color:0, 0, 0
                size_hint:(0.15,0.08)
        FloatLayout:
            orientation: 'vertical'    
            # padding: 0
            MDLabel:
                multiline: True
                text: "Respiratory Rate"
                pos_hint: {'center_x':0.5,'center_y':0.55}
                color:0, 0, 0
                # mode: "fill"
                font_size: "25sp"
                font_name: "Ultra"
                bold: True
            MDSlider:
                min: 0
                max: 40
                value: 0
                hint: True
                pos_hint: {'center_x':0.5,'center_y':0.60}
                color:0, 0, 0
                size_hint:(0.15,0.08)
                
            
                
<HelpScreen>:
    name: 'OPERATE'
    BoxLayout:
        canvas.before:
            Color:
                rgba: app.theme_cls.primary_color 
            Rectangle:
                pos: self.pos
                size: self.size
        # cols: 1
        orientation: 'vertical'
        MDToolbar:
            # title: "Tools"
            # size_hint: (0.1,1)
            height: '40'
            # pos_hint: {'center_x':0.5,'center_y':0.96}
            md_bg_color: app.theme_cls.primary_dark
            left_action_items: [["alpha-a-box", lambda x: app.about()], ["alpha-g-box",lambda x: root.first()],\
           ["account-plus",lambda x: root.add_user()],["account-check",lambda x: root.register_user()],\
           ["camera",lambda x: root.camera()],["alpha-h-box-outline",lambda x: root.help()]] 

        FloatLayout:
            cols: 1
            id: grid
            # orientation: 'vertical'

            # spacing:[6,6]
            # padding: 6
            MDRectangleFlatButton:
                id: Generate
                text: 'HELP'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                on_press: root.label()
                pos_hint: {'center_x':0.5,'center_y':0.5}
"""


class WelcomeScreen(Screen):
    pass
class StandbyScreen(Screen):
    def proceed(self):
        self.manager.current = 'login'
    def go(self):
        self.manager.current = 'new'
    def submit(self):
        self.manager.current = 'new'
class NewScreen(Screen):
    def proceed(self):
        self.manager.current = 'login'

class CameraScreen(Screen):
    def update(self, dt):
        global cam
        global names
        # display image from cam in opencv window
        ret, frame = self.capture.read()

        if frame is not None:
            frame = cv2.resize(frame, (self.width, self.height))

        # frame = imutils.resize(frame, width=self.width)
        # (h, w) = frame.shape[:2]

        if cam:
            print("active")
            cv2.putText(frame, "active", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)
            for barcode in decode(frame):
                # print(barcode.data)
                myData = barcode.data.decode('utf-8')
                # print(myData)
                # draw bounding box
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(frame, [pts], True, (255, 0, 255), 5)
                # put text
                pts2 = barcode.rect
                cv2.putText(frame, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX,
                            0.9, (255, 0, 255), 2)
            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

        else:
            print("inactive_mode")
            cv2.putText(frame, "inactive_mode", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 4)

            buf1 = cv2.flip(frame, 0)
            buf = buf1.tobytes()
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            # display image from the texture
            self.texture = image_texture

        # if cam variable is false convert to texture
        buf1 = cv2.flip(frame, 0)
        buf = buf1.tobytes()
        texture1 = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
        # if working on RASPBERRY PI, use colorfmt='rgba' here instead, but stick with "bgr" in blit_buffer.
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        self.img1.texture = texture1

    def toggle(self, instance):
        """toggles the camera variable"""
        global cam
        if cam:
            cam = False
        else:
            cam = True

    def close_all(self, instance):
        """closes GUI"""
        App.get_running_app().stop()

    def label(self):
        label = MDRoundFlatIconButton(
            text="toggle camera", icon='atom-variant', theme_text_color='Custom', text_color=(1, 0, 0, 1),
            font_name='ultra',
            pos_hint={"center_x": .5, "center_y": .03}, font_size='10sp', on_press=self.toggle,
        )
        label1 = MDRoundFlatButton(
            text="exit", text_color =(1, 0, 0, 1),
            font_name='ultra',
            pos_hint={"center_x": .8, "center_y": .03}, font_size='14sp', on_press=self.close_all,
        )
        layout = FloatLayout(pos_hint={"center_x": .5, "center_y": .5})
        layout.add_widget(label)
        layout.add_widget(label1)
        self.img1 = Image()
        self.ids.grid.remove_widget(self.ids.initialize)
        self.ids.grid.add_widget(self.img1)
        self.ids.grid.add_widget(layout)
        # opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        Clock.schedule_interval(self.update, 1.0 / 33.0)

    def first(self):
        self.manager.current = 'first'
    def new(self):
        self.manager.current = 'new'
    def add_user(self):
        self.manager.current = 'add'
    def register_user(self):
        self.manager.current = 'register'
    def camera(self):
        self.manager.current = 'camera'
    def help(self):
        self.manager.current = 'help'


class Content(BoxLayout):
    pass
class Explain(BoxLayout):
   pass

class FirstScreen(Screen):

    def proceed(self):
        self.manager.current = 'login'
    def first(self):
        self.manager.current = 'first'
    def add_user(self):
        self.manager.current = 'add'
    def register_user(self):
        self.manager.current = 'register'
    def camera(self):
        self.manager.current = 'camera'
    def help(self):
        self.manager.current = 'help'
    def home(self):
        self.manager.current = 'login'
    def take(self):
        self.manager.current ='screenshot'


class LoginUserScreen(Screen):
    def first(self):
        self.manager.current = 'first'

    def add_user(self):
        self.manager.current = 'add'

    def register_user(self):
        self.manager.current = 'register'

    def camera(self):
        self.manager.current = 'camera'

    def help(self):
        self.manager.current = 'help'


class RegisterUserScreen(Screen):

    def first(self):
        self.manager.current = 'first'

    def add_user(self):
        self.manager.current = 'add'

    def register_user(self):
        self.manager.current = 'register'

    def camera(self):
        self.manager.current = 'camera'


    def help(self):
        self.manager.current = 'help'
    def addDataToSheet(sheet):

        style1 = xlwt.easyxf(num_format_str='D-MM-YY')
        wb = xw.Workbook()
        # add_sheet is used to create sheet.
        sheet1 = wb.add_sheet('Sheet 1')
        AGE = (sheet.ids.age.text)
        BMI =(sheet.ids.bmi.text)
        initials =(sheet.ids.initials.text)
        Gender =(sheet.ids.gender.text)

        # Input data into rows

        sheet1.write(1, 1,AGE)
        sheet1.write(1, 2 ,BMI)
        sheet1.write(1, 3, initials)
        sheet1.write(1, 4, Gender)
        # Input data into columns
        sheet1.write(0, 0, 'Patient 1')
        sheet1.write(0, 1, 'AGE')
        sheet1.write(0, 2, 'BMI')
        sheet1.write(0, 3, 'INITIALS')
        sheet1.write(0, 4, 'GENDER')
        sheet1.write(0, 6, datetime.now(),style1)
        wb.save('xlwt patient data.xls')

class HelpScreen(Screen):
    def first(self):
        self.manager.current = 'first'

    def add_user(self):
        self.manager.current = 'add'

    def register_user(self):
        self.manager.current = 'register'

    def camera(self):
        self.manager.current = 'camera'

    def help(self):
        self.manager.current = 'help'

# Create the screen manager
sm = ScreenManager()
sm.add_widget(WelcomeScreen(name='welcome'))
sm.add_widget(StandbyScreen(name='standby'))
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(LoginUserScreen(name='login'))
sm.add_widget(NewScreen(name='new'))
sm.add_widget(RegisterUserScreen(name='register'))
sm.add_widget(CameraScreen(name='camera'))
sm.add_widget(HelpScreen(name='help'))






class DemoApp(MDApp):
    dialog = None
    def build(self):
        self.title = "Auatomated Bag Valve Mask Ventilator"
        self.icon = "medin.png"
        self.theme_cls.primary_palette = "Blue"
        screen = Builder.load_string(screen_helper)

        def cur(self):
            screen.current = 'standby'

        # screen.current='first'
        Clock.schedule_once(cur, 2)

        return screen

    def about(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="About the app",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDRaisedButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

    def device(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="About the device",
                type="custom",
                content_cls=Explain(),
                buttons=[
                    MDRaisedButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()
# Function to take a screenshot
    def screengrab(self, *largs):
       im2 = ImageGrab.grab(bbox=None)
       im2.show()
    #outname = self.fileprefix + '_%(counter)04d.png'
    #Window.screenshot(name=outname)

if __name__ == '__main__':
    DemoApp().run()




