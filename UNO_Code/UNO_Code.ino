const int steeringPin = 2; // CH1
const int throttlePin = 3; // CH2

void setup() {
  // Use a fast baud rate for low latency control
  Serial.begin(115200); 
  pinMode(steeringPin, INPUT);
  pinMode(throttlePin, INPUT);
}

void loop() {
  int steering = pulseIn(steeringPin, HIGH, 25000);
  int throttle = pulseIn(throttlePin, HIGH, 25000);
  
  // Failsafe: if transmitter is off, default to center values
  if (steering == 0) steering = 1500;
  if (throttle == 0) throttle = 1500;

  // Print format: steering,throttle
  Serial.print(steering);
  Serial.print(",");
  Serial.println(throttle);
  
  // Small delay to cap the refresh rate to ~100Hz
  delay(10); 
}