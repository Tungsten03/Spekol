import struct
from pymodbus.client import ModbusSerialClient
import json
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import serial

f = open('clients.json')
clients = json.load(f)

for i in clients:
    i["name"] = ModbusSerialClient(port=i["port"], baudrate=i["baudrate"], parity=i["parity"], timeout=i["timeout"])
    print(f'{i["name"]} created!')



#
# client = ModbusSerialClient(
#     method='rtu',
#     port='COM3',
#     baudrate=115200,
#     parity='N',
#     timeout=1
# )
#
#
#
# connection = client.connect()
#
# if connection:
#     print('client connected!')
#
#     req = client.read_holding_registers(address=1002, count=10, slave=1)
#     print(req.registers)
#     pos_act = client.read_holding_registers(address=1060, count=24, slave=1)
#     print(pos_act.registers)
#
#     client.write_coil(address=1036, value=True, slave=1)
#
# #     register_address = 1060
# #     # Frame parameters:
# #     device_address = 0x01
# #     function_code = 0x03
# #     start_register_address_hi = 0x04
# #     start_register_address_lo = 0x24
# #     num_registers_hi = 0x00
# #     num_registers_lo = 0x02
# #     crc_hi = 0x85
# #     crc_lo = 0x30
# #
# #     #Make frame
# #     frame = [
# #         device_address,
# #         function_code,
# #         start_register_address_hi,
# #         start_register_address_lo,
# #         num_registers_hi,
# #         num_registers_lo,
# #         crc_hi,
# #         crc_lo
# #     ]
# #
# #     # Convert to byte string
# #     modbus_frame = struct.pack('8B', *frame)
# #     regs = client.read_input_registers(address=1060, count=2, slave=1)
# #     print(modbus_frame)
# #
# #     # response = client.send(modbus_frame)
# #     print(regs.registers)
# #
# #     response = client.read_holding_registers(
# #         address=register_address,
# #         count=num_registers_lo,
# #         unit=device_address
# #     )
# #     print(response)
# #
# #     if not response.isError():
# #         register_1 = response.registers[0]
# #         register_2 = response.registers[1]
# #
# #         # Przelicz na liczbę 32-bitową
# #         position_32_bit = (register_2 << 16) + register_1
# #
# #         # Przelicz na obroty silnika
# #         position_in_rotations = position_32_bit / 12800.0
#
#         print(f"Aktualna pozycja silnika: {position_in_rotations} [obr]")
#     else:
#         print("Błąd podczas odczytu rejestru.")
#
# else:
#     print('failed to connect')
#
# # #read holding register 007F to read motor driver output
# res = client.read_holding_registers(address=0x07F, count=1, unit=1)
# print(res)


