.. _element/element_parts/rectangle:

=========
Rectangle
=========

Create rectangle
################

The rectangle can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_rectangle| from `toolbar`_ to add a rectangle.
    2. Click on the initial vertex from the rectangle in the `workspace`_.
    3. Click on the end vertex from the rectangle in the `workspace`_.

.. |icon_rectangle| image:: /_external/_images/_site-assets/user/ico/22x22/rectangle.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Rectangle properties
####################

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_rectangle.png
   :align: center

   Figure: QElectroTech rectangle part from element

QElectroTech allows customizing different rectangle properties:

:Appearence:

    :Color:

        The outline and filling color of the part can be defined from a list of 
        pre-defined colors.

    :Style:

        The type of outline representation can be chosen between: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The outline thickness (Weight) can be chosen between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Coordenates:

        The upper left vertice coordinates (x, y) can be defined.

    :Dimensions:

        The width and the height of the rectangle can be defined. The tangent point at the vertical 
        and horizontal edges can also be defined at the case that round verteg is desired. 

Rounding rectangle vertices
###########################

QElectroTech allows rounding the rectangle vertices from `information panel`_ or `workspace`_.

.. figure:: /_external/_images/en/qet_element/qet_element_part_rectangle_rounded.png
   :align: center

   Figure: QElectroTech rectangle part from element

Rounding rectangle vertices from information panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the rectangle to display the rectangle properties at `information panel`_.
    2. Define the distance between the vertice and the intersection point at the vertical edges.
    3. Define the distance between the vertice and the intersection point at the horizontal edges.
    4. Press intro.
    5. **Select none** from **Edit** menu or use ``Ctrl + Shift + a`` keyboard shortcut.

Rounding rectangle vertices from workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the rectangle drawn at `workspace`_. The rectangle outlines change to red color and the vertices and middle edge point to blue.
    2. Select the rectangle again. The outlines continue in red and the points change to green color.
    3. Select the rectangle for third time. The outlines continue in red and only one vertex is displayed, the color is pink.
    4. Displace the pink points arround the horizontal and vertical edge.
    5. **Select none** from **Edit** menu or use ``Ctrl + Shift + a`` keyboard shortcut.


.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html
