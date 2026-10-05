# UNO-RC

This project allows you to use an RC Transmitter and Receiver (like the FlySky GT3) as a virtual Xbox 360 controller on your PC. It uses an Arduino to read the PWM signals from the RC receiver and sends them over a serial connection to a Python script, which translates them into virtual gamepad inputs.

## Features

- **Steering** maps to the Left Joystick X-axis.
- **Throttle** maps to the Analog Triggers:
  - Pulling the throttle maps to the Right Trigger (Gas).
  - Pushing the throttle (brake/reverse) maps to the Left Trigger (Brake).
- Adjustable deadzone to prevent accidental movement when the trigger is neutral.
- Failsafe defaults to neutral if the transmitter is turned off.

## Requirements

### Hardware
- An Arduino (e.g., Arduino Uno)
- An RC Transmitter and Receiver (e.g., FlySky GT3)
- Jumper wires

### Software
- Python 3.x
- Arduino IDE (to upload the sketch)
- Python packages: `pyserial` and `vgamepad`

## Hardware Setup

Connect your RC receiver to the Arduino using the following pins:

| RC Receiver | Arduino Pin |
| ----------- | ----------- |
| CH1 (Steering)| Digital Pin 2 |
| CH2 (Throttle)| Digital Pin 3 |
| VCC         | 5V          |
| GND         | GND         |

## Installation & Usage

### 1. Arduino Setup
1. Open the `UNO_Code/UNO_Code.ino` sketch in the Arduino IDE.
2. Select your Arduino board and COM port.
3. Upload the code to your Arduino.
4. Note the COM port used by your Arduino (e.g., `COM13`).

### 2. Python Setup
1. Open a terminal or command prompt.
2. Install the required Python dependencies:
   ```bash
   pip install pyserial vgamepad
   ```
3. Open `rc_controller.py` in a text editor.
4. Modify the `SERIAL_PORT` variable on line 5 to match your Arduino's COM port (e.g., `SERIAL_PORT = 'COM13'`).
5. Run the Python script:
   ```bash
   python rc_controller.py
   ```

### 3. Play
Once the script is running, Windows will detect a new "Xbox 360 Controller for Windows". You can now launch your favorite racing games and use your RC transmitter as the controller!

Press `Ctrl+C` in the terminal to stop the script and disconnect the virtual controller.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
