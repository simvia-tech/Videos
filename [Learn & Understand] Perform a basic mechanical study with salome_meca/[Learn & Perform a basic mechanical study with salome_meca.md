In this document, we explain in detail everything covered in the video, with additional tips and comments. We provide as many timestamps as possible, as some sections involve complex 3D geometry that will be easier to understand by following along in the video.

Note that the buttons for each module in Salome_Meca can be moved. You can find all of them in the tabs at the top (next to File, Edit, View [................]).

# Shaper module `[0:16s - 2:52s]`

This module is used to define the geometry of the structure as well as the geometric groups, which are necessary for defining mesh groups. These groups isolate parts of the structure where we will apply boundary conditions and loads.

You can find the documentation in the Help/User's Guide/Shaper module tab `[0:21s]`.

## Sketch and 3d tools
Please note that there may be some differences between the video and the 2024 release of Salome_Meca. Click the sketch button to enter sketch mode. You can move the sketch toolbar by holding the left-click button on the left side of the sketch button and dragging it to any position you like.

Next, select the active plane for your sketch by clicking on it `[0:29s]`. Use `ctrl + right-click` to rotate the view, and `ctrl + middle-click` to pan it. The sketch panel will show additional options for the active plane: “Set Plane View” will recenter the view, while the “Change Sketch Plane” option allows you to select a new active plane.

Once you've chosen an active plane, select the rectangle tool to draw a rectangle on it. Then, click on the length tool `[0:36s]`, and click on the sides of the rectangle to set and constrain the dimensions. Draw a 60x40 rectangle (in arbitrary units). Then, select the point tool and click on the top side of the rectangle to add a point. Use the midpoint tool to center the point by clicking on the newly created point and the top side of the rectangle `[0:44s]`. Zoom in using `ctrl + left-click`. Next, select the arc tool and draw a circle by clicking on the point you just created. Set the radius by clicking on one of the rectangle's edges. After clicking once more, you’ll have created the arc. Use the line tool to draw a vertical line from the top of the arc to the bottom of the rectangle. Draw two additional diagonal lines from the sides of the arc to the lateral sides of the rectangle (see `[1:06s]`).

Now, use the coincident tool to align the lines with the point created earlier by clicking on the lines and the point in sequence. Finally, link the bottoms of the two diagonal lines with another line. All of these tools add geometric constraints to the sketch. So, if you click and drag the bottom line, the rest of the structure will adjust according to the constraints. Use the angle tool to set the angle between two consecutive lines to 45 degrees (`[1:17s]`). Finish the sketch by clicking on the green "accept" symbol in the sketch tab.

Once the sketch is finished, you can switch to the 3D toolbar. Look for the extrusion tool in the toolbar, and then click on the sketch you just created in the Object Browser. The extrusion tool will extend the sketch in 3D along a plane orthogonal to the sketch plane. You can adjust the direction of the extrusion. Set the options to extrude 5 units on both the front and back sides.

Next, we’ll create a hole in the structure. Click the sketch tool again, select a face on the front of the structure, and set the plane view. Click the circle button and draw a circle from the central point of the structure (`[1:36s]`). You can constrain the circle's radius using the radius tool: set it to 10 and define the radius variable by entering "radius=10". Press OK to exit the sketch view, then go to the extrusion cut tool in the 3D toolbar. Select the second sketch we just created. In the ExtrusionCut options, you should see "all-in-Sketch_2" under the "select a sketch face" option. Then, click on the "Cut from:" option and select all the other faces (`[1:50s]`). In the Object Browser, you can hide the sketches so that only the ExtrusionCut is visible. Since we defined the radius of the hole as a parameter by writing "radius=10" (instead of just "10"), it will appear in the "Parameters" folder and can be modified.


## Geometric groups 

To complete the geometry, we’ll define some geometric groups, which we will later use to define mesh groups (for imposing mechanical constraints on specific parts of the mesh). Select the group option (`[2:14s]`). Let’s create a first group called “lateral_blocked_face.” Define it as a surface group. This is where we’ll apply fixed degrees of freedom. Select the lateral faces of the structure (use Shift+click to select multiple faces), and press the OK icon with a small + to move on to creating the next group. This time, create a surface group called “pinned_face,” where we’ll apply a mechanical load, and select the bottom faces of the structure (`[2:34s]`). Finally, create another surface group called “pressure_face” and select the top part inside the hole. You can also create a 1D group called “progressive_rays” and pick all the external radial lines (this is done at `[4:04s]` in the video, showing that you can always return to a previous part of the study at any point).

Don't forget to save your progress to avoid losing the geometry we've just created!

# Mesh module `[2:54s - 5:14s]`

In this section, we'll create a hexahedral mesh for the structure, and then define a submesh in the most stressed area, using a finer mesh for better precision in the mechanical study (since this is the region that will undergo the most deformation). Once again, you can find the documentation in the Help tab, then in User's Guide, Mesh module.

## Meshing algorithm

Click the "Create Mesh" button. A window will open. First, select the geometric element you want to mesh by clicking on the ExtrusionCut in the Object Browser (`[3:12s]`). If you're unsure what the geometry of an element in the browser represents, click the eye symbol next to it to display it. You should see "ExtrusionCut_1_1" appear in the Geometry option.

Next, choose "Hexaedron(i,j,k)" in the 3D algorithm options, and "Quadrangle: Mapping" in the 2D algorithm options. Under the 2D hypothesis options, click the wheel button on the right and select "Quadrangle Parameters." A new "Hypothesis Construction" window will appear. Choose the "Quadrangle Preference" option and click OK. Then, go to the 1D algorithm options and select "Wire Discretization." Adjust the 1D mesh parameters in the "Number of Segments" hypothesis (select this hypothesis even if you don’t change it). When you're done, click "Apply and Close." A mesh object should appear in the Object Browser. Right-click it and select "Compute." If everything is correct, the mesh will be displayed in the interface, and a window summarizing the mesh information will appear. Close the window and check if the mesh looks acceptable.


## Sub-meshes

If the general mesh looks good, we can move on to creating the submesh. Click the submesh button. In the Mesh option, make sure the general mesh (called Mesh_1, unless renamed) is selected. We’re now going to refine the mesh around specific geometric groups of the general structure. In the Geometry option, select the 1D "progressive_rays" group in the Object Browser tab (located in ShaperResults/ExtrusionCut_1_1/, cf `[4:11s]`). In the 1D algorithm options, select "Wire Discretization." In the "Number of Segments" hypothesis, choose "Scale Distribution" for the "Type of Distribution" option, and set the scale factor to 15. In the "Reversed Edges" options, select all of the top and left rays (all the rays of the geometric group will be displayed in the interface when you hide the mesh; you can then select the ones you want). All arrows should be pointing outward from the hole. Please refer to `[4:24s]` for more details. After clicking OK for the "Number of Segments_2" hypothesis, press "Apply and Close." You can make Mesh_1 visible again by right-clicking it and selecting "Clear and Compute."

Finally, note that the geometric faces are now defined as mesh faces. This was done during the general mesh creation. You can display them in a different color. You can also change the display color for each subgroup if you’re working with large meshes containing many groups (`[4:59s]`). Don’t forget to save the final mesh.

# AsterStudy wizard `[5:16s - 8:06s]`

In this section, we’ll use a wizard to automatically configure most of the study commands and add a few additional ones. Note that the path where you save the project (.hdf file) must not contain spaces (even in folder names), otherwise you won’t be able to run Code_Aster. When you launch AsterStudy, you may encounter a display issue (the interface may freeze on "Please wait while AsterStudy finishes loading"). You can resolve this by clicking the "X" or right-clicking on the interface. The documentation is available in the Help/User's Guide/AsterStudy module.

## The Isotropic linear elasticity wizard

Right-click on "CurrentCase" in the Data Settings tab. Select "Add Stage with Assistant" and "Isotropic Linear Elasticity." This will automatically set up a simple case study. A window will open. Click "Next." Ensure that "Mesh_1" (or the name of the general mesh you created) is displayed in the input mesh. Then click "Next." Select "3D Model." Modify the Young's modulus (E) to 200,000 and click "Next." In the "Imposed Degrees of Freedom on Group" section, click the "Add Group" button and select "lateral_blocked_face" and "pinned_face." We’ll fix the "lateral_blocked_face" along the x and y axes by setting Dx and Dy to 0, and fix the "pinned_face" vertically by setting Dz=0. Click "Next," and in the "Pressure on Mesh Groups" option, add the "pressure_face" and set the pressure to 100 (arbitrary units). Click "Next," then enter the name for the output result. The output result is typically saved with the .rmed extension. Click "Finish," and a set of commands will automatically be loaded. Double-click on the "LIRE_MAILLAGE" command to display the mesh in the interface (you can navigate in the 3D interface as before, but without pressing `ctrl`).

## Implementing timesteps

Now we’ll add (non-physical) time steps to progressively apply the pressure and observe the deformation. First, go to the "Functions and Lists" command menu and select "DEFI_FONCTION." In the NOM_PARA option, select INST (instant). In the VALE option (values), click "Edit." Add the following three values:

| INST | Function |
| ---- | ---------|
| 0    |   0      |
| 0.5  |   0.5    |
| 1    |   1      |

Then click OK twice. We have defined a linear $f(x)=x$ function for the variable "INSTANT," with three values.

Next, go to "DEFI_LIST_REEL," set the "DEBUT" (start) option to 0, select the INTERVALLE (steps) option, and click "Edit." Enter 1 under "Until" in the table, and set the Value to 2. Click OK twice. We’ve created a list of values from 0 to 1, consisting of three values: 0, 0.5, and 1.

Finally, double-click on the "MECA_STATIQUE" result command in the Data Settings tab, and click on the "LIST_INST" option (it should be set to the list of real values we just created). Go to the EXCIT option and edit the mechanical CHARGE (load): activate the FONC_MULT option (it should also be set to the list of real values we just created). Now, the pressure will be applied progressively, with a scale factor equal to the instant (since we defined it linearly with 3 points, and chose P=100, at 0 there is no pressure, at 0.5 P=50, and at 1 P=100).

## Adding post-processing

Now, we’ll add a post-processing operation to compute two additional fields: EPSI_ELGA (small deformation) and SIEQ_NOEU (constraints). In the Post-Processing menu, select CALC_CHAMP (compute field). Select DEFORMATION, add an item, and set it to EPSI_ELGA. Select CRITERES, add an item, and set it to SIEQ_NOEU. Click OK. These two fields will now be available for visualization when displaying the results.


# Processing & Post-Processing `[8:06s - 9:10s]`

## Running the study

On the left side of AsterStudy, you should see an "History View" tab. Click on it. Save the study. Select the CurrentCase in the Cases panel. It should show "Stage_1" in the CurrentCase panel, with buttons on the right. Click the "+" button to instruct Code_Aster to run this case and press "Run." The output panel will open, and "RunCase_1" will appear with an hourglass logo in the history panel. You can click the refresh button to display Code_Aster’s logs during the study's compilation. You can also enable an Auto Refresh button to update the logs automatically at regular intervals. After some time, the hourglass logo will be replaced by a green circle, indicating that Code_Aster has successfully completed the study.

## Visualizing the result

Once Code_Aster has finished processing the study, go to the Data Files Summary panel on the left side of the History View in AsterStudy. You should see the result file you defined earlier (usually with the .rmed extension) marked as "out" under Mode. Right-click it and select "Post-Process." In this new view, the computed fields will appear on the left. You should find EPSI_ELGA and SIEQ_NOEU fields, and you can click on them to display their results. At the top of the interface, you can play the time steps and observe the pressure being applied progressively. On the right, you can adjust the ScaleFactor to exaggerate the deformation for better visualization.
