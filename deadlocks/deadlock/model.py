class Satellite:
    def __init__(self, uid, path_length, front_sensor):
        self.uid = uid
        self.path_length = path_length
        self.front_sensor = front_sensor


class Intersection:
    def __init__(self, uid, mutex, locked_by):
        self.uid = uid
        self.mutex = mutex
        self.locked_by = locked_by


class Crossing:
    def __init__(self, position, intersection):
        self.position = position
        self.intersection = intersection
