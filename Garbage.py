import pymodbus
from pymodbus.client import ModbusSerialClient
from pymodbus.exceptions import ModbusException
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
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
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(-3200)
    payload = builder.build()
    print(payload)
    print('moving to position...')
    client.write_registers(1036, payload, count=2, unit=1, skip_encode=True)
    print('device in position')

else:
    print('Connection not established!')