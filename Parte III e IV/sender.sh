#!/bin/bash

# executar sender workers

python ~/SCAPS/Parte III e IV/service_providers/senderWorker.py &

# executar sender portas

python ~/SCAPS/Parte III e IV/door/door1/senderDoor1.py &
python ~/SCAPS/Parte III e IV/door/door2/senderDoor2.py &
python ~/SCAPS/Parte III e IV/door/door3/senderDoor3.py &

# executar sender elevador

python ~/SCAPS/Parte III e IV/elevator/elevator1/senderElevator1.py &
python ~/SCAPS/Parte III e IV/elevator/elevator2/senderElevator2.py &
python ~/SCAPS/Parte III e IV/elevator/elevator3/senderElevator3.py &
python ~/SCAPS/Parte III e IV/elevator/elevator4/senderElevator4.py &
python ~/SCAPS/Parte III e IV/elevator/elevator5/senderElevator5.py &

# executar sender ladder

python ~/SCAPS/Parte III e IV/ladder/ladder1/senderLadder1.py &
python ~/SCAPS/Parte III e IV/ladder/ladder2/senderLadder2.py &
python ~/SCAPS/Parte III e IV/ladder/ladder3/senderLadder3.py &
python ~/SCAPS/Parte III e IV/ladder/ladder4/senderLadder4.py &
python ~/SCAPS/Parte III e IV/ladder/ladder5/senderLadder5.py &

