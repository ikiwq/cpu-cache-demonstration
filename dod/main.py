from utils import *

TEST_CASE_COUNT = 1_000_000

timer = Timer()

particles = [Particle() for i in range(TEST_CASE_COUNT)]
particles_x = [1 for j in range(TEST_CASE_COUNT)]
particles_velocity_x = [1 for k in range(TEST_CASE_COUNT)]

timer.start()
for particle in particles:
    particle.calculate_position(0.1)
timer.stop_and_print("OOP took %s seconds")

timer.start()
for i in range(0, TEST_CASE_COUNT):
    particles_x[i] += particles_velocity_x[i] * 0.1
timer.stop_and_print("DOD took %s seconds")
