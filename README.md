SMART HOME SYSTEM

For this project, we are developing a smart home system with the ability to automatically turn on and off the air-conditioner and fan with the help of IOTP devices. 
Using the BME sensor, the system will be able to detect changes in temperature and humidity in the home. If the temperature and humidity exceed a certain threshold, it will be able to automatically turn on the air-conditioning and fan. 
For our project, we have decided to simulate the air conditioning using the LED and the fan using the mini 5V fan. When temperatures exceed a threshold, it will turn on the mini fan (simulating the fan). If the humidity exceeds a threshold, it will turn on the LED (simulating the air-con). If the humidity exceeds a larger threshold, it will also turn on both the fan and air conditioning. 
The buzzer will represent an alert system within the house, just to notify the user when all appliances are turned on. 
Using MQTT, we can also send periodical updates to the user about the temperature and humidity in the home. An alert can be sent to the user if they wish to be notified when the temperature and humidity exceed the threshold and both the fan and air-conditioning are turned on. A button function is also added through MQTT, allowing the user to manually turn on the air-conditioning to cool the house down before they return.  
With the use of ThingBoard, the user will also be able to track the temperature and humidity in their home. Allowing for them to have a visual indicator of the temperature and humidity in their home.

IoT System Architecture
<img width="600" height="500" alt="image" src="https://github.com/user-attachments/assets/398f23f2-4c08-408c-97b9-9739b68c1766" />
MQTT App 
<img width="714" height="418" alt="image" src="https://github.com/user-attachments/assets/23510408-c5ae-42a7-a3f5-28242f2857d7" />
<img width="638" height="340" alt="image" src="https://github.com/user-attachments/assets/99d3dddf-3405-4219-aaf3-6ee6c108d5e0" />
<img width="531" height="429" alt="image" src="https://github.com/user-attachments/assets/932b8074-1dc5-45ed-ae60-f73338b30367" />
<img width="741" height="331" alt="image" src="https://github.com/user-attachments/assets/657526be-d9dc-4e43-ba99-58fcc05e1a05" />





