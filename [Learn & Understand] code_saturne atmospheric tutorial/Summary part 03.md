# Code_Saturne Atmospheric Module Tutorial
## Setting Up Code_Saturne and Post-Processing Results
### Initialization
In a Linux terminal (either on WSL or a native Linux system), start by typing:


    code_saturne create -s [study_name] -c [case_name]

Here, code_saturne is an alias defined in the .bashrc file to run the Docker image provided by Simvia. If you haven't installed it yet, refer to our Tips & Tricks video on installing Code_Saturne via Docker. 

Alias used in the video:

    alias code_saturne='docker run --rm --mount type=bind,source=$(pwd),target=/home/code_saturne -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY code_saturne:8.3.0'

Docker image: [simvia/code_saturne on Docker Hub](https://hub.docker.com/r/simvia/code_saturne)

If you're using your own code_saturne installation you can also do it using the command [path_to_code_saturne]/code_saturne/bin/code_saturne create.


This command creates a folder named [study_name], containing:

- a MESH folder (for mesh files),
- a [case_name] subfolder representing a CFD case,
- a POST folder for post-processing.


The [case_name] folder includes:

- SRC: for user-defined C functions or source terms,
- DATA: where setup.xml defines the simulation parameters,
- RESU: which will contain logs and result files.


Copy the mesh you exported from Salome (see the first two videos) into the MESH folder. To export from Salome, right-click the mesh in the Mesh module, select Export, and save it in .med format.

You’re now ready to configure the simulation. Launch the GUI with:

    code_saturne gui [study_name]/[case_name]/DATA/setup.xml

This opens the Code_Saturne GUI for the specified case. Under the Calculation Environment tab, the directories you just created should be automatically detected (`0:56`).

### Setting Up the Model
#### Mesh

Click the + button in the mesh section. This will open the MESH folder and display available files. Select the imported mesh.

In the Execution Mode section, switch to Mesh Preprocessing Only, then click Run (`1:13`). Name the output folder, save, and run the preprocessing. This step generates a mesh summary file: preprocessor.log.

Then, switch the Execution Mode back to Standard Computation.

#### Boundary Zones
In this step, you define all the surface groups created in Part 2 of the tutorial. You can either add them manually (matching the names defined in Salome), or automatically load them from the preprocessing step:

Click Import groups and references from preprocessor log. 
Navigate to the RESU directory, open the preprocessing output folder, and select preprocessor.log. The groups will be imported automatically. By default, they'll be named BC_X.

We strongly recommend renaming these groups with meaningful names (`1:39`).

#### Calculation Features
In the Flow Model section, choose Atmospheric Flow with Constant Density. This activates the atmospheric module.

#### Atmospheric Flow
This section configures atmospheric parameters. You can import a real meteorological dataset or use an idealized profile.
For this tutorial, select Idealized Large-Scale Meteorological Data and enter the following:

- Longitude, Latitude, Domain Orientation, Start Time:
used to approximate the position and evolution of the sun and moon cycles.
- Roughness height $z_0$ ​and Reference height $z_{ref}$ :
These define the wind profile:
$U(z) \propto ln(\frac{z-z_{ref}}{z_0})$
The values in the video are based on Eurocode Category 2 for urban terrain.
- Wind Speed and Direction:
Set to 27 m/s and 270°, matching our mesh with wind along the X-axis.
- Other options (e.g., humidity, friction) are left at default values, but feel free to explore how they impact the simulation.


#### Body Force

Define gravity: $g=9.81 m.s^{-2}$, applied in the –Z direction.

#### Turbulence Model
We use the standard linearized k−ϵ model. Keep in mind that atmospheric flows can be highly variable, and different models may be better suited depending on the context.

#### Volume Conditions (All Cells)

Select Material: Air.
Define dynamic viscosity as $1,8.10^{-5} Pa.s$.


#### Boundary Conditions

Assign boundary types to the imported surface groups:

- Bottom, Structure → Wall
- Inlet → Inlet
- Outlet → Outlet
- Sky, Symmetry → Symmetry

Each of these will now appear in the GUI for further configuration:

Bottom: smooth wall.
- Inlet: in Atmospheric Flows, enable:
Meteorological profile from data
Automatic inlet/outlet nature from data
Disable Mapped inlet
- Outlet: same as inlet.
- Sky/Symmetry: no direct GUI settings — advanced settings can be added manually.
- Structure: also apply a smooth wall (roughness studies could be done here).

#### Time Settings

Set a time step of 0.1 s. You can assess the time step using the length of the elements and the average wind velocity. Then take a smaller time step to ensure good convergence.

Stopping Criterion: 200 time steps → 20 seconds total simulation time.

#### Numerical Parameters
Set the pressure solver tolerance to $10^{-5}$.
We have done this because this gave faster convergence without significant impact on results (we checked). However, it's better to not modify the default values if you don't have any informations.

#### Postprocessing Settings

Log Frequency: every 10 time steps → written to run_solver.log


- In the Writer tab → Results section: Set output frequency to every 10 time steps. Include $t=0$ and $t=t_f$ → total of 21 saved steps

- In the Mesh sub-tab, you can add additional boundary zones. These will generate result files limited to the selected surfaces — useful for isolating stress fields on the building or ground.

- In the Monitoring section: Add a probe at (X=50, Y=0, Z=0). Select CSV output format — values at each time step will be written to a separate file.

#### Surface Solution Control

Select fields to output on boundaries:
- Stress
- Tangential Stress
- Normal Stress

#### Running the Simulation

Once all settings are configured, click Run. As for preprocessing, you’ll be prompted to name the output folder. You can configure the number of processes and threads (for parallel execution), but ensure this matches your machine’s capabilities. During the run, use the Convergence Tool to visualize residual evolution — this helps assess simulation stability.

### Visualizing Results in Paravis

#### Loading and Displaying

Launch Salome and switch to the Paravis module.

In the Pipeline Browser, right-click → Open (`6:08`).
Navigate to study/case/RESU/[run_folder]/postprocessing and open: result_Fluid_domain. (Optional) add boundary meshes like bottom or structure, if defined.

Display the fluid domain with Outline or Transparency.
To show stress fields on surfaces, make sure you're not at the first time step (wind has not yet propagated). Rescale color maps as needed.

#### Useful Filters

- Cell Data to Point Data: smooths color discontinuities via interpolation
- Stream Tracer: visualizes streamlines intersecting a user-defined line.
Set vertical/horizontal lines across the house to observe flow profiles.
Adjust resolution for density of streamlines. Streamlines can be color-mapped to a scalar field
- Glyphs (`8:20`): draw colored, oriented arrows representing vector fields (e.g., velocity)

#### Physical Interpretation

Max stress occurs on the wind-facing wall — consistent with expectations.
Wake region behind the house shows eddies and lower pressure. Pressure peak occurs at the windward wall; drop behind — typical aerodynamic behavior. 

Velocity peak observed at the roof crest, due to acceleration over slope. Velocity drop in the wake indicates effective wind blocking by the structure

These patterns are consistent with fluid dynamics theory. While no experimental data is included in this tutorial, the results appear physically sound and internally consistent. If a real study was to be performed, it would be interesting to compare the order of magnitudes with the simulation. 