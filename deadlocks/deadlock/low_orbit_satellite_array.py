import time


def lock_intersections_in_distance(id, reserve_start, reserve_end, crossings):
    intersections_to_lock = []
    for crossing in crossings:
        if reserve_end >= crossing.position >= reserve_start and crossing.intersection.locked_by != id:
            intersections_to_lock.append(crossing.intersection)

    intersections_to_lock = sorted(intersections_to_lock, key=lambda it: it.uid)

    for intersection in intersections_to_lock:
        intersection.mutex.acquire()
        intersection.locked_by = id
        time.sleep(0.01)


def move_satellite(satellite, distance, crossings):
    while satellite.front_sensor < distance:
        satellite.front_sensor += 1
        for crossing in crossings:
            if satellite.front_sensor == crossing.position:
                lock_intersections_in_distance(satellite.uid, crossing.position,
                                               crossing.position + satellite.path_length, crossings)
            back = satellite.front_sensor - satellite.path_length
            if back == crossing.position:
                crossing.intersection.locked_by = -1
                crossing.intersection.mutex.release()
        time.sleep(0.01)
