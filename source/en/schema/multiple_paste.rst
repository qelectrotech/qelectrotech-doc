.. _en/schema/multiple_paste

=================
Multiple paste
=================

For making more eficient the schema creation, QElectroTech provides the feature multiple paste. This 
feature allows `copy`_ and `paste`_ one or more objects automating some object definition actions.

.. figure:: graphics/qet_multiple_paste.png
    :align: center

    Figure: QElectroTech multiple paste

As a difference to the standard `copy`_ and `paste`_ feature, the multiple paste feature provides the following 
options:

    * `Copy`_ and `paste`_ an onject (`elements`_, `conductors`_, `text fields`_, etc.) multiple times in one action.
    * Use QElectroTech auto-conection feature for `element terminals`_ which are at the same horizontal or vertical line.
    * Self-numbering of the copied `element/s`_, the `standard copy`_ feature does not allow using auto-numbering patterns.
    * Self-numbering of the copied/created `conductor/s`_, the `standard copy`_ feature does not allow using auto-numbering patterns.

To copy and paste multiple times on or more object:

    1. `Select the object/s`_ which should be copied.
    2. Right click on the selected object/s.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element right click PopUP window

    3. Select the option **Multiple paste** to display the multiple paste PopUP window.

        .. figure:: graphics/qet_multiple_paste_window.png
            :align: center

            Figure: QElectroTech multiple paste PopUP window
    
    4. Define the ``X`` and ``Y`` offset between origianl and copy.
    5. Define the number of copies desired.
    6. Click the desired options about `Auto-connection`_, `Self-numebering of elements`_ and `Self-numebering of conductors`_.
    7. Press **OK** Button to close the multiple paste PopUP window and create the copies.

.. _Select the object/s: ../../en/schema/select/index.html
.. _paste: ../../en/schema/paste.html
.. _copy: ../../en/schema/copy.html
.. _standard copy: ../../en/schema/copy.html
.. _elements: ../../en/element/index.html
.. _element/s: ../../en/element/index.html
.. _conductors: ../../en/conductor/index.html
.. _conductor/s: ../../en/conductor/index.html
.. _text fields: ../../en/schema/text/index.html
.. _element terminals: ../../en/element/element_parts/terminal.html
.. _Auto-connection: ../../en/schema/conductor/conductor_creation.html
.. _Self-numebering of elements: ../../en/element/properties/element_numbering.html
.. _Self-numebering of conductors: ../../en/conductor/properties/conductor_numbering.html