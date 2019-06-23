.. _en/basics/start_linux

Start QElectroTech on Linux
===========================

After installation, Linux allows the user launching application from many different ways. Bellow, 
the most common ways are explained.

Start QElectroTech from terminal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To launch QElectroTech using the terminal, it is enough with the command:

    | ``$ qelectrotech``

The command mentioned above blocks the terminal for others processes. If the terminal should be 
available for others processes, the command to start QElectroTech is as follows:

    | ``$ gelectrotech &``

.. note::

   If the command is not working, list the applications installed and check with which name 
   QElectroTech has been installed.

   * Ubuntu command: ``$ apt list --installed``

.. figure:: graphics/qet_start.png
   :scale: 50 %
   :align: center

   Figure: Starting splash screen

Start QElectroTech from applications menu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As Windows, Linux operative systems allow the user to open applications from menus and icons. 
Where to go depends on the theme and distribution used. Bellow,  some possibilities according 
some configurations are mentioned. It is important to remark that not everybody can use them. 

    * Unity theme: The icon appears at the launcher bar.
    * Gnome shell: The icon appears at **[Menu]**, with the rest of applications.
    * Gnome Classic: QElectroTech can be started from **Applications > Graphics > QElectroTech**.
    * KDE: QElectroTech can be started from **[Menu]** at **Graphics > QElectroTech**.

Once QElectroTech has been started, the main window looks like the figure bellow.

.. figure:: graphics/qet_window.png
   :scale: 50 %
   :align: center

   Figure: Main window QElectroTech