.. _element/element_editor/interface/toolbars:

=======================
Element editor toolbars
=======================

In addition to the different menus, QElectroTech provides also toolbars. The toolbars are groups 
of buttons with icons which initiate an accion. In general, these buttons have its counterpart at one of 
the menus from the `menu bar`_.

The different toolbars can be hidden or placed in one or more rows below the `menu bar`_. The toolbars 
can also be placed on column at the left or right side from the main window.

.. note::

   To help the user, a tooltip is displayed when the arrow is placed on each button.

Toolbar Tools
~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_element/qet_element_editor_toolbar_tools.png
   :align: center

   Figure: QElectroTech element editor toolbar Tools 

The different buttons from toolbar **Tools** are: 

+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Tool          | Function                                                                       | Keyboard shortcut         | Icon               |
+===============+================================================================================+===========================+====================+
| New           | Creates a new element                                                          |   ``Ctrl + n``            | |document-new|     |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Open          | Opens an existing element from collection                                      |   ``Ctrl + o``            | |folder-open|      |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Save          | Saves the current element changes (overwrites)                                 |   ``Ctrl + s``            | |document-save|    |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Save as       | Saves the element as a new element from a library                              |                           | |document-save-as| |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
| Reload        | Reloads the opened element (all changes which are not saved are lost)          |   ``Ctrl + p``            | |view-refresh|     |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
|  Undo         | Undoes the previous action                                                     |  ``Ctrl + z``             | |edit-undo|        |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
|  Redo         | Restores the undone action                                                     |  ``Ctrl + y``             | |edit-redo|        |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+
|  Delete       | Removes selected elements from the folio                                       |  ``Del``                  | |edit-delete|      |
+---------------+--------------------------------------------------------------------------------+---------------------------+--------------------+


.. note::

   Select **Settings > Display > Tools** menu item to display or hidden the toolbar **Tools**.

Toolbar Display
~~~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_element/qet_element_editor_toolbar_display.png
   :align: center

   Figure: QElectroTech element editor toolbar Display

The different buttons from toolbar **Display** are:

+----------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Tool           | Function                                                                                   | Keyboard shortcut      | Icon                 |
+================+============================================================================================+========================+======================+
| Fit in view    | Adjusts the zoom on exactly the part of the workspace                                      |  ``Ctrl + 9``          | |view-fit-window|    |
+----------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+
| Reset zoom     | Restores default zoom level                                                                |  ``Ctrl + 0``          | |zoom-original|      |
+----------------+--------------------------------------------------------------------------------------------+------------------------+----------------------+

.. note::

   Select **Settings > Display > Display** menu item to display or hidden the toolbar **Display**.

Toolbar Element
~~~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_element/qet_element_editor_toolbar_element.png
   :align: center

   Figure: QElectroTech element editor toolbar Element

The different buttons from toolbar **Element** are:

+--------------+--------------------------------------------------------+---------------------------+-------------------+
| Tool         | Function                                               | Keyboard shortcut         | Icon              |
+==============+========================================================+===========================+===================+
| Information  | Edit name and information of the element               |  ``Ctrl + e``             | |names|           |
+--------------+--------------------------------------------------------+---------------------------+-------------------+
| Properties   | Edit element properties                                |                           | |element-edit|    |
+--------------+--------------------------------------------------------+---------------------------+-------------------+

.. note::

   Select **Settings > Display > Diagrams** menu item to display or hidden the toolbar **Element**.

Toolbar Parts
~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_element/qet_element_editor_toolbar_parts.png
   :align: center

   Figure: QElectroTech element editor toolbar Parts

The different buttons from toolbar **Parts** are:

+---------------+------------------------------------------------------+---------------------------+-------------------+
| Tool          | Function                                             | Keyboard shortcut         | Icon              |
+===============+======================================================+===========================+===================+
|  Line         | Add line to the workspace                            |                           | |line|            |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Rectangle    | Add rectangle to the workspace                       |                           | |rectangle|       |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Ellipse      | Add ellipse to the workspace                         |                           | |ellipse|         |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Polygon      | Add polygon to the workspace                         |                           | |polygon|         |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Text         | Add text field to the workspace                      |                           | |text|            |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Arc          | Add arc to the workspace                             |                           | |arc|             |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Terminal     | Add terminal to the workspace                        |                           | |terminal|        |
+---------------+------------------------------------------------------+---------------------------+-------------------+
|  Text field   | Add dynamic text field to the workspace              |                           | |textfield|       |
+---------------+------------------------------------------------------+---------------------------+-------------------+

