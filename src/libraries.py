import tkinter as tk
import tkinter.scrolledtext as st
import keyboard
import atexit
import os
import re
from win32api import GetSystemMetrics
from overlay import Window
from time import sleep
from googletrans import Translator
from threading import Thread