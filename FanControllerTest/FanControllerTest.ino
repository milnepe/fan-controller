/*
  Radial-G fan controller output test
 
 Author: Pete Milne
 Date: 27-05-2019
 Version: 0.1
 */

#include <SoftwareSerial.h>

SoftwareSerial serial1(2, 3); // RX, TX

long output; // serial output

void setup() {
  Serial.begin(9600);
  serial1.begin(9600);
}

void loop() {

  if (Serial.available() > 0) { // Read buffer
    output = Serial.parseInt(); // Convert digits until newline
  }

  //print the results to the Serial Monitor:
  serial1.println(output);
  delay(2);
}



