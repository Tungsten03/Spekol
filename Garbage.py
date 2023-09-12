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
    # read = client.read_holding_registers(address=1028, count=2, slave=1)
    # decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    # decoded = decoder.decode_32bit_int()
    # print(decoded)
    # brk_real_set(client, 1000)
    # wave_abs(client, 300)
    deviece_status(client)




else:
    print('Connection not established!')