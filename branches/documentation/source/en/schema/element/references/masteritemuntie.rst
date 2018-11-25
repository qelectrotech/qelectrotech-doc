.. _en/schema/element/references/masteritemuntie

================
Untie slave item
================

Some times is necessary to delete previous work, QElectroTech allows breaking/deleting links between elements. 

A slave element can be unlinked from a master element as follow:

    1. Select the master element which should be unlinked from the project collection or from the workspace.
    2. Right click on the selected element and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. Display the **Cross-reference (Master)** tab from the element editor PopUP window

        .. figure:: graphics/qet_master_reference.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired slave element from the **Element related** table.
    5. Press the **Untie item** button |icon_untie| to link the slave element to the master element.
    6. Press  **Apply** to accept and save the changes. 

.. |icon_untie| image:: graphics/qet_element_link_untie.png

.. note::

   The slave item can also be unlinked by right clik on the element and selectim the option **Unlink the item**.

.. figure:: graphics/qet_master_unlink.png
    :align: center

    Figure: QElectroTech cross reference tab element properties