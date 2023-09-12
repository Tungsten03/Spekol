from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder, Endian





def go_home(device:object, speed:(int,float)):
    """
    Takes a device object and a movement speed and sends the message to the device.
    Positive value starts homing of a device to position 0 (clockwise), negative value will move to max position
    (counter-clockwise)

    :param device: The client object of a selected device.
    :param speed: The movement speed to set. A positive value means forward motion,
                   and a negative value means reverse motion.

    :return None

    :raise ValueError: Raised if the provided speed is not of type int or float.

    e.g.
    go_home(my_client, 1)   # Sets the movement speed to 1 (forward motion)
    go_home(my_client, -0.5) # Sets the movement speed to -1.75 (reverse motion)
    """
    if not isinstance(speed, (int, float)):
        raise ValueError('wrong speed value. Must be int/float type')

    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(int(-6400*speed))
    payload = builder.build()
    device.write_registers(1036, payload, count=2, unit=1, skip_encode=True)


def pos_abs(device:object, position:float):
    """
    Moves device to absolute position given by user. Position is calculated to full engine rotation

    :param device: The client object of a selected device.
    :param position: given position
    :return: none

    :raise ValueError: Raised if the provided position is not of type int or float.

    """
    if not isinstance(position, (float, int)):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(abs(int(position*6400)))
    payload = builder.build()
    device.write_registers(1042, payload, count=2, unit=1, skip_encode=True)

def vel_abs(device, vel):
    """
    The vel_abs function sets the absolute velocity of the motor.

    :param device: Identify which device is being used
    :param vel: Set the velocity of the motor
    :return: None

    """
    if not isinstance(vel, int):
        raise ValueError('velocity must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(vel)
    payload = builder.build()
    device.write_registers(1038, payload, count=2, unit=1, skip_encode=True)


def wave_abs(device:object, wavelenght:int):
    """
    The wave_abs function takes a device object and an integer wavelength value as arguments.
    It then calculates the corresponding position of the monochromator using a linear equation,
    and writes that value to register 1042 on the device.

    :param device:object: Specify the device that is being used
    :param wavelenght:int: Set the wavelenght of the laser
    :return: None
    """
    if not isinstance(wavelenght, int):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    position = 1055 + int((wavelenght-300)*74.55) #Not accurate! REFINE!
    builder.add_32bit_int(abs(position))
    payload = builder.build()
    device.write_registers(1042, payload, count=2, unit=1, skip_encode=True)

def wave_rel(device:object, wavelenght:int):
    """
    The wave_rel function moves the monochromator to a new wavelength relative to its current position.
    The function takes two arguments: device and wavelenght.
    Device is an object that represents the connection between this program and the spectrometer, while wavelenght is an integer representing how many nanometers away from its current position you want it to move.

    :param device:object: Identify the device that is being used
    :param wavelenght:int: Set the wavelenght in nm
    :return: None
    """
    if not isinstance(wavelenght, int):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    steps = wavelenght*74.55
    builder.add_32bit_int(int(steps))
    payload = builder.build()
    device.write_registers(1044, payload, count=2, unit=1, skip_encode=True)

def acc_real_read(device:object):

    """
    The acc_real_read function reads the real acceleration value from the device.
    The function takes in a device as an argument and returns a decoded 32-bit integer.

    :param device: Specify the device that is being read from
    :return: The value of the real acceleration
    """
    read = device.read_holding_registers(address=1026, count=2, slave=1)
    decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    decoded = decoder.decode_32bit_int()
    print(decoded/64000)

def acc_real_set(device:object, acc:float):

    """
    The acc_real_set function sets the acceleration of the motor in real time.

    :param device:object: Specify the device that is being used
    :param acc:float: Set the acceleration value
    :return: None
    """
    if not isinstance(acc, (int,float)):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(int(64000*acc))
    payload = builder.build()
    device.write_registers(1026, payload, count=2, unit=1, skip_encode=True)

def brk_real_read(device_name:str):
    """
    The brk_real_read function reads the real power value from the BRK device.

    :param device_name: Specify the device you want to read from
    :return: The real power of the device
    """
    read = device_name.read_holding_registers(address=1028, count=2, slave=1)
    decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    decoded = decoder.decode_32bit_int()
    print(decoded)

def brk_real_set(device:object, brk:float):
    """
    The brk_real_set function sets the real break for the device.

    :param device:object: Specify the device to be used
    :param brk:float: Set the break for the motor
    :return: None
    """
    if not isinstance(brk, (float,int)):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(int(64000*brk))
    payload = builder.build()
    device.write_registers(1028, payload, count=2, unit=1, skip_encode=True)

def vel_max_read(device_name):
    """
    Not working porperly

    :param device_name:
    :return:
    """
    read = device_name.read_holding_registers(address=1030, count=2, slave=1)
    decoder = BinaryPayloadDecoder.fromRegisters(read.registers, byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    decoded = decoder.decode_32bit_int()
    print(decoded)

def vel_max_set(device:object, vel:int):

    """
    The vel_max_set function sets the maximum velocity of the motor.

    :param device:object: Identify the device that is being used
    :param vel:int: Set the maximum velocity of the motor
    :return: None
    """
    if not isinstance(vel, int):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(vel)
    payload = builder.build()
    device.write_registers(1030, payload, count=2, unit=1, skip_encode=True)

def check_power(device_name):
    """
    Read actual power set in engine register

    :param device_name:
    :return:
    """
    power = device_name.read_holding_registers(address=1003, count=1, slave=1)
    return power.registers

def set_power(device_name, power):
    """
    Sets the power in engine.
    (2...100% max value)

    :param device_name:
    :param power:
    :return:
    """
    device_name.write_register(1003, power, 1)
    power = check_power(device_name)
    print(f'Power set: {power}')

def device_on(devie_name):
    devie_name.write_coil(address=2000, value=True, slave=1)

def device_off(devie_name):
    devie_name.write_coil(address=2000, value=False, slave=1)

def device_status(device:object):

    """
    The device_status function takes a device name as an argument and returns the status of that device.
        The function uses the read_holding_registers method to read from address 1002, which is where the
        status register is located. It then prints out what state it's in based on its value.

    :param device:object: Specify the device that will be used to read the status
    :return: The status of the device
    """
    status = device.read_holding_registers(address=1002, count=1, slave=1)
    match status.registers[0]:
        case 0:
            print('motor disabled')
        case 1:
            print('motor enabled, motionless')
        case 2:
            print('motor in the set speed mode')
        case 3:
            print('motor in the set position mode')
        case 4:
            print('set position reached')
        case 5:
            print('set position error')
        case 6:
            print('motor in homing mode')
        case 8:
            print('position correction mode')
        case 9:
            print('limit position L reached')
        case 10:
            print('limit position R reached')
