#!/usr/bin/env python
import argparse
from my_types import Mode, Platform
from lang import languages, countries

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prod", help="Run this in production", action="store_true")
    parser.add_argument("-m", "--mode", help="How to read in your speech",
                        type=Mode, default=Mode.live, choices=list(Mode))
    parser.add_argument("--platform", help="Which platform to run this on",
                        type=Platform, default=Platform.fb, choices=list(Platform))
    parser.add_argument("-l", "--lang", help="Which language to translate to",
                        type=str, default="en-US", choices=list(languages))
    parser.add_argument("files", nargs="+", help="Which files to read. Only when --mode=audio_files")

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    print(get_args())
