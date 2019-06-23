.. _en/schema/basics/polygon

===========================
Working with polygons
===========================

Create polygon
###############

.. note::

    To draw more easily, the folio grid can be displayed from **Display > Display the grid** or 
    from the tool bar icon |icon_grid|. 

The polygon can only be added to the workspace by the tool bar.

    1. Select the icon |icon_polygon| from the toolbar to add a polygon.
    2. Draw connected lines by simple click on the beginning and end point from each line.
    3. Doble Click on the end vertex/point from the polygon at the workspace.

.. |icon_grid| image:: graphics/qet_grid_icon.png
.. |icon_polygon| image:: graphics/qet_polygon_icon.png

.. note::

   At everytime from the polygon creation, the previous line can be deleted without stopping the creation 
   process. Right click will delete the previous line without losing all the work.

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Add**.

Polygon properties
##################

The QElectroTech polygon is not necessarily a poligon, the polygon tools allows creating polygons and 
poly-lines, group of lines connected.

The poly-line is asimilated to a line and the customization posibilities are the same than a line. The 
initial point and the end point can or cannot be the same point. Please refers to the 
:ref:`Line properties` section for more information.

At the case that a closed polygon is desired, the **Closed polygon** check button from the polygon 
properties panel should be selected. At that case,QElectroTech allows the same type of customization 
than on a rectangle. Please refers to the :ref:`Rectangle properties` section for more information.

.. note::

   The a closed polygon is desired but the initial point and the end point are not the same, QElectroTech 
   will create automatically one new line to close the polygon.

The polygon properties can be displayed from the Menu bar, by right click on one polygon edge/line, 
from selection properties panel and using keyboard shortcut.

Polygon properties from Menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select one of the edges/lines from the polygon which should be edited.
    2. Select **Edit > Edit the selected object** menu item to display the polygon properties PopUP window.

.. figure:: graphics/qet_menu_edit.png
   :align: center

   Figure: QElectroTech Edit menu

Polygon properties by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Right click on one of the edges/lines from the polygon which should be edited.
    2. Select the option **Edit the selected object** to display the polygon properties PopUP window.

.. figure:: graphics/qet_polygon_right_click_line.png
   :align: center

   Figure: QElectroTech polygon selection PopUP window

Polygon properties from selection properties panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select one of the edges/lines from the polygon which should be edited and the properties from the polygon will appear at the selection properties panel.

.. figure:: graphics/qet_polygon_prop.png
   :align: center

   Figure: QElectroTech Polygon properties panel

.. note::

   If the properties panel is not displayed, it can be displayed from **Settings > Display > Selection properties**

Polygon properties using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech allows using keyboard shortcut to increase the working efficiency.

    1. Select one of the edges/lines from the polygon which should be edited.
    2. Press ``Ctrl + e`` to display the polygon properties PopUP window.

.. seealso::

    For more information about QElectroTech keyboard shortcut, please refers to `Menu bar <../../interface/menubar.html>`_ section.

Add new point to polygon
########################

    1. Right click on the place from the edges/lines of the polygon where the new porint should be created.
    2. Select the option **Add a point** to create the new point at the polygon.

.. figure:: graphics/qet_polygon_right_click_line.png
   :align: center

   Figure: QElectroTech polygon selection PopUP window

Delete point to polygon
#######################

    1. Right click on the point from the polygon which should be deleted.
    2. Select the option **Delete this point** to delete the point from the polygon.

.. figure:: graphics/qet_polygon_right_click_point.png
   :align: center

   Figure: QElectroTech polygon selection PopUP window