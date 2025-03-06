.. _schema/element/references/related_items:

================
Show linked item
================

On of the advantages of working with `cross references`_ on E-CAE tools like QElectroTech is the 
possibility to find the linked `elements`_ automatically. QElectroTech allows finding a linked `element`_ 
easily.

If the `master`_ and `slave/s`_ element/s are at the same `folio`_, only by placing the mouse at one 
`element`_, the other/s will be remarked in blue. The linked `element/s`_ can also be found from the  
`element properties`_.

.. figure:: /_external/_images/en/qet_find_cross_reference.png
    :align: center

    Figure: QElectroTech elements cross reference

At the case that the `elements`_ are at different `folios`_, the linked `element/s`_ can only be found 
from the `element properties`_.

Show slave linked item
~~~~~~~~~~~~~~~~~~~~~~

1. Select the `slave element`_ which should be linked from the `project collection`_ or from the `workspace`_.
2. Right click on the `element`_ selected and choose the option **Edit the element**.

.. figure:: /_external/_images/en/qet_element/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

.. figure:: /_external/_images/en/qet_element/qet_element_slave_references.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

4. Search and select the desired `slave element`_ from the **Element related** table.
5. Right clik on the `slave element`_ and select the option **Show item** to find and display the `master element`_.

.. figure:: /_external/_images/en/qet_element/qet_element_slave_link.png
            :align: center

            Figure: QElectroTech cross reference tab element properties
            

Show Master linked item
~~~~~~~~~~~~~~~~~~~~~~~

1. Select the `slave element`_ from the `project collection`_ or from the `workspace`_.
2. Right click on the selected element and choose the option **Edit the element**.

.. figure:: /_external/_images/en/qet_element/qet_element_right_click.png
            :align: center

            Figure: QElectroTech element options

3. `Display`_ the **Cross-reference (Slave)** tab from the element editor PopUP window

.. figure:: /_external/_images/en/qet_element/qet_element_slave_linked.png
            :align: center

            Figure: QElectroTech cross reference tab element properties

4. Press **See the linked item** to find and display the `master element`_.

.. _cross references: ../../../element/cross_reference/index.html
.. _element: ../../../element/index.html
.. _elements: ../../../element/index.html
.. _element/s: ../../../element/index.html
.. _folio: ../../../folio/index.html
.. _folios: ../../../folio/index.html
.. _Slave element: ../../../element/type/element_slave.html
.. _Slave/s: ../../../element/type/element_slave.html
.. _Master element: ../../../element/type/element_master.html
.. _Master: ../../../element/type/element_master.html
.. _Display: ../../../element/properties/element_properties_display.html
.. _project collection: ../../../element/collection/project_collection.html
.. _workspace: ../../../interface/workspace.html
.. _element properties: ../../../element/properties/index.html