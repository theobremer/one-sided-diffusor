# one-sided-diffusor
## Dependencies 
The instructions and tests are tailored to:
 - OpenFOAM v2406
## Test case
The current test case is the 2D RANS simulation with the kOmega-SST turbulence model of the one sided diffusor with the jet inactive. 
## current errors
 - no errors   
## Still TODO 
 - the values for k and omega were choosen by an approximation, but they are still not accurate enough. 
 - getting the 2D RANS case with the kOmega-SST turbulence model with the inactive jet to run properly
 - testing the 2D RANS case with the kOmega-SST turbulence model with the active jet
 - running the 3D RANS case with the kOmega-SST turbulence model with the inactive jet
 - running the 3D RANS case with the kOmega-SST turbulence model with the active jet
 - testing further turbulence models for 2D and 3D meshes 