class EulerAngle():
    ###################################
    __angles : tuple

    def __set_rotation(self, delta : tuple):
        self.__angles = ( delta[0] % 360, delta[1] % 360, delta[2] % 360, )

    angles = property(lambda self: self.__angles, __set_rotation)
    ###################################


    ###################################
    def __init__(self, angles : tuple = (0, 0, 0)):
        self.__angles = angles

    def __add__(self, delta : tuple):
        self.add_angle(delta)

        return self
    
    def __str__(self):
        return "EulerAngle{}".format(str(self.__angles))
    ###################################

    
    def reset(self):
        self.__angles = (0, 0, 0)
    
    def add_angle(self, delta : tuple):
        self.__set_rotation (
            (
                (self.__angles[0] + delta[0]),
                (self.__angles[1] + delta[1]),
                (self.__angles[2] + delta[2]),
            )
        )



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





if __name__ == "__main__":
    obj = Object( rotation=(60, 30, 15) )
    print(str(obj.rotation) + "\n")

    obj.rotation += (0, 90, 0)
    print(str(obj.rotation) + "\n")

    obj.rotation += (0, 0, 90)
    print(str(obj.rotation) + "\n")

    obj.rotation += (270, -90, 0)
    print(str(obj.rotation) + "\n")