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
r = sr.Recognizer()
mp4_file = 'tmp_dwnld.mp4'
wav_file = 'tmp_my_wav.wav'

def convert_speech_to_text(speech, lang='en-US'):
    txt = r.recognize_google(speech, language=lang)
    return txt

def record_speech(str_data):
    with sr.AudioFile(str_data) as source:
        rec = r.record(source)
    return rec

def convert_audio_from_url(url):
    download_from_url(url)
    mp4_to_wav(mp4_file)
    parse_audio_files([wav_file])
    try:
        remove(mp4_file)
        remove(wav_file)
    except:
        pass


def download_from_url(url):
    urllib.request.urlretrieve(url, mp4_file)
    print('Successfully saved file to : ' + mp4_file)

def mp4_to_wav(file_name):
    command = "ffmpeg -i %s -ab 160k -ac 2 -ar 44100 -vn %s" % (mp4_file, wav_file)
    print('Running the command: ')
    print(command)
    subprocess.call(command, shell=True)

def parse_audio_files(files, lang='en-US'):
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

if __name__ == '__main__':
    main()
