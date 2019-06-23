.. _en/element/element_parts/line

====
Line
====

Create line
~~~~~~~~~~~

The line can only be added to the workspace by the tool bar.

    1. Select the icon |icon_line| from the toolbar to add a line.
    2. Click on the initial point from the line at the workspace.
    3. Click on the end point from the line at the workspace.

.. |icon_line| image:: graphics/qet_line_icon.png

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Parts**.

Line properties
~~~~~~~~~~~~~~~

The properties from every element part can only be displayed at the properties panel when the part is 
selected.

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: graphics/qet_element_line.png
   :align: center

   Figure: QElectroTech line part from element

QElectroTech allows customizing different line properties:

:Appearence:

    :Color:

        The outline color and the filling color of the part can be defined from a list of 
        pre-defined colors. At the case of the line part the filling color is **None**.

    :Style:

        The type of outline representation can be choosed from the following options: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The thikness (Weight) from the outline can be choosed between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Coordenates:

        The coordinates (x, y) from the start point and end point can be defined.

    :End point:

        The extrem point from the line can be represented individually as:

        :Normal:
            The extrem point is represented as the rest of the line, there is no different representation 
            for the end point.
        :Simple arrow:
            The extrem point is represented as a filled arrow.
        :Triangle arrow:
            The extrem point is represented as an empty triangle arrow.
        :Circle:
            The extrem point is represented as an empty circle.
        :Diamond:
            The extrem point is represented as an empty diamond.