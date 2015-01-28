#!/usr/bin/env python
# coding=utf-8
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))

s.send('GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:close\r\n\r\n')

buffer = []

while True:
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)
s.close()
header, html = data.split('\r\n\r\n', 1)
#print header
header_itesm = header.split('\r')
#print header_itesm[0]
header_stage = header_itesm[0].split(' ')
print header_stage[1]

website_stage = int(header_stage[1])

if website_stage != 200:
    print "ERROR"
else:
    pass


