.. _en/schema/element/references/relateditems

================
Show linked item
================

On of the advnatages of working with corsreferences on E-CAD tools like QElectroTech is the posibility to 
find the linked elements automatically. QElectroTech allows found a linked element easily.

If the Master and slave/s item/s are at the same folio, only by placing the mouse at one element, 
the other/s will be remarked in blue. The linked element/s can also be found from the element 
properties.

.. figure:: graphics/qet_find_cross_reference.png
    :align: center

    Figure: QElectroTech elements cross reference

At the case that the elements are at different folios, the linked element/s can only be found from the 
element properties.

Show slave linked item
~~~~~~~~~~~~~~~~~~~~~~

    1. Select the slave element which should be linked from the project collection or from the workspace.
    2. Right click on the element selected and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. Display the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_references.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired slave element from the **Element related** table.
    5. Right clik on the slave element and select the option **Show item** to find and display the master element.

        .. figure:: graphics/qet_slave_link.png
            :align: center

            Figure: QElectroTech cross reference tab element properties
            

Show Master linked item
~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the slave element from the project collection or from the workspace.
    2. Right click on the selected element and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. Display the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_linked.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Press **See the linked item** to find and display the master element.
