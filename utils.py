from time import time
import random
import string

class Timer:
    def __init__(self):
        self.t1 = None
        self.t2 = None

    def start(self):
        self.t1 = time()

    def stop_and_print(self, string):
        self.t2 = time()
        elapsed = self.t2 - self.t1
        print(string % round(elapsed, 2))

        self.t1 = None
        self.t2 = None


class Particle:
    def __init__(self):
        self.position_x = 1
        self.velocity_x = 1.2

        self.unused_field1 = 0
        self.unused_field2 = 2
        self.unused_field3 = 4
        self.unused_field4 = 6
        self.unused_field5 = 8
        self.unused_field6 = 10
        self.unused_field7 = 12
        self.unused_field8 = 14
        self.unused_field9 = 16
        self.unused_field10 = 18
        self.unused_field11 = 20
        self.unused_field12 = 22
        self.unused_field13 = 24
        self.unused_field14 = 26
        self.unused_field15 = 28
        self.unused_field16 = 30
        self.unused_field17 = 32
        self.unused_field18 = 34
        self.unused_field19 = 36
        self.unused_field20 = 38
        self.unused_field21 = 40
        self.unused_field22 = 42
        self.unused_field23 = 44
        self.unused_field24 = 46
        self.unused_field25 = 48
        self.unused_field26 = 50
        self.unused_field27 = 52
        self.unused_field28 = 54
        self.unused_field29 = 56
        self.unused_field30 = 58
        self.unused_field31 = 60
        self.unused_field32 = 62
        self.unused_field33 = 64
        self.unused_field34 = 66
        self.unused_field35 = 68
        self.unused_field36 = 70
        self.unused_field37 = 72
        self.unused_field38 = 74
        self.unused_field39 = 76
        self.unused_field40 = 78
        self.unused_field41 = 80
        self.unused_field42 = 82
        self.unused_field43 = 84
        self.unused_field44 = 86
        self.unused_field45 = 88
        self.unused_field46 = 90
        self.unused_field47 = 92
        self.unused_field48 = 94
        self.unused_field49 = 96
        self.unused_field50 = 98

    def calculate_position(self, dt):
        self.position_x += self.velocity_x * dt


def generate_nxn_matrix(n : int):
    rows = []

    for i in range(0, n):
        rows.append([])
        for j in range(0, n):
            rows[i].append(j)

    return rows