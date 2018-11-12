from netty_finder import Network

detector = Network("08182315466")
network_name =detector.get_network_name()
print(network_name)

# >>> 9mobile

detector = Network("081823154660")
network_name =detector.get_network_name()
print(network_name)

# >>> netty_finder.NetworkException: 🚫 Error! Invalid number. Number must not be greater than 11 digits
