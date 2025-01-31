# The files within salome_meca

## The dump file

In the File tab of Salome_Meca, you can generate the dump file by clicking on "Dump study" (or pressing `Ctrl + D`). This is a Python file that lists everything done in the Salome interface. It shows the operations and parameters defined in the Shaper module, for instance. In the documentation (see the Help tab in Salome), you can find not only details on all of the buttons and tools in Salome_Meca, but also the syntax used in the dump study file (see `[1:34s]`).

AsterStudy is the only empty module in the dump file (`[1:47s]`). This is because AsterStudy generates its own files to run and execute Code_Aster.


## The AsterStudy files

To run a study with Code_Aster, AsterStudy generates two files: the export file and the command file. The command file summarizes all the operations Code_Aster must run, while the export file indicates how much memory to allocate for the run, where to find the command and mesh files, and other external resources...

### The command file .comm

Open the AsterStudy interface. Right-click on the Stage_1 item under CurrentCase in the Data Settings panel and select "Text Mode". This will display the exact equivalent of everything performed through the AsterStudy interface in the first video, but as Python code with functions and commands that Code_Aster can understand. You can save and export the command file (.comm) from Salome_Meca by right-clicking on Stage_1 and selecting "Export command file". The .comm file starts with `DEBUT()` (in French) and ends with `FIN()`, containing the same content as what was shown in "Text Mode".


### The export file .export

You can save the export file by right-clicking on the CurrentCase item in the Data Settings of AsterStudy and selecting "Export case" (this can also be done in the History view, as shown in the video at `[2:25s]`). If you open the export file after saving it, you’ll see several lines instructing Code_Aster to run with specific memory limits, number of CPUs, and—more importantly—the .comm file and the .med (mesh) file.


## The mesh file .med

In the Mesh module, right-click on the Mesh_1 item in the Object Browser (see `[2:55s]`). Select "Export" and choose the MED file format. You can save it independently.


# Importing the files


## The .hdf file

This file saves the details of the Code_Aster computation and its dependencies (including the .med mesh file). In Salome_Meca, you can generate an .hdf file when saving a project. You can open the .hdf file to load a Salome_Meca study.


## Importing the dump file

You can import the dump file by going to the File tab and selecting "Import script". Like .hdf files, the information in the Python dump file only includes what was done in a Salome_Meca study and can be imported to regenerate every step of the project. The key difference is that the commands in the dump file need to be recompiled. So, the dump file is useful for transferring large studies in a lightweight text format, while the .hdf file is preferable if the goal is to open the Salome_Meca study quickly. It is, of course, possible to modify some of the actions in the dump file before importing it.

## Importing the .med mesh file

If you already have the mesh from a previous study and the .dump file has been transferred to you, it's helpful to delete the commands in the mesh module of the dump file and import the mesh directly. You can do this by going to the Mesh module, right-clicking in the Object Browser, and selecting "Import". Note that the .med file will already be generated if the .hdf file is opened.


## Importing the Aster command .comm file

In the AsterStudy module, you can import the entire command file by right-clicking on CurrentCase in the Data Settings tab and selecting "Add Stage from file". All the commands will be generated, but the names and saving directories for the input and output files will need to be redefined (see `[6:25s]`). The export file will be automatically regenerated with Salome_Meca when running the study.


# code_aster from the bash

## Customize the computation ressources in the .export file

With a .export and .comm file, you can call Code_Aster directly without using Salome_Meca. This approach gives you more control over how the computation is done, as the .export file can be customized. It's also entirely possible to create the geometry, mesh, and .comm file with Salome_Meca, then extract the files and run Code_Aster directly from the console.

A more detailed explanation of how to edit the .export file will be provided in an additional video. Below is a brief overview of how to edit it.

Each line in the .export file starts with a "P" to define a parameter or an "F" for a file (to read, generate, etc.). To read a file, you typically use the line `F libr [name_file] D/R [unit]`: libr means you are using a file, D/R indicates whether it's a data or result file, and the unit is an integer that identifies the file within the code. For example, to tell Code_Aster where the mesh is located in the LIRE_MAILLAGE (read mesh) command in the .comm file, you would use `F libr [mesh.med] D 40` and set the unit to 40 in the LIRE_MAILLAGE command.

The .export file assigns resources, including giving Code_Aster the command file to run the computation. This is done with the line `F comm [command_file_name.comm] D 1`. The unit for the .comm file must always be set to 1.

The result file can be defined using `F rmed [name] R [unit]`. The logs (outputs from Code_Aster during the computation) can be defined using `F mess [name] R [unit]`.

The `ncpus` parameter (`P ncpus x`) defines how many CPUs will be used by certain linear solvers (e.g., MUMPS) in Code_Aster for OpenMP parallelization. Increasing the number of CPUs can speed up the SOLVER command. Similarly, the `mpi_nbcpu` and `mpi_nbnoeud` parameters define the CPUs and nodes for MPI parallelization (used by the parallel version of Code_Aster).


## Call Code_Aster directly from the shell

Once you have an appropriately set-up export file, you can compile Code_Aster by opening a Singularity shell with the following command in Ubuntu bash:

    Singularity run [name_of_the_salome_sif_file] shell

This opens Salome_Meca without displaying the GUI. The shell prompt should start with `Singularity>`

Once in this shell, simply type 

    run_aster [name_of_export_file]

to run Code_Aster and execute the study. Note that if you haven't defined a log file in the export file using `F mess`, you can also specify one directly by typing:

    run_aster [name_of_export_file] > [name_of_log_file]
