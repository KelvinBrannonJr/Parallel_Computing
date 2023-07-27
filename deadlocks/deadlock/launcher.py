from threading import Lock, Thread

from low_orbit_satellite_array import *
from draw_satellite import *
from model import *


path_length = 200


def main():
    win = GraphWin('Satellites in a box', 800, 800)
    win.setBackground('black')
    satellite_anim = SatelliteAnim(win, path_length)

    satellites = []
    intersections = []

    for i in range(4):
        satellites.append(Satellite(i, path_length, 0))

    for i in range(4):
        intersections.append(Intersection(i, Lock(), -1))

    t1 = Thread(target=move_satellite,
                args=(satellites[0], 780, [Crossing(320, intersections[0]), Crossing(460, intersections[1])]))

    t2 = Thread(target=move_satellite,
                args=(satellites[1], 780, [Crossing(320, intersections[1]), Crossing(460, intersections[2])]))

    t3 = Thread(target=move_satellite,
                args=(satellites[2], 780, [Crossing(320, intersections[2]), Crossing(460, intersections[3])]))

    t4 = Thread(target=move_satellite,
                args=(satellites[3], 780, [Crossing(320, intersections[3]), Crossing(460, intersections[0])]))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    while True:
        satellite_anim.update_satellites(satellites, intersections)
        time.sleep(0.01)


main()
