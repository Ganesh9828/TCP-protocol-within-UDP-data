UDP_PORT = 5005
MSS = 12 # maximum segment size

sock = socket.socket(socket.AF_INET,    # Internet
                     socket.SOCK_DGRAM) # UDP
