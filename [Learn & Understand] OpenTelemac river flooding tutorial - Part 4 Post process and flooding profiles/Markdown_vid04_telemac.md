This markdown is a summary of the part 4 of the tutorial on river flooding using open_telemac.

In part 3 we showed how to configure a steering file and start a run. We start here after the run has converged. The logs displayed in the terminal should end with the message : "my work is done". If you now look in the folder where the study has been launched, the results file in the .slf format should be there.

# Visualizing the results on Salome

## Basic visualization and initializing the river stationary state

If you're still in the open_telemac docker container, use the `ctrl+D` command to exit it. Then, start the salome software (you can install it here if you don't have it already : https://www.salome-platform.org/?page_id=2433)

In the Paravis module, you should be able to directly open the .slf file. Right click in the pipeline browser (`1:20`) and select the results file. If you click on apply the domain is going to be displayed in 2D, in a single color. If you want to see where are the nodes of the mesh, you can change the surface representation to surface with edges `1:37`.

You can change the physical field that is being displayed by clicking on the solid color button and selecting the variable you want to visualize `1:46`. The time steps menu is usually located by default on the top right of the interface. You can move it by drag and clicking on the left of it `1:57`. You can then play the animation.

The water propagates on both boundaries. On the downstream of the river it propagates rather quickly as we abruptly impose a water elevation of 1m there while there is no water in the domain (it's like a sudden wall of water is entering the mesh). But we see it stops rather fast, as the elevation condition get fullfilled.
Meanwhile, on the upstream of the river with a prescribed flowrate, there is a constant flowrate of 2 m3/s imposed so water makes a slow progress. At the end of the duration of the simulation, the river is far from being fully in a stationary state. It is therefore necessary to perform a hotstart using the end of this run as the beginning of a new run. 

Before continuing to initialize the river flow, we add in the variables for graphic printout the free surface (S parameter) as it's going to be necessary for some post-process effect. We also change the prescribed flowrate imposed for the stationary state, as the 2m3/s is a bit too slow for river initialization. Note that this shouldn't be done in a real hydraulic study, since in this case it's important to have a river initialized with the realistic data. We do it here for a faster initialization. Finally, we increate the duration of the run to make sure the full river is going to be in a correct stationary state. We then run the simulation again.

> Note:    
> It's not necessary in the case of a rerun to change the name of the results file (although it is advice for clarity). If you keep the same name, the results file that has this name will just change its name to "[results_name]_old.slf".

At the end of the second run; we can now visualize again on paravis the result. At the last time step we can see almost all of the river is wet, we're close but not yet at the stationary state. Let's rerun once again with a hotstart. As we did not change the name of the results file, the lastly generated file has taken the name of the previous results file. So, as it's already open in Salome, you can simply actualize it to see the new results by right clicking on the file in the pipeline browser and selecting "Reload files". We'll see it worked in Salome as the first timestep of the run is going to be at the last time value of the previous run. At the end of this third run, the river should be fully initialized in a stationary state.

## Post-processing using filters on Salome

To create a nice view of the results, use the "warp by scalar" filter of Paravis. It can be found in the filter menu, using the search feature `6:20`. This filter modify the mesh along a given axis using a scalar value defined on the mesh. In our case, we're going to select the bottom and press apply. The mesh is now displayed with a bit of relief. You can exagerate this visualization by increasing the scale factor but remember only scale factor = 1 is an accurate representation. You can also modify the colormap of the mesh and set it to represent the bottom variable. If you want to modify the default "coolwarm" colormap set on paravis, select the button under the coloring menu with a small heart on it (cf `6:46`). From there, a bunch of preset colormap will be suggested. For the bottom variable, I usually pick a linear colormap if bottom is fully positive or negative like here. 

We will now use the free surface variable to display on this 3d mesh the water. Select again in the pipeline browser the results .slf file. Once you clicked it, go in filter and apply again a warp by scalar filter. This time, warp the mesh using the free surface variable. The free surface is defined as bottom + water depth. Therefore, set a scale factor slighly smaller than the one used for the bottom warp by scalar to avoid 3d overlap of the elements. In the video since we used a scale factor of 5 for the bottom warp by scalar filter, we pick a scale factor of 4.99999 for the free surface. This way, the bottom is properly displayed in 3d, and when the water depth is non zero, the second warp by scalar filter displays only the water depth in 3d.

This setup provides a nice way of visualizing the results in Salome.

## Imposing a flooding profile

Now that we have properly initialized the river, we're going to simulate a flooding event. In a real study, these data should of course be taken from historical flooding event first, to check that the model outputs the same results than the historical water level measurements. Then these data could be increased to simulate a critical rainfall event due to climate change. 
Here we'll just put random values to show how this can be done.

First, create a new .csv file where you're going to set the values of the flooding profile. In the video, we do it using vscode. 

The first line of the .csv should list all of the variables that are going to be varied. The first one should be the time. In the video we set the second variable to be the flowrate and the third one to be the water elevation. The order is not particularly important. When you set a profile for the boundaries, whether it's a flowrate, a water elevation or anything else, you should specify what is the boundary you want to modify by adding next to the variable name a (boundary number). We know from the third video the first boundary is the downstream of the river and is a prescribed water elevation while to second boundary is the upstream and is a prescribed flowrate. Therefore, we write in the first line of the .csv:
T   Q(2)   SL(1)

- T is for time
- Q(2) is for 'prescribing a flowrate Q on the second liquid boundary'
- SL(1) is for 'prescribing a water elevation on the first liquid boundary'.

As in the steering file, if you try to prescribe the wrong type of liquid boundary in this csv file (like a flowrate to a water elevation type of boundary), the values are going to be ignored.
The second line can be used for writing the units of these variables. So we simply write:
s   m3/s    m

Then, you can set the values of these variables.

The value given in the video are purely indicative and should be carefully thought in a real study. Note that the final time in the .csv should be inferior or equal to the duration of the run. 

Finally, to input this csv file to Telemac, you'll have to add the keyword:
- LIQUID BOUNDARIES FILE = 'name of the .csv created'

Don't forget to comment the prescribed flowrate and elevations commands, as now the liquid boundaries values are given by the .csv.

Finally, you can use the keyword
- INITIAL TIME SET TO ZERO

So that if you perform a hotstart the first time step will be at t=0s.

Once the code has converged, you can refresh the result file on Paraview and observe the area that are sensitive to floodings. Feel free to change the values of the flooding profile and observe the results !

Thank you for following this tutorial. Feel free to give us feedback or any questions/comments you might have ! You can either create an issue on github, a comment on the youtube video, or reach us on Linkedin or using or website simvia.tech.

