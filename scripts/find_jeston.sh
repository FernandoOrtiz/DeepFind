#!/bin/bash
fping -c 1 -q -g -i 11 172.16.1.0/24 > /dev/null
arp -n | grep "00:04:4b:8d:02"
