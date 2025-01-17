.. _element/element_parts/arc:

===
Arc
===


Create arc
##########

The arc can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_arc| from `toolbar`_ to add an arc.
    2. Click at the position from the start point of the arc in the `workspace`_.
    3. Click at the position from the end point of the arc in the `workspace`_. The default arc has always an angle of 90 degrees.

.. |icon_arc| image:: /_external/_images/_site-assets/user/ico/22x22/arc.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Arc properties
##############

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_arc.png
   :align: center

   Figure: QElectroTech arc part from element

QElectroTech allows customizing different arc properties:

:Appearence:

    :Color:

        The outline color and the filling color of the part can be defined from a list of 
        pre-defined colors. At the case of the arc part the filling color is **None**.

    :Style:

        The type of outline representation can be chosen between: Normal 
        (Continuous), Dashed, Dotted or, Dots and dashes. 

    :Thickness:

        The outline thickness (Weight) can be chosen between: None, Thin, Normal, Strong 
        or High.

:Geometry:

    :Coordenates:

        The coordinates (x, y) from the ellipse center point can be defined.

    :Dimensions:

        The horizontal and vertical (minimum and maximum or maximum and minimum) diameters from the ellipse can be defined.
    
    :Point:

        The position of initial point and end point are defined as angle of the radius betuen the center and the respective point with the horizontal diameter. The angle value follows the mathematical rules, anti-clockwise for positive angles.

Arc extreme points definition
#############################

QElectroTech allows defining the arc extreme points from `information panel`_ or `workspace`_.

.. figure:: /_external/_images/en/qet_element/qet_element_part_arc_extremes.png
   :align: center

   Figure: QElectroTech arc extreme point

Arc extreme points definition from information panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the arc to display the rectangle properties at `information panel`_.
    2. Define the start angle, the angle from the diamete of the start point and the horizontal axes.
    3. Define the angle from the initial point and the end point of the arc.
    4. Press intro.
    5. **Select none** from **Edit** menu or use ``Ctrl + Shift + a`` keyboard shortcut.

Arc extreme points definition from workspace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the arc drawn at the `workspace`_. The arc line changes to red color and the control of the arc ellipse point to blue.
    2. Select the arc again. The line continues in red and the points change to green color.
    3. Select the arc for third time. The line continues in red and at this time only one extreme points are, the color is pink.
    4. Displace the pink points arround the ellipse outline.
    5. **Select none** from **Edit** menu or use ``Ctrl + Shift + a`` keyboard shortcut.

.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html