import signal, os
def receiveSignal(signalNumber, frame):
    print "Received: ", signalNumber
    print "Exit Python!"
    ########## YOUR CODE GOES HERE ##########

    grovepi.ledBar_setLevel(port_ledbar, 0)

    ########## YOUR CODE ENDS HERE ##########
    os._exit(0)
signal.signal(signal.SIGINT, receiveSignal)

########## YOUR CODE GOES HERE ##########
import grovepi

port_ledbar = 5
port_ranger = 4

grovepi.ledBar_init(port_ledbar, 0)
grovepi.ledBar_orientation(port_ledbar, 1)
grovepi.pinMode(port_ledbar, "OUTPUT")

range_max = 30
ledbar_nof_levels = 10
lvl = 0

while True:
    dist = grovepi.ultrasonicRead(port_ranger)

    if dist <= range_max :
        lvl = int((range_max - dist)/(range_max/ledbar_nof_levels))
    else:
        lvl = 0

    if lvl >= 0 and lvl <= ledbar_nof_levels:
        grovepi.ledBar_setLevel(port_ledbar, lvl)

    print lvl , "<->" , dist

########## YOUR CODE ENDS HERE ##########