# Tutorial on Von Karman vortices Part 2 - Code_saturne study and post-process on paravis


## Preparation of a code_saturne study

### Set up a new study

You can create a new folder containing all of the files and arborescence required by code_saturne by typing the following command 

  ```code_saturne create -s [study_name] -C [case_name]```

In this tutorial we named the study "study_von_karman" and the case "Case1" `[0:35]`. This command creates the [study_name] folder, that will contains the 
[case_name] folder, the MESH folder and the POST folder. 
The POST folder is used for post-process operation not detailed in this video. In the MESH folder you must put all of the meshes used by the study. The [case_name]
folder contains 3 other folders. We'll detail the DATA and SRC folder in another video. The only important thing to note about DATA is that it contains the setup.xml
file used to prepare the code_saturne GUI. Finally the RESU folder will contain all of the results (successful or not) of the case study.

Setting up several case might be interesting when you want to perform several simulations in parallel on the same mesh. We will now launch the interface by typing `[1:02]` :

```code_saturne GUI [Study_name]/[Case_name]/DATAS/setup.xml ```

### Mesh tab and preprocessing

This will automatically open the code_saturne interface and select the folder you just created. In the interface, go in mesh tab and click on the plus button to open 
the MESH folder. Open the mesh you just moved here (Mesh_1) in the video `[1:27]`.

We are going to do a preprocessing only of the mesh. In execution mode below "List of meshes", change to "Mesh preprocessing only" `[1:34]`. 
Press on the run button (`[1:37]`) to run Code_Saturne only for a mesh preprocessing, naming the study preproc and clicking on "save case and run". 

This run should be very fast, about 5 seconds. Don't forget to put the "Execution mode" back to "standard computation", otherwise you won't be able to keep going. 
Preprocessing the mesh is useful for setting up the boundary zone. Instead of manually adding and naming them we can directly use the results of the preprocessing
run to load every mesh groups that were created in salome. To do this, open the boundary zones tab. Then click on the button on the right of "import groups and 
references from the preprocessor log" `[2:05]`. Go in the RESU folder and select the preprocessor.log file.

All of the groups that has been created before are now created automatically in Code_Saturne and named as BC_n. You can rename them with the name they had in 
salome `[2:27]`. Don't forget to save the study. 

### Calculation features & turbulence model

Now we're going to move into the calculation feature and keep everything that was set by default `[2:42]` (standard Eulerian single phase, incompressible). 
We don't add any thermal body and any body forces but in the turbulance model tab we're going to pick "K-Epsilon". 
We are not putting any gravity so we're going to unpick the gravity terms `[2:57]` and we don't need any wall function type so let's put no wall function `[3:07]`.
Finally, we're going to set the velocity scale to 5 m/s in the reference values. 
We don't transport any species so now we're going to move on. 

### Volume conditions

In volume conditions go to the all cells tab and set the density to 1 and the viscosity to 0.001 in order to have a high enough Reynolds number `[3:22]`. 


### Boundary conditions

In boundary condition we're going to define the nature of all of the groups we created in code_saturne. We already named our boundary zones in a rather self-explanatory 
way. So set the walls to of course wall, the inlet to Inlet, Outlet to outlet and symmetry to Symmetry `[3:37]`. 

In the Inlet tab we're going to set a velocity of 5 m/s (Norm). The hydraulic parameter is four times the surface of the inlet divided by the perimeter. 
In our case for the geometry we define it is going to be 0.17 approximatively `[4:01]`. We're not going to change the wall, we are letting it as a Smooth Wall. 
We don't have to change anything in the outlet and symmetry tabs. 

### Time settings

In time settings, we're going to put a reference time step of 0.025s. The stopping criterion is going to be set until physical time of 15 seconds `[4:24]`.
We don't have to change anything in start and restart.


We'll not modify anything in numerical parameter nor in equation parameters, so we move on directly to the post-processing tab. 

### post-processing

