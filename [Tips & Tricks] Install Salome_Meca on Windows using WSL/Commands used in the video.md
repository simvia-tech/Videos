# Install Salome_Meca 2024 with WSL by Simvia  

## Prerequisites
WSL is already present by default on Windows 10 for the 2004 version and onwards, or on Windows 11. If you have an older version, try a manual installation.

## Install WSL

Type "powershell" in the Windows start menu, and execute it as an administrator. Launch the following command to activate WSL: 
 
    wsl --install

Once activated, type the command again to install a virtual machine (Ubuntu by default). The installation can take a little bit of time and may ask for a reboot, but once completed, launching the virtual machine is quick. When the installation is done, you'll have to type your username and password. Note them somewhere for later.

In the virtual machine, please update the libraries with the following command:

    sudo apt update && sudo apt upgrade

For more information on WSL and how to install it manually, refer to: [Manually installing WSL](https://learn.microsoft.com/fr-fr/windows/wsl/install-manual) 

## Install Singularity

Add Go to the PATH in order to be able to compile it. These commands can be customized as needed.

    grep -qxF 'export GOPATH=${HOME}/go' ~/.bashrc || echo 'export GOPATH=${HOME}/go' >> ~/.bashrc
    grep -qxF 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' ~/.bashrc || echo 'export PATH=/usr/local/go/bin:${PATH}:${GOPATH}/bin' >> ~/.bashrc
    source ~/.bashrc

The Singularity version within apt is too old, so it has to be manually installed. Before this, install the required libraries with:

    sudo apt-get install -y build-essential libseccomp-dev pkg-config squashfs-tools cryptsetup

Download Go:

    cd $HOME
    wget https://golang.org/dl/go1.15.5.linux-amd64.tar.gz
    tar -C ./ -xzf go1.15.5.linux-amd64.tar.gz
    go version

Download and compile golangci-lint:

    curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.32.2

Once Go is working, download Singularity by cloning its source code from GitHub:

    mkdir $HOME/dev && cd $HOME/dev
    git clone https://github.com/sylabs/singularity.git && cd singularity

Switch to the latest stable version of Singularity (3.7.0 when this document is being written):

    git checkout v3.7.0

Configure Singularity with the command:

    ./mconfig
    cd ./builddir
    make
    sudo make install

Check that the installation worked and that you have the correct version of Singularity:

    singularity version

## Install Salome_Meca

Download the binary files of Singularity for Salome_Meca on the website of Code-Aster
([follow the link](https://code-aster.org/spip.php?article295)).

Once on the download page, right-click on the file to download and click on "Save as a link". The download may occasionally stop and need to be resumed manually. This will be fixed soon.

Once the .sif file is fetched, move it to the `$HOME` folder of your WSL machine via the file explorer.

Launch the Singularity container with the following command:

    singularity run --app install salome_meca-lgpl-2024.1.0-1-20240327-scibian-11.sif

Salome_Meca will be installed and set up within this container, as well as Code-Aster. You just have to launch Salome_Meca with:

    ./salome_meca-lgpl-2024.1.0-1-20240327-scibian-11

If you have an Nvidia graphics card, Salome_Meca will use it to optimize its performance. You can also launch the software without a graphics card using:

    ./salome_meca-lgpl-2024.1.0-1-20240327-scibian-11 --soft

To leave the virtual machine, type `exit` or `Ctrl + D`.
To reopen a virtual machine, use the following command (or click on the virtual machine logo in the explorer):

    wsl --d [name_of_the_machine]

# Contact Us

Send us an email at [info@simvia.tech](mailto:info@simvia.tech)
