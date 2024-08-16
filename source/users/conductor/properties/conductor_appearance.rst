.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _conductor/properties/conductor_appearance:

====================
Conductor appearance
====================

The color, type and width from the line of the schema that represents the conductor 
can be defined. A line can have a main color and, if desired, a secondary color.

.. note::

    The secondary line is used when a dashes line with double color is desired.

        .. figure:: /_external/_images/en/qet_conductor/qet_conductor_secundary_line.png
            :align: center

            Figure: Conductor with red secundary color

.. figure:: /_external/_images/en/qet_conductor/qet_conductor_properties_appearance.png
   :align: center

   Figure: Multiline conductor appearance

* The different types of lines are: **Solid**, **Dashed** and **Dots and dasches**.
* The possible colors are defined by the `RGB scale range`_.
* The possible line thiknes are between 0.4 and 10 mm (0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, ... , 10). 

.. note::

    QElectroTech provides the option to pre-define the appearance of conductor before starting to 
    draw conductos at the folio. This feature increase the working eficiency and avoid defining the 
    appearence conductor by conductors after their creation.

    For more information about appearance pre-definition, refer to `folio properties`_ section.

.. _folio properties: ../../folio/properties/folio_appearance.html
.. _RGB scale range: ../../annex/color.html