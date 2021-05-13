# Robot Control Center App

## Table of contents
1. [Introduction](##introduction)
2. [Main Screen](##Home Screen)
3. [Buttons Screen](##Buttons Screen)
4. [Sliders Screen](##Sliders Screen)
5. [Joystick Screen](##Joystick Screen)
6. [Sensor Servo Screen](##Sensor Servo Screen)



## Introduction

**Robot Control Center** is a *kivy* app designed for the control of the *GoPiGo* from *Dexter OS*. It has four basic functionalities, of which the first three concern the movement of the robot and the last concerns the control of the servo-and-sensor system.

The application has five main screens: a home screen and a screen for each of the functionalities. An overview of each screen is given in the following sections.

## Home Screen

The home screen contains two sections: one which contains the elements necessary to make the connection with the robot and another which contains the links (buttons) to go to the other screens. All other screens also have a home button to return to the home screen.

The connection to the robot is done following these steps:

- Connect your device to the wifi network of the robot

- Open the app and enter the *IP* address of the robot in the first text box

- Enter the port that the robot is listening to in the second text box

- Hit the *connect* button

A popup window will display whether the connection has been successful or not.

## Buttons Screen

This screen contains nine buttons to control the robot movement (forward, right, left, stop etc.). A tenth button provides the link to the home screen.

## Sliders Screen

This screen provides two sliders: one to control the speed of the right motor (right slider) and another to control the speed of the left motor (left slider). The values of the slider are shown on the labels that are directly below them. The home button is a link to the home screen.

## Joystick Screen

This screen provides a means to control the robot via a joystick, which is positioned in the center of the canvas. Above the joystick, we also have four labels. The top two labels show the *x* and *y* positions of the joystick pointer. The lower two labels show the power that is being sent to each of the motors. Again, the home button links to the home screen.

## Sensor Servo Screen

This screen contains two useful functionalities: the control of the servo where the sensor is mounted, via the top three buttons (spin left, face forward, and spin right); and the measurement of distances by means of the distance sensor, which is done by clicking the *measure* button (the measurement is then displayed in the label right below the button). Again, there is also a home buton that links to the home screen.

