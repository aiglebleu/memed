#!/usr/bin/env python3
import socket
from random import randint

# TODO: Load the stuff below from a config file
MEMED_IP   = "127.0.0.1"
MEMED_PORT = 9001

# TODO: Retrieve the memes from a datasource
# TODO: Allow different types of memes (audio, gif, text, img...)
memes = []

with open("memes.txt") as f:
    memes = f.readlines()

# TODO: Allow UNIX socket usage
with socket.socket() as memed:
    # Prevents "address already in use"
    memed.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    memed.bind((MEMED_IP, MEMED_PORT))
    memed.listen(5)

    while True:
        # Discards remote address to close connection
        with memed.accept()[0] as conn:
            le_meme = memes[randint(0, 1)]
            conn.send(le_meme.encode())
