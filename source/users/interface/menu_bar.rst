.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _interface/menu_bar:

========
Menu bar
========

The menu bar is placed at top from QElectroTech interface. QElectroTech contains the 
menus ``File``, ``Edit``, ``Project``, ``Display``, ``Settings``, ``Windows`` and 
``Help``. Each menu provides many diferent options.  

.. note::

    A brief description of each menu option can be read from `help or information tool bar`_ by hovering over the option with the cursor.

File menu
~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_file.png
   :align: center

   Figure: QElectroTech file menu 

+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Option           | Function                                                         | Keyboard shortcut         | Icon               |
+==================+==================================================================+===========================+====================+
| Latest files     | Opens a project from history (recently opened files)             |                           | |document-recent|  |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| New              | Creates a new Project                                            |   ``Ctrl + n``            | |project-new|      |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Open             | Opens an existing project                                        |   ``Ctrl + o``            | |project|          |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Save             | Saves the current project and all its folios                     |   ``Ctrl + s``            | |document-save|    |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Save as          | Saves the current project with a different file name             |                           | |document-save-as| |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Close            | Closes the current project                                       |   ``Ctrl + w``            | |project-close|    |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Export           | Exports the curret folio to another format                       |   ``Ctrl + Shift + x``    | |document-export|  | 
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Print            | Print one or more folio of the current project                   |   ``Ctrl + p``            | |document-print|   |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+
| Quit             | Closes QElectroTech                                              | ``Ctrl + q``/ ``Alt + F4``| |application-exit| |
+------------------+------------------------------------------------------------------+---------------------------+--------------------+

Edit menu
~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_edit.png
   :align: center

   Figure: QElectroTech edit menu 

+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
| Option                    | Function                                                    | Keyboard shortcut         | Icon                  |
+===========================+=============================================================+===========================+=======================+
|  Undo                     | Undoes the previous action                                  |  ``Ctrl + z``             | |edit-undo|           |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Redo                     | Restores the undone action                                  |  ``Ctrl + y``             | |edit-redo|           |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Cut                      | Puts selected elements into the clipboard                   |  ``Ctrl + x``             | |edit-cut|            |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Copy                     | Copies selected elements                                    |  ``Ctrl + c``             | |edit-copy|           |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Paste                    | Pastes elements from the clipboard into the folio           |  ``Ctrl + v``             | |edit-paste|          |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Select All               | Selects all elements on the folio                           |  ``Ctrl + a``             | |edit-select-all|     |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Select none              | Deselect all elements on the folio                          |  ``Ctrl + Shift + a``     | |edit-select-none|    |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Invert selection         | Inverts selection of elements                               |  ``Ctrl + i``             | |edit-select-invert|  |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Delete                   | Removes selected elements from the folio                    |  ``Del``                  | |edit-delete|         |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Rotate                   | Rotates selected elements and texts                         |  ``Space``                | |transform-rotate|    |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Choose texts orientation | Rotates selected texts to a specific angle                  |  ``Ctrl + Space``         | |object-rotate-right| |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Find in the panel        | Finds the selected element in the collections panel         |                           | |zoom-draw|           |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Edit the selected object | Displays properties for the selected element / conductor    |  ``Ctrl + e``             | |element-edit|        |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Group selected texts     |                                                             |                           |                       |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Reset conductors         | Resets the conductors path ignoring the user changes        |  ``Ctrl + k``             | |conductor-reset|     |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Folio properties         | Edits the properties of the folio                           |  ``Ctrl + l``             | |folio-properties|    |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Add a column             | Adds a column to the folio                                  |                           | |insert-column-right| |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Remove a column          | Removes a column from the folio                             |                           | |delete-column|       |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Add a row                | Adds a row to the folio                                     |                           | |insert-row-under|    |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Remove a row             | Removes a row from the folio                                |                           | |delete-row|          |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Bring to front           | Brings the selection (s) to front                           |  ``Ctrl + Shift + Home``  | |bring_forward|       |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Raise                    | Aproachs the selection (s)                                  |  ``Ctrl + Shift + Up``    | |raise|               |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Lower                    | Moves away the selection (s)                                |  ``Ctrl + Shift + Down``  | |lower|               |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Send backwards           | Sends in the backwards the selection (s)                    |  ``Ctrl + Shift + End``   | |send_backward|       |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Search / Replace         | Display Search / Replace panel                              |  ``Ctrl + f``             |                       |
+---------------------------+-------------------------------------------------------------+---------------------------+-----------------------+

Project menu
~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_project.png
   :align: center

   Figure: QElectroTech project menu 

