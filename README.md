# one-sided-diffusor 
## Dependencies 
The instructions and tests are tailored to:
 - OpenFOAM v2406
 - Python 3.12
## Test case
To run a simulation case edit the case type and the new folder name in the Prerun script and execute. The script creates a folder in the run directory of the choosen case. go to the created folder and execute one of the following scripts. To only run the meshing execute the Meshrun scriprt. To run meshing, potentialFoam and simpleFoam execute the Steadyrun script. To run the transient simulation execute the Transrun. This script runs potentialFoam and simpleFoam beforehand as startvalues. To run the case with the active jet, run the Allrun script. This script also executes the steady case first and interpolates the solution with mapFields to the transient mesh with the jet as an inlet patch. It changes the boundary conditions of the jet from wall to inlet. Velocities for the jet can be changed in the Allrun script.

### 2D RANS simulation with the kOmega-SST turbulence model of the one sided diffusor
The main parameters of the simulation are:
- nu = 1.53e-5 m²/s
- rhoL = 1.225 kg/m³
- constant inlet velocity of 20 m/s 
- PreInlet block with a length 100 mm in flow direction and the slip Boundary condition
- Inlet block. Following the PreInlet block, with a length of 200 mm and the noSlip boundary condition
- The ramp has a length of 337 mm and is angled with 20°
- The jet is 20x0.5 mm and placed with a distance of 270 mm from the lower edge of the jet to the end of the ramp
- The inlet velocity of the jet is 20 m/s (and angled by 30° upwards) 
- The outlet is 5x the length of the ramp
- distance between the lower and upper wall of 400 mm 
- the case is currently tested with the jet as a wall simulate the recirculation bubble
  
## Current errors
 - The cases isn´t able to show the transient behavior of the recirculation bubble properly
## Still TODO 
 - running the mesh 3.1 transient for 0.3s 
 - testing the backward ddt scheme instead of Euler 
 - testing the Spalart Allmaras turbulence model