#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from os import path
import argparse
import sys


modes = ['live', 'audio_file']

file_name = sys.argv[1]
try:
    lang = sys.argv[2]
except IndexError:
    lang = "en-US"

r = sr.Recognizer()
with sr.AudioFile(file_name) as source:
    audio = r.record(source)

try:
    print('Here is what google thinks you said:')
    my_text = r.recognize_google(audio, language=lang)
    print(my_text)
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))

def main(): 
    pass
    # args = parseArgs()
    # fileOut = fileName(args.is_dev)
    # g = authenticate()
    # writeGitignore(fileOut, g, args.langs)


def parseArgs():
    """
    returns CLI args as list, and dev flag.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--is_dev", help="is_dev argparse help here", action="store_true")
    parser.add_argument("mode", help="live|audio_file", nargs="+")

    args = parser.parse_args()
    return args

