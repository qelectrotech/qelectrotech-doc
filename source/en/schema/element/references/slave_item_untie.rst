.. _en/schema/element/references/slave_item_untie

=================
Untie master item
=================

Some times is necessary to delete previous work, QElectroTech allows breaking/deleting 
`links between elements (cross references)`_. 

A `Master element`_ can be unlinked from a `Slave element`_ as follow:

    1. Select the `Slave element`_ which should be unlinked from the `project collection`_ or from the `workspace`_.
    2. Right click on the selected `element`_ and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_linked.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Press **Unlink** to delete the `cross reference`_ with the `Master element`_.
    5. Press **Apply** to accept and save the changes. 

.. _links between elements (cross references): ../../../../en/element/cross_reference/index.html
.. _Slave element: ../../../../en/element/type/element_slave.html
.. _Master element: ../../../../en/element/type/element_master.html
.. _Display: ../../../../en/element/properties/element_properties_display.html
.. _workspace: ../../../../en/interface/workspace.html
.. _project collection: ../../../../en/element/collection/project_collection.html
.. _element: ../../../../en/element/index.html
.. _cross reference: ../../../../en/element/cross_reference/index.html
.. _Display: ../../../../en/element/properties/element_properties_display.html