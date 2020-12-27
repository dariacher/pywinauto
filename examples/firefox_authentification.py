"""
Example script fill username and password fields using Windows Authentication

This example opens "Mozilla Firefox" web browser with open authentification window, 
fill username and password and click button "OK"
"""
import time

from pywinauto.application import Application

app = Application(backend='uia').connect(title_re=".*Firefox")
mozilla = app.window(title_re=".*Firefox")
main_win_wrapper = mozilla.set_focus() # not needed if this is already in focus

sign_in = mozilla.child_window(auto_id="commonDialogWindow", control_type="Custom")
# you can also do like this
# sign_in = mozilla.child_window(title="Authentication required - Mozilla Firefox", control_type="Custom")

username = sign_in.child_window(auto_id="loginTextbox", control_type="Edit")
password = sign_in.child_window(auto_id="password1Textbox", control_type="Edit")
sign_in_button = sign_in.child_window(title="OK", control_type="Button")

username.iface_value.SetValue("username")
password.iface_value.SetValue("password")
sign_in_button.invoke()


