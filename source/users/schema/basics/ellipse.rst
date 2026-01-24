.. SPDX-FileCopyrightText: 2026 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _schema/basics/ellipse:

========
Ellipse
========

Create ellipse
##############

.. note::

    To draw more easily, the folio grid can be displayed from **Display > Display the grid** or from `toolbar`_ icon |grid|. 

The ellipse can only be added to the `workspace`_ by `toolbar`_.

1. Select the icon |ellipse| from the `toolbar`_ to add an ellipse.
2. Click on the initial controlling point from the ellipse.
3. Click on the end controlling point from the ellipse.

.. |grid| image:: /_external/_images/_site-assets/user/ico/22x22/grid.png
.. |ellipse| image:: /_external/_images/_site-assets/user/ico/22x22/ellipse.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Add**.

Ellipse properties
#######################

The border line and the internal area from the ellipse can be customized at QElectroTech.   

* The border line from a ellipse has the same properties as a `line`_.
* The type of filling for closed primitive objects (rectangle, ellipse and closed polygon) are: **None**, **Solid line** and some types of grids.

.. figure:: /_external/_images/en/qet_close/qet_close_primitive_object_filling.png
            :align: center

            Figure: QElectroTech Color selection PopUP window

* The possible filling colors are defined by the `RGB scale range`_.

.. note::

    The position from the ellipse can be locked to prevent involuntary movement.

    * Go to ellipse properties and check the **Lock position** button.

The ellipse properties can be displayed from `menu bar`_, by right click on border from the ellipse, 
from selection properties panel and using keyboard shortcut.

Ellipse properties from menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select the border from the ellipse which should be edited.
2. Select **Edit > Edit the selected object** menu item to display the ellipse properties PopUP window.

.. figure:: /_external/_images/en/qet_menu/qet_menu_edit_object.png
            :align: center

            Figure: QElectroTech edit menu

Ellipse properties by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Right click on the border from the ellipse which should be edited.
2. Select the option **Edit the selected object** to display the ellipse properties PopUP window.

.. figure:: /_external/_images/en/qet_object_right_click.png
   :align: center

   Figure: QElectroTech ellipse selection PopUP window

Ellipse properties from selection properties panel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Select one the border from the ellipse which should be edited and the properties from the ellipse will appear at `selection properties panel`_.

.. figure:: /_external/_images/en/qet_close/qet_close_primitive_object_prop.png
   :align: center

   Figure: QElectroTech ellipse properties panel

.. note::

   If the `selection properties panel`_ is not displayed, it can be displayed from **Settings > Display > Selection properties**

Ellipse properties using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech allows using keyboard shortcut to increase the working efficiency.

1. Select the border from the ellipse which should be edited.
2. Press ``Ctrl + e`` to display the ellipse properties PopUP window.

.. seealso::

    For more information about QElectroTech keyboard shortcuts, refer to `menu bar`_ section.

.. _menu bar: ../../interface/menu_bar.html
.. _workspace: ../../interface/workspace.html
.. _toolbar: ../../interface/toolbars.html
.. _line: ../../schema/basics/line.html
.. _selection properties panel: ../../interface/panels/selection_properties_panel.html
.. _RGB scale range: ../../annex/color.html