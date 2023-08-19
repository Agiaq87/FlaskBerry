import threading

from config.flask_berry_config import FlaskBerryConfig
from config.singleton import Singleton
from model.state.user_session_state import UserSessionState
from util.net_converter import mac_from_ip


class PersistenceUserSessionManager(metaclass=Singleton):
    def __init__(self):
        self._retrieveDictionary = {"0.1.0.1": 0}
        self._banDictionary = {"0.1.0.1": 0}
        self._waitingForUnlockBanList = {"0.1.0.1": threading.Timer}
        self._presentedUser = {"0.1.0.1": False}

    def register_correct_presentation(self, ip_address: str):
        self._presentedUser[mac_from_ip(ip_address)] = True

    def register_incident(self, ip_address: str) -> UserSessionState:
        mac_address = mac_from_ip(ip_address)
        if mac_address in self._retrieveDictionary:
            self._retrieveDictionary[mac_address] += 1
        else:
            self._retrieveDictionary[mac_address] = 1

        if self._retrieveDictionary[mac_address] < FlaskBerryConfig().number_of_try_for_presentation():
            return UserSessionState.SHADOW_BAN

        if mac_address in self._banDictionary:
            self._banDictionary[mac_address] += 1
        else:
            self._banDictionary[mac_address] = 1

        if self._banDictionary[mac_address] < FlaskBerryConfig().number_for_permaban():
            delta = FlaskBerryConfig().delta_for_delay_try_presentation(self._retrieveDictionary[mac_address])
            if mac_address not in self._waitingForUnlockBanList:
                self._waitingForUnlockBanList[mac_address] = threading.Timer(
                    FlaskBerryConfig().delay_of_try_for_presentation() * delta * self._banDictionary[mac_address],
                    self._reset,
                    [mac_address]
                )
            else:
                self._waitingForUnlockBanList[mac_address].cancel()
                self._waitingForUnlockBanList[mac_address] = threading.Timer(
                    FlaskBerryConfig().delay_of_try_for_presentation() * delta * self._banDictionary[mac_address],
                    self._reset,
                    [mac_address]
                )

            self._waitingForUnlockBanList[mac_address].start()
            return UserSessionState.BAN
        else:
            return UserSessionState.PERMA_BAN

    def _reset(self, mac_address: str):
        del self._waitingForUnlockBanList[mac_address]
        self._retrieveDictionary[mac_address] = 0

    def check_is_shadow_ban(self, ip_address: str) -> bool:
        mac_address = mac_from_ip(ip_address)
        return mac_address in self._retrieveDictionary and self._retrieveDictionary[
            mac_address] < FlaskBerryConfig().number_of_try_for_presentation()

    def check_is_ban(self, ip_address: str) -> bool:
        mac_address = mac_from_ip(ip_address)
        return mac_address in self._banDictionary and self._banDictionary[
            mac_address] < FlaskBerryConfig().number_for_permaban()

    def check_is_perma_ban(self, ip_address: str) -> bool:
        mac_address = mac_from_ip(ip_address)
        return mac_address in self._banDictionary and self._banDictionary[
            mac_address] >= FlaskBerryConfig().number_for_permaban()

    def check_is_correct_presentation(self, ip_address: str):
        return mac_from_ip(ip_address) in self._presentedUser
