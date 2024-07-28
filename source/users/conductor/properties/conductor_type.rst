.. _conductor/properties/conductor_type:

==============
Conductor type
==============

Multiline conductor
~~~~~~~~~~~~~~~~~~~

For `multiline conductors`_, QElectroTech allows defining many different parameters from the 
conductor. The parameters which can be defined are:

* Display parameters:

   1. **Text size**: Size of the displayed text.
   2. **Text formula**: To be used if a variable value is desired at the **Text** field during `conductor creation`_.
   3. **Text**: Text field content to be displayed at `folio`_.
   4. **Text color**: Font color to be displayed at `folio`_.
   5. Positioning and orientation from the displayed text at `folio`_, vertical and horizontal `conductors`_.

* Conductor properties:

   6. **Function**: Variable from `conductor`_, it is used to define the wire phase (L1, L2, L3, N, etc.).
   7. **Voltage / Protocol**: Variable from the `conductor`_, it is used to define the wire voltage (0v,230V,400V, 6kV, etc.) or the wires network protocol (IP).
   8. **Conductor color**: Variable from the `conductor`_, it is used to define the wire color.
   9. **Conductor section**: Variable from the `conductor`_, it is used to define the wire section.
   10. **Cable**:
   11. **Bus**:

.. figure:: /_external/_images/en/qet_conductor/qet_conductor_properties_type_multiline.png
   :align: center

   Figure: Multiline conductor properties

.. note::

    Displaying the `conductor TAG (code)`_ at `multiline diagrams`_ is usual for an easily manage of the 
    manufacturing, erection, commissioning and maintenance phase of the product.

    QElectroTech allows an automatic conducto number definition for the text using the variable 
    ``%autonum`` at the **Text formula** field. This field have to be defined at `Folio properties`_ 
    before starting the `conductor creation`_. 

Single line conductor
~~~~~~~~~~~~~~~~~~~~~

For `single line conductors`_, the `conductors`_ are represented without any text infromation. Only 
the type of power system should be defined to have the correct symbol representation. 

QElectroTech allows the following options for `single line conductors`_:

   1. System with or without **Ground**
   2. System with or without **Neutral**
   3. **PEN** system, system where **Neutral** and **Ground** are the same wire.
   4. Systems with one, two or three phases

.. figure:: /_external/_images/en/qet_conductor/qet_conductor_properties_type_single_line.png
   :align: center

   Figure: Single line conductor properties

.. _multiline conductors: ../../folio/type/multiline_diagram.html
.. _multiline diagrams: ../../folio/type/multiline_diagram.html
.. _folio: ../../folio/index.html
.. _conductor: ../../conductor/index.html
.. _conductors: ../../conductor/index.html
.. _conductor creation: ../../schema/conductor/conductor_creation.html
.. _conductor TAG (code): ../../conductor/properties/conductor_numbering.html
.. _Folio properties: ../../folio/properties/folio_type.html
.. _single line conductors: ../../conductor/type/single_line_conductor.html
