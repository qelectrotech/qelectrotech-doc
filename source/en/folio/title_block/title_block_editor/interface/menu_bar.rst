.. _en/folio/title_block/title_block_editor/interface/menu_bar

===========================
Title block editor Menu bar
===========================

The framework and widget toolkit `Qt`_ allows the design of drop-down menus. The drop-down menus 
are a characteristic graphical control element from the desktop applications. Each of the drop-down 
menus contains a number of options to initiate an action. The Menu bar is placed at top from the main 
windows. The figure bellow shows how the menu bar from QElectroTech looks.

.. figure:: graphics/qet_titleblock_editor_menu_nar.png
   :align: center

   Figure: QElectroTech Element editor Menu bar

As is showed at the figure, QElectroTech Title block editor bar contains the Menus ``File``, ``Edit``, 
``Display``, ``Settings`` and ``Help``. 

|

+------------+------------------+------------------------------------------------------------------+---------------------------+----------------+
| Menu       | Options          | Function                                                         | Keyboard shortcut         | Toolbar icon   |
+============+==================+==================================================================+===========================+================+
| **File**   | New              | Creates a new Title Block                                        |   ``Ctrl + n``            | |icon_new|     |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Open             | Opens an existing Title Block from a library                     |   ``Ctrl + o``            | |icon_open|    |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Open from a file | Opens an existing Title Block from the disk                      |   ``Ctrl + Shift + o``    |                |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Save             | Saves the current Title Block changes (overwrites)               |   ``Ctrl + s``            | |icon_save|    |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Save as          | Saves the Title Block as a new Title Block from a library        |                           | |icon_save_as| |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Save to a file   | Saves the Title Block as a different file on disk                |   ``Ctrl + Shift + s``    |                |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------+
|            | Quit             |  Quits QElectroTech Title Block editor                           | ``Ctrl + q``/ ``Alt + F4``|                |
+------------+------------------+------------------------------------------------------------------+---------------------------+----------------+

|

+--------------+---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
| Menu         | Options                   | Function                                                     | Keyboard shortcut         | Toolbar icon      |
+==============+===========================+==============================================================+===========================+===================+
| **Edit**     |  Undo                     | Undo the last action at Title Block editor                   |  ``Ctrl + z``             | |icon_undo|       |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Redo                     | Recovers the last undo action at Title Block editor          |  ``Ctrl + y``             | |icon_redo|       |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Cut                      | Equivalent to copy + delete the cell content and properties  |  ``Ctrl + x``             |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Copy                     | Copies the content and properties from the selected cell     |  ``Ctrl + c``             |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Paste                    | Pastes the cell content and properties from last copy or cut |  ``Ctrl + v``             |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Add a row                | Adds an additional row to the Title Block                    |                           |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Add a column             | Adds an additional column to the Title Block                 |                           |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Merge cells              | Merges the selected cells                                    |  ``Ctrl + j``             | |icon_merge|      |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Split cells              | Splits the selected cells previously merged                  |  ``Ctrl + k``             | |icon_split|      |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Manage logos             | Displays the logos manager PopUp window                      |  ``Ctrl + t``             |                   |
+              +---------------------------+--------------------------------------------------------------+---------------------------+-------------------+
|              |  Edit extra information   | Displays the extra information PopUp window                  |                           |                   |
+--------------+---------------------------+--------------------------------------------------------------+---------------------------+-------------------+

|

+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+-------------------+
| Menu           | Options                        | Function                                                                                   | Keyboard shortcut      | Toolbar icon      |
+================+================================+============================================================================================+========================+===================+
| **Display**    | Zoom In                        | Magnify the Title Block for a closer view                                                  |  ``Ctrl + +``          | |icon_zoom_in|    |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+-------------------+
|                | Zoom Out                       | Reduce magnification of the Title Block; develops a distant view of the Title Block        |  ``Ctrl + -``          | |icon_zoom_out|   |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+-------------------+
|                | Fit in view                    | Define zoom level to fit the Title Block at workspace                                      |  ``Ctrl + 9``          ||icon_fit_in_view| |
+                +--------------------------------+--------------------------------------------------------------------------------------------+------------------------+-------------------+
|                | Reset zoom                     | Reset zoom levels to default value (zoom level just less than that of fit in view)         |  ``Ctrl + 0``          ||icon_reset_zoom|  |
+----------------+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+-------------------+

|

+---------------+--------------------------------+-------------------------------------------------+-------------------------------+--------------------------------------------------+-------------------+
| Menu          | Options                        | Function                                        | Keyboard shortcut             | Notes                                            | Toolbar icon      |
+===============+================================+=================================================+===============================+==================================================+===================+
| **Settings**  | Display                        | Display or hide toolbars and panels             |                               | Hides or shows elements panel, tool bar etc.,    |                   |
+               +--------------------------------+-------------------------------------------------+-------------------------------+--------------------------------------------------+-------------------+
|               | Full screen mode               | Spreads the window to fill the screen           |  ``Ctrl + Shift + f``         | Entire screen gets occupied by the window        |                   |
+               +--------------------------------+-------------------------------------------------+-------------------------------+--------------------------------------------------+-------------------+
|               | Configure QElectroTech         | Display QElectroTech configure PopUp window     |                               |                                                  |                   |
+---------------+--------------------------------+-------------------------------------------------+-------------------------------+--------------------------------------------------+-------------------+

|

+---------------+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| Menu          | Options                             | Function                                                                              | Keyboard shortcut         | Toolbar icon      |
+===============+=====================================+=======================================================================================+===========================+===================+
| **Help**      | What's This?                        | Enquires main menu options                                                            | ``Shift + f1``            |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | About QElectroTech                  | Displays information about authors, contributors, translators and Licensing           |                           |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | Online manual                       | Opens the explorer and redirects to the official QElectroTech documentation           | ``f1``                    |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | Youtube channel                     | Opens the explorer and redirects to the official QElectroTech Youtube channel         |                           |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | Download a new version (dev)        | Opens the explorer and redirects to the official QElectroTech download link           |                           |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | Support the project with a donation | Opens the explorer and redirects to the official QElectroTech donation paypal account |                           |                   |
+               +-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
|               | About Qt                            | Displays information about `Qt`_, a C++ toolkit for cross platform applications       |                           |                   |
+---------------+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+

.. _Qt: https://www.qt.io/

.. |icon_new| image:: graphics/qet_new_icon.png
.. |icon_open| image:: graphics/qet_editor_open_icon.png
.. |icon_save| image:: graphics/qet_toolbar_save.png
.. |icon_save_as| image:: graphics/qet_toolbar_save_as.png
.. |icon_undo| image:: graphics/qet_undo_icon.png
.. |icon_redo| image:: graphics/qet_redo_icon.png
.. |icon_merge| image:: graphics/qet_merge_cells_icon.png
.. |icon_split| image:: graphics/qet_split_cells_icon.png
.. |icon_zoom_in| image:: graphics/qet_zoom_in_icon.png
.. |icon_zoom_out| image:: graphics/qet_zoom_out_icon.png
.. |icon_fit_in_view| image:: graphics/qet_fit_in_view_icon.png
.. |icon_reset_zoom| image:: graphics/qet_reset_zoom_icon.png