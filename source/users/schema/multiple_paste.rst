.. _schema/multiple_paste:

==============
Multiple paste
==============

For making more eficient the schema creation, QElectroTech provides the feature multiple paste. This 
feature allows `copying`_ and `pasting`_ one or more objects automating some object definition actions.

.. figure:: ../images/qet_multiple_paste.png
    :align: center

    Figure: QElectroTech multiple paste

As a difference to the standard `copy`_ and `paste`_ feature, the multiple paste feature provides the following 
options:

    * `Copy`_ and `paste`_ an onject (`element`_, `conductor`_, `text field`_, etc.) multiple times in one action.
    * Use QElectroTech auto-conection feature for `element terminals`_ which are at the same horizontal or vertical line.
    * Self-numbering of the copied `element/s`_, the `standard copy`_ feature does not allow using auto-numbering patterns.
    * Self-numbering of the copied/created `conductor/s`_, the `standard copy`_ feature does not allow using auto-numbering patterns.

To copy and paste multiple times one or more object:

    1. `Select the object/s`_ which should be copied.
    2. Right click on the selected object/s.

        .. figure:: ../images/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element right click PopUP window

    3. Select the option **Multiple paste** to display the multiple paste PopUP window.

        .. figure:: ../images/qet_multiple_paste_window.png
            :align: center

            Figure: QElectroTech multiple paste PopUP window
    
    4. Define the ``X`` and ``Y`` offset between original and copy/copies.
    5. Define the number of copies desired.
    6. Click the desired options about `auto-connection`_, `self-numebering of elements`_ and `self-numebering of conductors`_.
    7. Press **OK** Button to close the multiple paste PopUP window and create the copies.

.. _Select the object/s: ../schema/select/index.html
.. _paste: ../schema/paste.html
.. _pasting: ../schema/paste.html
.. _copy: ../schema/copy.html
.. _copying: ../schema/copy.html
.. _standard copy: ../schema/copy.html
.. _element: ../element/index.html
.. _element/s: ../element/index.html
.. _conductor: ../conductor/index.html
.. _conductor/s: ../conductor/index.html
.. _text field: ../schema/text/index.html
.. _element terminals: ../element/element_parts/terminal.html
.. _auto-connection: ../schema/conductor/conductor_creation.html
.. _self-numebering of elements: ../element/properties/element_numbering.html
.. _self-numebering of conductors: ../conductor/properties/conductor_numbering.html