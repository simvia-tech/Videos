
This file is a written summary with extra details of the second part of the Open_Telemac river flooding tutorial. This second video details how to perform various data manipulation on the mesh (.slf file) and how to create and understand a boundary conditions file (.cli file).

# Creating a bottom friction variable in the mesh

## Loading the Corine Land Cover files

The Corine Land Cover (CLC) data are provided by various geographic institutes and describe the different types of land cover in a country. We use this file in Q4TS to determine an approximate value of the Strickler coefficient used in Open_Telemac for the law of bottom friction. A higher Strickler coefficient corresponds to a smoother bed and thus lower bottom friction, allowing water to propagate more easily.

In this second video we extracted the full 2018 Corine Land Cover data for France from the IGN (institut de géographie national) website. We then performed a cut of these data only in the vicinity of Yvette, the river of interest in this tutorial `0:45`. This reduced dataset can be downloaded in the folder provided with the first part of this tutorial. 

To load the CLC file, go in the "Add layer > add vector layer" section. Then, in source, on the left of the "vector dataset" browser, click on the ... button and select the .gpkg file. You can then press the add button. A new layer will be created and will contain the CLC data, but the layer will initially appear in a single color `1:00`. To display properly the colors, right-click on the CLC layer and select properties, then in the symbology section, click on the style button > load style at the bottom left of the window `1:10`. You can then click on the ... button next to "File" `1:14` and open either the .sld or .qml files (also provided in the folder of this github repository associated to the first part of the tutorial). You can finally press the "load style" button. The legend of the various land cover types will be loaded, press the "add" button to display properly the colors `1:23`.

## Using the Q4TS "projection CLC" module

Open the projection CLC module using the Q4TS button `1:51`. In the "CLC data file" section, click on the menu and select the CLC vector layer we just loaded `1:55`. Make sure you selected the last mesh you generated in "input mesh" and choose a name and folder where the output mesh (with the bottom friction coefficient) will be.

The newly generated mesh layer won't look any different than before. To check that the CLC data have been properly added in the new mesh layer, right click on it, go in properties, symbology and all the variables contained in the mesh should appear `2:28`. Click on the square next to the variable name to change the current variable displayed and press add `2:30`. Now in the browser under the layer the legend should now show the values of the Strickler coefficient. 

Some CLC data are not precise enough to properly capture smaller rivers like Yvette. We will now use the projection field module of Q4TS to impose a greater bottom friction coefficient (typical of riverbeds) in the vicinity of Yvette.

## Projecting a constant value of the bottom friction along the riverbed

Open the projection field module of Q4TS `2:50`. Make sure the variable name field is set to bottom friction, and add some quotes "", as there is a space in the name of the variable. The area layer field determines on which part of the input mesh the projection is going to be made. In our case we select the refinement layer `3:10` (in a more realistic study, another layer should be made, even thinner, to draw precisely the riverbed). In the field value, enter the value that the variable should take in the area layer. In the video we choose 25 for the bottom friction in the riverbed. Finally, select the correct CRS system (recall that we use the EPSG:2154 coordinate system for France) `3:18`. Finally, pick again the correct input mesh (the one we just generated with the CLC data), and select a place where to save the output mesh.

The newly generated mesh layer will again display the bottom variable. In property/symbology, if the bottom friction variable is selected you should now see a new color on the riverbed `3:53`.


# Changing a variable to a non-constant value

## The python code

In the example study of this tutorial, the bottom variable is not very accurate, the riverbed is not clearly defined. For the sake of the example, we are going to dig the area we draw as a refinement layer. In this case, assigning a constant value with the projection field module is not ideal, as the upstream part of the area is much greater than the downstream part. While it is possible to project the riverbed by part, we are rather going to use the python scripts provided in the Open_Telemac software.

The python code used in the video to modify the mesh bottom value can be found in this github folder. Two input data are required: the geometry file that is going to be modified (.slf) and a .csv file containing the x and y coordinates of the polygon on which we are going to modify the mesh elements. We can already put the lastly generated .slf file by Q4TS in the input `4:43`. 


## Extracting the polygon vertices on QGIS

