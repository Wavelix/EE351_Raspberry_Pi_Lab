import smbus
import math

bus = smbus.SMBus(1)
address = 0x48
control_byte_1 = 0x40

def read_analog_input():
    bus.write_byte(address, control_byte_1)

    # 读取第一次数据（废弃的）
    bus.read_byte(address)

    # 读取实际的AD转换数据
    digital_value = bus.read_byte(address)

    return digital_value


def convert(digital_value):
    Vr=5*float(digital_value)/255
    Rt=10000*Vr/(5-Vr)
    T=1/(math.log(Rt/10000)/3950+1/398.15)
    return T

try:
    while True:
        digital_value = read_analog_input()
        result = convert(digital_value)
        print(result)

except KeyboardInterrupt:
    print("程序中断")

finally:
    bus.close()  # 关闭I2C总线连接