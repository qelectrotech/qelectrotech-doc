.. _en/schema/layers

====================
Working with layers
====================

Overlap of `elements`_ or `pictures`_ may occur at `workspace`_, QElectroTech allows defining the level 
order from `elements`_ and `pictures`_ at each `folio`_. 

QElectroTech allows the actions defined bellow:

===================      ==============      ====================================================================================      =========================
Icon                     Action              Definition                                                                                Keyboard shortcut
===================      ==============      ====================================================================================      =========================
|icon_bring_front|       Bring to front      The element or picture will be at the top and completly visible                           ``Ctrl + Shift + Home``
|icon_raise|             Raise               The element or image will be sent one level up                                            ``Ctrl + Shift + Up``
|icon_lower|             Lower               The element or image will be sent one level down                                          ``Ctrl + Shift + Down``
|icon_backward|          Send backwards      The element or picture will be at the bottom and probably will be partially covered       ``Ctrl + Shift + End``
===================      ==============      ====================================================================================      =========================

.. |icon_bring_front| image:: graphics/qet_bring_front_icon.png
.. |icon_raise| image:: graphics/qet_raise_icon.png
.. |icon_lower| image:: graphics/qet_lower_icon.png
.. |icon_backward| image:: graphics/qet_backward_icon.png

.. note::

   The layer level from multiples objects can be defined at the same time `selecting multiple objects`_.

The definition of layer level from each element or picture level can be made from the `Menu bar`_, 
`toolbar`_, by right click on the object and using the corresponding keyboard shortcut. 

Define object layer from Menu bar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. `Select the object/s`_ which layer level should be defined.
    2. Select **Edit** from the `Menu bar`_ and the desired action.

.. figure:: graphics/qet_menu_edit.png
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

.. figure:: graphics/qet_element_right_click.png
   :align: center

   Figure: QElectroTech element right click items

Define object layer using keyboard shortcut
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As many other tools, QElectroTech is an applications which allows using keyboard shortcut.

    1. `Select the object/s`_ which layer level should be defined.
    2. Press the corresponding keyboard shortcut (keyboard shortcut from above table) to realize the desired action.

.. seealso::

    For more information about QElectroTech keyboard shortcut, please refers to `Menu bar`_ section.

.. _Menu bar: ../../en/interface/menu_bar.html
.. _toolbar: ../../en/interface/toolbars.html
.. _elements: ../../en/element/index.html
.. _pictures: ../../en/schema/picture.html
.. _workspace: ../../en/interface/workspace.html
.. _folio: ../../en/folio/index.html
.. _Select the object/s: ../../en/schema/select/index.html
.. _selecting multiple objects: ../../en/schema/select/select_multiple_objects.html