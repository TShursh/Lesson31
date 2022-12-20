from prod.model.entity import *


class Manager:
    SHORT = (3, 0.5)
    NORM = (5, 1.0)
    SUPER = 2.0

    @staticmethod
    def calculate(transport, hour):
        if isinstance(transport, Transport) and hour > 0:
            if transport.spuare <= Manager.SHORT[0]:
                amound = Manager.SHORT[1]
            elif transport.spuare <= Manager.NORM[0]:
                amound = Manager.NORM[1]
            else:
                amound = Manager.SUPER[1]
            return amound * hour
        else:
            raise Exception()

