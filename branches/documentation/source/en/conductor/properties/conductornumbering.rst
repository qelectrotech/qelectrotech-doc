.. _en/conductor/properties/conductornumbering

====================
Conductor numbering
====================

QElectroTech allows an automatic codification of conductors. This feature is very usefull for the 
creation of reports, cable list, and for the identification of cables at the physical installation and 
schemas. 

QElectroTech allows the definition of multiples auto numbering pattern. It also provides many flexibility 
on the creation of auto numbering pattern using text, variables and sequential numbers. 

.. figure:: graphics/qet_conductor_auto_numbering.png
   :align: center

   Figure: QElectroTech conductor auto numbering 

.. admonition:: Example

    Taking the content from the image above:
    
    +---+---+----+-----+---+
    | W | X | XX | XXX | N |
    +---+---+----+-----+---+

    :W:
        Code defined by `IEC 81346`_ norm.

            * **W**: Guiding or transporting from one place to another.
    :X:
        Alphanumeric code corresponding to the following coding:

            * H: High voltage
            * B: 400 V AC 
            * C: 230 V AC 
            * D: Digital signal
            * A: Analog signal 
            * @: Network

    :XX:
        Installation or functional unit to which the cable belongs (schema where the cable can be found).

            * 001: Incoming plant
            * 002: Global auxiliary power
            * 003: Distribution Network
            * 004: instalation 1
            * 005: installation 2
            * ...
            * 999: ...

    :XXX:

        Folio where the cable is represented.
    
    :N:
        Cable number.

.. seealso::

    For more information about how to define auto numbering patterns, please refers to: `project auto numbering properties <../../project/properties/numberingprop.html>`_ section.

    For more information about how to manage the codification of conductors, please refers to: `create conductor <../../schema/conductor/conductorcreation.html>`_ section.

.. _IEC 81346: https://www.iso.org/standard/50858.html