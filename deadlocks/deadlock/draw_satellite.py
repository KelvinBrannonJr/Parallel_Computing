from graphics import *


class SatelliteAnim:
    def __init__(self, win, satellite_length):
        self.colours = [color_rgb(233, 33, 40), color_rgb(78, 151, 210),
                        color_rgb(251, 170, 26), color_rgb(11, 132, 54)]

        self.satellite_length = satellite_length

        path0 = Line(Point(10, 330), Point(790, 330))
        path1 = Line(Point(10, 470), Point(790, 470))
        path2 = Line(Point(330, 10), Point(330, 790))
        path3 = Line(Point(470, 10), Point(470, 790))
        self.draw_path(win, path0)
        self.draw_path(win, path1)
        self.draw_path(win, path2)
        self.draw_path(win, path3)
        self.satellite0 = Line(Point(10, 330), Point(10 - satellite_length, 330))
        self.satellite1 = Line(Point(470, 10), Point(470, 10 - satellite_length))
        self.satellite2 = Line(Point(790, 470), Point(790 + satellite_length, 470))
        self.satellite3 = Line(Point(330, 790), Point(330, 790 + satellite_length))
        self.draw_satellite(win, self.satellite0, self.colours[0])
        self.draw_satellite(win, self.satellite1, self.colours[1])
        self.draw_satellite(win, self.satellite2, self.colours[2])
        self.draw_satellite(win, self.satellite3, self.colours[3])
        self.boxes = [Rectangle(Point(350, 350), Point(360, 360)),
                      Rectangle(Point(450, 350), Point(440, 360)),
                      Rectangle(Point(450, 450), Point(440, 440)),
                      Rectangle(Point(350, 450), Point(360, 440))]
        for box in self.boxes:
            self.draw_crossing(win, box)

    def update_satellites(self, satellites, intersections):
        current_x = self.satellite0.getP2().getX() - 10 + self.satellite_length
        self.satellite0.move(satellites[0].front_sensor - current_x, 0)

        current_x = 790 - self.satellite2.getP2().getX() + self.satellite_length
        self.satellite2.move(current_x - satellites[2].front_sensor, 0)

        current_y = self.satellite1.getP2().getY() - 10 + self.satellite_length
        self.satellite1.move(0, satellites[1].front_sensor - current_y)

        current_y = 790 - self.satellite3.getP2().getY() + self.satellite_length
        self.satellite3.move(0, current_y - satellites[3].front_sensor)

        for i in range(4):
            if intersections[i].locked_by < 0:
                self.boxes[i].setFill(color_rgb(185, 185, 185))
            else:
                self.boxes[i].setFill(self.colours[intersections[i].locked_by])

    def draw_crossing(self, win, box):
        box.setFill(color_rgb(185, 185, 185))
        box.draw(win)

    def draw_path(self, win, line):
        line.setFill(color_rgb(185, 185, 185))
        line.setWidth(4)
        line.draw(win)

    def draw_satellite(self, win, line, colour):
        line.setFill(colour)
        line.setWidth(14)
        line.draw(win)