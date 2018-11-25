.. _en/element/elementeditor/elementparts/rectangle

=========
Rectangle
=========

Create rectangle
################

The rectangle can only be added to the workspace by the tool bar.

    1. Select the icon |icon_rectangle| from the toolbar to add a line.
    2. Click on the initial point from the line at the workspace.
    3. Click on the end point from the line at the workspace.

.. |icon_rectangle| image:: graphics/qet_rectangle_icon.png

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Parts**.

Rectangle properties
####################

The properties from every element part can only be displayed at the properties panel when the part is 
selected.

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: graphics/qet_element_rectangle.png
   :align: center

   Figure: QElectroTech rectangle part from element

QElectroTech allows customizing different rectangle properties:

:Appearence:

    :Color:

        The outline color and the filling color of the part can be defined from a list of 
        pre-defined colors.

    :Style:

        The type of outline representation can be choosed from the following options: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The thikness (Weight) from the outline can be choosed between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Coordenates:

        The coordinates (x, y) from the upper left vertice can be defined.

    :Dimensions:

        The width and the height of the rectangle can be defined. The tangent point at the vertical 
        and horizontal edges can also be defined at the case that round verteg is desired. 

Rounding rectangle vertices
###########################

QElectroTech allows rounding the vertices from the rectangle at the information panel or at the workspace.

.. figure:: graphics/qet_element_rectangle_rounded.png
   :align: center

   Figure: QElectroTech rectangle part from element

Rounding rectangle vertices from information panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the rectangle to display the rectangle properties at the information panel.
    2. Define the distance between the vertice and the intersection point at the vertical edges.
    3. Define the distance between the vertice and the intersection point at the horizontal edges.
    4. Press intro.

Rounding rectangle vertices from workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the rectangle drawn at the workspace. The rectangle outlines change to red color and the vertices and middle edge point to blue.
    2. Select the rectangle again. The outlines continue in red and the points will change to green color.
    3. Select the rectable for third time. The outlines continue in red and at this time only one vertex is displaied, the color is pink.
    4. Displace the pink points arround the horizontal and vertice edge



