##Hardware list:

*Car Frame

*Raspberry Pi 3 Model B or Pi4

*L298N Dual H-Bridge Motor Driver(if you are using DC motors)

*Ultrasonic Sensor (HC-SR04)

*Pi Camera Module (or any USB cam will work fine)

*Lipo battery 


##prerequisites

*OpenCV 4
*FFmpeg(This will be used to send the stream to a laptop / any device )
*Tensorflow 
*SSH

##Setup:

[Raspberry Pi motor circuitry](https://business.tutsplus.com/tutorials/controlling-dc-motors-using-python-with-a-raspberry-pi--cms-20051)

[Raspberry Pi range sensor circuitry](https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi)

[For detailed design](http://www.jayeshg.com/self-driving-car/)


##Data collection
The TensorFlow machine learning algorithm/model needs data to learn from. The data consists of two parts.

Video data: A video is nothing more than a series of photos. I use OpenCV to represent each frame as a matrix of numbers, where each number represents a pixel. If you want black-and-white video, OpenCV will give you a 2-dimensional matrix consisting of a frame's height and width. If you decide you want color video, then OpenCV will give you a 3-dimensional matrix consisting of not just height and width but also color depth: red, green, and blue. The machine learning model will use the pixels of the matrix as predictors.

Command data: Commands tell the motors what to do and represent the target variable. The model will try to learn which commands to send to the motor based on the video that it sees. I went for simplicity, so I defined only three types of commands: left, right, and forward. This makes driving a multinomial classification problem. The downside of having just three commands is that the instructions can be rather crude. There is no distinction between a wide and a sharp turn.


##How data collection works
*Raspberry Pi video streaming using a complicated Linux video utility
*A tangled mess for viewing and saving the streamed video data
*A restful API web server that runs on the Pi and takes commands from a web browser like Google Chrome running on your laptop
*Something for moving API command files from the Pi to your laptop where the video data is saved
*A data cleaning tool that matches your target and predictor data by timestamp and outputs a final clean numpy file that TensorFlow can ingest

#Run these commands
sudo ffserver -f /etc/ff.conf_original & ffmpeg -v quiet -r 5 -s 320x240 -f video4linux2 -i /dev/video0 http://localhost/webcam.ffm

sudo python3 drive_api.py --speed_percent 50

python3 save_streaming_video_data.py --host localhost/webcam.jpg


