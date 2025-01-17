.. _element/element_parts/dynamic_text:

============
Dynamic text
============

The dynamic text field is an object that displays a text that is comming from a variable value. The text 
value is changing with the variable is changed, editing the part is not necessary to change the text 
content.

Create dynamic text
~~~~~~~~~~~~~~~~~~~

The text field can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_dynamic_text| from `toolbar`_ to add a dynamic text field.
    2. Click the positional point from the text field in the `workspace`_.

.. |icon_dynamic_text| image:: /_external/_images/_site-assets/user/ico/22x22/textfield.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Dynamic text properties
~~~~~~~~~~~~~~~~~~~~~~~

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_dynamic_text.png
   :align: center

   Figure: QElectroTech dynamic text field part from element

QElectroTech allows customizing different text properties:

:Placement:

    :Position:

        The dynamic text coordinates (x, y) can be defined.
    
    :Rotation:

        The text display angle can be defined in the range of 0 to 360 degrees.
    
    :Frame:

        The posibility to display the text inside a rectangle frame is provided.
    
    :Alignemnt:

        The text position inside the frame can be defined. Left, center or right and top, middle or bottom.

:Content:

    :Source:

        The source content can be user text (similar to static text), element information parameter or composite text.

    :Size:

        The text size can be defined. 

    :Color:

        The text color can be choosed from RGB color code database.

.. _element: ../../element/index.html
.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html