# n-body-simulation-VPython
In this gravitational N-body simulation, I generate the initial positions and velocities of N stars such that they follow the Plummer Sphere model's mass and potential profiles. The total mass contained within a sphere of radius r is given by the formula: 

<img width="804" height="176" alt="Screenshot 2026-01-08 192947" src="https://github.com/user-attachments/assets/9bbbf116-e252-4a2c-887b-03d2d0c423aa" />

Considering the mass of the entire system/cluster to be 1, I generate a random number from 0-1 to represent the mass contained within some radius r. I then re-arrange the equation to solve for r, where Xi=M(r):

<img width="326" height="87" alt="Screenshot 2026-01-08 193753" src="https://github.com/user-attachments/assets/f06bb6fc-64c8-43d3-8ac8-22bb9ce06ea5" />

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>v</mi><mrow><mi>e</mi><mi>s</mi><mi>c</mi></mrow></msub><mo>=</mo><msqrt><mfrac><mrow><mn>2</mn><mi>G</mi><mi>M</mi></mrow><msqrt><mrow><msup><mi>r</mi><mn>2</mn></msup><mo>+</mo><msup><mi>a</mi><mn>2</mn></msup></mrow></msqrt></mfrac></msqrt></mrow><annotation encoding="text/plain">v sub e s c end-sub equals the square root of the fraction with numerator 2 cap G cap M and denominator the square root of r squared plus a squared end-root end-fraction end-root</annotation></semantics></math>



