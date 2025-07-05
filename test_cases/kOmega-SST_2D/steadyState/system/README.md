In this folder are two different types of geometry:
- The .m meshes are geometries with a sharpe Edge in between the lowerWall in the Inlet section and the diffusor ramp
- The .v meshes are meshes with a rounded edge in between the lowerWall in the Inlet section and the diffusor ramp

- The first number stands for the refinment level.
- The second number stands for the radius (just for .v meshes). Bigger numbers are smaller radiuses.

- blockMeshDict.t5 highly refined mesh with wall resulution calculated for turbulent boundary layer of flat plate for a lenght of 0.2m and yPlus of 1. The part above the boundary layer starts with the same cell size as the last cell of the boundary layer.  

- blockMeshDict.t4 highly refined mesh with wall resulution calculated for turbulent boundary layer of flat plate for a lenght of 0.2m and yPlus of 1. The part above the boundary layer starts with twice the cell size as the last cell of the boundary layer.  