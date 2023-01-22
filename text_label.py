from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon

class DemoApp(MDApp):
    def rgb_converter(self, tup):
        return (tup[0]/255, tup[1]/255, tup[2]/255, tup[3])
    def build(self):
        label = MDLabel(text="Fuck you, world!", halign="center", 
                        theme_text_color="Custom", text_color=self.rgb_converter((255, 102, 0, 1),),
                        font_style="H1"
                        )
        icon_label = MDIcon(icon='language-python', halign='center')
        return icon_label
    
DemoApp().run()