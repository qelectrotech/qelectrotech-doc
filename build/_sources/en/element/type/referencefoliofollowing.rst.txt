.. _en/element/type/referencefoliofollowing

==========================
Reference folio following
==========================

Element which link the end of a conductor with the begining of the conductor represented at 
previous, following or the same folio.

.. figure:: graphics/qet_element_reference_folio.png
   :align: center

   Figure: QElectroTech reference folio following

For reference folio following element exist two type of variables, the general variables that are 
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
    * **Label**: Internal variable which defines the position of the linked previous referencing element. It is defined as ``%id-%l%c``, variables took from the cross reference linked element.
    * **Voltage/Protocol**: Voltage/Protocol property from the conductor connected to the element terminal.