from datetime import datetime
from math import sin, cos, radians
import pygame

class Clock:
    def __init__(self, width=640, height=480):
        self._width = width
        self._height = height

    def run(self):
        self._startup()
        while self._running:
            self._input()
            self._update()
            self._draw()
        self._shutdown()

    def _startup(self):
        pygame.init()
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._font = pygame.font.SysFont(None, 30)
        self._clock = pygame.time.Clock()
        self._running = True

    def _shutdown(self):
        pass

    def _input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self._running = False

    def _update(self):
        self._clock.tick(60)
        self._now = datetime.now()

    def _draw_hand(self, color, center, width, increment, length):
        cx, cy = center
        box = pygame.Rect(0, 0, 0, 0)
        box.w = width
        box.h = width
        box.center = center

        right = radians(90)
        theta1 = 90 - (360 / length * increment)
        theta1 = radians(theta1)
        theta2 = 90 - (360 / length * (increment-1))
        theta2 = radians(theta2)
        pygame.draw.arc(self._screen, color, box, theta1, theta2, 1)

    def _draw(self):
        self._screen.fill((0, 0, 0))
        # line(surface, color, start_pos, end_pos, width)
        # ellipse(surface, color, rect)
        # arc(surface, color, rect, start_angle, stop_angle)
        center = pygame.Rect(200, 200, 200, 200)

        self._draw_hand(
                (150, 255, 100),
                (300, 300), 160,
                self._now.hour % 12, 12)

        self._draw_hand(
                (150, 100, 255),
                (300, 300), 180,
                self._now.minute, 60)

        self._draw_hand(
                (255, 100, 150),
                (300, 300), 200,
                self._now.second, 60)

        color = (255, 0, 0)
        datesurf = self._font.render(
                "{d.hour:02}:{d.minute:02}:{d.second:02}".format(d=self._now),
                False, color)
        datesurf_rect =  datesurf.get_rect()
        datesurf_rect.topleft = (50, 50)
        self._screen.blits([
            (datesurf, datesurf_rect),
            ])

        pygame.display.flip()

if __name__ == '__main__':
    clock = Clock()
    clock.run()
