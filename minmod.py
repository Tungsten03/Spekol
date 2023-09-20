import minimalmodbus
from minimalmodbus import Instrument
import serial


instrument = Instrument(port='COM3', slaveaddress=1, debug=True)

instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 115200        # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout  = 0.05          # seconds

print(instrument.read_registers(1031, 1))
instrument.write_register()
print(instrument.read_registers(1003, 1))
