.. _element/element_editor/edition/graphic/layers:

========================
Layers in element editor
========================

Overlaping of parts, graphical elements, may occur at the graphical representation of elements. QElectroTech 
allows defining the representation order from part. Working with layers will be necessary, for example, 
when a filled part as `rectangle`_ or `ellipse`_ hides a `text`_.

The definition of layer level from each `part`_ can only be done from `menu bar`_.

    1. Select the `part`_ which layer level should be defined.
    2. Select **Edit** from the main bar and the desired layer action.

.. figure:: /_external/_images/en/qet_element/qet_element_editor_menu_edit.png
   :align: center

   Figure: QElectroTech element editor Edit Menu

Regarding the layer actions allowed by QElectroTech, the following table defines all possibilities.

===================      ==============      ================================================================      =========================
Icon                     Action              Definition                                                            Keyboard shortcut
===================      ==============      ================================================================      =========================
|bring_forward|          Bring to front      Brings the selection (s) to front                                     ``Ctrl + Shift + Home``
|raise|                  Raise               Aproachs the selection (s)                                            ``Ctrl + Shift + Up``
|lower|                  Lower               Moves away the selection (s)                                          ``Ctrl + Shift + Down``
|send_backward|          Send backwards      Sends in the backwards the selection (s)                              ``Ctrl + Shift + End``
===================      ==============      ================================================================      =========================

.. _rectangle: ../../../../element/element_parts/rectangle.html
.. _ellipse: ../../../../element/element_parts/ellipse.html
.. _text: ../../../../element/element_parts/text.html
.. _menu bar: ../../../../element/element_editor/interface/menu_bar.html
.. _part: ../../../../element/element_parts/index.html

.. |bring_forward| image:: /_external/_images/_site-assets/user/ico/22x22/bring_forward.png
.. |raise| image:: /_external/_images/_site-assets/user/ico/22x22/raise.png
.. |lower| image:: /_external/_images/_site-assets/user/ico/22x22/lower.png
.. |send_backward| image:: /_external/_images/_site-assets/user/ico/22x22/send_backward.png