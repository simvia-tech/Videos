# Potential Issues When Running Salome

After following the first video on how to install Salome_Meca, you should have an executable for Salome on your virtual machine (or directly on your computer if you're using Linux). Run it (add --soft at the end if you do not have an Nvidia card):

    ./salome_meca-lgpl-2024.1.0-1-20240327-scibian-11 --soft


We noticed a few issues that may occur when launching Salome_Meca. We will work on fixing them when possible. For now, here are some temporary solutions.

### Mouse and Interface Buttons Are Not Aligned
Sometimes, the software may not display correctly, resulting in an offset between the mouse pointer and the interface. In the video, I show the bug at `0:32s`. This problem can be solved by setting Salome_Meca to fullscreen mode and then returning it to windowed mode. This can be achieved by pressing the `F11` key twice (see video).

### The AsterStudy Interface Freezes on "Please Wait Until AsterStudy Finishes Loading"
This issue also appears in the video, although I did not comment on it. After clicking the AsterStudy button, the interface where the mesh can be observed will sometimes freeze on the initial "Please wait until AsterStudy finishes loading" message. I believe this happens because the interface is not refreshed when launching AsterStudy. A simple right-click on the interface will refresh it and solve the problem. I demonstrate this in the video at `0:57s`.

# Running a Test Case
Once AsterStudy is properly loaded, click on the CurrentCase file in the Data Settings tab, usually located on the left in AsterStudy. Then, right-click it and choose "Import Testcase." This will open a window with all of the available test cases for Code_Aster. You can search for a specific one (in the video, I launch "forma01a"). Click on the test case you want to open, then press "Import." An error message will appear explaining that there are files with undefined names. These are the files where you need to tell AsterStudy where to save them (usually the result files). Close the error message, and in the "Data Files of CurrentCase" tab under "Data Settings," you should see the files you need to save, marked in red and labeled "undefined." Double-click on them, and a tab will open on the right titled "Edit Data Files." Click the "..." button next to "Filename" in the menu. This will open your file explorer so you can select where to save the file. You can also name the file as you wish. If it is a result file, it is usually saved with the .rmed extension. Once done, press the "OK" button at the bottom of the "Edit Data Files" tab. Repeat this process for every undefined file in the "Data Files of the CurrentCase" section.

You can view the mesh of the test case by double-clicking the "LIRE_MAILLAGE" (read mesh in French) command in the Data Settings tab. It will open in the interface (`2:04s` in the video).

To run the test case, click on the "History View" tab, located on the left side of AsterStudy. Before running the test case, you need to save it. Once saved, you should see a list of all the CurrentCases in the middle of the AsterWorkspace. Press the "+" button ( `2:30s` in the video) to add it to the list of CurrentCases that Code_Aster will run. Then, press the "Run" button at the bottom. An output tab should open. Clicking the "Refresh" button will display the logs at the current moment of the run. You can also set up "Auto-refresh" to automatically refresh the logs every few seconds. After a while, if the CurrentCase ran properly, a green icon should appear above the logs, indicating that the run finished correctly (see `2:50s` in the video). You can click on this icon, and the files related to this run will appear in the "Data Summary Files" tab. There, you should see the result files you saved earlier. You can right-click on them and select "Post-process" to open an interface to visualize the fields you computed. In the video, I display the displacement field of the plate.

Finally, note that you can find documentation on all the test cases in Code_Aster at:

https://codeaster.gitlab.io/doc/docaster/manuals/man_v/other_pages/list/index.html

The documentation is in French but will soon be available in English. For each test case, it explains the physics, the mesh, what is done, why it is done, and what the test case is trying to check.
