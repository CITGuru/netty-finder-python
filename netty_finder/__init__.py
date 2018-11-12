#!/usr/bin/python
# -*- coding: utf-8 -*-

networks = {
    '9mobile': ['0809', '0909', '0817', '0818', '0908'],
    'mtn': ['0806', '0803', '0816', '0813', '0810', '0814', '0903', '0906', '0703', '0706'],
    'glo': ['0805','0705','0905','0807','0815'],
    'airtel': ['0802', '0902', '0701', '0808', '0708', '0812', '0907'],
    'starcomms': ['07028', '07029', '0819'],
    'visafone': ['07025', '07026', '0704'],
    'multilinks': ['07027', '0709'],
    'zoom': ['0707'],
    'ntel': ['0804'],
    'smile': ['0702']
}

class NetworkException(Exception):
    pass

class Network(object):
    """
    A network class for detecting nigerians number network
    """
    
    def __init__(self, phone, *args, **kwargs):
        self.phone = str(phone)
    
    def get_networks(self):
        return networks

    def get_network_name(self):
        self.validate()
        phone_primary_prefix = self.get_phone_prefix()
        phone_secondary_prefix = self.get_phone_prefix(5)
        networks = self.get_networks()

        if phone_primary_prefix in networks["mtn"]:
            return "MTN"
        elif phone_primary_prefix in networks["glo"]:
            return "GLO"
        elif phone_primary_prefix in networks["9mobile"]:
            return "9mobile"
        elif phone_primary_prefix in networks["airtel"]:
            return "Airtel"
        elif phone_secondary_prefix in networks["starcomms"] or phone_primary_prefix in networks["starcomms"]:
            return "Starcomms"
        elif phone_secondary_prefix in networks["visafone"] or phone_primary_prefix in networks["visafone"]:
            return "Visafone"
        elif phone_primary_prefix in networks["multilinks"] or phone_secondary_prefix in networks["multilinks"]:
            return "Multilinks"
        elif phone_primary_prefix in networks["zoom"]:
            return "Zoom"
        elif phone_primary_prefix in networks["ntel"]:
            return "Ntel"
        elif phone_primary_prefix in networks["smile"]:
            return "Smile"
        else:
            return None
        
    def get_phone_prefix(self, length=4):
        return self.phone[0:length]
    
    def validate(self):
        if len(self.phone) == 0:
            raise NetworkException("Invalid phone number")
        
        if not self.phone.isdigit():
            raise NetworkException("Phone number contains unwanted characters")

        if len(self.phone) < 11:
            raise NetworkException("🚫 Error! Invalid number. Number must not be lesser than 11 digits")

        if len(self.phone) > 11:
            raise NetworkException("🚫 Error! Invalid number. Number must not be greater than 11 digits")

        return True