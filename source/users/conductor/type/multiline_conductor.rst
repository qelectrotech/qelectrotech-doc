.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _conductor/type/multiline_conductor:

====================
Multiline conductor
====================

Multiline conductors are used at `multiline diagrams`_. Multiline conductors are used for the 
representation of each terminal, line and phase from two and three phase power systems. 
Multiline conductors are used for the individual representation of all electric and control 
systems.

.. note::

   At fluid power schemas, a multiline conductor represents each pressure, return and 
   pilote line.

The main difference of multiline with respect to `single line conductors`_ is the posibility to 
display text which is linked to the `conductor properties`_. 

.. figure:: /_external/_images/en/qet_conductor/qet_conductor_multiline.png
   :align: center

   Figure: Multiline conductor

The main features of multiline conductors are:

    1. Possibility to define properties (Function and voltage/protocol)
    2. Text linked to the conductor which can be displayed and its position is relative to the conductor position.
    3. Possibility of displaying variables values at the conductor text (Auto numbering, function or voltage/protocol).
    4. Possibility of using the conductor variables at `element dynamic text`_ (Function and voltage/protocol).

.. _Multiline diagrams: ../../folio/type/multiline_diagram.html
.. _single line conductors: ../../conductor/type/single_line_conductor.html
.. _conductor properties: ../../conductor/properties/index.html
.. _element dynamic text: ../../element/element_parts/dynamic_text.html