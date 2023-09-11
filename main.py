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

pymodbus.pymodbus_apply_logging_config(log_file_name='log.txt')

connection = client.connect()

if connection:
    print('Connection established')

    try:
        move_to_wavelenght(client, 450)
        # move_device(client, int(1055+(3.5*6400)))
        # go_home(client, 1)

    except ModbusException as e:
        print(f'Error: {e}')
    finally:
        client.close()

else:
    print('Connection failed')