# -*- coding: utf-8 -*-


import requests
from datetime import datetime, timezone
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import json

class ValeConnect():

    self.ROOT_URL = ""

    # Constructor
    def __init__(self,root_url):
        # no need for super init

        self.ROOT_URL = root_url
