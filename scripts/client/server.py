# -*- coding: utf-8 -*-
"""
    Simple server for test of client
"""
__author__ = 'Dmitry Kryukov'

from socket import *

def create_connection(HOST, PORT):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)
    return s

def activate(s):
    while True:
        client,addr = s.accept()
        print 'Connection from %s, port %s' % addr
        req = ''
        while True:
            chunk = client.recv(8192)
            req += chunk
            if '\r\n\r\n' in req:
                break
        print req
        answer = 'HTTP/1.0 200 OK\r\nServer: nginx\r\n'
        answer += 'Content-Type: text/html; charset=UTF-8\r\n'
        answer += 'Connection: close\r\n\r\n'
        answer += """<html>
                        <head>
                            <title>Тест</title>
                            <link rel="shortcut icon" href="http://static.rutracker.org/favicon.ico" type="image/x-icon">
                        </head>
                        <body>
                            <a href="./first.php">1</a>
                            <a href="../second.php">2</a>
                            <a href="http://wiki.rutracker.org/">3</a>
                            <a href="/go/4">4</a>
                            <a href="../../../../../../../forum/viewforum.php?f=329">5</a>
                            <a href="viewtopic.php?t=964118">6</a>
                        </body>
                    </html>"""
        client.send(answer)
        client.close()

if __name__ == '__main__':
    HOST = ''
    PORT = 8080
    s = create_connection(HOST, PORT)
    activate(s)

