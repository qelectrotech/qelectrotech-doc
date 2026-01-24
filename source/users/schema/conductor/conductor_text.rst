.. SPDX-FileCopyrightText: 2026 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _users/schema/conductor/conductor_text:

========================
Define text at conductor
========================

QElectroTech allows defining and displaying information text at each `conductor`_. 

.. note::

   Only `multiline conductors`_ allow text definition.

To define the conductor text:

1. `Select the conductor`_ which should be edited. 
2. `Display conductor properties`_ PopUp window.
3. Go to multiline section from **Type** tab.

.. figure:: /_external/_images/en/qet_conductor/qet_conductor_properties_type_multiline.png
            :align: center

            Figure: QElectroTech multiline conductor text section

4. Choose the desired parameters for text positioning, text content or formula, text size, etc.
5. Click the check button **Apply properties to all conductor of this potential** if the changes should be applied for all `conductor`_ with common initial or end `terminal`_.
6. Press **OK** button to save and apply the property changes.

.. seealso::

   For more information about multiline properties, refer to `conductor type properties`_ 
   section.

   For more information about automatic text definition during conductor creation, refer to 
   `project folio properties`_ section.

.. _conductor: ../../conductor/index.html
.. _conductors: ../../conductor/index.html
.. _terminal: ../../element/element_parts/terminal.html
.. _multiline conductors: ../../conductor/type/multiline_conductor.html
.. _Select the conductor: ../../schema/select/select_object.html
.. _Display conductor properties: ../../conductor/properties/display_conductor_properties.html
.. _conductor type properties: ../../conductor/properties/conductor_type.html
.. _project folio properties: ../../project/properties/new_folio/conductor.html