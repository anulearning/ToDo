from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.widget import Widget
#from kivymd.uix.list import MDList,OneLineListItem
#from kivy.uix.scrollview import ScrollView
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder


# from helpers import ToDo_helper
# from helpers import Add_helper
# from helpers import High_helper


class MyToDo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
       # screen = MDScreen()

        # scroll = ScrollView()
        # list_view = MDList()
        # item1 = OneLineListItem(text = "Item 1")
        screen = Builder.load_file('mytodo.kv')
        # text_ToDo = Builder.load_string(ToDo_helper)
        # btn_Add = Builder.load_string(Add_helper)
        #  btn_High = Builder.load_string(High_helper)

        # scroll.add_widget(list_view)
        # list_view.add_widget(item1)
        # screen.add_widget(scroll)
        # screen.add_widget(text_ToDo)
        # screen.add_widget(btn_Add)
        # screen.add_widget(btn_High)

        return screen



    # mylist = OneLineListItem(text=self.ToDo_helper.textfield.text)

    # self.list_view.add_widget(mylist)

    def call(self, obj):
        if obj.icon == "priority-high":
            self.add_task_high()
        elif obj.icon == "priority-low":
            print("Save the task as severity 2 in the DB")
        else:
            print("Mark the task as done in the DB")

    def add_task_high(self):
        print("Save the task as severity 1 in the DB and show in list")
        print(self.root.ids.textfield.text)
        items = self.root.ids.textfield.text
        self.root.ids.list.text = items
        self.root.ids.textfield.text = ""
       # self.root.ids.but.close()

if __name__ == "__main__":
    MyToDo().run()
