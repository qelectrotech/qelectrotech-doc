.. _en/schema/element/references/slave_item_bind

================
Bind master item
================

Some times one device should be represented in the `project`_ using different `elements`_, power and 
control subsystem and auxiliary subsystems. All these `elements`_ should be always considered as one 
device. For this reason QelectroTech works with `Master`_ and `Slave`_ elements which are linked using 
`cross references`_. 

A `Master element`_ can be linked to a `Slave element`_ as follow:

    1. Select the `Slave element`_ which should be linked from the `project collection`_ or from the `workspace`_.
    2. Right click on the selected `element`_ and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_references.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired `Master element`_ from the available master elements table.
    5. Right clik on the `Master element`_ and select the option **Link the item** to link the `Master element`_ to the `Slave element`_.

        .. figure:: graphics/qet_slave_link.png
            :align: center

            Figure: QElectroTech cross reference tab element properties
            
    6. Press  **Apply** to accept and save the changes.

.. _elements: ../../../../en/element/index.html
.. _element: ../../../../en/element/index.html
.. _Slave element: ../../../../en/element/type/element_slave.html
.. _Slave: ../../../../en/element/type/element_slave.html
.. _Master element: ../../../../en/element/type/element_master.html
.. _Master: ../../../../en/element/type/element_master.html
.. _project: ../../../../en/project/index.html
.. _project collection: ../../../../en/element/collection/project_collection.html
.. _cross references: ../../../../en/element/cross_reference/index.html
.. _Display: ../../../../en/element/properties/element_properties_display.html
.. _workspace: ../../../../en/interface/workspace.html