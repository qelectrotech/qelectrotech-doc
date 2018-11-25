.. _en/schema/element/references/slaveitembind

================
Bind master item
================

Some times one device should be represented many times in the project using different elements but it
should be always considered as one. For this reason QelectroTech works with Master and Slave elements 
Which are linked using cross references. 

A master element can be linked to a slave element as follow:

    1. Select the slave element which should be linked from the project collection or from the workspace.
    2. Right click on the selected element and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. Display the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_references.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired master element from the available master elements table.
    5. Right clik on the master element and select the option **Link the item** to link the master element to the slave element.

        .. figure:: graphics/qet_slave_link.png
            :align: center

            Figure: QElectroTech cross reference tab element properties
            
    6. Press  **Apply** to accept and save the changes.