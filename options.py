#!/usr/bin/env python

import sqlite3
from db import conn, c
from audio_to_text import DEFAULT_DEST, DEFAULT_SRC

def set_defaults(options_dict):
    if 'dest' not in options_dict:
        options_dict['dest'] = DEFAULT_DEST
    if 'src' not in options_dict:
        options_dict['src'] = DEFAULT_SRC    
    return options_dict

# options_str looks like "#options dest:en src:fr"
def parse_options(options_str):
    tokens = options_str.split()[1:]
    options_dict = {}
    for token in tokens:
        try:
            [key, val] = token.split(':')
            options_dict[key] = val
        except:
            pass
    return set_defaults(options_dict)

def update_options(sender_id, options):
    options = set_defaults(options)
    print('Inside update_options, options: ')
    print(options)
    q = 'INSERT OR IGNORE INTO users (id, src, dest) VALUES (?, ?, ?)'
    conn.execute(q, (str(sender_id), options['src'], options['dest']))
    q = 'UPDATE users SET src=?, dest=? where id = ?'
    conn.execute(q, (options['src'], options['dest'], str(sender_id)))
    print('Updated users options. Src: %s, Dest: %s' % (options['src'], options['dest']))
    c.commit()
def get_options(sender_id):
    print('AAAAAAAAAAAAAAAAAAA')
    q = 'SELECT src, dest from users where id=%s' % (str(sender_id))
    print(q)
    conn.execute(q)
    (src, dest) = conn.fetchone()
    return {
        'src': src,
        'dest': dest
    }
    # return (src, dest)


default_opts = {
    'src': 'auto',
    'dest': 'en'
}
