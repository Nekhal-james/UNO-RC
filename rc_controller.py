import serial
import vgamepad as vg

# Change this to your Arduino's COM port
SERIAL_PORT = 'COM13' 
BAUD_RATE = 115200

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=0.1)
    print(f"Connected to Arduino on {SERIAL_PORT}")
except Exception as e:
    print(f"Error opening serial port: {e}")
    exit()

# Initialize the virtual Xbox 360 controller
gamepad = vg.VX360Gamepad()

def map_value(x, in_min, in_max, out_min, out_max):
    """Maps a value from one range to another."""
    return int(max(out_min, min(out_max, (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)))

print("Virtual Xbox Controller running. Press Ctrl+C to stop.")

try:
    while True:
        if ser.in_waiting > 0:
            # Read the serial line and decode it
            line = ser.readline().decode('utf-8').strip()
            
            if ',' in line:
                try:
                    steering_str, throttle_str = line.split(',')
                    steering = int(steering_str)
                    throttle = int(throttle_str)
                    
                    # 1. Map Steering (1000-2000) to Xbox Left Stick X (-32768 to 32767)
                    x_axis = map_value(steering, 1000, 2000, -32768, 32767)
                    gamepad.left_joystick(x_value=x_axis, y_value=0)

                    # 2. Map Throttle/Brake to Xbox Analog Triggers (0 to 255)
                    # We use deadzones (1480-1520) so the car doesn't creep forward or brake when the trigger is resting.
                    if throttle > 1520: 
                        # Gas (Pulling trigger)
                        gas = map_value(throttle, 1520, 2000, 0, 255)
                        gamepad.right_trigger(value=gas)
                        gamepad.left_trigger(value=0)
                    elif throttle < 1480: 
                        # Brake/Reverse (Pushing trigger)
                        # Notice we map 1480 down to 1000, converting to 0-255 pressure
                        brake = map_value(throttle, 1480, 1000, 0, 255)
                        gamepad.left_trigger(value=brake)
                        gamepad.right_trigger(value=0)
                    else:
                        # Center / Neutral
                        gamepad.left_trigger(value=0)
                        gamepad.right_trigger(value=0)

                    # Send the updated state to the OS
                    gamepad.update()
                except ValueError:
                    # Ignore corrupted serial reads
                    pass
except KeyboardInterrupt:
    print("\nExiting...")
finally:
    ser.close()