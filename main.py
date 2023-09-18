import pymodbus
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
import time
from func import *

client = ModbusSerialClient(port='COM3',
                            baudrate=115200,
                            bytesize=8,
                            parity='N',
                            stopbits=1)

# pymodbus.pymodbus_apply_logging_config(log_file_name='log.txt')

connection = client.connect()

if connection:
    print('Connection established')

    try:
        # go_home(client, 1)
        # time.sleep(1)
        # vel_max_set(client, 1)
        # wave_abs(client, 720)
        device_status(client)





    except ModbusException as e:
        print(f'Error: {e}')
    finally:
        client.close()

else:
    print('Connection failed')