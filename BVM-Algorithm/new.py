from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, Clock
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.tab import MDTabsBase


class Test(MDApp):

    def build(self):
        return Builder.load_string("KV")


KV = '''
BoxLayout:
    orientation:'vertical'

    MDToolbar:
        title: 'Rust App'
        md_bg_color: 157, 58, 22, 1


    MDBottomNavigation:
        panel_color: .2, .2, .2, 0

        MDBottomNavigationItem:
            name: 'screen 1'
            text: 'Eco Raiding'
            icon: 'axe'
            MDRaisedButton:
                id: button1
                text: "Object"
                pos_hint: {"center_x": .4, "center_y": .85}
                size_hint: .4, .05
                on_release: app.menu.open()



            MDRaisedButton: 
                id: buttonX
                text: "X"
                pos_hint: {"center_x": .7, "center_y": .85}
                size_hint: .05, .05
                on_release: app.menu2.open()

            MDRaisedButton:
                id: buttontool
                text: "Tool"
                pos_hint: {"center_x": .5, "center_y": .45}
                size_hint: .4, .05
                on_release: app.menutools.open()

        MDBottomNavigationItem:
            name: 'screen 2'
            text: 'Explosive Raiding'
            icon: 'bomb'
            MDRaisedButton:
                id: button
                text: "Object"
                pos_hint: {"center_x": .4, "center_y": .85}
                size_hint: .4, .05
                on_release: app.menu.open()

            MDRaisedButton: 
                id: buttonX2
                text: "X"
                pos_hint: {"center_x": .7, "center_y": .85}
                size_hint: .05, .05
                on_release: app.menu3.open()

            MDRaisedButton:
                id: buttonexplosive 
                text: "Explosive"
                pos_hint: {"center_x": .5, "center_y": .45}
                size_hint: .4, .05
                on_release: app.menuexplosive.open()



        MDBottomNavigationItem:
            name: 'screen 3'
            text: 'Recycle Calculator'
            icon: 'recycle'

            MDLabel:
                text: 'Unknown Content'
                halign: 'center'
'''


class Test(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        # menu_items = [{"text": f"Item"} for i in range(10)]

        menu_items = [
            {"text": f"Wooden Wall"},
            {"text": f"Stone Wall"},
            {"text": f"Sheet Metal Wall"},
            {"text": f"Armored Wall"},
            {"text": f"Wooden Door"},
            {"text": f"Sheet Metal Door"},
            {"text": f"Armored Door"},
            {"text": f"Garage Door"},
            {"text": f"High Ex. Wooden Wall"},
            {"text": f"High Ex. Stone Wall"},
        ]
        menu_items2 = [
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},
            {"text": "1"},

        ]

        menu_tools = [
            {"text": f"Wooden Spear"},
            {"text": f"Bone Knife"},
            {"text": f"Salvaged Sword"},
            {"text": f"Hammer"},
            {"text": f"Pickaxe"},

        ]

        menu_explosive = [
            {"text": f"Satchel Charge"},
            {"text": f"Explosive Round"},
            {"text": f"Rocket"},
            {"text": f"C4"},

        ]

        self.menu = MDDropdownMenu(
            caller=self.screen.ids.button1,
            items=menu_items,
            width_mult=5,

        )

        self.menu2 = MDDropdownMenu(
            caller=self.screen.ids.buttonX,
            items=menu_items2,
            width_mult=1
        )

        self.menu3 = MDDropdownMenu(
            caller=self.screen.ids.buttonX2,
            items=menu_items2,
            width_mult=1
        )

        self.menutools = MDDropdownMenu(
            caller=self.screen.ids.buttontool,
            items=menu_tools,
            width_mult=5,
        )
        self.menuexplosive = MDDropdownMenu(
            caller=self.screen.ids.buttonexplosive,
            items=menu_explosive,
            width_mult=5,
        )

        self.menu.bind(on_release=self.menu_callback)

    def menu_callback(self, instance_menu, instance_menu_item):
        print(instance_menu, instance_menu_item)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Red"
        return self.screen


Test().run()