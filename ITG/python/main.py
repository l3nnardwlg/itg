import time
import turtle


from turtle import *
while True:
    forward(100)
    left(85)
    if abs(pos()) < 1:
        stop
