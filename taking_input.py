from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from main_kv import phone_kv, encrypt_key, msg

from plyer import sms
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
from cryptography import *


hkdf = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=None,
        backend=default_backend()
)

class DemoApp(MDApp):
    def p(self, val):
        return {"center_x": val[0], "center_y": val[1]}
    
    def binded_function(self, obj):
        if self.phone.text and self.encryption_key.text and self.message.text:
            key = base64.urlsafe_b64encode(hkdf.derive(
                bytes(self.encryption_key.text, 'utf-8')))
            f = Fernet(key)
            encMsg = f.encrypt(bytes(self.message.text, 'utf-8'))
            print(encMsg.decode())
            print(type(self.phone.text), type(int(self.phone.text)))
            sms.send(recipient=int(self.phone.text), message=encMsg.decode())
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"
        self.phone = Builder.load_string(phone_kv)
        self.encryption_key = Builder.load_string(encrypt_key)
        self.message = Builder.load_string(msg)
        
        button = MDRectangleFlatButton(text="send", pos_hint=self.p((.5, .5)),
                                       on_release=self.binded_function)
        screen.add_widget(self.phone)
        screen.add_widget(self.encryption_key)
        screen.add_widget(self.message)
        screen.add_widget(button)
        return screen

DemoApp().run()