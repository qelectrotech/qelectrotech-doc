.. _en/folio/foliotype

=============
Type of folio
=============

QelectroTech has two different type of folio, single line and multiline. The type of folio can be defined 
at the properties from the folio. 

Multiline diagram
~~~~~~~~~~~~~~~~~

The multiline diagram is the representation of each terminal, line and phase from the two and three phase 
power systems. The multiline diagram is also used for the representation of all the electric and control 
systems.

.. figure:: graphics/qet_multiline.png
   :align: center

   Figure: Multiline diagram

For the multiline diagrams, QElectroTech allows defining many different parameters from the text of the 
connectors. All parameters which can be defined are listed bellow.

|   1. Text size
|   2. 
|   3. 
|   4. 
|   5. 

.. figure:: graphics/qet_folio_multiline.png
   :align: center

   Figure: Multiline properties

Single line diagram
~~~~~~~~~~~~~~~~~~~

The single line diagram is a simplified notation for representing a two and three phase power system. 

.. figure:: graphics/qet_singleline.png
   :align: center

   Figure: Single line diagram

For simple line diagrams, the connectors are represented without any text infromation. Only the type 
of power system should be defined to have the correct symbol representation. 

QElectroTech allows the following options for single line diagrams:

|   1. System with or without **Ground**
|   2. System with or without **Neutral**
|   3. **PEN** system, system where the **Neutral** and the **Ground** are the same conductor.
|   4. Systems with one, two or three phases

.. figure:: graphics/qet_folio_singleline.png
   :align: center

   Figure: Single line properties

.. note::

   At the fluid power schematics, the multiline diagram represent the pressure line and the return line using 
   different connectors. At the single line diagram, on connector from the schema represents both pipes.