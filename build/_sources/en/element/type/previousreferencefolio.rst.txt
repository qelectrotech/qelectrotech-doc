.. _en/element/type/previousreferencefolio

========================
Previous reference folio
========================

Element which link the begining of a conductor with the end of the conductor represented at 
previous, following or the same folio.

.. figure:: graphics/qet_element_reference_folio.png
   :align: center

   Figure: QElectroTech previous reference folio

For previous referencing folio element exist two type of variables, the general variables that are 
common for all type of elements and the specific variables for this type of element.

QElectroTech does not allow defining variable values for this type of element. QElectroTech does 
also not allows defining new variables. QElectroTech allows only displaying the specific variables 
at dynamic texts. 

General variables 

    * **% {l}**: Folio line number from the workspace where the element can be found
    * **% {c}**: Folio column number from the workspace where the element can be found
    * **% {id}**: Folio position in the project (Schema number)

Specific variables

    * **Function**: Function property from the conductor connected to the element terminal.
    * **Label**: Internal variable which defines the position of the linked reference folio following element. It is defined as ``%id-%l%c``, variables took from the cross reference linked element.
    * **Voltage/Protocol**: Voltage/Protocol property from the conductor connected to the element terminal.