"""
Example script captures network traffic using WireShark and prints a short summary for every protocol.

Requirements:
  - Wireshark 2.2.5
  - pywinauto 0.6.1+
This example opens "Wireshark", navigates to 'network_connection_name',
captures network traffic for 'capture_time' seconds, saves all the data to a temporary file,
parses it and shows a short summary for every protocol.
"""
import time

from pywinauto.application import Application

app = Application().connect(title_re=".*Firefox")
mozilla = app.window(title_re=".*Firefox")
main_win_wrapper = mozilla.set_focus()

time.sleep(1)
mozilla.type_keys("username")
mozilla.type_keys("{TAB}")
mozilla.type_keys("password")
#mozilla.type_keys("{ENTER}")

