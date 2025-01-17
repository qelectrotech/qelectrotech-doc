.. _element/type/element_master:

==================
Master element
==================

The master elements represent the devices from the command circuit such the coil from a relay or 
contactor.

.. figure:: /_external/_images/en/qet_element/qet_element_master.png
   :align: center

   Figure: QElectroTech master element

For master element exist two type of variables, the general variables that are 
common for all type of elements and managed internally by QElectroTech, and the specific 
variables for this type of element.

QElectroTech allows defining variable values from master element at the **Selection properties** 
panel. QElectroTech does not allow defining new variables. QElectroTech allows only displaying 
variables at dynamic texts and define value of the specific variables.

.. note::

If the Selection properties panel is not displayed, it can be displayed from **Settings > Display > Selection properties**.

General variables 

* **% {F}**: Label from the folio where the element can be found
* **% {f}**: Number from the folio where the element can be found
* **% {M}**: Plant variable from the folio where the element can be found
* **% {LM}**: Location variable of the folio where the element can be found
* **% {l}**: Folio line number from the workspace where the element can be found
* **% {c}**: Folio column number from the workspace where the element can be found
* **% {id}**: Folio position in the project (Schema number)

Specific variables

* **Label formula**: Definition of the formula which defines the **Label** value. If a auto numbering pattern is selected during terminal creation, QElectroTech defiens ``%autnum`` as default formula.
* **Label**: Internal variable which is used to defines the element code.
* **Annotation**: Internal variable, it cannot be a formula (group of other variables).
* **Textual description**: Internal variable, it cannot be a formula (group of other variables).
* **Article number**: Internal variable which, it cannot be a formula (group of other variables).
* **Manufacturer**: Internal variable, it cannot be a formula (group of other variables).
* **Order number**: Internal variable, it cannot be a formula (group of other variables).
* **Supplier**: Internal variable, it cannot be a formula (group of other variables).
* **Auxiliry block 1**: Internal variable, it cannot be a formula (group of other variables).
* **Auxiliry block 2**: Internal variable, it cannot be a formula (group of other variables).
* **Internal number**: Internal variable, it cannot be a formula (group of other variables).
* **Location**: Internal variable, it cannot be a formula (group of other variables).
* **Function**: Internal variable, it cannot be a formula (group of other variables).
* **Voltage/Protocol**: Internal variable, it cannot be a formula (group of other variables).