from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.dialog import MDDialog

list_kv = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

class DemoApp(MDApp):
    def show_dialog(self, obj):
        dialog = MDDialog(title="Print Details", text=obj.text,
                            size_hint=(.7, 1.8), height=900)
        dialog.open()
        
    def on_start(self):
        for i in range(21):
            items = OneLineIconListItem(
                text="Name " + str(i+1),
                size_hint_x=None, width=333,
                pos_hint={"center_x": .5, "center_y":1},
                on_release=self.show_dialog
            )
            icon = IconLeftWidget(icon="language-python")
            items.add_widget(icon)
            self.root.ids.container.add_widget(items)
            
    def build(self):
        screen = Builder.load_string(list_kv)
        return screen
    
DemoApp().run()