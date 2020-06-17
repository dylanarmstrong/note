#!/usr/bin/env python3
import os
from sys import argv
from time import strftime, localtime
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def main():
    if len(argv) == 1:
        print('note [note text]')
        exit(1)

    data = ''
    path = '{}/notes.yml'.format(os.environ['HOME'])
    local = localtime()
    date = strftime('%B %d, %Y', local)
    time = strftime('%H:%M', local)

    if os.path.isfile(path):
        with open(path) as file:
            data += file.read()
        yml = load(data, Loader=Loader)
        if date not in yml:
            yml[date] = []
    else:
        yml = dict({ date: [] })

    note = ' '.join(argv[1:])
    yml[date].append('({}) {}'.format(time, note))

    with open(path, 'w') as file:
        dump(yml, file, Dumper=Dumper, default_flow_style=False)

if __name__ == '__main__':
    main()
