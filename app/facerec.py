# Import Kivy dependencies
# App Layer
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

# kivy UX components
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label

# to make continuous updates to our app
from kivy.clock import Clock
# we should convert our OpenCV image to Texture and set our image equal to that texture
from kivy.graphics.texture import Texture
# to show some matrices
from kivy.logger import Logger

# import other dependencies
import cv2
import tensorflow as tf
from layers import L1Dist
import os
import numpy as np


# Build app and layout
class CamApp(App):

    def build(self):
        # Main layout Components
        self.web_cam = Image(size_hint=(1, .8))  # Real time web cam feed
        self.button = Button(
            text="Verify", size_hint=(1, .1))  # Click to verify
        self.verification = Label(
            text="Verification Uninitiated", size_hint=(1, .1))  # the output/state

        # Add items to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.web_cam)
        layout.add_widget(self.button)
        layout.add_widget(self.verification)

        # Setup video capture device
        # get image form webcam
        self.capture = cv2.VideoCapture(0)
        # schedule_interval: will do this event every x seconds
        Clock.schedule_interval(self.update, 1.0/33.0)

        return layout

    # Run continuously to get webcam feed
    # convert raw OpenCV image -> texture can be rendered
    def update(self, *args):

        # Read frame form OpenCV
        ret, frame = self.capture.read()
        frame = frame[120:120+250, 200:200+250, :]

        # Flip horizontall and convert image to texture
        # save cv2 image
        buf = cv2.flip(frame, 0).tostring()
        # Create image texture with this frame sizes and color format (bgr is the color format of opencv images)
        img_texture = Texture.create(
            size=(frame.shape[0], frame.shape[1]), colorfmt='bgr')
        # Convert image  to Texture
        img_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # Assign the texture to the webcam
        self.web_cam.texture = img_texture

    def preprocess(file_path):
        # Read in image, as a bytes-like object, from file path
        byte_img = tf.io.read_file(file_path)
        # load in the image
        img = tf.io.decode_jpeg(byte_img)

        # Preprocessing steps
        # 1. resizing the image to be 100x100
        img = tf.image.resize(img, (100, 100))
        # 2. Scale image to be between 0 and 1
        img /= 255.0
        return img


if __name__ == '__main__':
    CamApp().run()
