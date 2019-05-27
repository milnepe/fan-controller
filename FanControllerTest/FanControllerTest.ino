/*
  Radial-G fan controller output test

  Author: Pete Milne
  Date: 27-05-2019
  Version: 0.1
*/

long RGspeed; // Speed in kph sent from Radial-G

void setup() {
  Serial.begin(9600);
}

void loop() {

  if (Serial.available() > 0) { // Read buffer
    RGspeed = Serial.parseInt(); // Convert digits until newline
  }

  //print the results to the Serial Monitor:
  Serial.print("RG Speed = ");
  Serial.print(RGspeed);
  Serial.println("kph");
  delay(2);
}


