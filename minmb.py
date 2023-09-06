from pymodbus.client import AsyncModbusSerialClient
from pymodbus.transaction import ModbusRtuFramer

client1 = AsyncModbusSerialClient(port='COM3', framer=ModbusRtuFramer, baudrate=38400)

client1.connect()

client1.read_coils(1002, 1, 1)


