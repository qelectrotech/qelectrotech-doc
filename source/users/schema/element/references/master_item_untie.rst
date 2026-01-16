.. _schema/element/references/master_item_untie:

================
Untie slave item
================

Some times is necessary to delete previous work, QElectroTech allows breaking/deleting 
`links between elements (cross references)`_. 

A `Slave element`_ can be unlinked from a `master element`_ as follow:

1. Select the `master element`_ which should be unlinked from the `project collection`_  or from the `workspace`_.
2. Right click on the selected `element`_ and choose the option **Edit the element**.

.. figure:: /_external/_images/en/qet_element/qet_element_right_click.png
    :align: center

    Figure: QElectroTech element options

3. `Display`_ the **Cross-reference (Master)** tab from the element editor PopUP window

.. figure:: /_external/_images/en/qet_element/qet_element_master_reference.png
    :align: center

    Figure: QElectroTech cross reference tab element properties

4. Search and select the desired `slave element`_ from the **Element related** table.
5. Press the **Untie item** button |icon_untie| to unlink the `slave element`_ from the `master element`_.
6. Press  **Apply** to accept and save the changes. 

.. |icon_untie| image:: /_external/_images/_site-assets/user/ico/22x22/go/go-up.png

.. note::

   The `slave element`_ can also be unlinked by right click on the `element`_ and selecting the option **Unlink the item**.

.. figure:: /_external/_images/en/qet_element/qet_element_master_unlink.png
    :align: center

    Figure: QElectroTech cross reference tab element properties

.. _links between elements (cross references): ../../../element/cross_reference/index.html
.. _Slave element: ../../../element/type/element_slave.html
.. _Master element: ../../../element/type/element_master.html
.. _Display: ../../../element/properties/element_properties_display.html
.. _workspace: ../../../interface/workspace.html
.. _project collection: ../../../element/collection/project_collection.html
.. _element: ../../../element/index.html