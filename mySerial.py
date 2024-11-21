import serial
import serial.tools.list_ports as list_ports

def get_ports():
    return [port.device for port in list(serial.tools.list_ports.comports())]

def connect(port, baudrate):
    try:
        ser = serial.Serial(port, int(baudrate))
        print("成功连接到 " + port)
        # 在连接成功后，你可以添加更多的操作，例如数据读取等
        ser.close()  # 连接成功后记得关闭串口
    except Exception as e:
        print("连接失败: " + str(e))

def main():
    print("可用的串口:")
    ports = get_ports()
    for i, port in enumerate(ports):
        print(f"{i + 1}: {port}")

    port_choice = input("请选择串口 (输入数字): ")
    try:
        selected_port = ports[int(port_choice) - 1]
    except (IndexError, ValueError):
        print("无效的串口选择。")
        return

    baudrate = input("请输入波特率（如9600）：")

    connect(selected_port, baudrate)

if __name__ == "__main__":
    main()
