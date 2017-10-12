#!/usr/bin/env python
import socket
from random import randint

# TODO: Load the stuff below from a config file
MEMED_IP   = "127.0.0.1"
MEMED_PORT = 9001

# TODO: Retrieve the memes from a datasource
# TODO: Allow different types of memes (audio, gif, text, img...)
memes = ["Generic meme \#1", "Generic meme \#2"]

# TODO: Allow UNIX socket usage
memed = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
memed.bind((MEMED_IP, MEMED_PORT))
memed.listen(1)

conn, addr = memed.accept()
conn.send(memes[randint(0, 1)])
