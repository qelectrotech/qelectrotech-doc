.. _element/properties/element_numbering:

===================
Element numbering
===================

QElectroTech allows an automatic codification of `elements`_. This feature is useful for the 
creation of reports, `Bill of Materials (BOM)`_, and for the identification of devices at the physical 
installation and schemas. 

QElectroTech allows defining multiples auto numbering patterns. It also provides many flexibility 
on the creation of auto numbering pattern using text, variables and sequential numbers. 

.. figure:: /_external/_images/en/qet_element/qet_element_prop_auto_numbering.png
   :align: center

   Figure: QElectroTech element auto numbering 

.. admonition:: Example
    
    +---+------+
    | X | AAAA |
    +---+------+

    :X:
        Code defined by `IEC 81346`_ norm.

        * **A**: Two or more purposes or tasks.
        * **B**: Converting an input variable into a signal for further processing.
        * **C**: Storing of energy, information or material.
        * **E**: Providing radiant or thermal energy.
        * **F**: Direct protection from dangerous or unwanted conditions.
        * **G**: Initiating a flow of energy or material.
        * **H**: Producing a new kind of material or product.
        * **K**: Processing signals or information.
        * **M**: Providing mechanical energy for driving purposes.
        * **P**: Presenting information.
        * **Q**: Controlled switching or varying a flow of energy, of signals or of material.
        * **R**: Restricting or stabilizing motion or a flow of energy or material.
        * **S**: Converting a manual operation into a signal for further processing.
        * **T**: Conversion of energy maintaining the kind of energy.
        * **U**: Keeping objects in a defined position.
        * **V**: Processing (treating) of material or products.
        * **W**: Guiding or transporting from one place to another.
        * **X**: Connecting objects
        
    :AAAA:
        Alphanumeric code which identify the element.

.. seealso::

    For more information about how to define auto numbering patterns, refer to `project auto numbering properties`_ section.

    For more information about how to manage the codification of conductors, refer to `add element`_ section.

.. _IEC 81346: https://www.iso.org/standard/50858.html

.. _Bill of Materials (BOM): ../../reports/component_list.html
.. _elements: ../../element/index.html
.. _project auto numbering properties: ../../project/properties/numbering_prop.html
.. _Add element: ../../schema/element/element_add.html
