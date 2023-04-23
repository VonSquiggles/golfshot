from golfshot import GolfShot
import pandas

def test_sim_out():
    sim = GolfShot(launch_velocity=75,launch_angle=10,rotation_rate=300)
    state_history = sim.run_sim()
    assert isinstance(state_history, pandas.core.frame.DataFrame)
    assert state_history.shape[1] == 3