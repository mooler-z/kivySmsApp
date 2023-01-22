from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton,\
    MDFloatingActionButton


class DemoApp(MDApp):
    def p(self, val):
        return {"center_x": val[0], "center_y": val[1]}
    
    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        
        flat_butt = MDFlatButton(text="send", pos_hint=self.p((.5, .5)))
        
        rect_flat_butt = MDRectangleFlatButton(text="receive", pos_hint=self.p((.5, .4)))
        
        icon_butt = MDIconButton(icon="language-python", pos_hint=self.p((.5, .6)))
        
        float_butt_1 = MDFloatingActionButton(icon="tooltip-plus",pos_hint=self.p((.3, .3)))
        float_butt_2 = MDFloatingActionButton(icon="home-lock",pos_hint=self.p((.4, .3)))
        float_butt_3 = MDFloatingActionButton(icon="lock",pos_hint=self.p((.5, .3)))
        float_butt_4 = MDFloatingActionButton(icon="fullscreen-exit",pos_hint=self.p((.6, .3)))
        
        screen.add_widget(icon_butt)
        screen.add_widget(flat_butt)
        screen.add_widget(rect_flat_butt)
        
        screen.add_widget(float_butt_1)
        screen.add_widget(float_butt_2)
        screen.add_widget(float_butt_3)
        screen.add_widget(float_butt_4)
        return screen
    
DemoApp().run()