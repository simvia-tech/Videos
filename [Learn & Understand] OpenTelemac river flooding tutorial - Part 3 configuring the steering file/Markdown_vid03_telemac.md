# Open_Telemac river flooding tutorial part 3: steering file

## Requirements

The geometry files (.slf) and the boundary conditions (.cli) file created in the previous video. They are available in this github folder. 

## Writing the steering file

### Syntax rules

The steering file is simply a text file, and can be written and modified with any text editor. It has the .cas format. You can create it from scratch or download the empty template in this github folder. It is conventional to start the name of this file for the telemac2d module by "t2d_....cas"

Telemac reads all of the lines in the steering file, from top to bottom. If the same keyword is declared several times, the latest declaration is considered. Any line starting with "/" is skipped by the reader. Creating sections like we did in the video is therefore fully optionnal and not understood by the reader, but strongly advised for readability. 

You can put as many space as you want in the steering file, they do not matter. The keywords can either be provided in english or french, but you cannot use both languages in a .cas file. It is very important to look in the reference documentation of the module you're using (here it's telemac2d) to have the full list, syntax and details of the keywords. You may find all of the telemac documentation here: http://wiki.opentelemac.org/doku.php?id=documentation_9.0.0 

### File section

In this section, we list all of the files that will be used during the simulation by Telemac2d.

- GEOMETRY FILE  = 'geo_yvette.slf' : this line provide to the Telemac2d module the mesh geometry data that are going to be used for the simulation.
- BOUNDARY CONDITIONS FILE = 'create_boundary.cli' : this line provide to the Telemac2d module the boundary condition file (.cli), listing which node are liquid or solid boundary, and providing the nature of the liquid boundaries (prescribed flowrate, elevations...).
-RESULTS FILE = 'r2d_yvette.slf' : the file containing all of the results of the simulation: physical fields for every mesh elements and at every time step. It's conventional to start the name of Telemac2d results files with "r2d_....slf"
-FORTRAN FILE = "none here" : we can provide either a folder containing several fortran scripts or just a fortran script. This keyword is useful to include in the code some user defined operations, like bottom smoothing (user_corfon). Check the documentation to learn more about Fortran scripting. This will be the topic of further videos.


### Time parameters and IO section

- TIMESTEP = 5   : the elementary time step (in seconds) of the simulation. It is crucial for numerical convergence and accurate physical description. Usually, the smaller the time step the better it is for convergence. But a too small time step will take more simulation time, and can even also lead to a convergence issues. Below we give a thumb rule on how to compute the time step.

> How to assess the time step of a telemac2d study:
> 
> 1) Estimate a characteristic length for the mesh elements. In the example of the video, near the riverbed, it was given by the value of phy_size in Q4TS in the refinement layer. So L~8m
> 2) Estimate a characteristic depth of the river. You can look for the maximum of the water depth if you already have it. In the case of yvette, we expect a water depth of H ~ 1m
> 3) Compute the average horizontal velocity of the flow. You can use the maximum of the velocity field if you already have a first simulation that converged, or simply estimate it. Here we assess the velocity to be lesser than 2 m/s in magnitude. U~ 2 m/s.
> 4) You can compute a first time scale: $\Delta t_{adv} = L/U \approx 4s$
> 5) There is another important time scale that must not be forgotten : Telemac solve the Saint-Venant equations. An averaged of the Navier-Stokes equations was performed on the vertical direction, but it has consequences on the model and must be considered. In the case of a Telemac2d simulation, for shallow water, this can be done by computing the celerity $c = \sqrt{g H}$. You can then gets a rough estimate of the time scale of information propagation due to gravity : $\Delta t_{wave} = L/c \approx 3s$. 
> 6) Take the minimal value; here the time step should therefore be 3s. You can then change a bit this value and see how this affect convergence. In the video we find that 5s gives good results while reducing simulation time, so we chose a value slightly bigger than 3s.

- DURATION = 20000 : the number of timesteps before the run ends.

- VARIABLES FOR GRAPHIC PRINTOUTS = 'U,V,B,W,F,Q' : the list of physical fields that will be saved in the results field. Each variable is associated to a letter. For instance, U and V are for the x and y components of the velocity field. Please refer to the reference manual to get the full list of the variable that can be saved.

-   GRAPHIC PRINTOUT PERIOD = 200: period in timesteps for saving the variables for graphic printout. At the end of the run the results file will contain DURATION/GRAPHIC PRINTOUT PERIOD time steps.

- LISTING FOR PRINTOUT PERIOD = 200: period in timesteps for displaying the logs in the terminal and in the log file.

### Initial and boundary conditions

