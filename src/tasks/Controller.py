#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 20:09:08 2021

@author: bernat
"""

#!/usr/bin/env python3

import socket
HOST = '10.10.10.10'  # The server's hostname or IP address (raspberry IP)
#HOST = '127.0.0.1'
PORT = 65432        # The port used by the server

while True:    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        msg = bytes(input(), 'utf-8')
        s.sendall(msg)
        data = repr(s.recv(1024))
        datarefined = data[2:len(data)-1:]
    
    print('Executing', datarefined)
