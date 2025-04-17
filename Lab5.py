import smbus
import time

bus = smbus.SMBus(1)
address = 0x48
control_byte_1 = 0x40
control_byte_2 = 0x42

def read_analog_input():
    bus.write_byte(address, control_byte_1)

    # 读取第一次数据（废弃的）
    bus.read_byte(address)

    # 读取实际的AD转换数据
    digital_value = bus.read_byte(address)

    return digital_value

def convert_to_voltage(digital_value):
    voltage = digital_value * 3.3 / 255
    return voltage

def digital_to_analog(digital_value):
    bus.write_byte(address, control_byte_2)
    bus.write_byte_data(address, control_byte_1, digital_value)

try:
    while True:
        digital_value = read_analog_input()
        voltage = convert_to_voltage(digital_value)
        digital_to_analog(digital_value)
        print(f"当前电压值: {voltage:.2f} V -------- {digital_value}")
        time.sleep(0.1)

except KeyboardInterrupt:
    print("程序中断")

finally:
    bus.close()  # 关闭I2C总线连接