+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Option                                     | Function                                                                                                                    | Keyboard shortcut      | Icon                  |
+============================================+=============================================================================================================================+========================+=======================+
| Project properties                         | Display project properties PopUp window                                                                                     |                        | |project-properties|  |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Add a folio                                | Adds a new folio (drawing sheet) to the active project.                                                                     |  ``Ctrl + t``          | |folio-new|           |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Delete this folio                          | Deletes the active folio (drawing sheet) of the project                                                                     |                        | |folio-delete|        |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Clean project                              | Purges the active project of unused elements and empty categories and templates                                             |                        | |edit-clear|          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Add a summary                              | Creates an index table for the active project                                                                               |                        | |table-of-content|    |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Add a nomenclature                         | Creates a Bill Of Material (BOM) table for the active project                                                               |                        | |table-of-content|    |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Export to CSV                              | Generates a ``.csv`` file summary of elements used in the active project according to defined filtering options             |                        | |export-csv|          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Export the list of names of wires          | Generates a ``.csv`` file summary of conductors used in the active project                                                  |                        | |export-csv|          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Launch the terminal block creation pluging |                                                                                                                             |                        | |terminalstrip|       |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+
| Export the internal project database       | Generates a SQLite database of the active project                                                                           |                        | |export-csv|          |
+--------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------+------------------------+-----------------------+

Display menu
~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_display.png
   :align: center

   Figure: QElectroTech display menu 

+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Option                         | Function                                                                                   | Keyboard shortcut      |Icon                  |
+================================+============================================================================================+========================+======================+
| Display projects               | Shows the various opened projects in windows or tabs                                       |                        | |configure-toolbars| |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Select                         | Allows to select elements                                                                  |                        | |select|             |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Move                           | Allows to view the folio without modifying it                                              |                        | |move|               |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Display the grid               | Displays or hidden the grid of folio                                                       |                        | |grid|               |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Background color white / gray  | Displays the background color of the folio in white or gray                                |                        | |diagram_bg|         |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Zoom In                        | Expands the folio                                                                          |  ``Ctrl + +``          | |zoom-in|            |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Zoom Out                       | Shrinks the folio                                                                          |  ``Ctrl + -``          | |zoom-out|           |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Zoom content                   | Adjusts the zoom to display all the content of folio regardless of context                 |  ``Ctrl + 8``          | |zoom-draw|          |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Fit in view                    | Adjusts the zoom on exactly trhe part of the folio                                         |  ``Ctrl + 9``          | |view-fit-window|    |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Reset zoom                     | Restores default zoom level                                                                |  ``Ctrl + 0``          | |zoom-original|      |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+

Settings menu
~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_settings.png
   :align: center

   Figure: QElectroTech settings menu 

+--------------------------------+-----------------------------------------------------------+-------------------------------+----------------------+
| Option                         | Function                                                  | Keyboard shortcut             | Icon                 |
+================================+===========================================================+===============================+======================+
| Display                        | Displays or hides toolbars and panels                     |                               | |configure-toolbars| |
+--------------------------------+-----------------------------------------------------------+-------------------------------+----------------------+
| Full screen mode               | Displays QElectroTech in full screen mode                 |  ``Ctrl + Shift + f``         | |view-fullscreen|    |
+--------------------------------+-----------------------------------------------------------+-------------------------------+----------------------+
| Configure QElectroTech         | Allows specifying various parameters for QElectroTech     |                               | |configure|          |
+--------------------------------+-----------------------------------------------------------+-------------------------------+----------------------+

Windows menu
~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_windows.png
   :align: center

   Figure: QElectroTech windows menu 

+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| Option                         | Function                                                                                      | Keyboard shortcut             | Icon              |
+================================+===============================================================================================+===============================+===================+
| Close                          | Closes the current project                                                                    |  ``Ctrl + f4``                | |project-close|   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| Tile                           | Adds a new drawing sheet to the active project. (Folio means drawing sheet)                   |                               |                   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| Cascade                        | Deletes the active drawing of the project                                                     |                               |                   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| Next Project                   | Activates the next project                                                                    |  ``Ctrl + tab``               |                   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| Previous Project               | Activates the previous project                                                                |  ``Ctrl + Shift + Backtab``   |                   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+
| (Opened Projects)              | Below **Previous Project** QElectroTech list all opened projects to select the active project |                               |                   |
+--------------------------------+-----------------------------------------------------------------------------------------------+-------------------------------+-------------------+

Help menu
~~~~~~~~~

.. figure:: /_external/_images/en/qet_menu/qet_menu_help.png
   :align: center

   Figure: QElectroTech help menu 

+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| Option                              | Function                                                                              | Keyboard shortcut         | Icon              |
+=====================================+=======================================================================================+===========================+===================+
| What's This?                        | Enquires main menu options                                                            | ``Shift + f1``            |                   |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| About QElectroTech                  | Displays information about QElectroTech                                               |                           | |qet-icon|        |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| Online manual                       | Lauches the default browser to the online manual of QElectroTech                      | ``f1``                    | |help-contents|   |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| Youtube channel                     | Lauches the default browser on the Youtube channel of QElectroTech                    |                           | |show-video|      |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| Support the project with a donation | Lauches the default browser on the QElectroTech donation paypal account               |                           | |help-donate|     |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+
| About Qt                            | Displays information about `Qt`_ library                                              |                           | |qt-icon|         |
+-------------------------------------+---------------------------------------------------------------------------------------+---------------------------+-------------------+

