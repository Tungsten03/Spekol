from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadBuilder, Endian



def go_home(device:object, speed:(int,float)):
    """
    Takes a client object and a movement speed and sends the message to the device.
    Positive value starts homing of a device to position 0 (clockwise), negative value will move to max position
    (counter-clockwise)

    :param device: The client object of a selected device.
    :param speed: The movement speed to set. A positive value means forward motion,
                   and a negative value means reverse motion.

    :return None

    :raise ValueError: Raised if the provided speed is not of type int or float.

    e.g.
    go_home(my_client, 2.5)   # Sets the movement speed to 2.5 (forward motion)
    go_home(my_client, -1.75) # Sets the movement speed to -1.75 (reverse motion)
    """
    if not isinstance(speed, (int, float)):
        raise ValueError('wrong speed value. Must be int/float type')

    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(int(-6400*speed))
    payload = builder.build()
    device.write_registers(1036, payload, count=2, unit=1, skip_encode=True)


def move_device(device:object, position:int):
    """
    7455 = 400nm
    Moves device to given position

    :param device: The client object of a selected device.
    :param position:
    :return:
    """
    if not isinstance(position, int):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(abs(position))
    payload = builder.build()
    device.write_registers(1042, payload, count=2, unit=1, skip_encode=True)

def move_to_wavelenght(device:object, wavelenght:int):
    """
    7455 = 400nm
    Moves device to given position

    :param device: The client object of a selected device.
    :param position:
    :return:
    """
    if not isinstance(wavelenght, int):
        raise ValueError('Position must be integer')
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    position = 1055 + int((wavelenght-300)*74.55)
    builder.add_32bit_int(abs(position))
    payload = builder.build()
    device.write_registers(1042, payload, count=2, unit=1, skip_encode=True)


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

def deviece_status(device_name):
    status = device_name.read_holding_registers(address=1002, count=1, slave=1)
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