.. note::

   Select **Settings > Display > Diagrams** menu item to display or hidden the toolbar **Parts**.

Toolbar Depth
~~~~~~~~~~~~~

.. figure:: /_external/_images/en/qet_element/qet_element_editor_toolbar_depth.png
   :align: center

   Figure: QElectroTech element editor toolbar Depth 

The different buttons from toolbar **Depth** are:

+---------------------+-----------------------------------------------------------+---------------------------+-------------------+
| Tool                | Function                                                  | Keyboard shortcut         | Icon              |
+=====================+===========================================================+===========================+===================+
|  Bring forward      | Brings the selection (s) to front                         |  ``Ctrl + shift + Home``  | |bring_forward|   |
+---------------------+-----------------------------------------------------------+---------------------------+-------------------+
|  Raise              | Aproachs the selection (s)                                |  ``Ctrl + shift + Up``    | |raise|           |
+---------------------+-----------------------------------------------------------+---------------------------+-------------------+
|  Lower              | Moves away the selection (s)                              |  ``Ctrl + shift + Down``  | |lower|           |
+---------------------+-----------------------------------------------------------+---------------------------+-------------------+
|  Send backwards     | Sends in the backwards the selection (s)                  |  ``Ctrl + shift + End``   | |send_backward|   |
+---------------------+-----------------------------------------------------------+---------------------------+-------------------+

.. note::

   Select **Settings > Display > Diagrams** menu item to display or hidden the toolbar **Depth**.

.. _menu bar: ../../../element/element_editor/interface/menu_bar.html

.. |document-new| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-new.png
.. |folder-open| image:: /_external/_images/_site-assets/user/ico/22x22/folder/folder-open.png
.. |document-save| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-save.png
.. |document-save-as| image:: /_external/_images/_site-assets/user/ico/22x22/document/document-save-as.png
.. |view-refresh| image:: /_external/_images/_site-assets/user/ico/22x22/view/view-refresh.png
.. |edit-undo| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-undo.png
.. |edit-redo| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-redo.png
.. |edit-delete| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-delete.png
.. |view-fit-window| image:: /_external/_images/_site-assets/user/ico/22x22/view/view-fit-window.png
.. |zoom-original| image:: /_external/_images/_site-assets/user/ico/22x22/zoom/zoom-original.png
.. |names| image:: /_external/_images/_site-assets/user/ico/22x22/names.png
.. |element-edit| image:: /_external/_images/_site-assets/user/ico/22x22/element/element-edit.png
.. |line| image:: /_external/_images/_site-assets/user/ico/22x22/line.png
.. |rectangle| image:: /_external/_images/_site-assets/user/ico/22x22/rectangle.png
.. |ellipse| image:: /_external/_images/_site-assets/user/ico/22x22/ellipse.png
.. |polygon| image:: /_external/_images/_site-assets/user/ico/22x22/polygon.png
.. |text| image:: /_external/_images/_site-assets/user/ico/22x22/text/text.png
.. |arc| image:: /_external/_images/_site-assets/user/ico/22x22/arc.png
.. |terminal| image:: /_external/_images/_site-assets/user/ico/22x22/terminal/terminal.png
.. |textfield| image:: /_external/_images/_site-assets/user/ico/22x22/textfield.png
.. |bring_forward| image:: /_external/_images/_site-assets/user/ico/22x22/bring_forward.png
.. |raise| image:: /_external/_images/_site-assets/user/ico/22x22/raise.png
.. |lower| image:: /_external/_images/_site-assets/user/ico/22x22/lower.png
.. |send_backward| image:: /_external/_images/_site-assets/user/ico/22x22/send_backward.png