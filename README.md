# Double-Pendulum

Double Pendulum implemented with Python and Tkinter

# Required Modules

The following are used:

- `numpy`
- `odeint`
- `tkinter`
- `time`

# Instructions

Just run the script and the animation will start.
Almost every line is commented on. You can change masses, lengths of the rods, initial conditions etc. in the script.

# Issues

As of the first release of the script, there are a few problems. I initially tried to create the time array to be incremented 0.1 seconds going up to any amount of time.
I set the .after() function argument to 0.1 seconds as well to achieve a smooth animation. Animation turned out to be too slow for some reason.
I then had to decrease .after() function argument to 0.01 seconds which seemed much more smoother. 
Now i don't know if the animation is actually accurate to real life in terms of timing and movement of the masses. I hope to solve this in the future.
