# Install Docker and pull Code_Saturne with WSL  

## Prerequisites
WSL is already present by default on Windows 10 for the 2004 version and onwards, or on Windows 11. If you have an older version, try a manual installation.

## Docker

This section describes how to install Docker. See the [official documentation](https://docs.docker.com/engine/install/) for more information.

Add Docker's official GPG key:

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Add the repository to Apt sources:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

and update the repository
```bash
sudo apt-get update
```

Install and check the docker install

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Try whether the installation succeeded  (fail if no sudo)

```bash
sudo docker run hello-world
```

Gives the rights on Docker Group:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Docker can now be used without sudo rights:

```bash
docker run hello-world
```

If this command doesn't work, you may need to reboot WSL and try again the last command.

## Pulling Code_Saturne image

Simvia gives you access to pre-constructed images of EDF simulation codes. These are available on the company's DockerHub. For Code_Saturne, the link is as follows: [hub.docker.com/r/simvia/code_saturne](https://hub.docker.com/r/simvia/code_saturne).

To download the image of the software, use the following command line:

```bash
docker pull simvia/code_saturne:latest
```

## Creating an alias for Code_Saturne

An alias is a way of keeping commands that can take a long time to write in Linux. In our case, we may wish to hide the use of Docker and use the commands as if Code_Saturne were directly installed on our machine.

To do this, you need to edit the `.bashrc` file, located at the root of the user account (path given by `$HOME/.bashrc` or `~/.bashrc`. Use your favorite text editor to do this (`vim` in the video).

```bash
alias code_saturne='docker run -v $(pwd):/home/code_saturne -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=unix$DISPLAY simvia/code_saturne'
```

Few information about this command :
 - `-v $(pwd):/home/code_saturne`: to share the directory in which you launch the command on your local machine (`$(PWD)`) with a folder in the Docker container (`/home/code_saturne`)
 - `-v /tmp/.X11-unix:/tmp/.X11-unix`: to redirect the graphical interface in the Docker container with your local machine
 - `-e DISPLAY=unix$DISPLAY`: to allow graphical applications inside the Docker container to be displayed on your machine's screen
 - `simvia/code_saturne`: the tag given by default to your Docker image whan you do the pullong action

Once it's done you can relaunch your terminal. If you try to do the completion action, the command `code_saturne`should be considered now.

> *Note: To run GUI applications in Docker on Wayland, you need to manage access to either Xwayland (for X apps) or the Wayland compositor. For X apps, use `xhost` to allow access (e.g., `xhost +SI:localuser:$(id -un)`) and specify the user with `--user=$(id -u):$(id -g)` in the Docker command. For Wayland apps, share the Wayland socket (`WAYLAND_DISPLAY`), set `XDG_RUNTIME_DIR`, and run the application with the appropriate flags. Tools like `x11docker` simplify this process and preserve container isolation.*

## Launch you first commands

To print the help of Code_Saturne, just type:

```bash
code_saturne
```

To create a folder and a case related needed to start with Code_Saturne, use the following command:

```bash
code_saturne -s study1 -c case1
```

Finally, to launch the graphical interface of Code_Saturne on our newly created case, just type:

```bash
code_saturne gui study1/case1/DATA/setup.xml
```

## Remarks

Code_Saturne images correspond to different versions of the software. If you wish to have access to older versions or versions compiled for other operating systems, please contact Simvia via this address: [info@simvia.tech](mailto:info@simvia.tech).
