.. SPDX-FileCopyrightText: 2024 QElectroTech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only
.. _developer/build:

=================================
Building QET from source
=================================

This section is for users and contributors wanting to build and/or improve QElectroTech (QET).

This guide assumes that you have forked the source repo and that your system has the Git VCS (Version Control System) configured to point to that fork. 

If you need help to setup Git or you are unsure about something regarding pushing code to the repo, please have a look at the :doc:`Contributing guidelines <contributing>`.


Prerequisites
=============

- Get the sources and initialize the submodules by running this command

.. code-block:: bash

    git clone --recursive https://github.com/qelectrotech/qelectrotech-source-mirror.git


Linux
-----

Native
^^^^^^
- For a Debian-like machine (Ubuntu, Linux Mint, etc), install the required packages 
        
.. code-block:: bash

    sudo apt install libqt5svg5-dev qt5-qmake qtbase5-dev libkf5widgetsaddons-dev libkf5coreaddons-dev libsqlite3-dev pkgconf


Containerized
^^^^^^^^^^^^^

If you are worried about risks of dependency breakage, you can use a tool like `Distrobox`_ to easily setup a contained environment.
After creating the box with your choice OS, follow the package install guidelines in the "Native" part of the build docs.

*Example of Debian box creation. Replace <name> with the one you want to give to it.*

.. code-block:: bash

     distrobox-create -i debian:latest -n <name>


Windows
-------

*Due to the fact that Windows doesn't ship with a GCC version by default and uses its own C compiler (MSVC), the Prerequisites Step is a little bit more involved than on Linux.*

1. Download the `Qt Online Installer`_.
2. During installation:
   - Select **Custom Installation**.
   - See Qt 5 by checking 'Archive' and clicking 'Filter' button
   - Enable **Qt 5.15.2** → **MinGW 8.1.0 64-bit** under the `Archive` section.
   - Enable **Build Tools** → **MinGW 8.1.0 64-bit**.
3. After installation:
   - Qt will be installed at: `C:\Qt\5.15.2\mingw81_64`.
   - MinGW will be available at: `C:\Qt\Tools\mingw810_64\bin`.


Compilation instructions
========================

After setting your developer environment, you will now learn how to compile the QET source code from the IDE or the CLI.

IDE Setup and Compilation
-------------------------

Windows
^^^^^^^

To install the QT Creator IDE on Windows, you can choose one of the two following options:

- Use the `Qt Online Installer`_ previously mentioned, in which case you can select the QT Creator IDE as a component to install during the Setup.   

Linux
^^^^^

1. After installing the dependencies, install the QT Creator IDE. Depending on your OS type, you have two options:
    
    
- If you are using a bleeding edge distro like Fedora, Arch or `Ubuntu Non LTS`_ , chances are that their builds are up to date. Install it by running the :code:`apt` command:
    
.. code-block:: bash
        
    sudo apt install qt-creator
    

- If you are using a distro with a slower release cycle like Debian, you'll need to do two things:
   
  #. First setup `Flatpak`_
  #. Then use Flatpak to install the `QT Creator IDE`_
        
.. code-block:: bash

    flatpak install flathub io.qt.QtCreator



After installation, click on "File">"Open File or Project" or use the shortcut ``ctrl+O`` to open your OS file dialog. Click the *.pro* file to open the project and click "Build">"Run" to run the project.

CLI Compilation
---------------
Windows
^^^^^^^

Linux
^^^^^

If you do not want to use the QT Creator IDE or you are using another IDE (VSCode, Sublime Text, etc...), you can compile the codebase using these commands:

.. code-block:: bash

    cd qelectrotech-source-mirror.git
    mkdir build && cd build
    qmake  ../qelectrotech.pro
    make -j$(nproc)

This will instruct :code:`qmake` to prepare the required files in the :code:`build` directory and launch compilation with the :code:`make` command.  

.. _Ubuntu Non LTS: https://ubuntu.com/about/release-cycle
.. _Flatpak: https://flathub.org/setup
.. _Distrobox: https://distrobox.it
.. _QT Creator IDE: https://flathub.org/apps/io.qt.QtCreator
.. _QT Online Installer: https://doc.qt.io/qtcreator/creator-how-to-install.html