.. _Qt: https://www.qt.io/

.. _Help or Information tool bar: .. _interface/help_bar:

.. |document-recent| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-open-recent.png
.. |project-new| image:: /_external/_images/_site-assets/user/ico/22x22/project/project-new.png
.. |project| image:: /_external/_images/_site-assets/user/ico/22x22/project/project.png
.. |document-save| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-save.png
.. |document-save-as| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-save-as.png
.. |project-close| image:: /_external/_images/_site-assets/user/ico/22x22/project/project-close.png
.. |document-export| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-export.png
.. |document-print| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-print.png
.. |application-exit| image:: /_external/_images/_site-assets/user/ico/22x22/application/application-exit.png
.. |edit-undo| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-undo.png
.. |edit-redo| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-redo.png
.. |edit-cut| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-cut.png
.. |edit-copy| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-copy.png
.. |edit-paste| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-paste.png
.. |edit-select-all| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-select-all.png
.. |edit-select-none| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-select-none.png
.. |edit-select-invert| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-select-invert.png
.. |edit-delete| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-delete.png
.. |transform-rotate| image:: /_external/_images/_site-assets/user/ico/16x16/transform-rotate.png
.. |object-rotate-right| image:: /_external/_images/_site-assets/user/ico/16x16/object/object-rotate-right.png
.. |element-edit| image:: /_external/_images/_site-assets/user/ico/16x16/element/element-edit.png
.. |conductor-reset| image:: /_external/_images/_site-assets/user/ico/16x16/conductor/conductor-reset.png
.. |folio-properties| image:: /_external/_images/_site-assets/user/ico/16x16/folio/folio-properties.png
.. |insert-column-right| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-table-insert-column-right.png
.. |delete-column| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-table-delete-column.png
.. |delete-row| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-table-delete-row.png
.. |insert-row-under| image:: /_external/_images/_site-assets/user/ico/16x16/edit/edit-table-insert-row-under.png
.. |bring_forward| image:: /_external/_images/_site-assets/user/ico/22x22/bring_forward.png
.. |raise| image:: /_external/_images/_site-assets/user/ico/22x22/raise.png
.. |lower| image:: /_external/_images/_site-assets/user/ico/22x22/lower.png
.. |send_backward| image:: /_external/_images/_site-assets/user/ico/22x22/send_backward.png
.. |project-properties| image:: /_external/_images/_site-assets/user/ico/16x16/project/project-properties.png
.. |folio-new| image:: /_external/_images/_site-assets/user/ico/16x16/folio/folio-new.png
.. |folio-delete| image:: /_external/_images/_site-assets/user/ico/16x16/folio/folio-delete.png
.. |edit-clear| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-clear.png
.. |table-of-content| image:: /_external/_images/_site-assets/user/ico/16x16/table-of-content.png
.. |export-csv| image:: /_external/_images/_site-assets/user/ico/22x22/export-csv.png
.. |terminalstrip| image:: /_external/_images/_site-assets/user/ico/22x22/terminal/terminalstrip.png
.. |select| image:: /_external/_images/_site-assets/user/ico/16x16/select.png
.. |move| image:: /_external/_images/_site-assets/user/ico/16x16/move.png
.. |grid| image:: /_external/_images/_site-assets/user/ico/16x16/grid.png
.. |diagram_bg| image:: /_external/_images/_site-assets/user/ico/22x22/diagram/diagram_bg.png
.. |zoom-in| image:: /_external/_images/_site-assets/user/ico/16x16/zoom/zoom-in.png
.. |zoom-out| image:: /_external/_images/_site-assets/user/ico/16x16/zoom/zoom-out.png
.. |zoom-draw| image:: /_external/_images/_site-assets/user/ico/22x22/zoom/zoom-draw.png
.. |view-fit-window| image:: /_external/_images/_site-assets/user/ico/22x22/view/view-fit-window.png
.. |zoom-original| image:: /_external/_images/_site-assets/user/ico/22x22/zoom/zoom-original.png
.. |configure-toolbars| image:: /_external/_images/_site-assets/user/ico/16x16/configure/configure-toolbars.png
.. |view-fullscreen| image:: /_external/_images/_site-assets/user/ico/16x16/view/view-fullscreen.png
.. |configure| image:: /_external/_images/_site-assets/user/ico/16x16/configure/configure.png
.. |qet-icon| image:: /_external/_images/_site-assets/user/ico/16x16/qet.png
.. |help-contents| image:: /_external/_images/_site-assets/user/ico/16x16/help/help-contents.png
.. |show-video| image:: /_external/_images/_site-assets/user/ico/16x16/kdenlive-show-video.png
.. |help-donate| image:: /_external/_images/_site-assets/user/ico/16x16/help/help-donate.png
.. |qt-icon| image:: /_external/_images/_site-assets/user/ico/16x16/qt.png
