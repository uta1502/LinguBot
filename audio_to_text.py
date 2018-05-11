#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from os import path
import argparse
import sys
from arg_parser import get_args


def main():
    args = get_args()
    print(args)
    exit(1)
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

if __name__ == '__main__':
    main()
