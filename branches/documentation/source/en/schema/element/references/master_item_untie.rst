.. _en/schema/element/references/master_item_untie

================
Untie slave item
================

Some times is necessary to delete previous work, QElectroTech allows breaking/deleting 
`links between elements (cross references)`_. 

A `Slave element`_ can be unlinked from a `Master element`_ as follow:

    1. Select the `Master element`_ which should be unlinked from the `project collection`_  or from the `workspace`_.
    2. Right click on the selected `element`_ and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Master)** tab from the element editor PopUP window

        .. figure:: graphics/qet_master_reference.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired `Slave element`_ from the **Element related** table.
    5. Press the **Untie item** button |icon_untie| to unlink the `Slave element`_ from the `Master element`_.
    6. Press  **Apply** to accept and save the changes. 

.. |icon_untie| image:: graphics/qet_element_link_untie.png

.. note::

   The `Slave element`_ can also be unlinked by right clik on the `element`_ and selectim the option **Unlink the item**.

.. figure:: graphics/qet_master_unlink.png
    :align: center

    Figure: QElectroTech cross reference tab element properties

.. _links between elements (cross references): ../../../../en/element/cross_reference/index.html
.. _Slave element: ../../../../en/element/type/element_slave.html
.. _Master element: ../../../../en/element/type/element_master.html
.. _Display: ../../../../en/element/properties/element_properties_display.html
.. _workspace: ../../../../en/interface/workspace.html
.. _project collection: ../../../../en/element/collection/project_collection.html
.. _element: ../../../../en/element/index.html