from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (360, 680)

screen_kv = """
# Screen:
#     BoxLayout:
#         orientation: 'vertical'
#         MDToolbar:
#             title: 'Demo app'
            # left_action_items: [["menu", lambda x: app.navigation_draw()]]
            # right_action_items: [["timer", lambda x: app.navigation_draw()]]
            # elevation: 20
#         MDLabel:
#             text: 'Hello, world!'
#             halign: 'center'
        
#         MDBottomAppBar:
#             MDToolbar:
#                 title: 'Demo app'
#                 left_action_items: [["menu", lambda x: app.navigation_draw()]]
#                 right_action_items: [["timer", lambda x: app.navigation_draw()]]
#                 elevation: 20
            
BoxLayout:
    orientation:'vertical'
    MDToolbar:
        title: 'Demo App'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1
        left_action_items: [["menu", lambda x: app.navigation_draw()]]
        right_action_items: [["timer", lambda x: app.navigation_draw()]]
        elevation: 20
    MDBottomNavigation:
        panel_color: .2, .2, .2, 1
        MDBottomNavigationItem:
            name: 'enc_msg'
            icon: 'message-text-lock-outline'
            MDLabel:
                text: 'encrypt message'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'decrypt_msg'
            icon: 'lock-open-variant'
            MDLabel:
                text: 'decrypt message'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'peer_screen'
            icon: 'account-plus'
            MDLabel:
                text: 'Peer+'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'enc_screen'
            icon: 'key-chain-variant'
            MDLabel:
                text: 'generate encryption key'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'saved_msg'
            icon: 'inbox-multiple-outline'
            MDLabel:
                text: 'show saved messages'
                halign: 'center'
        MDBottomNavigationItem:
            name: 'saved_peers'
            icon: 'account-box-multiple-outline'
            MDLabel:
                text: 'show saved peers'
                halign: 'center'
"""

class DemoAll(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.theme_style = 'Dark'
        screen = Builder.load_string(screen_kv)
        return screen
    
    def navigation_draw(self):
        print("Navigation")

DemoAll().run()