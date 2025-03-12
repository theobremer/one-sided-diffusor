# one-sided-diffusor
## Dependencies 
The instructions and tests are tailored to:
 - OpenFOAM v2406
## Test case
The current test case is the 2D RANS simulation with the kOmega-SST turbulence model of the one sided diffusor with the jet inactive
## current errors
 - currently throws the 2D case a floating point excpection for U inlet BC bigger then 10m/s  
## Still TODO 
 - testing the 2D RANS case with the kOmega-SST turbulence model with the active jet
 - running the 3D RANS case with the kOmega-SST turbulence model with the inactive jet
 - running the 3D RANS case with the kOmega-SST turbulence model with the inactive jet
 - testing further turbulence models for 2D and 3D meshes 