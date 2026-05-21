#include <NewPing.h>
#include <ESP32Servo.h>

// -------------------- Ultrasonic Pins --------------------
#define TRIG_PIN 5
#define ECHO_PIN 18
#define MAX_DISTANCE 200

// -------------------- Motor Pins --------------------
#define ENA 14
#define IN1 27
#define IN2 26

#define ENB 25
#define IN3 33
#define IN4 32

// -------------------- Servo Pin --------------------
#define SERVO_PIN 13

// -------------------- Objects --------------------
NewPing sonar(TRIG_PIN, ECHO_PIN, MAX_DISTANCE);
Servo myservo;

// -------------------- Variables --------------------
int distance = 100;

// ======================================================
// SETUP
// ======================================================

void setup() {

  Serial.begin(115200);

  // Motor Pins
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);

  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);

  pinMode(ENA, OUTPUT);
  pinMode(ENB, OUTPUT);

  // Servo Setup
  myservo.attach(SERVO_PIN);
  myservo.write(115);

  Serial.println("Robot Starting...");
  
  delay(2000);

  distance = readPing();
}

// ======================================================
// LOOP
// ======================================================

void loop() {

  Serial.print("Distance: ");
  Serial.println(distance);

  if (distance <= 15) {

    Serial.println("Obstacle Detected");

    stopMotors();
    delay(300);

    Serial.println("Moving Backward");
    moveBackward();
    delay(400);

    stopMotors();
    delay(300);

    int rightDistance = lookRight();
    delay(300);

    int leftDistance = lookLeft();
    delay(300);

    Serial.print("Right Distance: ");
    Serial.println(rightDistance);

    Serial.print("Left Distance: ");
    Serial.println(leftDistance);

    if (rightDistance >= leftDistance) {

      Serial.println("Turning Right");
      turnRight();

    } else {

      Serial.println("Turning Left");
      turnLeft();
    }

    stopMotors();

  } else {

    Serial.println("Moving Forward");
    moveForward();
  }

  distance = readPing();

  delay(200);
}

// ======================================================
// ULTRASONIC FUNCTIONS
// ======================================================

int readPing() {

  delay(70);

  int cm = sonar.ping_cm();

  if (cm == 0) {
    cm = 250;
  }

  return cm;
}

// ======================================================
// SERVO LOOK FUNCTIONS
// ======================================================

int lookRight() {

  Serial.println("Looking Right");

  myservo.write(50);

  delay(500);

  int distance = readPing();

  myservo.write(115);

  return distance;
}

int lookLeft() {

  Serial.println("Looking Left");

  myservo.write(170);

  delay(500);

  int distance = readPing();

  myservo.write(115);

  return distance;
}

// ======================================================
// MOTOR FUNCTIONS
// ======================================================

void moveForward() {

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void moveBackward() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  analogWrite(ENA, 180);
  analogWrite(ENB, 180);
}

void stopMotors() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
}

void turnRight() {

  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);

  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);

  delay(500);
}

void turnLeft() {

  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);

  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);

  delay(500);
}