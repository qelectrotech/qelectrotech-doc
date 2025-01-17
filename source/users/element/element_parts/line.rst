.. _element/element_parts/line:

====
Line
====

Create line
~~~~~~~~~~~

The line can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_line| from `toolbar`_ to add a line.
    2. Click on the initial point from the line in the `workspace`_.
    3. Click on the end point from the line in the `workspace`_.

.. |icon_line| image:: /_external/_images/_site-assets/user/ico/22x22/line.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Line properties
~~~~~~~~~~~~~~~

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_line.png
   :align: center

   Figure: QElectroTech line from element

QElectroTech allows customizing different line properties:

:Appearence:

    :Color:

        The outline and filling color of the part can be defined from a list of 
        pre-defined colors. At the case of the line part the filling color is **None**.

    :Style:

        The outline representation type can be chosen between: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The outline thickness (Weight) can be chosen between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Coordenates:

        The start and end point coordinates (x, y) can be defined.

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

.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html