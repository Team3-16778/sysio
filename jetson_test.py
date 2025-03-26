import serial
import time

# Open both Arduinos
arduino1 = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
arduino2 = serial.Serial('/dev/ttyACM1', 9600, timeout=1)
time.sleep(2)  # Allow time to reset

# Send commands
arduino1.write(b'START_MOTOR\n')
arduino2.write(b'READ_SENSOR\n')

# Read responses
resp1 = arduino1.readline().decode().strip()
resp2 = arduino2.readline().decode().strip()

print("Arduino 1:", resp1)
print("Arduino 2:", resp2)
