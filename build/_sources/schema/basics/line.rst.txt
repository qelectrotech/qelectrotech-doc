.. _schema/basics/line

=====
Line
=====

Create line
###########

.. note::

    To draw more easily, the folio grid can be displayed from **Display > Display the grid** or from `toolbar`_ icon |grid|. 

A line can only be added to the `workspace`_ by `toolbar`_.

    1. Select the icon |line| from `toolbar`_ to add a line.
    2. Click on the initial point from the line.
    3. Click on the end point from the line.

.. |grid| image:: ../../images/ico/22x22/grid.png
.. |line| image:: ../../images/ico/22x22/line.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Add**.

Line properties
###############

QElectroTech allows customizing the type of line, the thikness from the line and the color of the line. 

    * The different types of lines are: **normal**, **dashed**, **dotted**, **dots and dasches**, **dash dot dot** and **custom dash line**.

        .. figure:: ../../images/qet_line_type.png
            :align: center

            Figure: QElectroTech Color selection PopUP window

    * The possible line thiknes are between 0.2 and 50 mm (0.2, 0.4, 0.8, 0.6, 0.8, 1, 1.2, 1.4, ... , 50).
    * The possible colors are defined by the `RGB scale range`_.

.. note::

    The position from the line can be locked to prevent involuntary movement. 
        
        * Go to line properties and check the **Lock position** button.

The line properties can be displayed from `menu bar`_, by right click on the line, from selection 
properties panel and using keyboard shortcut.

Line properties from menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the line which should be edited.
    2. Select **Edit > Edit the selected object** menu item to display the line properties PopUP window.

        .. figure:: ../../images/qet_menu_edit_object.png
            :align: center

            Figure: QElectroTech edit menu

Line properties by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Right click on the line which should be edited.
    2. Select the option **Edit the selected object** to display the line properties PopUP window.

.. figure:: ../../images/qet_object_right_click.png
   :align: center

   Figure: QElectroTech line selection PopUP window

Line properties from selection properties panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the line which should be edited and the properties from the line will appear at `selection properties panel`_.

.. figure:: ../../images/qet_line_prop.png
   :align: center

   Figure: QElectroTech Line properties panel

.. note::

   If the `selection properties panel`_ is not displayed, it can be displayed from **Settings > Display > Selection properties**

Line properties using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech allows using keyboard shortcut to increase the working efficiency.

    1. Select the line which should be edited.
    2. Press ``Ctrl + e`` to display the line properties PopUP window.

.. seealso::

    For more information about QElectroTech keyboard shortcuts, refer to `menu bar`_ section.

.. _menu bar: ../../interface/menu_bar.html
.. _workspace: ../../interface/workspace.html
.. _toolbar: ../../interface/toolbars.html
.. _selection properties panel: ../../interface/panels/selection_properties_panel.html
.. _RGB scale range: ../../annex/color.html