In this section we parametrize the various boundaries of the .slf file. To that end, it's crucial to understand how the boundaries are numbered. This can be found directly in the .cli file: the 1st liquid boundary is the first line in the .cli file starting by another code than a solid boundary (2 2 2 for the first 3 columns). In the case of the video `7:22`, the first liquid boundary encountered at the top of the .cli file is a 5 4 4 (prescribed water elevation). At the bottom of the file we find the 4 5 5 (prescribed flowrate). Therefore, the first boundary is the downstream of the river (water elevation) and the second boundary is the flowrate (flowrate). In the case where there are multiple liquid boundaries of the same type, it may be harder to visualize what is the number of the liquid boundaries. In that case, you can either use QGIS to visualize the number of the nodes on the boundaries, or use some of the python script in the telemac system dedicated to displaying the boundaries number (the plot.py mesh2d function in /opt/open_telemac/scripts/python3). See `8:34` to find where this script is and how to use it.

- PRESCRIBED FLOWRATES = 0; 2 : the ; separates the liquid boundaries. As the first liquid boundary is a "water elevation type", it is not sensitive to the prescribed flowrates instruction. We write 0, but if there is a non-zero value it will be ignored if the boundary is not compatible with a flowrates. As for the second liquid boundary (upstream), we know it is a flowrate type, therefore the value is imposed there: we prescribe a constant flowrate of 2 $m^3.s^{-1}$ profile.

- PRESCRIBED WATER ELEVATIONS = 60.5; 0: This command behave exactly as the PRESCRIBED FLOWRATES command, but affects liquid boundaries of type "water elevation". The value of 60.5 at the downstream of the river is chosen after looking the value of the bottom at the neighborhood of the boundary on QGIS and adding 1m so there is about 1m of water depth on top of the bottom at this boundary.

- VELOCITY PROFILE = 4;4 : the general shape of the velocity profile at this boundary. 4 is for a square root type of profile, with a maximum of the velocity magnitude at the center of the liquid boundary. This is the classical scenario used in most river simulations. Please refer to the reference manual to understand the other options.

### Physical parameters

- LAW OF BOTTOM FRICTION = 3 : The expression used by the telemac system to compute the friction with the liquid using the coefficient of bottom friction. 3 corresponds to the Strickler law: https://en.wikipedia.org/wiki/Manning_formula

- FRICTION COEFFICIENT (= whatever): The value of the friction coefficient for used in the law of bottom friction. This value will be used if no bottom variable has been set locally in the .slf file. Here, we already imposed with the Corine Land Cover data a value of the bottom friction variable locally on the mesh. So the value set here is going to be ignored.


### Numerical parameters 

We won't give much details on the solver parameters in this section. Most of the keywords here should be modified with cautious and only with a good understanding of the underlying models and numerical scheme at play behind. We will give more details on this in further videos.

- SCHEME FOR ADVECTION OF VELOCITIES = what mathematical framework is used to compute the advection of velocities.
- SOLVER = What is the numerical model used for solving the equations.
- SOLVER ACCURACY = By default, 10^(-4) here is more than enough. 
- MASS-BALANCE = computation and log printout of the in and out -flow process in the mesh domain.


## Running the simulation

Once the steering file has been fully written; it can be launched using the telemac2d.py function and giving the value of the steering file. In the docker container, the telemac2d.py function can be found by typing the open_telemac alias to get inside the shell of the container and then moving to the folder where the steering file is and typing:
```
/opt/open_telemac/scripts/python3/telemac2d.py [steering file]
```

Check the logs that are going to appear in the terminal when running the simulation. In the video, there was a syntax error.

### A very classic error message; and the necessity of hotstarts

The second error encountered in the video is rather common and is worth detailing. If you encounter this message in the logs:
"PROBLEM ON BOUNDARY NUMBER: X, GIVE A VELOCITY PROFILE IN THE BOUNDARY CONDITIONS FILE OR CHECK THE WATER DEPTHS. OTHER POSSIBLE CAUSE: SUPERCRITICAL ENTRY WITH FREE DEPTH. IN THIS CASE GIVE A POSITIVE DEPTH IN THE INITIAL CONDITIONS OR PRESCRIBE THE DEPTH AT THE ENTRANCE."

This error message can occur when there is no water depth in the vicinity of the liquid boundary. Note this can also be caused by a poor time step choice. In the case of the video, this mistake is related to dry liquid boundaries: indeed, when providing the .slf file with the GEOMETRY FILE keyword, the water depth field we initialized next to the liquid boundaries in the second part of the tutorial is discarded. To take it into consideration, we are going to ask Telemac to use this .slf file as the reference file of a previous telemac computation. This is called a "hotstart". To do so, you'll have to add the following keywords:

- COMPUTATION CONTINUED  = YES
- PREVIOUS COMPUTATION   = 'name of the .slf file'

Here, by giving the name of the .slf file we already set in the geometry file, the water depth field is going to be properly read. Now if the simulation is run again, the error message won't show up as the liquid boundaries are indeed initialized with water.

> Note:  
> If at some point of the run the liquid boundaries end up with no water close to them, the simulation will crash in a similar way.