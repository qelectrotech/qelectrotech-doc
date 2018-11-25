.. _en/element/elementeditor/elementparts/polygon

=======
Polygon
=======

Create polygon
~~~~~~~~~~~~~~

The polygon can only be added to the workspace by the tool bar.

    1. Select the icon |icon_polygon| from the toolbar to add a polygon.
    2. Click on the initial point from the polygon at the workspace.
    3. Click on the rest of point from the polygon at the workspace.
    4. Doble click on the end position of the polygon to finish the polygon edition.

.. |icon_polygon| image:: graphics/qet_polygon_icon.png

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Parts**.

Polygon properties
~~~~~~~~~~~~~~~~~~

The properties from every element part can only be displayed at the properties panel when the part is 
selected.

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: graphics/qet_element_polygon.png
   :align: center

   Figure: QElectroTech polygon part from element

QElectroTech allows customizing different polygon properties:

:Appearence:

    :Color:

        The outline color and the filling color of the part can be defined from a list of 
        pre-defined colors. At the case of an open polygon part the filling color is **None**.

    :Style:

        The type of outline representation can be choosed from the following options: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The thikness (Weight) from the outline can be choosed between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Type of polygon:

        QElectroTech has two different types of polygons, open polygon which is assimilaed to a 
        group of connected lines and close polygon which is asimilated to closed geometry as the 
        rectangle.
    
    :Coordenates:

        The coordinates (x, y) from all polygon point can be defined and are storaged at a list.