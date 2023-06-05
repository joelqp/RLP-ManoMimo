import cv2
import numpy as np
import socket
import struct
import pickle

from functions import calculate_the_angles
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import time
from collections import deque
import logging


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

from models import models
from models import model_medio
from models import model_anular
from models import model_menique
from models import model_pulgar