from enum import Enum


# Three type of ban:
# Shadow ban only for user that do not complex error but use a REST without respect standard request (MAC)
# Ban for user that cannot communicate with FlaskBerry for a little delay of time
# Perma ban for user that are not allowed to communicate with FlaskBerry
class UserSessionState(Enum):
    OK = 0
    SHADOW_BAN = 1
    BAN = 2
    PERMA_BAN = 3
