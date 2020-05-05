from euler_angles import EulerAngle

class Object:
    __position : tuple
    __rotation : EulerAngle

    def __set_rotation(self, rotation : EulerAngle):
        self.__rotation = rotation

    position = property(lambda self: self.__position)
    rotation = property(lambda self: self.__rotation, __set_rotation)

    def __init__(self, position : tuple = (0, 0, 0), rotation : tuple = (0, 0, 0)):
        self.__position = position
        self.__rotation = EulerAngle(rotation)
