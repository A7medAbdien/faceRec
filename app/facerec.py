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
        self.img1 = Image(size_hint=(1, .8))  # Real time web cam feed
        self.button = Button(
            text="Verify", size_hint=(1, .1))  # Click to verify
        self.verification = Label(
            text="Verification Uninitiated", size_hint=(1, .1))  # the output/state

        # Add items to layout
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.img1)
        layout.add_widget(self.button)
        layout.add_widget(self.verification)

        return layout


if __name__ == '__main__':
    CamApp().run()
