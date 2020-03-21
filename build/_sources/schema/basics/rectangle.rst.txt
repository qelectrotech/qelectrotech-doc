.. _schema/basics/rectangle

==========
Rectangle
==========

Create rectangle
###################

.. note::

    To draw more easily, the folio grid can be displayed from **Display > Display the grid** or from `toolbar`_ icon |grid|. 

The rectangle can only be added to the `workspace`_ by `toolbar`_.

    1. Select the icon |rectangle| from `toolbar`_ to add a rectangle.
    2. Click on the initial vertix from the rectangle.
    3. Click on the end vertex from the rectangle.

.. |grid| image:: ../../images/ico/22x22/grid.png
.. |rectangle| image:: ../../images/ico/22x22/rectangle.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Add**.

Rectangle properties
#######################

The edges and the internal area from the triangle can be costumized at QElectroTech.   

    * The edges from a rectangle have the same properties as a `line`_.
    * The type of filling for closed primitive objects (rectangle, ellipse and closed polygon) are: **None**, **Solid line** and some types of grids.

        .. figure:: ../../images/qet_close_primitive_object_filling.png
            :align: center

            Figure: QElectroTech Color selection PopUP window

    * The possible filling colors are defined by the `RGB scale range`_.

.. note::

    The position from the rectangle can be locked to prevent involuntary movement. 
        
        * Go to rectangle properties and check the **Lock position** button.

The rectangle properties can be displayed from `menu bar`_, by right click on one rectangle edge, 
from selection properties panel and using keyboard shortcut.

Rectangle properties from menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select one of the edges from the rectangle which should be edited.
    2. Select **Edit > Edit the selected object** menu item to display the rectangle properties PopUP window.

        .. figure:: ../../images/qet_menu_edit_object.png
            :align: center

            Figure: QElectroTech edit menu

Rectangle properties by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Right click on one of the edges from the rectangle which should be edited.
    2. Select the option **Edit the selected object** to display the rectangle properties PopUP window.

.. figure:: ../../images/qet_object_right_click.png
   :align: center

   Figure: QElectroTech rectangle selection PopUP window

Rectangle properties from selection properties panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select one of the edges from the rectangle which should be edited and the properties from the rectangle will appear at `selection properties panel`_.

.. figure:: ../../images/qet_close_primitive_object_prop.png
   :align: center

   Figure: QElectroTech Rectangle properties panel

.. note::

   If the `selection properties panel`_ is not displayed, it can be displayed from **Settings > Display > Selection properties**

Rectangle properties using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech allows using keyboard shortcut to increase the working efficiency.

    1. Select one of the edges from the rectangle which should be edited.
    2. Press ``Ctrl + e`` to display the rectangle properties PopUP window.

.. seealso::

    For more information about QElectroTech keyboard shortcuts, refer to `menu bar`_ section.

.. _menu bar: ../../interface/menu_bar.html
.. _workspace: ../../interface/workspace.html
.. _toolbar: ../../interface/toolbars.html
.. _line: ../../schema/basics/line.html
.. _selection properties panel: ../../interface/panels/selection_properties_panel.html
.. _RGB scale range: ../../annex/color.html