To make the .csv file, let's open the toolbox of QGIS `5:12`. Then look in the vector geometry section for the "Extract vertices" function. Select in the layers browser the refine layer (or the polygon you want to extract the vertices), then double click on this extract vertices function and press run. A new layer made of the polygon vertices displayed as points should be created `5:35`. It can now be saved by right-clicking it, going in export and save as feature. Select a .csv format on the window that will open. In the geometry section, make sure to pick "as_XY". Make sure the CRS is the correct one, and save the layer somewhere using the "..." button next to "file name". In the field browser make sure to unpick any field called "X" or "Y" to avoid any naming problems. Then press ok. The .csv exported should list the X and Y coordinates in the first two columns (make sure the coordinates are consistent with the one on QGIS) `6:09`. You can then put this .csv file in the python script. The code also has a "bottom_shift" variable, set to -2 to dig the mesh of 2 meters on every element overlapping the considered polygon. Feel free to modify it, and to play with the code if you have to modify the other mesh data.

## Running the script

To run the python code, you need to use the python of the Telemac codes. If you're using our docker image, make sure you are inside the docker container to run it (use the open_telemac alias we provided in the github description of the first video). A plot of the modified mesh will appear, just to visualize the modifications. Back in QGIS, select the lastly generated mesh in the layer browser and click on the refresh button `7:11` to display the modification on the interface.

# Initializing the water level next to the boundaries

Open_Telemac crashes if a liquid boundary is or becomes dry. One way to initialize the liquid boundaries is to directly use the projection field Q4TS modules to add water where we want to define liquid boundaries.

## Drawing the areas

We need first to draw some new polygons where we are going to impose a non-zero water elevation. This can be done in QGIS in the Layer > Create layer > New Shapefile Layer menu. On the window that just opened, select in geometry type "polygon", name the file and pick the correct CRS `7:33 - 7:43`. Once the layer is created, select it in the browser, toggle on editing mode and click on the draw button `7:47`. You can then draw small areas next to the place where you're going to define a liquid boundary. Save the modifications.

## Adding water depth on the areas

Open again the Q4TS projection field module. In the variable name select "water depth" (with the "" as the variable contains a space). In area layer, pick the polygon layer you just defined. Make sure you choose the correct CRS. Then in field value, you can specify how much water you want to set in the area (in m). Here we impose 1m of water depth, just for the initialization. Make sure you have the latest input mesh selected, and save where the new output mesh is going to be. You can finally press run. In the newly generated mesh, a water depth variable should appear in properties > symbology.

# The boundaries conditions file

Open the create boundary Q4TS module. In input mesh, select the latest mesh you generated (in fact, all of the meshes in this video have the same node positions so it shouldn't make any difference which mesh you pick here). Click on the + button next to contour. Q4TS is going to create a new contour layer, made of green points corresponding to all of the nodes of the mesh belonging to the contour of the domain `9:33`. Q4TS displays green points to indicate solid boundaries (walls, with code 222, as this is the default value of the create boundary module). To add some liquid boundaries, click on the "+" button next to "boundaries". You can then click on the green points of the contour. Select two green points and right click. A window will open and ask to allow python macros to run, select yes. Then, another window will ask what type of boundary all of the points that are in between the two points you selected are  going to be. For the upstream of the river, you can pick a prescribed Q (flowrate). Similarly, impose a "prescribed H" (water elevation) liquid boundary on the downstream of the river `10:29`. Select where you want to save an output mesh (the .slf file generated at this stage is irrelevant and does not contain any physical field), and press the run button.

In the folder where you saved the output mesh you should find also a .cli file `10:50`. This is the boundary conditions. It is simply a text file. You can open it with your favorite text editor. The three first columns of each line is the code of the liquid boundary. We already said 222 is a wall. 5 4 4 is for a prescribed water elevations type of liquid boundary. 4 5 5 corresponds to a prescribed flowrate type of boundaries. Each line corresponds to a specific mesh node on the contour. The last number of the line is a numerotation of this node. You can find more information on the .cli file in the user manual of telemac2d (section 4.2.2): http://wiki.opentelemac.org/doku.php?id=documentation_9.0.0.

As the .slf does not contain any information, delete it, and look for the last .slf file you generated with Q4TS. You can rename it geo_yvette.slf for the next tutorial. 

# Summary of the files generated in this video

At the end of this video you should have a .slf file with:

- The bottom variable set to the domain topography
- The riverbed dug of 2m, this should be visible when displaying the bottom variable.
- A Strickler coefficient locally defined everywhere on the domain using the Corine Land Cover data.
- A higher Strickler coefficient assigned along the riverbed.
- A non zero water depth variable in the vicinity of the liquid boundary.

Additionally, you should have a .cli boundaries condition file defining two liquid boundaries (prescribed flowrate at the upstream and prescribed elevation at the downstream).
