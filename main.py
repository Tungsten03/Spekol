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
        device_on(client)
        time.sleep(2)

        deviece_status(client)
        move_device(client, 1)
        time.sleep(2)
        deviece_status(client)

        deviece_status(client)
        move_device(client, 0)
        time.sleep(2)
        deviece_status(client)

        device_off(client)

    except ModbusException as e:
        print(f'Error: {e}')
    finally:
        client.close()

else:
    print('Connection failed')