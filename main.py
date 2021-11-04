from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
# from kivymd.uix.list import MDList,OneLineListItem  list
# from kivy.uix.scrollview import ScrollView        list
from kivymd.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from helpers import ToDo_helper
from helpers import Add_helper
from helpers import High_helper



class MyToDo(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        self.theme_cls.primary_hue = "A700"
        screen = MDScreen()

       # scroll = ScrollView()      list
      #  list_view = MDList()       list
       # item1 = OneLineListItem(text = "Item 1")       list
       # builder.load_string('mytodo.kv')
        text_ToDo = Builder.load_string(ToDo_helper)
        btn_Add = Builder.load_string(Add_helper)
        btn_High = Builder.load_string(High_helper)

       # scroll.add_widget(list_view)       list
       # list_view.add_widget(item1)        kist
     #   screen.add_widget(scroll)      list
        screen.add_widget(text_ToDo)
        screen.add_widget(btn_Add)
        screen.add_widget(btn_High)

        return screen

    def add_task_high(self):
        print("Save the task as severity 1 in the DB and show in list")
      #  mylist = OneLineListItem(text=self.dialog.content_cls.textfield.text)

       # self.list_view.add_widget(mylist)

    def call(self,obj):
        if obj.icon == "priority-high":
            self.add_task_high()
        elif obj.icon == "priority-low":
            print("Save the task as severity 2 in the DB")
        else:
            print("Mark the task as done in the DB")



MyToDo().run()
