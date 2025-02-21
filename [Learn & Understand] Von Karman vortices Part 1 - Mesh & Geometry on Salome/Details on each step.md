# Tutorial on Von Karman vortices - Part 1 : mesh and geometry on Salome

## Introduction

This video is a direct follow-up to the previous one on how to install code_saturne with docker.
If you haven't watched it already a link is there [link](link).

We are now going to use this docker installation of code_saturne to showcase a basic Von Karman
Vortex study. We'll first use a docker image of salome to create the geometry and the mesh then
move in the code_saturne docker and run the study. Finally I'll show you how to
postprocess the results on par properly so first let's open salome with the docker container.

## Creating a geometry with GEOM

### Simple plate

For this video we're going to go into the geometry module. We'll start by creating a rectangle as
we are going to do a 2d study. This rectangle will be a plate so we don't really care about the
dimension along Z let's put it to 0.1. The other two dimensions are going to be 2.2 and 0.41.
Let's apply and close.

### Small tips on Salome

Now we don't really see the box so let's zoom a little bit. I remind you that if you want to zoom
you can press control and left click and if you want to rotate you can press control and right
click control and middle click will allow you to span in the 2D plane the picture.

### Hole

Now we are going to generate a cylinder that will act as our main obstacle. As a radius we'll put 0.05.
We don't care about the height as it's going to be 2d at the end of the (set it to 1). Let's now translate this
rectangle like that to put it in the middle of the plate. Apply. Now we're going to perform a cut with
the following button. We'll select as the main object the box that is going to be the flow and as a tool
object the translated cylinder. Let's apply and close. Now you see the cylinder disappeared and we have a hole
where the cylinder was before.

## Creating the geometry groups with GEOM

### Partition

Now in order to make things easier for the meshing algorithm we're going to intersect this flow with some planes.
Let us start by creating two points the first point is going to be at the following coordinates which corresponds
roughly to the center of the obstacle. You can see it here. The second point
is going to be at the following coordinates and you should see it here.

Now let's create the planes. Use this tool to generate planes. As a first plane you're going to select
the point in the middle of the obstacle (vertex_1) and this vector along y. It will create you the first plane.
We don't need it to be so big so put it to for instance to six but check that it's getting your whole geometry.
Now you can press apply and we're going to generate other planes. The second
planes is also going to go through the first point but this time it's going to be orthogonal to this vector. We don't need
it to be so big again so you can put like 3, should be enough. Apply. Now the third plane is going to go through vertex_2
and be orthogonal to this Vector. Apply. Now we're going to generate planes with three points. Let's move a little bit the
view on this side. As the first point we're going to select the first vertex again but now as a second and third points we
are selecting these two. We don't need this plane to be so big let's put it to six. Apply. And finally let's do the same on
the other diagonal of the rectangle there. So the first point is going to be vertex one and the two other points are going
to be this one and this one. Apply and close. So it looks messy but at the end of the day what you should observe if you're
looking the thing from a top view by clicking on this button is that the plane should cut the mesh in this way. We are doing
all of these planes in order to create a partition of the flow. Go to the partition tool and select as the object the cut
and as a tool object select all of the planes we just created. Apply and close. Now you can see that the geometry for
the flow has the obstacle but also some planes lines. They are going to be useful for the meshing algorithm later but
before moving to the meshing algorithm we're going to create some geometric groups go in the menu. Rename the partition
as flow as this is going to be the geometry of the flow.

### Groups

Now you can right click and select "create group". We are going
to create several groups. Let's start with the inlet: this is where the water is going to come inside the mesh.
Apply. Similarly we are going to create an outlet: this is where the water is going to leave the mesh after it flowed.
We're selecting these two faces, let's add them and apply. Now we're going to create some symmetry groups: as the geometry
is 2D we don't really care about these two faces so we're going to define them in Code_Saturne as symmetries. To select
several faces this way you should press shift plus left click. Now go on the other side and pick all of the faces here
too. Once you're done select add, you should get at the end 20 faces. If you did any mistakes like I did here and you
want to add faces to (an already created) group you can click on the group and right click it. Go in edit group and
then you can add the faces that you forgot to put. Like this ! Finally, we're going to create a last surface group
that is going to be the walls of the flow. Select the sides. You should have six faces for the sides. Do not forget
to now add the obstacle. Apply. Now finally we're going to create a 1D group made of all of the vertices that are
along the z-axis. Let's name it Z vertices. This group is going to be useful when we'll be doing the mesh.
 
At the end of the day you should have the following groups the inlet, the outlet, the symmetry that are basically
the planes orthogonal to Z and finally the walls. if you make everything else invisible the walls should just be the
lateral side as well as the obstacle. And of course the 1D Z vertices group we just created.

## Creating a butterfly mesh with the MESH module

Now let's move to the mesh module we start by expanding the menu of flow, the geometry we just created,
and we are going to select it and go on the create mesh button. As algorithm we're going to select the hexahedral algorithm.

Then we'll move on to 2D and impose the quadrangle mapping algorithm so that we have quadrilateral elements on the surface.
We create a new hypothesis quadrangle parameter and select "quadrangle preferences".

Move into 1D and we're going to impose a wire discretization algorithm with the hypothesis "number of segments" set to 30.
At this stage if you right click on the mesh you just created and go on compute you're going to see that you have a much
finer mesh around the hole than elsewhere. Second thing you'll notice is in 3D along the z-axis you have much more elements
than what you want. We need only one element along Z.

## Refining the mesh by adding sub-meshes

We are now going to create sub meshes to solve these issues. Right click on the mesh you just created and go on create submesh.
Here we'll select the Z edges geometry group and impose a new 1D wire discretization algorithm. Go into hypothesis
and create a new number of segment hypothesis and this time you can set it to one. This way, we'll impose only one
element along the z-axis. You can clear and compute the mesh and as you can see now there is only one cell along the
Z axis. Finally let's make a final mesh on this side of the geometry create a sub mesh and this time select the X edges
group. Add another wire discretization algorithm and another set of hypothesis number of segments and put 160 segments.
Press ok. apply and close. If we compute again the mesh we see that we have a finer mesh everywhere ! So butterfly meshing
is not only necessary for the hexahedral algorithm but it is also a way of locally refining the mesh.

## Exporting the mesh as a .MED file

Finally once we are done we can export the mesh by right clicking it and go into export med file and here you can save
it wherever you want. I'm going to call it mesh one. Save.
