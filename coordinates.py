from typing import NamedTuple
import requests  #install requests
import http.client
import geocoder  #install geocoder
import stun  #install pystan3

import config
from exceptions import CantGetCoordinates, CantGetIP
from config import USE_ROUNDED_COORDS

class Coordinates(NamedTuple):
    latitude: float
    longitude: float

def _get_ip_1() -> str:
    """Returns IP using ifconfig.me"""
    conn = http.client.HTTPConnection("ifconfig.me")
    conn.request("GET", "/ip")
    ipi = conn.getresponse().read().decode("utf-8")  #first_way
    return ipi

def _get_ip_2() -> str:
    """Returns IP using stun"""
    ipi = stun.get_ip_info()[1]  #second_way
    return ipi

def _right_ip():
    try:
        ipi = _get_ip_1()
        if ipi:
            return ipi
    except:
        pass
    try:
        ipi = _get_ip_2()
        if ipi:
            return ipi
        else:
            raise CantGetIP
    except Exception:
        raise CantGetIP

def _round_coordinates(coordinates: Coordinates) -> Coordinates:
    if not config.USE_ROUNDED_COORDS:
        return coordinates
    else:
        return (Coordinates(round(coordinates.latitude, 1), round(coordinates.longitude, 1)))

#def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP"""
    ipi = _right_ip()
    try:
        geo = geocoder.ip(ipi)
        lat, lng = geo.latlng
        if not lat or not lng:
            raise CantGetCoordinates
    except Exception:
        raise CantGetCoordinates
    return _round_coordinates(Coordinates(latitude=lat, longitude=lng))

def get_coordinates() -> Coordinates:
    return Coordinates(latitude=55.4227, longitude=21.0834)