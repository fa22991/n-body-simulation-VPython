# n-body-simulation-VPython
In this gravitational N-body simulation, I generate the initial positions and velocities of N stars such that they follow the Plummer Sphere model's mass and potential profiles. The total mass contained within a sphere of radius r is given by the formula: 

<img width="804" height="176" alt="Screenshot 2026-01-08 192947" src="https://github.com/user-attachments/assets/9bbbf116-e252-4a2c-887b-03d2d0c423aa" />

Considering the mass of the entire system/cluster to be 1, I generate a random number from 0-1 to represent the mass contained within some radius r. I then re-arrange the equation to solve for r, where Xi=M(r):

<img width="326" height="87" alt="Screenshot 2026-01-08 193753" src="https://github.com/user-attachments/assets/f06bb6fc-64c8-43d3-8ac8-22bb9ce06ea5" />

I then generate a uniformly random number in the range [-1,1] for cos θ (polar angle), and a number in the range [0, 2π] for ϕ (azimuthal angle, to calculate the actual coordinates of the star as shown below: 

<img width="300" height="256" alt="image" src="https://github.com/user-attachments/assets/eb3deac8-1e10-4615-87f6-a24a5558effe" />

I implement rejection sampling (Von Neumann) to assign initial velocities to the stars following a Plummer Model potential. To do this, I first calculate the escape velocity (minimum speed required to escape a gravitational field) using the formula:

<img width="237" height="83" alt="image" src="https://github.com/user-attachments/assets/8028166c-16fe-45b4-931a-cb637e27c92e" />

Here, a is the scale length (Plummer radius), that is set to 1. In order to implement rejection sampling, I need a probability density function (PDF) to base these rejections/acceptions on. Considering q the ratio between the stars' individual velocities and the escape velocity (q = V/Vesc), the PDF is given by the following equation, where q ∈ [0,1] and g(q) ∈ [0,0.1] :

<img width="522" height="104" alt="image" src="https://github.com/user-attachments/assets/6d9b87af-1df0-46ba-ad1e-4df3b1d6b918" />

I sample 2 uniformly random numbers x and y in the range [0,1]. For each pair, if 0.01*y < g(x), I accept q = x. This PDF is graphed below, where I reject samples like A and B, but accept P, Q and R as valid values of q. 

<img width="901" height="254" alt="image" src="https://github.com/user-attachments/assets/4ce50eee-3448-4a18-8dd8-c158df351a5e" />

Since velocities are isotropic (same magnitude in all directions) I use the same method outlined above for the positions to assign random directions to the velocities. 





