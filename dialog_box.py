from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFillRoundFlatButton, MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
from main_kv import phone_kv, encrypt_key, msg

class DemoApp(MDApp):
    def p(self, val):
        return {"center_x": val[0], "center_y": val[1]}
    
    def binded_function(self, obj):
        if self.phone.text and self.encryption_key.text and self.message.text:
            close_butt = MDFlatButton(text="close", on_release=self.close_dialog)
            more_butt = MDFlatButton(text="more")
            
            dialog_str = "Phone number: {}\nEncryption key: {}\nMessage: {}\n"
            dialog_str = dialog_str.format(self.phone.text, self.encryption_key.text, self.message.text)
            self.dialog = MDDialog(title="Print Details", text=dialog_str,
                            size_hint=(.7, 1), buttons=[close_butt, more_butt])
            butt_fill = MDFillRoundFlatButton(text="E-send", pos_hint=self.p((.5, .3)))
            self.dialog.add_widget(butt_fill)
            self.dialog.open()
            print(self.message.text)
        
    def close_dialog(self, obj):
        self.dialog.dismiss()
            
    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Light"
        self.phone = Builder.load_string(phone_kv)
        self.encryption_key = Builder.load_string(encrypt_key)
        self.message = Builder.load_string(msg)
        
        button = MDFillRoundFlatButton(text="send", pos_hint=self.p((.5, .5)),
                                       on_release=self.binded_function)
        screen.add_widget(self.phone)
        screen.add_widget(self.encryption_key)
        screen.add_widget(self.message)
        screen.add_widget(button)
        return screen
        

DemoApp().run()