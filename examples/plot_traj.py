import plotly.express as px
from golfshot import GolfShot

# coefficients for converting units of intial states
rpm_to_rad_per_s = 1/9.549297 # rotations per minute to radians per second coeff
miles_ph_to_mps = 1/2.23694 # miles per hour to meters per second coeff

launch_vel_mph = 135 # Typical for an amateur golfer (miles per hour)
launch_vel_mps = launch_vel_mph*miles_ph_to_mps # convert to meters per second

launch_angle_deg = 14 # Varies greatly for amateurs (degrees)

rotation_rate_rpm = 2700 # Typical for an amateur golfer (rotations per minute)
rotation_rate_rps = rotation_rate_rpm*rpm_to_rad_per_s # convert to radians per second

sim = GolfShot(launch_velocity=launch_vel_mps,
                launch_angle=launch_angle_deg,
                rotation_rate=rotation_rate_rps)
vals = sim.run_sim()

# df = pd.DataFrame(dict(x=vals[0], y=vals[1])) # create data fram for plotting
fig = px.line(  vals, x="x", y="y",
                labels={"x": "Distance (meters)", "y": "Height (meters)",},
                title=f'Golf Shot; launch velocity: {launch_vel_mph} (miles per hour)') # plot
fig.show() # show figure in default browser
