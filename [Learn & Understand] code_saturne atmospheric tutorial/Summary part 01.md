# Code_saturne atmospheric module tutorial

## Creation of the CAO using shaper

### Importing the house

In this video we start by importing a house, in the .xao format, for pedagogical reason. Feel free to make your own house if you'd like. Otherwise, the house can be found in this github repository.

To import the house in code_saturne, start the shaper module, then click on file (top left), import, on CAD format. A import pannel should open. You can select there the format you want plan to import in Salome. Then click on the button with the "..." next to Import file, and select the .xao file (make sure to change the "file of type" in the menu if it does not appear, as we do at `0:35`).


### Creation and placement of the smaller air domain

From now on, we'll assume you either using our .xao file or have made a house with the same dimensions than us.
Start by creating a 15x15x63 rectangle (`0:49-1:00`). You can then use the translation button to center the house in the box (`1:14`). In our case we perform a translation of (DX=-3.5 ; DY = -3.5 ; DZ = 0.).
You can use the measurement tool (`1:32`) to make sure the house in correctly centered.


### Sketching on the domain

The hexahedral meshing algorithm requires to divide the geometry to mesh in such a way that every sub volumic elements has six faces. To do this, we will use the sketch module of shaper. Start by drag and dropping the sketch toolbar so it is fully displayed (see `1:51`). You may now click on the sketch button (`1:55`). You must then select a plane in which you are going to draw: it can either be a plane of an already existing object (here the fluid domain), or the (xy, yz, xz) planes. Select one of the side faces of the rectangle. It is then possible to click on the "set plane view" button in the sketch pannel (`2:01`) to center the camera on the sketch plane.

We'll now use the various operation available for sketching. These are all of the buttons in the sketch toolbar. 
- Let's start with the projection operation (`2:06-2:12`). This button toggle on projection mode: you can then click on any already existing vertices to project it in the sketching plane. We'll use this to project the walls and roofs of the house on the sketching plane.
- We then use the create line button to vertically slice this face of the rectangle (`2:13`). We create the lines by clicking on the bottom and top vertices of the rectangle. Once a line is created, it will be displayed in **red if there are still degrees of freedom (meaning it can be move in one way or another), or in green if it is completely fixed.**
- In order to fix the first created line, we use the distance operation (`2:20-2:27`) and set to zero the distance between the red line and the projected line of the roof of the house. To do this, click on the red line, then on the projected roof line, and a small window asking for the distance to impose will open (otherwise, use the distance window displayed in the sketch pannel). With this, the line is in red: its length is constrained by the edges of the rectangle, it is built perpendicular to the bottom and top vertices, and it is positioned along the projected roof line. Therefore the line appears in green.
- At `2:31` we create a second line that remain red even after constraining its distance. This is because we did not click properly on the top vertex of the rectangle, so the line has no constrained length and can be made longer or shorter on the top side (see `2:50`). To solve this issue, use the length operation (`3:03`), then click on the line and impose a length of 63 (the vertical dimension of the box). Everything will then appear in green.
- We'll use again the projection tool on the other side of the rectangle, but this time we'll select the line from the sketch we just made. This way we don't have to redo everything.
- Then just do the same thing on the other lateral sides of the rectangle (`3:22-3:32`).

### Generating plans and partitioning

Now that we have made sketches on all lateral sides of the rectangle that slice the faces vertically on the house walls and roofs (`3:40`), we'll create some planes along the z axis that will partition the rectangle. Click on the create plan button (`3:42`), then click on three points using the sides of the sketch lines we created to make plans as we did in the video (`3:45 - 4:07`). Then, use the partition button (`4:08`), and select the house, the translated rectangle, and all of the generated plans. This will generate one element composed of the intersection of all of these shapes (`4:15`). As we are interested in meshing the air domain outside of the house, we would now want to remove the inside of the house itself. The partition operation generate a list of all the partitioned volumic elements (see `4:30`). Look for the volumic element corresponding to inside the house by making them visible and invisible as we do at `4:33`. In the video the inside of the house is elements named "partition_1_1_5" and "partition_1_1_6". Once identified, use the remove subshape operation (`4:39`) and select these elements to generate one final element containing all of the partition except the one selected `4:45`. 

Additionnally, there is an obvious symmetry plane along the center of the roof, so we also create a vertical plane cutting the domain in half at `5:02-5:20` and make one final partition.

### Projecting the roofs with extrusion

The resulting partition (minus the inside the house) is made of 6 faces volumic sub elements, except at some places due to the roof sides. So, we'll have to divide a bit more the fluid domain. Let's use the sketch mode again to project the side of the roofs on the side of the domain (`5:27-5:37`).
We will then use an extrusion to create the volumic sub elements of the appropriate size and make one final partition. To know which value to impose for the extrusion, you can use the measurement tool (`5:37-5:46`). Once you know the right value, use the extrusion operation, select the face you draw in the sketch (that is the projection of the roof sides) and extrude it of the correct value (`5:50`). Do the same on the other sides. Then do a partition. The final result should look like what is displayed at `6:33`.

## Conclusion

We have used the sketch option of shaper to divide the global domain in such a way that every volumic sub element is made of six faces. This will turn out to be very useful for hexahedral meshing. In video 02 we'll make a bigger fluid domain and connect it to the small one we made, then create the mesh. Finally, in video 03 we'll setup the atmospheric CFD study using code_saturne.