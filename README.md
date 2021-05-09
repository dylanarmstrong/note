### note.py

```
$ ./note.py hello world
```

Will write to `$HOME/notes.db`.

This can be read with:

```
$ ./note.py --read
```

Returning:

```
May 09, 2021:
- (11:25) hello world
```

For optimal use, put in `$HOME/bin` folder under a name like `note` for easier usage.
