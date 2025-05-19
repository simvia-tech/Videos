This file is a written summary with extra details of the first part of the Open_Telemac river flooding tutorial. The aim of this tutorial is to provide a tutorial video on how to prepare, run and analyze a hydraulic study using [Q4TS](https://plugins.qgis.org/plugins/q4ts/) and [Open_Telemac](https://www.opentelemac.com/). The focus of this first video is exclusively on Q4TS and QGIS.

# Loading a reference map (.xyz)

After clicking on the new study button on QGIS `0:21`, the first thing you're likely to need is a map that's going to be used as a reference. In this first video we're going to use [OpenStreetMap](https://www.openstreetmap.org/#map=6/46.45/2.21). It can be found in the browser in XYZ tiles `0:23`, as it is by default available in QGIS.

OpenStreetMap is an open source map of the world, and is loaded .xyz tiles. The CRS of these types of tiles should not be modified, as they contain explicit coordinates. These tiles are loaded and unloaded automatically using an internet connection, but can also be downloaded if necessary.

Note that there are other types of tiles: WMS and WFS. This will be covered in future videos. Sometimes it might be useful to use maps containing some specific types of information and these might be available as tiles in these types of formats.


# coordinates reference systems (CRS) `0:26 - 1:04`

Each item on QGIS is displayed using a CRS. These contains informations on what types of mapping should be done on the zoom level, map rotation, or coordinate placement in order to display properly all the data. It's important to have the data in the correct CRS otherwise even if they are displayed correctly on screen, the coordinates of one layer will not be correct relatively to another one. To avoid any potential issue, we're going to set the project CRS: this way, any layer created in this project is going to have the desired CRS.

## Set the project CRS

Click on the button on the bottom right of QGIS `0:27`. As we're going to study a 
French river in this tutorial, we will manipulate data in the French coordinates system. So, in the filter box, type 2154 and select the predefined CRS `0:34`:

    Lambert Conformal Conic - RGF93 v1 / Lambert-93 "EPSG:2154"

>Warning:  
>The .xyz files contains directly coordinates value. As such, the OpenStreetMap layer should be kept in its native CRS (which is EPSG:3857). Setting its layer CRS to EPSG:2154 will apply a visual transformation to it, but not to the coordinates values it contains. So if you draw a mesh covering Paris after changing the CRS of OpenStreetMap, the mesh will be at the wrong coordinates, even though you set the project CRS to 2154.

# Introduction of Q4TS and its docker image `1:04 - 1:58`


Q4TS is a plugin developed by EDF R&D. It allows to perform many operations on meshes: from creation, to interpolation and projection of field data, but also refinement and modifications of the mesh. The plugin needs a path to the salome software and to OpenTelemac to work properly. In the video we use a docker image of Open_Telemac, QGIS and Q4TS that has everything already set up and ready to be used. Feel free to pull the docker image from [this page](https://hub.docker.com/r/simvia/opentelemac). On the dockerhub page of the image you'll find the two aliases you'll need to run the open_telemac container in a terminal, and to open and use QGIS with Q4TS.

# The create mesh module `2:00 - 3:37`

To open the module, you can either click on the Q4TS button (`1:15`) directly, and open the interface in a separate window, or click on the sliding arrow on the right of the Q4TS button, select a module and display it in a pannel on the left of the interface.

The create mesh modules allows to draw or load 4 types of layers, and then execute the Salome software to display a mesh.

## How to draw, edit and create layers with Q4TS: example of the contour layer

The contour layer is the only mandatory layer to create a mesh, as it indicates the area that shall be meshed.

### Layout of Q4TS 

On the right of the contour layer section, 4 buttons can be seen. The "..." allows to load an already existing layer. The second button allows to zoom on the layer currently selected (does nothing if no layer is selected as a contour layer). The two arrows button is a way of refreshing the currently selected layer. In this video we use the green plus button, that allows to create and draw a new layer. Please note the green plus button might also appear on the left of the layer. This one allows to add (if possible) other layers of this type.

### Geopackages .gpkg & .q4ts folder

As soon as you try to create a new layer, Q4TS will ask to save a new .gpkg file `2:17`. A gpkg file always contain a group of different layers. Q4TS will hereafter save all of the created layer it uses in the .gpkg.

>Note:  
>The Q4TS will create a .q4ts hidden folder in your home folder (or wherever you mount the docker container through the alias in your machine). This folder is useful for storing the .gpkg and all temporary layers. You can then copy paste from this .q4ts folder the final layer you'll use for the Open_Telemac study.

### Drawing

Once a .gpkg file has been created, Q4TS will directly allow you to draw on a map the contour layer. You can start to draw directly, but just for clarity we also show how to toggle on and off the draw option. Click on the contour layer in the bottom left layers browser. Then click on the yellow pencil `2:42` to toggle on editing mode. Finally, click on the green "add polygon" button `2:44` to be able to draw new shapes in the current layer. Once you are done, don't forget to click on the save modifications button `3:10` and to toggle off editing mode.

>Note:  
>If you click on save modifications, it will store them in the .gpkg file Q4TS created. If you forgot, when you'll try to run any of the Q4TS you'll be asked to save in the .gpkg the layers before the run.

If you can draw on the map, the cursor should look like a circle with a + intersecting it `2:47`. In this mode, left click to create a new point. You cannot move points in draw mode, but if you make any mistakes, you can correct them afterward (cf below "editing mode"). For each points you add, you'll generate a close loop that will define the extents of the contour layer. If there are green squares on the the close loop, it simply means it's self intersecting there (can be corrected with editing mode). Once you are done drawing, right click. This will open up a small window asking for the layer name. You don't really need to name your fields here, so you can just press enter to be done with the creation process `3:00`.

### Editing

Click on the layer of interest on the bottom left of QGIS, then toggle on editing mode. The editing button is located to the left of the draw button (see `3:14`). In editing mode the cursor looks like a +. You can then left click on a point of the closed loop to move it (press left click again to place it where the cursor is). In addition, you can press on the red + that appears when the cursor is on a line between two points in order to create a new point at the center of that line, and place it wherever your cursor is (see `3:20`). Do not forget to save modifications and toggle off editing mode at the end.

## The other optionnal layers of the create mesh module

Each of the following layers is not necessary to create the mesh but are very useful to customize it. They can all be drawn and edited as the contour layer. It's possible to have several occurrences of these layers, so the green + button on the left allows to add more of them (but to create & draw use the + on the right of the layer).

### The island layer

Allows to draw a contour that is going to be excluded from the mesh. Useful to define obstacles, or areas not supposed to ever be wet. In the video for the sake of giving an example we define a small island layer `3:40 - 4:17`.

### The constraint lines layer

Allows to draw a line that's going to constrain the mesh to make nodes along this line. Not used in this video but very useful for dykes or roads.


### The refinement area layer

This layer define an area where the mesh is going to be finer or coarser than the global parameters specified in the create_mesh module. In the tutorial we draw the riverbed of the domain, as this is where the flow is going to occur and we want a finer mesh there. So, after a rather rough sketch of the riverbed (since we did not aim at being very precise and we want to avoid very long videos) `4:34-5:06` we right click to finish drawing and Q4TS will open a new window, asking for the type of mesh refinement. In the videos we closed this window and show how to reopen and modify it. To do this, right click on the refinement layer and select "open attribute layer" `5:30`, then toggle editing mode and modify the values. In this table the name is not relevant. min_size and max_size denotes the minimum and maximum size of a mesh element in the refinement layer. phy_size is the average size the elements in the refinement layer will try to tend to. Growth rate defines the sharpness of the transition from larger to smaller elements. In the video we set a min_size of 3 and a max_size and phy_size to be 8m. We leave the growth rate as 1.3.


## Creating the mesh 

Once all of the desired layers have been created, you may input the general mesh characteristics under the refinement layer section. Only the max and min mesh size are required. The growth rate defined here represents how fast we transition from the smaller to bigger mesh elements.

Once the parameters have been given, Q4TS requires to save the resulting .slf file somewhere. To do this, click on the "..." button next to the result .slf item `6:06`. We advise to save all mesh in the .q4ts folder and move only the last, final mesh for the open_telemac study.

You can finally click on the run button `06:24`. Depending on the mesh parameters this step can take more or less time. Once Q4TS is done generating the mesh it will automatically appear as a layer on the left, in a "creation" group `6:40`.

You'll see a more refined mesh in the refinement area. Note that you can show or hide layers in the Layers browser on the bottom left of QGIS. You can also drag and drop the layers: the ones on top of the list will be at the foreground. For instance in the video you can see the refinement layer is put on top of the mesh to be visible, and then is turned invisible `6:45 - 6:55`.


# Find, load, manipulate data and interpolate them to a mesh

## About the data

A very important part of a telemac study is the gathering of physical data for the study. The different types of informations required for a study can be divided as follow:

- The topographic (bathymetry) data: represented by the "bottom" variable of the .slf, these are fundamental to accurately describe the considered domain.
- The bottom friction data: typically represented using Manning’s or Strickler’s coefficient fields in Telemac. These are crucial for modeling flow resistance and are stored as variables in the .slf mesh file.
- Informations on the desired flow and model : these are very dependent of the physics to be simulated. In flooding models, this includes flowrates profiles, water depths at various points of the mesh... In coastal models (coupling with the TOMAWAC module), these can include waves heights or frequencies. It could also be the wind intensity...

These data can be downloaded by various providers that may depend on the country, such as the [nasa earthdata website](https://www.earthdata.nasa.gov/), or the [european Copernicus program](https://www.copernicus.eu/fr). If you can find a provider specialized in the country you wish to study the data are likely to be more precise. 

In this video in the case of France, the data displayed at `6:58-7:12` have been downloaded from the [IGN](https://www.ign.fr/) (institut de géographie nationale), a french specialized geography institute. From there, the topographic data have been downloaded from [this page](https://geoservices.ign.fr/bdalti), for the department of "Essonne", 91, where the Yvette river is located. These topographic data are from a project of a topographic mesh of France and are delivered in the .asc format, depicting a mesh (or point data) of the topography.

As for the Corine land cover data, they have been downloaded from [this page](https://www.data.gouv.fr/fr/datasets/corine-land-cover-edition-2018-france-metropolitaine/) for the full France domain in the .gpkg format. These data provide a list of what type of terrain (city, swampland, forests, lakes) can be found locally in France. They are essential for defining a bottom friction coefficient. As we only need the corine land cover data in the vicinity of the river we are simulating (the mesh domain), I used QGIS's extraction tool to save in a different file only the domain size we want for the Yvette study (and reduce the size of the data to download).

>Note   
>At `07:10` the data displayed are not the one used afterward in the videos, as they are CLC data in the .shp format but of 2012 and before, only for the "Île de France" region. We displayed them but eventually preferred to download the full France CLC data of 2018 as a .gpkg file and extract from these only the vicinity of Yvette. If you are interested in these data they can still be found [here](https://www.donnees.statistiques.developpement-durable.gouv.fr/donneesCLC/CLC/region/). For practicing we recommand to just use the recent 2018 data that we extracted only in the neighborhood of the domain.

## The interpolation point cloud module: assigning the bottom variable

### Loading and converting the topographic data

The interpolation point cloud Q4TS module requires a .xyz file format `7:33` to proceed. We're going to load the .asc topography data of the "Essonne" department, check which tiles contains our domain and convert them in the .xyz format.

The .asc format can be read using QGIS raster layers. Go in layer -> add a raster layer. On the raster dataet(s) field, click on the ... button and select all of the .asc data. Then press "add" `7:47-8:00`.
Now, we drag and drop the mesh in front of the tiles to make it visible, and pick and unpick the tiles one by one to see with which tiles the mesh is overlapping. In this video, the mesh domain overlap only with one tile, but if was overlapping with more, we could use the QGIS merge tool (can be found in Raster -> Miscellaneous -> Merge) before doing a conversion. Once we identifed which tile are overlapping, we can delete all of the other ones `08:00-08:20`.

Now we can perform the conversion. Go in Raster -> Conversion -> Translate (convert format)... `08:48`. Then, in input layer, select the layer you want to convert (the merged one if you had to deal with several tiles). In converted, click on the three dots button and select "Save to file" `08:58`. A menu is going to open to ask where you want to save the converted file. Give it a name, and in Files of type, select ".xyz" files `09:04`. You can then press the run button, and the conversion will happen, creating a .xyz layer. You can then remove the .asc layer.

Note that .xyz are simply points. After the conversion it is displayed as polygon so it might not look like it. We could go in properties and in symbology display the layer as points, but to really illustrate that they are mere points, we are going to reload the .xyz file as a text file. Go to the Layer tab -> Add layer -> Add Delimited Text Layer. Then, next to file name, click on the ... button and select the xyz tile. Pick in File format a space as a custom delimiter `09:50`. In record and fields option, unpick the "first record has field names" option. In geometry definition, select as X, Y and Z fields field_1, field_2 and field_3 `10:00`. Set the geometry CRS to ESPG:2154 (as this .xyz has been generated in this coordinates system), and press add. You can now see it loaded as points `10:15`.

### Running the interpolation point cloud module

Open the module either by clicking on the Q4TS button and selecting the interpolation point cloud tab, or by clicking on the arrow of the Q4TS button and opening it as a window on the left of the interface.

In the input mesh section, make sure to select the latest mesh you generated. In input point cloud, load the .xyz file we just converted `10:31`. Change the delimiter for a space, and save the output mesh somewhere (here we saved it in the .q4ts folder as this is not going to be the final mesh). Then press on the run button `10:52`.

A new layer will be created with the output mesh, in a "interpolation" group. The mesh will automatically displayed its "bottom" (topography) variable with a colormap `11:00`. You can drag and drop the initial mesh in the foreground to see the discretization again (`11:06`). The bottom variable is now added in the property/symbology section of the newly generated interpolated mesh.
