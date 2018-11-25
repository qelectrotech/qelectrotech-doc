.. _en/element/type/elementslave

==================
Slave element
==================

The slave elements represent the power circuit devices such the main contactors from 
power contactors. The slave elements also represent the auxiliary contactors. Even if an 
auxiliary contactor is part of the command circuit, its activation is forced by another 
element.

.. figure:: graphics/qet_element_slave.png
   :align: center

   Figure: QElectroTech slave element

For slave element exist two type of variables, the general variables that are 
common for all type of elements and managed internally by QElectroTech, and the specific 
variables for this type of element.

QElectroTech does not allow defining variable values for slave element. QElectroTech does 
also not allows defining new variables. QElectroTech allows only displaying the specific 
variables at dynamic texts. 

General variables 

    * **% {l}**: Folio line number from the workspace where the element can be found
    * **% {c}**: Folio column number from the workspace where the element can be found
    * **% {id}**: Folio position in the project (Schema number)

Specific variables

    * **Position master element**: Internal pre-defined variable which is automatically displayed under dinamic texts of the element. The formula from the variable is ``(%id-%l%c)``, variables took from master element. 

.. note::

    QElectroTech allows also displaying the specific variables from the `Master element <../../../en/element/type/elementmaster.html>`_ at the dynamic text fields.