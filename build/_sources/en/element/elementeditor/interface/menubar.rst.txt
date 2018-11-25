.. _en/element/elementeditor/interface/menubar

Menu bar
========

The framework and widget toolkit `Qt`_ allows the design of drop-down menus. The drop-down menus 
are a characteristic graphical control element from the desktop applications. Each of the drop-down 
menus contains a number of options to initiate an action. The Menu bar is placed at top from the main 
windows. The figure bellow shows how the menu bar from QElectroTech looks.

.. figure:: graphics/qet_elementeditor_menu.png
   :align: center

   Figure: QElectroTech Element editor Menu bar

As is showed at the figure, QElectroTech bar contains the menus ``File``, ``Edit``, ``Display``, 
``Settings`` and ``Help``. A brief description of each such option can be read from the help 
or information tool bar, located to the bottom left corner of the QElectroTech 
window by hovering over the option with the cursor. The following tables summarizes the available 
options from the main menu bar.

|

+------------+------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
| Menu       | Options          | Function                                                         | Keyboard shortcut         | Notes                              |
+============+==================+==================================================================+===========================+====================================+
| **File**   | Recently opened  | Open a project from history (recently opened files)              |                           |                                    |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | New              | Creates a new Project                                            |   ``Ctrl + n``            | Same as ``New`` on tool bar        |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Open             | Opens an existing project from the disk                          |   ``Ctrl + o``            | Same as ``Open`` on tool bar       |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Save             | Saves the current changes to the project (overwrites)            |   ``Ctrl + s``            |  Same as ``Save`` on tool bar      |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Save as          | Saves the current project as a different file on disk            |                           |  Same as ``Save as`` on tool bar   |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Close            | Closes the current project (prompts for saving changes)          |   ``Ctrl + w``            |  Same as ``Close`` on tool bar     |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Export           |  Opens a dialogue to export drawings from a project              |   ``Ctrl + Shift + x``    |  For customization refer `Export`_ | 
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Print            |  Opens a dialogue to print drawings from a project               |   ``Ctrl + p``            |  Same as ``Print`` on tool bar     |
+            +------------------+------------------------------------------------------------------+---------------------------+------------------------------------+
|            | Quit             |  Quits the QElectroTech main window (prompts for saving changes) |   ``Ctrl + q``            |  ``Alt + F4`` can also be used     |
+------------+------------------+------------------------------------------------------------------+---------------------------+------------------------------------+

|

+--------------+-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
| Menu         | Options                                   | Function                                             | Keyboard shortcut         | Notes                      |
+==============+===========================================+======================================================+===========================+============================+
| **Edit**     |  Undo                                     | Undo the last action in the active drawing (folio)   |  ``Ctrl + z``             | Same as Undo on tool bar   |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Redo                                     | Repeat the last action in the active drawing (folio) |  ``Ctrl + Shift + z``     | Same as Redo on tool bar   |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Cut                                      | Equivalent to copy + delete the object (active folio)|  ``Ctrl + x``             | Same as Cut on tool bar    |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Copy                                     | Copies the object selected in the active drawing     |  ``Ctrl + c``             | Same as Copy on tool bar   |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Paste                                    | Pastes the object from last copy or cut (any folio)  |  ``Ctrl + v``             | Same as Paste on tool bar  |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Select All                               | Selects all objects in the active drawing area       |  ``Ctrl + a``             | Refer to graphic `Fig.20`_ |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Select none                              | Removes all current selections in the active folio   |  ``Ctrl + Shift + a``     |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Invert selection                         | Inverts selection of objects in the active folio     |  ``Ctrl + i``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Delete                                   | Deletes the selected object in the active folio      |  ``Del``                  | Same as Delete on tool bar |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Rotate                                   | Rotates selected object(s) in the active folio       |  ``Space``                |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Choose texts orientation                 | Rotates selected text field(s) in the active folio   |  ``Ctrl + Space``         |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Find in the panel                        | Identifies the selected element in elements panel    |                           | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Edit the selected object                 | Opens properties window for the selected element     |  ``Ctrl + e``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Reset conductors                         | Resets selected conductor(s) to a shortest path      |  ``Ctrl + k``             | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Folio properties                         | Opens the properties window for the active drawing   |  ``Ctrl + l``             | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Add a column                             | Adds an additional column to the active drawing      |                           | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Remove a column                          | Removes a column from the active drawing             |                           | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Add a row                                | Adds an additional row to the active drawing         |                           | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Remove a row                             | Removes a row from the active drawing                |                           | Same as in tool bar        |
+--------------+-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+

|

+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
| Menu           | Options                        | Function                                                                                   | Keyboard shortcut      |
+================+================================+============================================================================================+========================+
| **Display**    | Display projects               | Set preference for projects and folios appearance as either tabs (default) or windows      |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Select                         | Use choose tool (default) to select individual elements, conductors in the workspace       |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Move                           | Use move tool to hold and drag the drawing sheet (folio) when zoomed in excess of display  |                        |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Zoom In                        | Magnify the drawing for a closer view; (use move tool to drag the folio to view all parts) |  ``Ctrl + +``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Zoom Out                       | Reduce magnification of the drawing; develops a distant view of the folio                  |  ``Ctrl + -``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Zoom content                   | The window magnifies to a level that fits all the elements of the active folio to display  |  ``Ctrl + 8``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Fit in view                    | Reset zoom levels to fit the active folio including grid and title block to display        |  ``Ctrl + 9``          |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+
|                | Reset zoom                     | Reset zoom levels to a default value (zoom level just less than that of fit in view)       |  ``Ctrl + 0``          |
+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+

|

+---------------+--------------------------------+-------------------------------------------------+--------------------------------------------------+
| Menu          | Options                        | Function                                        | Notes                                            |
+===============+================================+=================================================+==================================================+
| **Settings**  | Display                        | View or hide options in the QET main window     | Hides or shows elements panel, tool bar etc.,    |
+               +--------------------------------+-------------------------------------------------+--------------------------------------------------+
|               | Full screen mode               | Spreads the window to fill the screen           | Entire screen gets occupied by the window        |
+               +--------------------------------+-------------------------------------------------+--------------------------------------------------+
|               | Configure QElectroTech         | Opens the configure QElectroTech window         | Same as described in `Section.4`_                |
+---------------+--------------------------------+-------------------------------------------------+--------------------------------------------------+

|

+---------------+--------------------------------+-----------------------------------------------------------------------------+---------------------------+
| Menu          | Options                        | Function                                                                    | Keyboard shortcut         |
+===============+================================+=============================================================================+===========================+
| **Help**      | What is this ?                 | Enquires main menu options                                                  | ``Shift + F1``            | 
+               +--------------------------------+-----------------------------------------------------------------------------+---------------------------+
|               | About QElectroTech             | Displays information about authors, contributors, translators and Licensing |                           |
+               +--------------------------------+-----------------------------------------------------------------------------+---------------------------+
|               | About Qt                       | Displays information about Qt, a C++ toolkit for cross platform applications|                           |
+---------------+--------------------------------+-----------------------------------------------------------------------------+---------------------------+

|

.. _Qt: https://www.qt.io/