# RLP-ManoMimo

# Table of Contents
   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
   * [Documentation](#documentation)
   * [How to use](#how-to-use)
   * [Client-Server connection](#client-server-connection)
      * [Client](#client)
      * [Server](#server)
   * [Hand Detection](#hand-detection)
      * [Mediapipe landmark detection](#mediapipe-landmark-detection)
      * [Angles function](#angles-function)
      * [Finger models](#finger-models)
   * [Use-case](#use-case)
   * [Contribution](#contribution)
   * [Citing](#citing)
   * [Support](#support)
   * [Authors](#authors)

# What is this?

This is a collection of codes to make a robotic hand mimic movements

Features:

1. Easy to read, well structured and well commented.

2. There are tests of different types of servers and the most optimal ones are selected.

3. The code ranges from models to train fingers, landmark detection and servers to transfer information.


# Requirements

For running:

- [Python 3.11.x](https://www.python.org/)
- [OpenCV 4.4.0](https://opencv.org/)
- [Raspbian buster](https://downloads.raspberrypi.org/raspbian/images/raspbian-2019-07-12/)
- [Mediapipe](https://pypi.org/project/mediapipe/)

For development:
  
- [Matplotlib](https://matplotlib.org/stable/users/installing/index.html) (to view the results)


# Documentation

This README only shows our progress in the project and the different tests that we have been carrying out.

If you want to improve it, you can try more advanced models and different types of clients and servers.

# How to use

# Client-Server connection

Regarding the client-server connection we have tested 2 types:
- TCP
- UDP

Finally we have stayed with the tcp because when we receive frames from the camera we do not want to run the risk of them being lost because then the movements would be different from the real ones.

When doing the tests between the two, we thought that UDP would be faster than TCP, but it was something that we denied in a short time, since the times were almost identical. That made the decision even easier.

## Client

The most important thing to know is:

1. You can vary the frequency of the servos if necessary using the pca.frequency in line 22.
2. The server ip is added by SERVER_IP in line 28.
3. The server listening port is selected by SERVER_PORT on line 29
4. You can modify the camera index by CAMERA_INDEX in line 32
5. You can adjust the timeout using TIMEOUT on line 40, depending on the type of connection you have. The slower the more timeout will be necessary.
6. You can modify the size of the image by varying camera.set(cv2.CAP_PROP_FRAME_WIDTH, X) for the width and camera.set(cv2.CAP_PROP_FRAME_HEIGHT, Y) for the height on lines 49 and 50

## Server

The most important thing to know is:

1. As in the client, the server ip and the listening port are selected using SERVER_IP and SERVER_PORT in lines 51 and 52
2. Latency can be modified, which is the time that the hand records, then it is processed and sent to the client. It is explained in depth in the code on line 93

# Hand detection

## Mediapipe landmark detection

## Angles function

## Finger models

# Use-case

# Contribution

Contributions are always welcome! Please submit a Pull Request or send us an email.

# Citing

If you use this project's code for your academic work, we encourage you to cite it.

If you use this project's code in industry, we'd love to hear from you as well; feel free to reach out to the developers directly.

# Support

If you have any issues or suggestions, please open submit a Pull Request.

# Sponsors

This project is proudly supported by:

## Universidad Autónoma de Barcelona (UAB)

We're immensely grateful for the support provided by the Universidad Autónoma de Barcelona, our home institution. The academic knowledge, facilities, and inspiring environment at UAB have been crucial to the success of this project.

We invite other potential sponsors interested in supporting our project to contact us.

# Authors
