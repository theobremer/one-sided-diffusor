# one-sided-diffusor 
## Dependencies 
The instructions and tests are tailored to:
 - OpenFOAM v2406
## Test case
To run a simulation case, create a folder called run, create a copy of the simulation setup in the run folder, and execute the Allrun script. To only run the meshing execute the Meshrun scriprt. To run meshing, potentialFoam and simpleFoam execute the Steadyrun script. To only run the transient simulation execute the Transrun. In this case it is necessary that the Steadyrun was executed already. 

### 2D RANS simulation with the kOmega-SST turbulence model of the one sided diffusor
The main parameters of the simulation are:
- nu = 1.53e-5
- constant inlet velocity of 20 m/s 
- PreInlet block with a lenght 100 mm in flow direction and the slip Boundary condition
- Inlet block. Following the PreInlet block, with a lenght of 200 mm and the noSlip boundary Condition
- The ramp has a lenght of 337 mm and is angled with 20°
- The jet is 20x0.5 mm and placed with a distance of 270 mm from the lower edge of the jet to the end of the ramp
- The inlet velocity of the jet is 20 m/s (and angled by 30° upwards) 
- The outlet is 5x the lenght of the ramp
- distance between the lower and upper wall of 400 mm 
  
## current errors
 - sed command to change the boundary conditions of the jet to transient is copying uniform (0 0 0) insteady of uniform (20 0 0)
## Still TODO 
 - optimizing the mesh to achieve y+ <= 1 
 - running the tranisient 2D simulation with physically sensible results
 - including functional objects (sampling, wall shear stress etc.)
 - adding a 3D case of the one sided diffusor