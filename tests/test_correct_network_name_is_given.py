from unittest import TestCase
from netty_finder import Network

class NetworkDetector:
    phone = None
    network_name = None

    def setUp(self):
        self.detector = Network(self.phone)
    
    def test_none_is_not_returned(self):

        assert self.detector.get_network_name() is not None

    def test_right_network_name_is_given(self):
        
        assert self.detector.get_network_name() == self.network_name


class NetworkDetector9Mobile(NetworkDetector, TestCase):
    phone = "08182315466"
    network_name = "9mobile"

    

