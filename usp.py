import serial
import time


port = input("Enter your modeum porrt >>> ")
baud_rate = 9600


modem = serial.Serial(port, baud_rate, timeout=1)


def send_ussd_command(command):
    try:

        modem.write(b'AT\r')
        time.sleep(1)
        response = modem.read(modem.in_waiting).decode('utf-8')
        print("تأكيد الاتصال:", response)


        modem.write(f'AT+CUSD=1,"{command}",15\r'.encode())
        time.sleep(5)


        response = modem.read(modem.in_waiting).decode('utf-8')
        print("رد الموديم:", response)

    except Exception as e:
        print(f"حدث خطأ: {e}")
    finally:
        modem.close()


ussd_code = "*878#"  
send_ussd_command(ussd_code)
