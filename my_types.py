#!/usr/bin/env python

"""
Custom types
"""

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
