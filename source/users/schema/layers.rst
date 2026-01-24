.. SPDX-FileCopyrightText: 2018-Present Qelectrotech Team <license@qelectrotech.org>

.. SPDX-License-Identifier: GPL-2.0-only


.. _schema/layers:

==================
Object layer level
==================

Overlapping of `elements`_ or `pictures`_ may occur at `workspace`_, QElectroTech allows defining the level 
order from `elements`_ and `pictures`_ at each `folio`_. 

QElectroTech allows the following actions:

=================      ==============      ==========================================     =========================
Icon                   Action              Definition                                     Keyboard shortcut
=================      ==============      ==========================================     =========================
|bring_forward|        Bring to front      Brings the selection (s) to front              ``Ctrl + Shift + Home``
|raise|                Raise               Move over other elements (s)                   ``Ctrl + Shift + Up``
|lower|                Lower               Moves under other elements (s)                 ``Ctrl + Shift + Down``
|send_backward|        Send backwards      Sends in the backwards the selection (s)       ``Ctrl + Shift + End``
=================      ==============      ==========================================     =========================

.. |bring_forward| image:: /_external/_images/_site-assets/user/ico/22x22/bring_forward.png
.. |raise| image:: /_external/_images/_site-assets/user/ico/22x22/raise.png
.. |lower| image:: /_external/_images/_site-assets/user/ico/22x22/lower.png
.. |send_backward| image:: /_external/_images/_site-assets/user/ico/22x22/send_backward.png

.. note::

   The layer level from multiples objects can be defined at the same time `selecting multiple objects`_.

The level from each `element`_ or `picture`_ can be defined from `menu bar`_, `toolbar`_, by right click 
on the object and using the corresponding keyboard shortcut. 

Define object layer from menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Select the object/s`_ which layer level should be defined.
2. Select **Edit** menu and the desired action.

.. figure:: /_external/_images/en/qet_menu/qet_menu_edit.png
   :align: center

   Figure: QElectroTech Edit menu 

Define object layer from toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Select the object/s`_ which layer level should be defined.
2. Select the corresponding icon from `toolbar`_ (icons from above table) to realize the desired action.

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Depth**

Define object layer by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Select the object/s`_ which layer level should be defined.
2. Right click and select the desired layer definition action.

.. figure:: /_external/_images/en/qet_element/qet_element_right_click.png
   :align: center

   Figure: QElectroTech element right click items

Define object layer using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As many other tools, QElectroTech is an applications which allows using keyboard shortcut.

1. `Select the object/s`_ which layer level should be defined.
2. Press the corresponding keyboard shortcut (keyboard shortcut from above table) to realize the desired action.

.. seealso::

    For more information about QElectroTech keyboard shortcuts, refer to `menu bar`_ section.

.. _menu bar: ../interface/menu_bar.html
.. _toolbar: ../interface/toolbars.html
.. _elements: ../element/index.html
.. _element: ../element/index.html
.. _pictures: ../schema/picture.html
.. _picture: ../schema/picture.html
.. _workspace: ../interface/workspace.html
.. _folio: ../folio/index.html
.. _Select the object/s: ../schema/select/index.html
.. _selecting multiple objects: ../schema/select/select_multiple_objects.html