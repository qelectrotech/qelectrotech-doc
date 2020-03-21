.. _conductor/properties/conductor_numbering

====================
Conductor numbering
====================

QElectroTech allows an automatic codification of `conductors`_. This feature is very usefull for the 
creation of `reports`_, `conductor list`_, and for the identification of `conductors`_ at the physical 
systems and `schemas`_. 

QElectroTech allows the definition of multiples auto numbering patterns. It also provides many 
flexibility on the creation of auto numbering patterns using text, variables and sequential numbers. 

.. figure:: ../../images/qet_project_properties_auto_numbering.png
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
        Installation or functional unit to which the cable belongs (`schema`_ where the cable can be found).

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

    For more information about how to define auto numbering patterns, refer to 
    `project auto numbering properties`_ section.

    For more information about how to manage the codification of conductors, refer to 
    `create conductor`_ section.

.. _IEC 81346: https://www.iso.org/standard/50858.html
.. _conductors: ../../conductor/index.html
.. _reports: ../../reports/index.html
.. _conductor list: ../../reports/conductor_list.html
.. _schemas: ../../schema/index.html
.. _schema: ../../schema/index.html
.. _create conductor: ../../schema/conductor/conductor_creation.html
.. _project auto numbering properties: ../../project/properties/numbering_prop.html