.. _element/type/reference_folio_following:

==========================
Reference folio following
==========================

Element which link the end of a `conductor`_ with the begining of the `conductor`_ represented at 
previous, following or the same `folio`_.

.. figure:: /_external/_images/en/qet_element/qet_element_reference_folio.png
   :align: center

   Figure: QElectroTech reference folio following

For reference folio following element exist two type of variables, the general variables that are 
common for all type of `elements`_ and the specific variables for this type of `element`_.

QElectroTech does not allow defining variable values for this type of `element`_. QElectroTech does 
also not allows defining new variables. QElectroTech allows only displaying the specific variables 
at `dynamic texts`_. 

General variables 

* **% {F}**: Label from the `folio`_ where the `element`_ can be found.
* **% {f}**: Number from the `folio`_ where the `element`_ can be found.
* **% {M}**: Plant variable from the `folio`_ where the `element`_ can be found.
* **% {LM}**: Location variable of the `folio`_ where the `element`_ can be found.
* **% {l}**: Folio line number from the `workspace`_ where the `element`_ can be found.
* **% {c}**: Folio column number from the `workspace`_ where the `element`_ can be found.
* **% {id}**: Folio position in the `project`_ (Schema number).

Specific variables

* **Function**: Function property from the `conductor`_ connected to the `element terminal`_.
* **Label**: Internal variable which defines the position of the linked `previous reference folio`_ element.
* **Voltage/Protocol**: Voltage/Protocol property from the `conductor`_ connected to the `element terminal`_.

.. note:: 

    The **Label** property can be defined as a formula by the user at `New folio`_ section from 
    `project properties`_. By default the formula is ``%id-%l%c``, variables took from 
    `previous reference folio`_ linked element.

    For more information about how to define the **Label** formula, please refers to 
    `folio referencing project properties`_.

.. _conductor: ../../conductor/index.html
.. _folio: ../../folio/index.html
.. _element: ../../element/index.html
.. _elements: ../../element/index.html
.. _project: ../../project/index.html
.. _workspace: ../../interface/workspace.html
.. _element terminal: ../../element/element_parts/terminal.html
.. _dynamic texts: ../../element/element_parts/dynamic_text.html
.. _previous reference folio: ../../element/type/previous_reference_folio.html
.. _project properties: ../../project/properties/index.html
.. _New folio: ../../project/properties/new_folio/index.html
.. _folio referencing project properties: ../../project/properties/new_folio/folio_referencing.html