.. _element/type/element_slave:

==================
Slave element
==================

The slave elements represent the power circuit devices such the main contactors from 
power contactors. The slave elements also represent the auxiliary contactors. Even if an 
auxiliary contactor is part of the command circuit, its activation is forced by another 
element.

.. figure:: /_external/_images/en/qet_element/qet_element_slave.png
   :align: center

   Figure: QElectroTech slave element

For slave element exist two type of variables, the general variables that are 
common for all type of elements and managed internally by QElectroTech, and the specific 
variables for this type of element.

QElectroTech does not allow defining variable values for slave element. QElectroTech does 
also not allows defining new variables. QElectroTech allows only displaying the specific 
variables at dynamic texts. 

General variables 

* **% {F}**: Label from the folio where the element can be found
* **% {f}**: Number from the folio where the element can be found
* **% {M}**: Plant variable from the folio where the element can be found
* **% {LM}**: Location variable of the folio where the element can be found
* **% {l}**: Folio line number from the workspace where the element can be found
* **% {c}**: Folio column number from the workspace where the element can be found
* **% {id}**: Folio position in the project (Schema number)

Specific variables

* **Position master element**: Internal pre-defined variable which is automatically displayed under dinamic texts of the element. The default formula from the variable is ``(%id-%l%c)``, variables took from master element. 

.. seealso::

    The default formula from the **Position master element** and the position where it should be 
    displayed can be defined at cross references tab from **New project** preferences.  

.. note::

    QElectroTech allows also displaying the specific variables from the `Master element <../../element/type/elementmaster.html>`_ at the dynamic text fields.