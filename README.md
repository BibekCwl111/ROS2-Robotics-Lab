# ROS2 Distance Monitoring System 🚀

A real-time ROS2-based distance monitoring system using an HC-SR04 ultrasonic sensor and Arduino.

## 📌 Features

- Real-time distance measurement
- ROS2 Publisher & Subscriber communication
- Obstacle detection logic
- Arduino serial communication
- Distance filtering for invalid readings

---

# 🛠️ Hardware Used

- Arduino UNO
- HC-SR04 Ultrasonic Sensor
- USB Cable
- Ubuntu 22.04
- ROS2 Humble

---

# 📂 Project Structure

```bash
ROS2_Projects/
 ├── src/
 │    ├── distance_monitor/
 │
 ├── arduino/
 │    ├── distance_sensor/
 │    │    ├── distance_sensor.ino
 │
 ├── images/
 │
 ├── README.md
 ├── .gitignore
```

---

# ⚙️ ROS2 Nodes

## Distance Publisher
Reads distance data from Arduino serial port and publishes it to the `/distance` topic.

## Distance Subscriber
Subscribes to `/distance` topic and detects nearby obstacles.

---

# 🚀 How to Run

## Build Workspace

```bash
cd ~/ROS2_Projects
colcon build
source install/setup.bash
```

## Run Publisher

```bash
ros2 run distance_monitor distance_publisher
```

## Run Subscriber

```bash
ros2 run distance_monitor distance_subscriber
```

---

# 🔌 Arduino Wiring

| HC-SR04 | Arduino UNO |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | D9 |
| ECHO | D10 |

---

# 📸 Output

Real-time distance values and obstacle warnings are displayed in ROS2 terminal nodes.

---

# 🎯 Future Improvements

- Radar GUI
- Buzzer alert system
- Traffic monitoring integration
- Motor control system

---

# 👨‍💻 Author

Bibek

