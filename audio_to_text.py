#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from os import path
import argparse
import sys
from arg_parser import get_args
from my_types import Mode, Platform

r = sr.Recognizer()
def convert_speech_to_text(speech, lang):
    txt = r.recognize_google(speech, language=lang)
    return txt

def parse_audio_files(files, lang):
    for file_name in files:
        with sr.AudioFile(file_name) as source:
            audio = r.record(source)
        try:
            txt = convert_speech_to_text(audio, lang)
            # print('Here is what google thinks you said:')
            print(txt)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

def parse_live_speech(args):
    print('Not implemented yet')
    pass

def main():
    args = get_args()
    files = args.files
    lang = args.lang
    mode = args.mode
    if mode == Mode.audio_file:
        parse_audio_files(files, lang)
    else:
        parse_live_speech(args)
    # exit(1)

if __name__ == '__main__':
    main()
