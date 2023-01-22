phone_kv = """
MDTextField:
    hint_text: "Phone Number"
    helper_text: "Enter peer number dumb ass"
    helper_text_mode: "on_focus"
    icon_right: "phone"
    # icon_right_color: app.theme_cls.primary_palette
    pos_hint: {"center_x": .5, "center_y": .8}
    size_hint_x: None
    width: 234
    
# MDTextField:
#     hint_text: "Encryption Key"
#     helper_text: "Enter Strong Encryption Key"
#     helper_text_mode: "on_focus"
#     icon_right: "key-variant"
#     pos_hint: {"center_x": .5, "center_y": .4}
#     size_hint_x: None
#     width: 234
"""

encrypt_key = """
MDTextField:
    hint_text: "Encryption Key"
    helper_text: "Enter Strong Encryption Key"
    helper_text_mode: "on_focus"
    icon_right: "key-variant"
    pos_hint: {"center_x": .5, "center_y": .7}
    size_hint_x: None
    width: 234
"""

msg = """
MDTextField:
    multiline: True
    hint_text: "Message"
    helper_text: "Write your dumb message here"
    helper_text_mode: "on_focus"
    icon_right: "message"
    pos_hint: {"center_x": .5, "center_y": .6}
    size_hint_x: None
    width: 234
"""