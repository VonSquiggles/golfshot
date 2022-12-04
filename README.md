golfshot allows users to run a 2D simulation of a golf shot given the following parameters:
- launch_angle: angle between horizon and the golf ball path at impact (degrees)
- launch_velocity: golf ball velocity off the club face (meters per second)
- rotation_rate: golf ball back spin at impact (radians per second)


Assumptions:
- The air temperature is 15C or 59F
  - Thus, kinematic viscosity is 1.48*10**-5 m/s/s

- Also, air pressure is 1 atm (sea-level) and 0% humidity.
  - Thus, air density is 1.225 kg/(m^3)

- Drag and lift coefficient equations are from the publication "Aerodynamics of Golf Balls in Still Air"
  - Assumptions and error in coefficient equations can be found in the publication


1. Lyu, Kensrud, et al. Aerodynamics of Golf Balls in Still Air. 23 February 2018. 
https://www.researchgate.net/publication/323372659_Aerodynamics_of_Golf_Balls_in_Still_Air
    
