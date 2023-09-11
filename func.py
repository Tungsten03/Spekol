from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadBuilder, Endian



def go_home(client, speed):
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(int(-6400*speed))
    payload = builder.build()
    print(payload)
    print('Homing....')
    client.write_registers(1036, payload, count=2, unit=1, skip_encode=True)
    print('device position zeroed')
def move_device(client, position):
    """
    Moves device to left (position=0) and right (position=1) limit position.

    No idea, just works...

    :param device_name:
    :param position:
    :return:
    """
    builder = BinaryPayloadBuilder(byteorder=Endian.BIG, wordorder=Endian.LITTLE)
    builder.add_32bit_int(position)
    payload = builder.build()
    print(payload)
    print('moving to position...')
    client.write_registers(1042, payload, count=2, unit=1, skip_encode=True)
    print('device in position')

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
