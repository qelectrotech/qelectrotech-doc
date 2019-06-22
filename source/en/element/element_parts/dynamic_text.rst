.. _en/element/element_parts/dynamic_text

============
Dynamic text
============

The dynamic text field is an object that display a text that is comming from a variable value. The text 
value is changing with the variable is changed, editing the part is not necessary to change the text 
content.

Create dynamic text
~~~~~~~~~~~~~~~~~~~

The text field can only be added to the workspace by the tool bar.

    1. Select the icon |icon_dynamic_text| from the toolbar to add a dynamic text field.
    2. Click at the workspace the positional point from the text field where the dynamic text field should be introduced.

.. |icon_dynamic_text| image:: graphics/qet_dynamic_text_icon.png

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Parts**.

Dynamic text properties
~~~~~~~~~~~~~~~~~~~~~~~

The properties from every element part can only be displayed at the properties panel when the part is 
selected.

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: graphics/qet_element_dynamic_text.png
   :align: center

   Figure: QElectroTech dynamic text field part from element

QElectroTech allows customizing different text properties:

:Placement:

    :Position:

        The coordinates (x, y) from the dynamic text field positional point can be defined.
    
    :Rotation:

        The display angle from the text can be defined in the range of 0 to 360 degrees.
    
    :Frame:

        The posibility to display the text inside a rectangle frame is provided.
    
    :Alignemnt:

        The position of the text inside the frame can be defined. Left, center or right and top, middle or bottom.

:Content:

    :Source:

        The source content can be user text (similar to static text), element nformation parameter or composite text.

    :Size:

        The text size can be defined. 

    :Color:

        The color from the text can be choosed from the RGB color code database.