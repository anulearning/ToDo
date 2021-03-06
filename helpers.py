#: import utils kivy.utils
ToDo_helper = '''
MDTextField: 
    id: textfield
    hint_text: 'Add Task'
    font_size: 15
    required: True
    #helper_text: ""
    #helper_text_mode: "on_focus"
    pos_hint: {'center_x': 0.2, 'center_y': 0.1}
    size_hint: 0.35, 0.15
    multiline: True
'''

Add_helper = '''
MDFloatingActionButtonSpeedDial:
    data: {'Top Priority': 'priority-high', 'Low Priority': 'priority-low', 'Accomplished': 'check'}
    rotation_root_button: True
   # hint_animation : True
    callback: app.call
'''

High_helper = '''
MDFloatingActionButton:
    icon: 'priority-high'
   # text: 'High Priority'
    #font_size: "32sp"
   # background_color: '#FFBF00'
   # theme_text_color: "Custom"
   # text_color: 0, 0, 1, 1
   # line_color: 1, 0, 1, 1
   # icon_color: 1, 0, 0, 1
    pos_hint: {"center_x": .2, "center_y": .9}
    size_hint_x: None
    width: 200
'''