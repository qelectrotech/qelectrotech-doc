.. _element/element_parts/polygon:

=======
Polygon
=======

Create polygon
~~~~~~~~~~~~~~

The polygon can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_polygon| from `toolbar`_ to add a polygon.
    2. Click on the initial point from the polygon in the `workspace`_.
    3. Click on the rest of point from the polygon in the `workspace`_.
    4. Doble click on the end position of the polygon to finish the polygon edition.

.. |icon_polygon| image:: /_external/_images/_site-assets/user/ico/22x22/polygon.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Polygon properties
~~~~~~~~~~~~~~~~~~

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_polygon.png
   :align: center

   Figure: QElectroTech polygon part from element

QElectroTech allows customizing different polygon properties:

:Appearence:

    :Color:

        The outline and filling color of the part can be defined from a list of 
        pre-defined colors. At the case of an open polygon part the filling color is **None**.

    :Style:

        The outline representation type can be chosen between: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The outline thickness (Weight) can be chosen between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Type of polygon:

        QElectroTech has two different types of polygons, open polygon which is assimilated to a 
        group of connected lines and close polygon which is assimilated to closed geometry as the 
        rectangle.
    
    :Coordenates:

        The polygon points coordinates (x, y) can be defined and storaged in a list.

.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html