.. _en/element/element_editor/edition/graphic/layers

========================
Layers in element editor
========================

Overlap of part, graphical elements, may occur at the graphical representation of an element. QElectroTech 
allows defining the representation order from the part. Working with layers will be necessary, for example, 
when a filled part as rectangle or ellipse hides a text.

The definition of layer level from each part can only be done from the Menu bar.

    1. Select the element part which layer level should be defined.
    2. Select **Edit** from the main bar and the desired layer action.

.. figure:: graphics/qet_elementeditor_menu_edit.png
   :align: center

   Figure: QElectroTech element editor Edit Menu

Regarding the layer actions allowed by QElectroTech, the following table defines all possibilities.

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