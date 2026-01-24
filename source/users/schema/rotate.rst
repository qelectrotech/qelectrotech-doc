.. SPDX-FileCopyrightText: 2018-Present Qelectrotech Team <license@qelectrotech.org>

.. SPDX-License-Identifier: GPL-2.0-only


.. _schema/rotate:

=============
Rotate object
=============

QElectroTech allows choosing the orientation from many object which are represented at the `folio`_. 
The objects which orientation can be chosen are the following:

* `Element`_
* `Picture`_
* `Text field`_

QElectroTech does not allow all orientations for the objects mentioned before, only 4 different 
orientations are possible: **0**, **90**, **180** and **270** degrees.

.. note::

    QElectroTech only offers the possibility to rotate **90** degrees on the clock direction.

    * To rotate **180** degrees the actions should be repeated once.
    * To rotate **270** degrees the actions should be repeated twice.

.. note::

   Multiples objects can be rotated at the same time `selecting multiples object`_

Rotating objects can be done from `menu bar`_, `toolbar`_, by right click on the object and using 
the corresponding keyboard shortcut.

Rotate object from menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Select the object`_ which should be rotated.
2. Select **Edit > Rotate** menu item to rotate the object.

.. figure:: /_external/_images/en/qet_menu/qet_menu_edit.png
   :align: center

   Figure: QElectroTech Edit menu

Rotate object from toolbar
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Select the object`_ which should be rotated.
2. Select the icon |transform-rotate| from `toolbar`_ to rotate the object.

.. |transform-rotate| image:: /_external/_images/_site-assets/user/ico/16x16/transform-rotate.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Tools**.

Rotate object by right click
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Right click on the object which should be rotated.
2. Select the option **Rotate** to delete the object.

.. figure:: /_external/_images/en/qet_element/qet_element_right_click.png
   :align: center

   Figure: QElectroTech right click PopUP window

Rotate object using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech allows using keyboard shortcut to increase the working efficiency.

1. `Select the object`_ which should be rotated.
2. Press ``Space`` to rotate the object.

.. seealso::

    For more information about QElectroTech keyboard shortcuts, refer to `menu bar`_ section.

.. _Menu bar: ../interface/menu_bar.html
.. _toolbar: ../interface/toolbars.html
.. _element: ../element/index.html
.. _conductor: ../conductor/index.html
.. _text field: ../schema/text/index.html
.. _picture: ../schema/picture.html
.. _paste: ../schema/paste.html
.. _folio: ../folio/index.html
.. _project: ../project/index.html
.. _selecting multiples object: ../schema/select/select_multiple_objects.html
.. _basic object: ../schema/basics/index.html
.. _Select the object: ../schema/select/index.html