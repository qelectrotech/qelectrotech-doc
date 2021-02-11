.. _element/element_editor/interface/menu_bar

=======================
Element editor menu bar
=======================

The menu bar is placed at top from element editor window. The element editor contains the 
menus ``File``, ``Edit``, ``Display``, ``Settings``, and ``Help``. Each menu provides many 
diferent options.  

.. note::

    A brief description of each menu option can be read from `help or information tool bar`_ by hovering over the option with the cursor.

File menu
~~~~~~~~~~

.. figure:: ../../../images/qet_element_editor_menu_file.png
   :align: center

   Figure: QElectroTech file menu 

+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Option                                 | Function                                                                       | Keyboard shortcut         | Icon               |
+========================================+================================================================================+===========================+====================+
| New                                    | Creates a new element                                                          |   ``Ctrl + n``            | |document-new|     |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Open                                   | Opens an existing element from collection                                      |   ``Ctrl + o``            | |folder-open|      |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Open from a file                       | Opens an existing element from file                                            |   ``Ctrl + o``            | |folder-open|      |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Starting the DXF converter pluging     | Import element from DXF file                                                   |   ``Ctrl + o``            | |run-dxf|          |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Recently opened                        | Open an element from history (recently opened files)                           |   ``Ctrl + s``            | |document-recent|  |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Save                                   | Saves the current element changes (overwrites)                                 |   ``Ctrl + s``            | |document-save|    |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Save as                                | Saves the element as a new element from a library                              |                           | |document-save-as| |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Save to a file                         | Saves the Element as a different file on disk                                  |   ``Ctrl + Shift + x``    | |document-save-as| | 
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Reload                                 | Reloads the opened element (all changes which are not saved are lost)          |   ``Ctrl + p``            | |view-refresh|     |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Quit                                   | Quits QElectroTech Element editor                                              |       ``Ctrl + q``        | |application-exit| |
+----------------------------------------+--------------------------------------------------------------------------------+---------------------------+--------------------+

Edit menu
~~~~~~~~~~

.. figure:: ../../../images/qet_element_editor_menu_edit.png
   :align: center

   Figure: QElectroTech edit menu 

+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
| Option                                     | Function                                                    | Keyboard shortcut         | Icon                  |
+============================================+=============================================================+===========================+=======================+
|  Undo                                      | Undoes the previous action                                  |  ``Ctrl + z``             | |edit-undo|           |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Redo                                      | Restores the undone action                                  |  ``Ctrl + y``             | |edit-redo|           |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Select All                                | Selects all elments on the folio                            |  ``Ctrl + a``             | |edit-select-all|     |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Select none                               | Deselect all elments on the folio                           |  ``Ctrl + Shift + a``     | |edit-select-none|    |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Invert selection                          | Inverts selection of elements                               |  ``Ctrl + i``             | |edit-select-invert|  |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Cut                                       | Puts selected elements into the clipboard                   |  ``Ctrl + x``             | |edit-cut|            |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Copy                                      | Copies selected elements                                    |  ``Ctrl + c``             | |edit-copy|           |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Paste                                     | Pastes elements from the clipboard into the folio           |  ``Ctrl + v``             | |edit-paste|          |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Paste in the area                         | Pastes elements from the clipboard into the folio           |  ``Ctrl + v``             | |edit-paste|          |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Paste from                                | Pastes elements from the clipboard into the folio           |  ``Ctrl + v``             | |edit-paste|          |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Delete                                    | Removes selected elements from the folio                    |  ``Del``                  | |edit-delete|         |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Edit name and information of the element  | Rotates selected elements and texts                         |  ``Space``                | |names|               |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Edit author information                   | Rotates selected texts to a specific angle                  |  ``Ctrl + Space``         | |preferences-user|    |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Edit element properties                   | Finds the selected element in the collections panel         |                           | |element-edit|        |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Bring to front                            | Brings the selection (s) to front                           |  ``Ctrl + Shift + Home``  | |bring_forward|       |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Raise                                     | Aproachs the selection (s)                                  |  ``Ctrl + Shift + Up``    | |raise|               |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Lower                                     | Moves away the selection (s)                                |  ``Ctrl + Shift + Down``  | |lower|               |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+
|  Send backwards                            | Sends in the backwards the selection (s)                    |  ``Ctrl + Shift + End``   | |send_backward|       |
+--------------------------------------------+-------------------------------------------------------------+---------------------------+-----------------------+

