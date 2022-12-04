from golfshot import GolfShot

sim = GolfShot(launch_velocity=75,launch_angle=10,rotation_rate=300)
state_history = sim.run_sim()

print(state_history)