In the post-processing tab, add an output every 5 time steps `[4:42]`. This output should be understand as a log refreshing frequency: it will not save any datas, only the
feedback of the execution. These logs can be found in the RESU/run_solver.log. To visualize the results you need to go in the writer section of post-processing, on
the left of "Output controp", click on results, and below set in Frequency "output every 'n' time steps" `[5:00]`. In the video we set this to 5. 
This mean we'll visualize the datas every 5 time steps: since a time step is 0.025, we'll save the results every 0.125s. 
Finally, in the mesh pannel we're going to add all of the boundary zones we defined earlier in code_saturne `[5:12-5:27]`. Adding these here will allow to 
visualize the associated areas of the mesh when postprocessing. 

We are not going to change anything else.

### Executing code_saturne

Press on the run computation button `[5:36]`, and this time we are going to execute our case study. In the video we name it "exec" `[5:41]`. Press save case and 
run computation.  It's going to open a panel to show code_saturne is currently working. You can click on convergence tool to observe in real time the 
value of the residues `[5:48]`. You can set the number of subplots to one, and press refresh to see the value of the residue at the current iteration the code is. 
The residue are high in the beginning because the code is initializing the flow `[6:04]`. 

We then display the residue at the end of the simulation (this takes 5 minutes approximatively) `[6:16]`. 
The residues a bit high but we are simulating unsteady flow so it should not come as a surprise. 


## Post-processing on Paravis

### Open and display the datas

Let us now postprocess the results on paravis. Open salome, you can either create a new study and save it or open the one we did before in which we made the geometry
and the mesh. Once you're in salome, go into paravis `[6:30]` and in the pipeline browser right click and select open. Go into the folder of the study 
(here it's Von_Karman) and into the case that you created. Then go into the RESU folder and you should find here all of the run you made with code_saturne. 
Open the one that converged (in my case it's exec) and go into postprocessing. Here you will find all of the datas generated by code_saturne for each of the 
boundary zones defined earlier you can find a "results.case" then the name of the boundary zone. So you have the results Inlet results Symmetry and so on `[7:11]`... 
We are going to look in details to the fluid so let's just open the RESULTS_FLUID_DOMAIN.case and click on apply `[7:24]`.

In the video we are looking at the pressure of the mesh by default, so let's set it to the velocity `[7:29]`. You can change the time iterations using the buttons 
looking like a play button of a video `[7:34]`. When launching the animation we see the progressive formation of the Von_Karman vortices. 

### Filters

We are now going to apply some filter to better visualize the results. Click on the results in the pipeline browser and then you should see a filter tab `[8:04]`. 
Go into alphabetical and it will display all of the filters that are currently in paravis. From there you can select the "cell data to point data" filter `[8:17]`. 
This filter makes mapping from the mesh to a more smooth function allowing you to enhance the aspect of the velocity profile `[8:32]`. Now once you have done
this we're going to create a glyph filter. Go into filter, search, and then you can type glyph `[8:42]`. Select it. As a scale you will put no scale array 
and put a scale factor of 0.04 for example `[8:48]`. As an orientation select velocity. We have now generate arrows that are going to follow the velocity 
profile `[9:03]`. The color scale is wrong, it is displaying the colorscale of the pressure. Go into coloring and change it to Velocity `[9:10]`. 
We can make the arrows a little bit bigger let's say 0.08.  

You can see that even though we define only one cell element it's not exactly 2D since we have in reality two planes where the computation 
is performed `[9:28]` but for now we are going to set the view only on one side. Finally we are going to plot the velocity lines of the Flow by creating a new filter. 
Select the cell data to point data filter in the pipeline browser as it's going to be the input for this new filter and click on the stream tracer filter button. 
You can also look for the stream Tracer filter as we did before `[9:45]`. Then, the filter is going to ask you to create a line from 2 points that is going to be crossed 
by all of the stream lines of the flow. We are going to set point 1 to  (x=0.1, y=0.1, z=0.1) and point 2 to (x=1, y=0.41, z=0.1) so we are going to be in one of the two 
planes of the rectangle orthogonal to the Z axis `[10:20]`.

You should see all of the line of the Velocity flow but the color is once again not good so make sure you have set the colormap to the Velocity profile. 
The number of stream lines can be changed by tuning the resolution parameter `[10:37]`. Now if you display both the stream lines and the glyph you can have
a nice view of the flow and play the animation `[11:14]`. You should clearly see the Von Karman vortices forming here with an alternating curl.

