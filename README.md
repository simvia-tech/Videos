# Videos @simvia

Welcome to the official repository for [**Simvia**](https://www.simvia.tech). Here, you will find detailed explanations and resources related to the videos we post on my YouTube channel : [Simvia-tech](https://www.youtube.com/@Simvia-tech).

## About This Repository

This repository is a companion to my YouTube channel, where we dive deeper into the concepts and topics discussed in our videos. The content here provides:

- **Code snippets**: The full code used in the video.
- **Detailed explanations**: Further clarifications and elaborations of the video material.
- **Links & Resources**: Additional resources, references, or external links relevant to the video.

## Videos

Below are the links to our videos along with a brief description of each. The video are regrouped by playlists, click on the ones you wish to expand.

<details>
<summary><h3> Tips & Tricks </h3></summary>

### [Install Salome_Meca on Windows using WSL](https://www.youtube.com/watch?v=dgr5NA9gd3A)
First tutorial on the installation of salome_meca with WSL. In this video, we activate WSL on Windows, install the singularity software and its dependencies and download and run with singularity the salome_meca software.

- Software: [code_aster](https://code-aster.org/spip.php?rubrique1), [salome_meca](https://www.salome-platform.org/?page_id=150)
- In-depth breakdowns: [[Tips & Tricks] Install Salome_Meca on Windows using WSL/Commands used in the video.md](https://github.com/simvia-tech/Videos/blob/main/%5BTips%20%26%20Tricks%5D%20Install%20Salome_Meca%20on%20Windows%20using%20WSL/Commands%20used%20in%20the%20video.md)

### [Run a test case with salome meca](https://www.youtube.com/watch?v=gp3PgDTOGUY)
Learn how to open and run a test case of code_aster within salome_meca. There are many test case you can try, all of them are documented.

- Software: [code_aster](https://code-aster.org/spip.php?rubrique1), [salome_meca](https://www.salome-platform.org/?page_id=150)
- In-depth breakdowns: [[Tips & Tricks] Run a test case with Salome meca/Additionnal details on the video.md](https://github.com/simvia-tech/Videos/blob/main/%5BTips%20%26%20Tricks%5D%20Run%20a%20test%20case%20with%20Salome%20meca/Additionnal%20details%20on%20the%20video.md)

### [How to install Docker on Windows and get started with code_saturne](https://www.youtube.com/watch?v=toaXeW8Wt94)
In this tutorial, we walk you through the process of installing Docker on your Windows computer and guide you on how to download the
Code_Saturne image directly from our DockerHub. You'll also learn the essential first commands to run Code_Saturne smoothly and get
started with your simulations. Whether you're a beginner or looking to streamline your setup, this video makes the process quick and easy.

- Software: [code_saturne](https://www.code-saturne.org/cms/web/)
- In-depth breakdowns: [[Tips & Tricks] How to install Docker on Windows and get strated with Code_Saturne/Main steps.md](https://github.com/simvia-tech/Videos/blob/main/%5BTips%20%26%20Tricks%5D%20How%20to%20install%20Docker%20on%20Windows%20and%20get%20started%20with%20Code_Saturne/Main%20steps.md)

</details>

<details>
<summary><h3> Learn & Understand </h3></summary>

### [Perform a basic mechanical study with salome_meca](https://www.youtube.com/watch?v=vjUMgDSKJjY)
In this video, you will learn the fundamentals of a standard mechanical study in salome_meca: Create the geometry and groups with the sketch module | Create a mesh for the geometry | Read the mesh with Aster_Study and set up the model using the "isotropic linear elastic" assistant | Run the simulation | Visualize the results with post-processing tools

- Software: [code_aster](https://code-aster.org/spip.php?rubrique1), [salome_meca](https://www.salome-platform.org/?page_id=150)
- In-depth breakdowns: [[Learn & Understand] Perform a basic mechanical study with salome_meca/Additionnal details.md](https://github.com/simvia-tech/Videos/blob/main/%5BLearn%20%26%20Understand%5D%20Perform%20a%20basic%20mechanical%20study%20with%20salome_meca/%5BLearn%20%26%20Understand%5D%20Perform%20a%20basic%20mechanical%20study%20with%20salome_meca.md)

### [Behind the scenes of salome_meca: scripting and files](https://www.youtube.com/watch?v=P9Tcn4K-XGQ)
This video is a direct continuation of "[Learn & Understand] Perform a basic mechanical study with salome_meca." If you haven't seen it yet, you can watch it here: [Link to the video](https://www.youtube.com/watch?v=vjUMgDSKJjY) 

In this video, we focus on the powerful Python scripting capabilities within salome_meca. We explain how to work with the dump file from the previous study, provide a complete overview of the generated files, their functions, and demonstrate how to use them to compile code_aster directly from the bash.

- Software: [code_aster](https://code-aster.org/spip.php?rubrique1), [salome_meca](https://www.salome-platform.org/?page_id=150)
- In-depth breakdowns: [[Learn & Understand] Behind the scenes of salome_meca: scripting and files/Additionnal details.md](https://github.com/simvia-tech/Videos/blob/main/%5BLearn%20%26%20Understand%5D%20Behind%20the%20scenes%20of%20salome_meca%20scripting%20and%20files/Additionnal%20details.md)

### [Von Karman vortices Part 1 - Mesh & Geometry on Salome](https://www.youtube.com/watch?v=Sh26NeNrjn4)
In this two-part tutorial, we showcase the powerful capabilities of Salome and Code_Saturne by demonstrating their performance on the well-documented Von Karman vortex phenomenon.

In Part 1, we guide you step-by-step through the creation of geometry and mesh, highlighting key tips and tricks in the Geom and Mesh modules. You'll also learn how easy it is to get started with the Docker version of Code_Saturne, which offers impressive performance with minimal installation effort..

- Software: [salome](https://www.salome-platform.org/)
- In-depth breakdowns: [[Learn & Understand] Von Karman vortices Part 1 - Mesh & Geometry on Salome
/Details on each step.md](https://github.com/simvia-tech/Videos/blob/main/%5BLearn%20%26%20Understand%5D%20Von%20Karman%20vortices%20Part%201%20-%20Mesh%20%26%20Geometry%20on%20Salome/Details%20on%20each%20step.md)

### [Von Karman vortices Part 2 - code_saturne study and post-process on paravis](https://www.youtube.com/watch?v=WT91OAqHOl4)

In Part 2, we guide you step-by-step through the creation of a code_saturne study, showcasing some of the many possibilities the code offers to simulate flows. You'll also learn how to visualize the results on paravis and apply basic filters to understand better the datas. 

- Software: [Code_saturne](https://www.code-saturne.org/cms/web/)
- In-depth breakdowns: [[Learn & Understand] Von Karman vortices Part 2 - code_saturne study and post-process on paravis
/Tutorial walkthrough.md](https://github.com/simvia-tech/Videos/blob/main/%5BLearn%20%26%20Understand%5D%20Von%20Karman%20vortices%20Part%202%20-%20code_saturne%20study%20and%20post-process%20on%20paravis/Tutorial%20walkthrough.md)

### [Open_Telemac river flooding tutorial - Part 1: First steps with QGIS & Q4TS](https://youtu.be/NFo-HavVz70)

This video is the first part of a tutorial on how to simulate river flooding using Open_Telemac.
In this initial video, we focus on creating the model and preparing the data. Using the Q4TS plugin in QGIS, we create a mesh for a domain that we draw directly on the map. We use a French river as an example, but the steps described here can be applied to any river in the world, provided topographic data is available.

Once the mesh is generated, we project the topographic data onto it (specifically, the "bottom" variable). This forms the foundation of the data required for the Open_Telemac model to run a flood simulation.

- Softwares: [Open_Telemac](http://www.opentelemac.com/), [QGIS](https://www.qgis.org/), [Q4TS](https://plugins.qgis.org/plugins/q4ts/)
- Summary with extra details: [[Learn & Understand] Open_Telemac river flooding tutorial - Part 1: First steps with QGIS & Q4TS/Summary of the video.md](https://github.com/simvia-tech/Videos/blob/main/%5BLearn%20%26%20Understand%5D%20Open_Telemac%20river%20flooding%20tutorial%20-%20Part%201%3A%20First%20steps%20with%20QGIS%20%26%20Q4TS/Summary%20of%20the%20video.md)


</details>

> *Note: Each video will be updated with additional content and resources here as we continue building this repository.*

## How to Use This Repository

1. **Clone the repository**: You can clone the repository to your local machine using the following command:

    ```bash
    git clone https://github.com/simvia-tech/Videos.git
    ```

2. **Navigate to the video folder**: Each video has its own folder with explanations, code, and additional files.

3. **Check out the README for each video**: Inside each video folder, you’ll find a `markdown` file with further details.

## Contributions

If you would like to contribute or suggest improvements to this repository, feel free to fork it, make changes, and submit a pull request. Contributions are always welcome!

## Contact

If you have any questions or need further clarification on anything, feel free to reach out to me at:

- YouTube: [Simvia-tech](https://www.youtube.com/@Simvia-tech)
- LinkedIn: [simvia-tech](https://www.linkedin.com/company/simvia-tech/)
- Email: [info@simvia.tech](mailto:info@simvia.tech)

## Acknowledgements

An essential part of the videos on our YouTube channel was created in collaboration with our partners at [Phimeca](https://www.phimeca.com/en/).
