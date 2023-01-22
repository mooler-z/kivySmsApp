from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.list import MDList, OneLineListItem, TwoLineListItem, ThreeLineListItem, ThreeLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView

class DemoApp(MDApp):
    def build(self):
        screen = Screen()
        # for i in range(6):
        #     item = OneLineListItem(text="Item "+str(i), pos_hint={"center_x": .5, "center_y":0.9-(i/10)}, size_hint_x=None, width=633)
        #     screen.add_widget(item)
        self.dialog = MDDialog(title="Print Details", text="",
                            size_hint=(.7, 1.8), height=900)
        item1 = OneLineListItem(text="Name 1", size_hint_x=None, width=333, on_release=self.item)
        self.item2 = OneLineListItem(text="Name 2", pos_hint={"center_x": .5, "center_y":0.6}, size_hint_x=None, width=633, on_release=self.dialog_a)
        icon = IconLeftWidget(icon="cellphone-lock")
        item3 = ThreeLineIconListItem(text="Name 3", secondary_text="Phone number", tertiary_text="Encryption Key",size_hint_x=None, width=333, on_release=self.item)
        item3.add_widget(icon)
        item4 = TwoLineListItem(text="Item 4", secondary_text="Encryption key", size_hint_x=None, width=333, on_release=self.item)
        # screen.add_widget(self.dialog)
        list_view = MDList(pos_hint={"center_x": .5, "center_y":0.6})
        scroll_view = ScrollView()
        list_view.add_widget(item1)
        list_view.add_widget(item3)
        list_view.add_widget(item4)
        scroll_view.add_widget(list_view)
        # self.dialog.add_widget(scroll_view)
        screen.add_widget(scroll_view)
        screen.add_widget(self.item2)
        # self.dialog.add_widget(screen)
        # self.dialog.add_widget(list_view)
        return screen
    
    def item(self, obj):
        print("U touched me")
        self.dialog.dismiss()
        self.item2.text = str(obj)
        print(self.item2.text)
    
    def dialog_a(self, obj):
        self.dialog.open()

DemoApp().run()