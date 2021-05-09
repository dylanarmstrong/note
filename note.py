#!/usr/bin/env python3
from pathlib import Path
from sys import argv
import argparse
import datetime
import os
import sqlite3

def main():
    parser = argparse.ArgumentParser(description='Take Notes')
    parser.add_argument('--read', action='store_true', help='Read current notes')
    parser.add_argument('words', type=str, nargs='*', help='All the words to put in note', default='')
    args = parser.parse_args()

    home = str(Path.home())
    path = f'{home}/notes.db'

    read = args.read
    words = ' '.join(args.words)
    if not read and len(words) == 0:
        print(parser.format_help())
        exit(1)

    con = sqlite3.connect(
        path,
        detect_types=sqlite3.PARSE_DECLTYPES
    )
    cur = con.cursor()

    if read:
        cur.execute('select date, note from notes order by date desc')
        prev_date = ''
        for [stamp, note] in cur.fetchall():
            date = stamp.strftime('%B %d, %Y')
            if prev_date != date:
                if prev_date != '':
                    print('')
                print(f'{date}:')
                prev_date = date
            time = stamp.strftime('%H:%M')
            print(f'- ({time}) {note}')

    else:
        cur.execute('''
            create table if not exists notes (
                id integer primary key,
                date timestamp default (datetime('now', 'localtime')),
                note text
            )'''
        )

        cur.execute('insert into notes (note) values (?)', [words])
        con.commit()

    con.close()

if __name__ == '__main__':
    main()
