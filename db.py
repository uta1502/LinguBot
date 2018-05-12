#!/usr/bin/env python

import sqlite3

DB_FILE = 'users.db'
c = sqlite3.connect(DB_FILE, check_same_thread=False)
conn = c.cursor()
