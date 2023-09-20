from tkinter import ttk
from ttkthemes import ThemedTk
from func import *
import GUI_tk

root = ThemedTk(theme="radiance")
Askr(root)


#
# client = ModbusSerialClient(port='COM3',
#                             baudrate=115200,
#                             bytesize=8,
#                             parity='N',
#                             stopbits=1)
#
# # pymodbus.pymodbus_apply_logging_config(log_file_name='log.txt')
#
# connection = client.connect()
# open_gui()
root.mainloop()
# if connection:
#     print('Connection established')
#
#     try:
#         go_home(client, 1, 1)
#
#         device_status(client)


#
#
#
#     except ModbusException as e:
#         print(f'Error: {e}')
#     finally:
#         client.close()
#
# else:
#     print('Connection failed')