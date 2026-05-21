#define TRIG_PIN 5
#define ECHO_PIN 18

#define IN1 26
#define IN2 27
#define IN3 14
#define IN4 13

#include  <NewPing.h>        //Ultrasonic sensor function library. You must install this library
#include  <Servo.h>          //Servo motor library. This is standard library


const  int LeftMotorForward = 2;
const int LeftMotorBackward = 3;
const int RightMotorForward  = 4;
const int RightMotorBackward = 5;

//sensor pins
#define trig_pin  A1 //analog input 1
#define echo_pin A2 //analog input 2

#define maximum_distance  200
boolean goesForward = false;
int distance = 100;

NewPing sonar(trig_pin,  echo_pin, maximum_distance); //sensor function
Servo servo_motor; //our servo  name


void setup(){

pinMode(RightMotorForward, OUTPUT);
pinMode(LeftMotorForward,  OUTPUT);
pinMode(LeftMotorBackward, OUTPUT);
pinMode(RightMotorBackward,  OUTPUT);
  
servo_motor.attach(8); //our servo pin
33
34  servo_motor.write(115);
35  delay(2000);
36  distance = readPing();
37  delay(100);
38  distance = readPing();
39  delay(100);
40  distance = readPing();
41  delay(100);
42  distance = readPing();
43  delay(100);
44}
45
46void loop(){
47
48  int distanceRight = 0;
49  int  distanceLeft = 0;
50  delay(50);
51
52  if (distance <= 20){
53    moveStop();
54    delay(300);
55    moveBackward();
56    delay(400);
57    moveStop();
58    delay(300);
59    distanceRight = lookRight();
60    delay(300);
61    distanceLeft  = lookLeft();
62    delay(300);
63
64    if (distance >= distanceLeft){
65      turnRight();
66      moveStop();
67    }
68    else{
69      turnLeft();
70      moveStop();
71    }
72  }
73  else{
74    moveForward(); 
75  }
76    distance = readPing();
77}
78
79int  lookRight(){  
80  servo_motor.write(50);
81  delay(500);
82  int distance =  readPing();
83  delay(100);
84  servo_motor.write(115);
85  return distance;
86}
87
88int  lookLeft(){
89  servo_motor.write(170);
90  delay(500);
91  int distance = readPing();
92  delay(100);
93  servo_motor.write(115);
94  return distance;
95  delay(100);
96}
97
98int  readPing(){
99  delay(70);
100  int cm = sonar.ping_cm();
101  if (cm==0){
102    cm=250;
103  }
104  return cm;
105}
106
107void moveStop(){
108  
109  digitalWrite(RightMotorForward,  LOW);
110  digitalWrite(LeftMotorForward, LOW);
111  digitalWrite(RightMotorBackward,  LOW);
112  digitalWrite(LeftMotorBackward, LOW);
113}
114
115void moveForward(){
116
117  if(!goesForward){
118
119    goesForward=true;
120    
121    digitalWrite(LeftMotorForward,  HIGH);
122    digitalWrite(RightMotorForward, HIGH);
123  
124    digitalWrite(LeftMotorBackward,  LOW);
125    digitalWrite(RightMotorBackward, LOW); 
126  }
127}
128
129void moveBackward(){
130
131  goesForward=false;
132
133  digitalWrite(LeftMotorBackward, HIGH);
134  digitalWrite(RightMotorBackward,  HIGH);
135  
136  digitalWrite(LeftMotorForward, LOW);
137  digitalWrite(RightMotorForward,  LOW);
138  
139}
140
141void turnRight(){
142
143  digitalWrite(LeftMotorForward,  HIGH);
144  digitalWrite(RightMotorBackward, HIGH);
145  
146  digitalWrite(LeftMotorBackward,  LOW);
147  digitalWrite(RightMotorForward, LOW);
148  
149  delay(500);
150  
151  digitalWrite(LeftMotorForward, HIGH);
152  digitalWrite(RightMotorForward, HIGH);
153  
154  digitalWrite(LeftMotorBackward, LOW);
155  digitalWrite(RightMotorBackward,  LOW);
156 
157  
158  
159}
160
161void turnLeft(){
162
163  digitalWrite(LeftMotorBackward,  HIGH);
164  digitalWrite(RightMotorForward, HIGH);
165  
166  digitalWrite(LeftMotorForward,  LOW);
167  digitalWrite(RightMotorBackward, LOW);
168
169  delay(500);
170  
171  digitalWrite(LeftMotorForward, HIGH);
172  digitalWrite(RightMotorForward, HIGH);
173  
174  digitalWrite(LeftMotorBackward, LOW);
175  digitalWrite(RightMotorBackward,  LOW);
176}