Display menu
~~~~~~~~~~~~

.. figure:: ../../../images/qet_element_editor_menu_display.png
   :align: center

   Figure: QElectroTech display menu 

+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Option                         | Function                                                                                   | Keyboard shortcut      |Icon                  |
+================================+============================================================================================+========================+======================+
| Zoom In                        | Expands the workspace                                                                      |  ``Ctrl + +``          | |zoom-in|            |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Zoom Out                       | Shrinks the workspace                                                                      |  ``Ctrl + -``          | |zoom-out|           |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Fit in view                    | Adjusts the zoom on exactly trhe part of the workspace                                     |  ``Ctrl + 9``          | |view-fit-window|    |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Reset zoom                     | Restores default zoom level                                                                |  ``Ctrl + 0``          | |zoom-original|      |
+--------------------------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+

Settings menu
~~~~~~~~~~~~~

.. figure:: ../../../images/qet_menu_settings.png
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

Help menu
~~~~~~~~~

.. figure:: ../../../images/qet_menu_help.png
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

.. _Help or Information tool bar: ../../../element/element_editor/interface/help_bar.html

.. |document-new| image:: ../../../images/ico/22x22/document-new.png
.. |folder-open| image:: ../../../images/ico/22x22/folder-open.png
.. |run-dxf| image:: ../../../images/ico/16x16/run-dxf.png
.. |document-recent| image:: ../../../images/ico/22x22/document-open-recent.png
.. |document-save| image:: ../../../images/ico/22x22/document-save.png
.. |document-save-as| image:: ../../../images/ico/22x22/document-save-as.png
.. |project-close| image:: ../../../images/ico/22x22/project-close.png
.. |document-export| image:: ../../../images/ico/22x22/document-export.png
.. |view-refresh| image:: ../../../images/ico/22x22/view-refresh.png
.. |application-exit| image:: ../../../images/ico/22x22/application-exit.png
.. |edit-undo| image:: ../../../images/ico/22x22/edit-undo.png
.. |edit-redo| image:: ../../../images/ico/22x22/edit-redo.png
.. |edit-cut| image:: ../../../images/ico/22x22/edit-cut.png
.. |edit-copy| image:: ../../../images/ico/22x22/edit-copy.png
.. |edit-paste| image:: ../../../images/ico/22x22/edit-paste.png
.. |edit-select-all| image:: ../../../images/ico/22x22/edit-select-all.png
.. |edit-select-none| image:: ../../../images/ico/16x16/edit-select-none.png
.. |edit-select-invert| image:: ../../../images/ico/16x16/edit-select-invert.png
.. |edit-delete| image:: ../../../images/ico/22x22/edit-delete.png
.. |names| image:: ../../../images/ico/22x22/names.png
.. |preferences-user| image:: ../../../images/ico/22x22/preferences-desktop-user.png
.. |element-edit| image:: ../../../images/ico/22x22/element-edit.png
.. |bring_forward| image:: ../../../images/ico/22x22/bring_forward.png
.. |raise| image:: ../../../images/ico/22x22/raise.png
.. |lower| image:: ../../../images/ico/22x22/lower.png
.. |send_backward| image:: ../../../images/ico/22x22/send_backward.png
.. |zoom-in| image:: ../../../images/ico/16x16/zoom-in.png
.. |zoom-out| image:: ../../../images/ico/16x16/zoom-out.png
.. |view-fit-window| image:: ../../../images/ico/22x22/view-fit-window.png
.. |zoom-original| image:: ../../../images/ico/22x22/zoom-original.png
.. |configure-toolbars| image:: ../../../images/ico/16x16/configure-toolbars.png
.. |view-fullscreen| image:: ../../../images/ico/16x16/view-fullscreen.png
.. |configure| image:: ../../../images/ico/16x16/configure.png
.. |qet-icon| image:: ../../../images/ico/16x16/qet.png
.. |help-contents| image:: ../../../images/ico/16x16/help-contents.png
.. |show-video| image:: ../../../images/ico/16x16/kdenlive-show-video.png
.. |help-donate| image:: ../../../images/ico/16x16/help-donate.png
.. |qt-icon| image:: ../../../images/ico/16x16/qt.png