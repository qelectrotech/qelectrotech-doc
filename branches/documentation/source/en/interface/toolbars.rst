.. _en/interface/toolbars

Toolbars
========

In addition to the different menus, QElectroTech provides also toolbars. The toolbars are groups 
of buttons with icons which initiate an accion. In general, these buttons have its counterpart at one of 
the menus from the Menu bar. The aim from the toolbars is make easier and more grafically the use of 
QElectroTech. 

The different toolbars can be hidden or placed in one or more rows bellow the Menu bar. The toolbars 
can also be placed on column at the left or right side from the main window.

.. note::

   To help the user, a tooltip is displayed when the arrow is placed on each button.

Toolbar Tools
~~~~~~~~~~~~~

.. figure:: graphics/qet_toolbar_tools.png
   :align: center

   Figure: QElectroTech toolbar Tools 

The different button from the toolbar Tools are mentioned and described bellow. 

+------------+------------------+------------------------------------------------------------------+---------------------------+
| Toolbar    | Options          | Function                                                         | Keyboard shortcut         |
+============+==================+==================================================================+===========================+
| **Tools**  | New              | Creates a new Project                                            |                           |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            | Open             | Opens an existing project from the computer                      |   ``Ctrl + o``            | 
+            +------------------+------------------------------------------------------------------+---------------------------+
|            | Save             | Saves the current changes to the project (overwrites)            |   ``Ctrl + s``            |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            | Save as          | Saves the current project as a different file on disk            |                           |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            | Close            | Closes the current project (prompts for saving changes)          |   ``Ctrl + w``            |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            | Print            |  Opens a dialogue to print drawings from a project               |   ``Ctrl + p``            |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Undo            | Undo the last action in the active drawing (folio)               |  ``Ctrl + z``             |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Redo            | Repeat the last action in the active drawing (folio)             |  ``Ctrl + Shift + z``     |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Cut             | Equivalent to copy + delete the object (active folio)            |  ``Ctrl + x``             |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Copy            | Copies the object selected in the active drawing                 |  ``Ctrl + c``             |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Paste           | Pastes the object from last copy or cut (any folio)              |  ``Ctrl + v``             |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Delete          | Deletes the selected object in the active folio                  |  ``Del``                  |
+            +------------------+------------------------------------------------------------------+---------------------------+
|            |  Rotate          | Rotates selected object(s) in the active folio                   |  ``Space``                |
+------------+------------------+------------------------------------------------------------------+---------------------------+

.. note::

   Select **Settings > display > Tools** menu item to display or hidden the toolbar Tools.

Toolbar Display
~~~~~~~~~~~~~~~

.. figure:: graphics/qet_toolbar_display.png
   :align: center

   Figure: QElectroTech toolbar Display

The different button from the toolbar Display are mentioned and described bellow.

+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
| Toolbar        | Options                        | Function                                                                                   | Keyboard shortcut      |
+================+================================+============================================================================================+========================+
| **Display**    | Select                         | Use choose tool (default) to select individual elements, conductors in the workspace       |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Move                           | Use move tool to hold and drag the drawing sheet (folio) when zoomed in excess of display  |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Display the grid               | Display or hide the grid from the folio                                                    |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Background color white / gray  | Change the background color from the folio, change color from white to gray or vice versa  |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Zoom content                   | The window magnifies to a level that fits all the elements of the active folio to display  |  ``Ctrl + 8``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Fit in view                    | Reset zoom levels to fit the active folio including grid and title block to display        |  ``Ctrl + 9``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Reset zoom                     | Reset zoom levels to a default value (zoom level just less than that of fit in view)       |  ``Ctrl + 0``          |
+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+

.. note::

   Select **Settings > display > Display** menu item to display or hidden the toolbar Display.

Toolbar Diagram
~~~~~~~~~~~~~~~

.. figure:: graphics/qet_toolbar_diagram.png
   :align: center

   Figure: QElectroTech toolbar Diagram

The different button from the toolbar Diagram are mentioned and described bellow.

+--------------+-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------+
| Toolbar      | Options                                   | Function                                                                                                                     | Keyboard shortcut         |
+==============+===========================================+==============================================================================================================================+===========================+
| **Diagram**  |  Folio properties                         | Opens the properties window for the active drawing                                                                           |  ``Ctrl + l``             |
+              +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------+
|              |  Reset conductors                         | Resets selected conductor(s) to a shortest path                                                                              |  ``Ctrl + k``             |
+              +-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------+
|              |  Automatic creation conductor             | Permits automatic conductors creation when two terminals of an element are aligned in either vertical or horizontal plane    |                           |
+--------------+-------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+---------------------------+

.. note::

   Select **Settings > display > Diagrams** menu item to display or hidden the toolbar Diagram.

Toolbar Add
~~~~~~~~~~~

.. figure:: graphics/qet_toolbar_add.png
   :align: center

   Figure: QElectroTech toolbar Add

The different button from the toolbar Add are mentioned and described bellow.

+--------------+----------------------+------------------------------------------------------+---------------------------+
| Toolbar      | Options              | Function                                             | Keyboard shortcut         |
+==============+======================+======================================================+===========================+
|   **Add**    |  Add a textfield     |                                                      |                           |
+              +----------------------+------------------------------------------------------+---------------------------+
|              |  Add a picture       |                                                      |                           |
+              +----------------------+------------------------------------------------------+---------------------------+
|              |  Add line            |                                                      |                           |
+              +----------------------+------------------------------------------------------+---------------------------+
|              |  Add a rectangle     |                                                      |                           |
+              +----------------------+------------------------------------------------------+---------------------------+
|              |  Add an ellipse      |                                                      |                           |
+              +----------------------+------------------------------------------------------+---------------------------+
|              |  Add a polygon       |                                                      |                           |
+--------------+----------------------+------------------------------------------------------+---------------------------+

.. note::

   Select **Settings > display > Diagrams** menu item to display or hidden the toolbar Add.

Toolbar Depth
~~~~~~~~~~~~~

.. figure:: graphics/qet_toolbar_depth.png
   :align: center

   Figure: QElectroTech toolbar Depth 

The different button from the toolbar Depth are mentioned and described bellow.

+--------------+---------------------+------------------------------------------------------+---------------------------+
| Toolbar      | Options             | Function                                             | Keyboard shortcut         |
+==============+=====================+======================================================+===========================+
|  **Depth**   |  Bring to front     |                                                      |                           |
+              +---------------------+------------------------------------------------------+---------------------------+
|              |  Raise              |                                                      |                           |
+              +---------------------+------------------------------------------------------+---------------------------+
|              |  Lower              |                                                      |                           |
+              +---------------------+------------------------------------------------------+---------------------------+
|              |  send backwards     |                                                      |                           |
+--------------+---------------------+------------------------------------------------------+---------------------------+

.. note::

   Select **Settings > display > Diagrams** menu item to display or hidden the toolbar Depth.