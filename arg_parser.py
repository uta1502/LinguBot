#!/usr/bin/env python
import argparse
from enum import Enum

class Mode(Enum):
    live = 'live'
    audio_file = 'audio_file'

    def __str__(self):
        return self.value

class Platform(Enum):
    fb = 'fb'
    slack = 'slack'

    def __str__(self):
        return self.value

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    parser.add_argument("--prod", help="Run this in production", action="store_true")
    parser.add_argument("-m", "--mode", help="How to read in your speech", type=Mode, choices=list(Mode))
    parser.add_argument("--platform", help="Which platform to run this on", type=Platform, choices=list(Platform))
    args = parser.parse_args()
    return args

print(get_args())
