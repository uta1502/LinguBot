#!/usr/bin/env python
# -*- coding: utf-8 -*-

import speech_recognition as sr
from os import path, remove
import argparse
import sys
from arg_parser import get_args
from my_types import Mode, Platform
import subprocess
import urllib.request
import uuid

r = sr.Recognizer()
mp4_file = 'tmp_dwnld-' + str(uuid.uuid4()) + '.mp4'
wav_file = 'tmp_my_wav-' + str(uuid.uuid4()) + '.wav'

DEFAULT_SRC = 'en'
DEFAULT_DEST = 'es'

def convert_speech_to_text(speech, lang=DEFAULT_SRC):
    txt = r.recognize_google(speech, language=lang)
    return txt

def record_speech(str_data):
    with sr.AudioFile(str_data) as source:
        rec = r.record(source)
    return rec

def convert_audio_from_url(url, lang=DEFAULT_SRC):
    download_from_url(url)
    mp4_to_wav(mp4_file)
    try:
        [txt] = parse_audio_files([wav_file], lang)
    except Exception as e:
        print('Encountered exception: ' + str(e))
        txt = "Sorry, I could not translate that"
    try:
        remove(mp4_file)
        remove(wav_file)
    except Exception as e:
        print(e)
    return txt

def download_from_url(url):
    urllib.request.urlretrieve(url, mp4_file)
    print('Successfully saved file to : ' + mp4_file)

def mp4_to_wav(file_name):
    command = "ffmpeg -y -i %s -ab 160k -ac 2 -ar 44100 -vn %s" % (mp4_file, wav_file)
    print('Running the command: ')
    print(command)
    subprocess.call(command, shell=True)

def parse_audio_files(files, lang=DEFAULT_SRC):
    return_value = []
    for file_name in files:
        with sr.AudioFile(file_name) as source:
            audio = r.record(source)
        try:
            txt = convert_speech_to_text(audio, lang)
            # print('Here is what google thinks you said:')
            return_value.append(txt)
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
    return return_value

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

if __name__ == '__main__':
    main()
