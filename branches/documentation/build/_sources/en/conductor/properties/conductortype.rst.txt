.. _en/conductor/properties/conductortype

==============
Conductor type
==============

Multiline conductor
~~~~~~~~~~~~~~~~~~~

For the multiline diagrams, QElectroTech allows defining many different parameters from the text of the 
connectors. All parameters which can be defined are listed bellow.

   1. **Text size**: Size of the test displayed.
   2. **Text formula**: To be used if a variable value is desired at the **Text** field during conductor creation.
   3. **Text**: Text field content to be displayed att he folio.
   4. **Function**: Variable from conductor, it is used to define the phase from the conductor (L1, L2, L3, N, etc.).
   5. **Voltage/Protocol**: Variable from the conductor, it is used to define the voltage (0v,230V,400V, 6kV, etc.) or the network protocol (IP).
   6. Positioning and orientation of the text displayed at the folio at vertical and horizontal conductors.

.. figure:: graphics/qet_conductor_properties_type_multiline.png
   :align: center

   Figure: Multiline conductor properties

.. note::

    Display the conductor number at multiline schemas is ussual for an easyly manage of the 
    manufacturing, erection, commisioning and maintenace phase of the product.

    QElectroTech allows an automatic conducto number definition for the text using the variable 
    ``%autonum`` at the **Text formula** field. This field have to be defined at 
    `Folio properties <../../../en/folio/properties/foliotype.html>`_ before starting the conductor 
    creation. 

Single line conductor
~~~~~~~~~~~~~~~~~~~~~

For simple line diagrams, the connectors are represented without any text infromation. Only the type 
of power system should be defined to have the correct symbol representation. 

QElectroTech allows the following options for single line diagrams:

   1. System with or without **Ground**
   2. System with or without **Neutral**
   3. **PEN** system, system where the **Neutral** and the **Ground** are the same conductor.
   4. Systems with one, two or three phases

.. figure:: graphics/qet_conductor_properties_type_singleline.png
   :align: center

   Figure: Single line conductor properties