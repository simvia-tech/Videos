# Code_Saturne Atmospheric Module Tutorial
## Creating the Hexahedral Mesh from the CAD Model in Shaper
In this video, we expand the fluid domain geometry created in Part 1 of the tutorial. The final mesh must be sufficiently large compared to the house to capture the wind evolution throughout the domain.

### Expanding the Fluid Domain in Shaper
We begin by creating a larger rectangular domain with dimensions 315×315×63, and translating it so that the house is centered along the Y-axis and slightly shifted toward the inlet along the X-axis (DX = -78.5, DY = -153.5). Use the measurement tool to verify the alignment.

Next, we connect this larger rectangle to the original smaller fluid domain. In the Sketch module, project all vertices from the smaller domain onto the new geometry. Then use the extrusion feature to extend the smaller domain into the larger one (`1:28`). Repeat this process on the remaining sides.
Additionally, project the roof height onto the extended diagonal area using the same projection and extrusion techniques.
Finally, create a partition and use the Remove Sub-Shapes tool to exclude the house interior (refer to Part 1 for details on using this tool).

### Defining Code_Saturne Groups

For the CFD simulation, the following surface groups are required:

- Inlet: upstream face (before the house, along the X-axis)
- Outlet: downstream face (after the house, also along the X-axis)
- Bottom: all ground surfaces except the house footprint
- Structure: all faces of the house and roof
- Symmetry: lateral faces in the XZ planes
- Sky: all top faces of the domain

To define the Structure group, use the Shaper history. Double-click on the right of the relevant blue entry in the object browser (`4:13`) to move the construction pointer to the step where the house was first created or imported. Define the group at this point.

Then, return to the final model by double-clicking the last entry in the history. Right-click the Structure group in the object browser and select Move to the End. Shaper will preserve correct face associations even through partitions.

### Creating the Hexahedral Mesh
Switch to the Mesh module. Click Create Mesh (`5:05`) and ensure the selected geometry corresponds to the latest partition from Shaper (named partition_6_1 in the video).

- Set the 3D algorithm to Hexahedron (i,j,k).
- In the 2D tab, choose Quadrangle Mapping, and create a new hypothesis using Quadrangle Parameters.
- In the 1D tab, select Wire Discretisation, create a new hypothesis, and set the number of segments to 3.

This configuration tells Salome to:
- Generate 3D hexahedral (six-faced) elements
- Use 2D quadrangles where applicable
- Subdivide all 1D edges into three equal parts

Using just 3 segments initially helps validate the mesh generation. If some 2D regions appear triangular, they may require further refinement (e.g., additional partitions). Right-click Mesh_1 in the object browser and select Compute. In the video, the mesh is created successfully without triangular elements.

However, the Wire Discretisation algorithm may produce overly fine elements on very short edges—often unnecessary unless strong field gradients are expected (e.g., near the house). Because the current partitioning introduces small edges in low-gradient areas, the mesh becomes inefficient. Increasing the global segment count later would only exacerbate this.

To resolve this, we’ll define edge groups and apply local meshing strategies using submeshes.

    Note:
    Finer elements near the house are useful, as this is where the flow field exhibits significant variation.


### Creating Submeshes

Return to Shaper and select the final geometry (partition_6_1). Click Create Group (or right-click → Create Group) and name the group small_elements.
In the group creation panel, use Selection by Filters with the Edge Size filter, a < operator, and a value of 2. Use Show Only to preview the selection, then confirm.

Repeat this process to create:

- medium_small_elements: edges between 2 m and 5 m
- medium_elements: edges between 5 m and 10 m

Back in the Mesh module, right-click Mesh_1 and choose Create Submesh. For each 1D group, assign a Wire Discretisation algorithm with the following segment counts:

- small_elements → 1 segment
- medium_small_elements → 3 segments
- medium_elements → 5 segments

Then edit the global mesh settings:
Right-click Mesh_1 → Edit Mesh → 1D tab → set the global segment count to 60.
Finally, right-click again on Mesh_1 → Clear + Compute.

The resulting mesh should now feature elements with sizes adapted to the local geometry, balancing resolution and performance.

### Conclusion
In this video, we extended the fluid domain using sketches, extrusions, and partitions as introduced in Part 1. We then defined the surface groups required by Code_Saturne, which will be used in Part 3.

We demonstrated how to create a structured hexahedral mesh using the Wire Discretisation algorithm and highlighted the value of selective mesh refinement. Submeshes allow for local control over edge discretisation, overriding global settings to improve mesh quality and computational efficiency.

Note:
In cases where submeshes overlap on shared geometry, it may be necessary to define computation priorities to ensure correct mesh generation.

