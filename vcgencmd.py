import sys
import zmq

# ...
context = zmq.Context()

# Socket Sub
subsocket = context.socket(zmq.SUB)
subsocket.connect('tcp://{}:9003'.format(sys.argv[1]))
subsocket.subscribe('')

# Socket Pub
pubsocket = context.socket(zmq.PUB)
pubsocket.connect('tcp://{}:9002'.format(sys.argv[1]))

while True:
  msg = "01 CC"
  msg = bytearray([int(i,16) for i in msg.split(' ')])  
  pubsocket.send(msg)

  try:
    rec_msg = subsocket.recv(flags=zmq.NOBLOCK)
    print(rec_msg)
  except zmq.Again:
    continue
