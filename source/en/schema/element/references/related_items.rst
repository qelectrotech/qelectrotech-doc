.. _en/schema/element/references/related_items

================
Show linked item
================

On of the advantages of working with `cross references`_ on E-CAE tools like QElectroTech is the 
posibility to find the linked `elements`_ automatically. QElectroTech allows finding a linked `element`_ 
easily.

If the `Master`_ and `Slave/s`_ element/s are at the same `folio`_, only by placing the mouse at one 
`element`_, the other/s will be remarked in blue. The linked `element/s`_ can also be found from the  
`element properties`_.

.. figure:: graphics/qet_find_cross_reference.png
    :align: center

    Figure: QElectroTech elements cross reference

At the case that the `elements`_ are at different `folios`_, the linked `element/s`_ can only be found 
from the `element properties`_.

Show slave linked item
~~~~~~~~~~~~~~~~~~~~~~

    1. Select the `Slave element`_ which should be linked from the `project collection`_ or from the `workspace`_.
    2. Right click on the `element`_ selected and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_references.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Search and select the desired `Slave element`_ from the **Element related** table.
    5. Right clik on the `Slave element`_ and select the option **Show item** to find and display the `Master element`_.

        .. figure:: graphics/qet_slave_link.png
            :align: center

            Figure: QElectroTech cross reference tab element properties
            

Show Master linked item
~~~~~~~~~~~~~~~~~~~~~~~

    1. Select the `Slave element`_ from the `project collection`_ or from the `workspace`_.
    2. Right click on the selected element and choose the option **Edit the element**.

        .. figure:: graphics/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

    3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

        .. figure:: graphics/qet_slave_linked.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

    4. Press **See the linked item** to find and display the `Master element`_.

.. _cross references: ../../../../en/element/cross_reference/index.html
.. _element: ../../../../en/element/index.html
.. _elements: ../../../../en/element/index.html
.. _element/s: ../../../../en/element/index.html
.. _folio: ../../../../en/folio/index.html
.. _folios: ../../../../en/folio/index.html
.. _Slave element: ../../../../en/element/type/element_slave.html
.. _Slave/s: ../../../../en/element/type/element_slave.html
.. _Master element: ../../../../en/element/type/element_master.html
.. _Master: ../../../../en/element/type/element_master.html
.. _Display: ../../../../en/element/properties/element_properties_display.html
.. _project collection: ../../../../en/element/collection/project_collection.html
.. _workspace: ../../../../en/interface/workspace.html
.. _element properties: ../../../../en/element/properties/index.html