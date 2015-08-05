#!/bin/bash
#This script run every 15 seconds
while (sleep 10 && python /home/geek/h.py) &
do
  wait $!
done