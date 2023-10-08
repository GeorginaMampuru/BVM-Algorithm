from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window

Window.maximize()
import time
# from kivymd.font_definitions.theme_font_styles
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton, MDRoundFlatButton
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDRoundFlatIconButton
from kivymd.uix.label import MDLabel
import os

from time import *

screen_helper = """
<TooltipMDIconButton@MDIconButton+MDTooltip>
#: import FadeTransition kivy.uix.screenmanager.FadeTransition

ScreenManager:
    transition: FadeTransition()
    WelcomeScreen:
    StandbyScreen:
    FirstScreen:
    LoginUserScreen:
    RegisterUserScreen:
    # CameraScreen:
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
                on_press: root.proceed()
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
            MDRectangleFlatButton:
                text: 'ABOUT THE DEVICE'
                text_color: 1, 1, 1, 1
                font_name: "Ultra"
                bold: True
                md_bg_color: 0.9, 0.4, 0.5, 0.9
                on_press: root.proceed()
                pos_hint: {'center_x':0.5,'center_y':0.5}

            TooltipMDIconButton:
                icon: "chart-line"
                tooltip_text: "Record snapshot"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.about()
                # md_bg_color:  app.theme_cls.primary_color 

            TooltipMDIconButton:
                icon: "alpha-a-box"
                tooltip_text: "Patient Data"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.about()
                # md_bg_color:  app.theme_cls.primary_color 
            TooltipMDIconButton:
                icon: "card-text-outline"
                tooltip_text: "user manual"
                pos_hint: {"center_x": .5, "center_y": .5}
                on_press: app.about()
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
                    text: 'Alarms'
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
            left_action_items: [["information-variant", lambda x: app.about()], ["alpha-g-box",lambda x: root.first()],\
           ["account-plus-outline",lambda x: root.add_user()],["account-check",lambda x: root.register_user()],\
           ["cog-outline",lambda x: root.setting()],["alpha-h-box",lambda x: root.help()]] 

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
            left_action_items: [["alpha-a-box", lambda x: app.about()], ["alpha-g-box",lambda x: root.first()],\
           ["account-plus",lambda x: root.add_user()],["account-check-outline",lambda x: root.register_user()],\
           ["camera",lambda x: root.camera()],["alpha-h-box",lambda x: root.help()]] 
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
                on_press: root.label()
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
            on_press: root.proceed()  
            font_size: 15
            pos_hint: {"center_x": 0.5} 
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


class Content(BoxLayout):
    pass


class FirstScreen(Screen):

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
sm.add_widget(RegisterUserScreen(name='register'))

sm.add_widget(HelpScreen(name='help'))


class DemoApp(MDApp):
    dialog = None

    def build(self):
        self.title = "automated Bag valve mask"
        self.icon = "medin.png"
        # self.theme_cls.primary_palette = "Blue"
        self.image = "images.jpg"
        screen = Builder.load_string(screen_helper)

        def cur(self):
            screen.current = 'standby'

        # screen.current='first'
        Clock.schedule_once(cur, 2)

        return screen

    def about(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="About App",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDRaisedButton(
                        text="OK", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()


if __name__ == '__main__':
    DemoApp().run()