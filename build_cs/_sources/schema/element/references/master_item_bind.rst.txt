.. _schema/element/references/master_item_bind

===============
Bind slave item
===============

It can happen that one device should be represented in the `project`_ using different `elements`_, power and 
control subsystem and auxiliary subsystems. All these `elements`_ should be considered as one device. 
QElectroTech works with `master`_ and `slave`_ elements which are linked using `cross references`_ to 
represent the device. 

A `slave element`_ can be linked to a `master element`_ with the following steps:

    1. Select the `master element`_ which should be linked from the `project collection`_ or from the `workspace`_.
    2. Right click on the selected `element`_ and choose the option **Edit the element**.

        .. figure:: ../../../images/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Master)** tab from the element editor PopUP window.

        .. figure:: ../../../images/qet_element_master_reference.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired `slave element`_ from the **Availabel elements** table.
    5. Press **Bind item** |icon_bind| to link the `slave element`_ to the `master element`_.
    6. Press **Apply** to accept and save the changes.

.. |icon_bind| image:: ../../../images/ico/22x22/go-down.png

.. note::

   At the avaliable elements table, the `slave element`_ can also be linked by right click on the 
   `element`_ and selectimg the option **Link the item**.

.. figure:: ../../../images/qet_element_master_link.png
    :align: center

    Figure: QElectroTech cross reference tab element properties

.. _elements: ../../../element/index.html
.. _element: ../../../element/index.html
.. _Slave element: ../../../element/type/element_slave.html
.. _Slave: ../../../element/type/element_slave.html
.. _Master element: ../../../element/type/element_master.html
.. _Master: ../../../element/type/element_master.html
.. _project: ../../../project/index.html
.. _project collection: ../../../element/collection/project_collection.html
.. _cross references: ../../../element/cross_reference/index.html
.. _Display: ../../../element/properties/element_properties_display.html
.. _workspace: ../../../interface/workspace.html