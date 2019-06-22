.. _en/schema/element/references/master_item_bind

===============
Bind slave item
===============

Some times one device should be represented in the `project`_ using different `elements`_, power and 
control subsystem and auxiliary subsystems. All these `elements`_ should be always considered as one 
device. For this reason QelectroTech works with `Master`_ and `Slave`_ elements which are linked using 
`cross references`_. 

A `Slave element`_ can be linked to a `Master element`_ as follow:

    1. Select the `Master element`_ which should be linked from the `project collection`_ or from the `workspace`_.
    2. Right click on the selected `element`_ and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Master)** tab from the element editor PopUP window.

        .. figure:: graphics/qet_master_reference.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired `Slave element`_ from the **Availabel elemetns** table.
    5. Press **Bind item** |icon_bind| to link the `Slave element`_ to the `Master element`_.
    6. Press **Apply** to accept and save the changes.

.. |icon_bind| image:: graphics/qet_element_link_bind.png

.. note::

   At the avaliable elements table, the `Slave element`_ can also be linked by right click on the 
   `element`_ and selectimg the option **Link the item**.

.. figure:: graphics/qet_master_link.png
    :align: center

    Figure: QElectroTech cross reference tab element properties

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