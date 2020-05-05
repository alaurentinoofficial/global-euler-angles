from object import Object


if __name__ == "__main__":
    obj = Object( rotation=(60, 30, 15) )
    print(str(obj.rotation) + "\n")

    obj.rotation += (0, 90, 0)
    print(str(obj.rotation) + "\n")

    obj.rotation += (0, 0, 90)
    print(str(obj.rotation) + "\n")

    obj.rotation += (270, -90, 0)
    print(str(obj.rotation) + "\n")