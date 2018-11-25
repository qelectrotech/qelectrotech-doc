.. _en/schema/element/references/masteritembind

===============
Bind slave item
===============

Some times one device should be represented many times in the project using different elements but it
should be always considered as one. For this reason QelectroTech works with Master and Slave elements 
Which are linked using cross references. 

A slave element can be linked to a master element as follow:

    1. Select the master element which should be linked from the project collection or from the workspace.
    2. Right click on the selected element and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. Display the **Cross-reference (Master)** tab from the element editor PopUP window

        .. figure:: graphics/qet_master_reference.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired slave element from the **Availabel elemetns** table.
    5. Press **Bind item** |icon_bind| to link the slave element to the master element.
    6. Press  **Apply** to accept and save the changes.

.. |icon_bind| image:: graphics/qet_element_link_bind.png

.. note::

   The slave item can also be linked by right clik on the element and selectim the option **Link the item**.

.. figure:: graphics/qet_master_link.png
    :align: center

    Figure: QElectroTech cross reference tab element properties