.. SPDX-FileCopyrightText: 2026 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _project/properties/new_folio/folio_referencing:

=============================
Folio referencing properties
=============================

QElectroTech allows creating schemas with multiple `folios`_, only part of the `schema`_ is represented 
at each `folio`_. This means that part of a `conductor`_ can be at one `folio`_ and the continuation at a 
different `folio`_. 

QElectroTech provides folio referencing elements to indicate from where a `conductor`_ is coming or where 
it is going. These `elements`_ can display at the `workspace`_ from the `folio`_ some information about the 
folio referencing element linked. The information which should be displayed can be defined by the user 
at **Folio referencing** tab from **New Folio** section of the `project properties`_.

.. seealso::

    For more information about folio referencing, refer to `Reference folio following`_ and 
    `Previous reference folio`_. 

.. figure:: /_external/_images/en/qet_project/qet_project_folio_referencing_prop.png
   :align: center

   Figure: Project folio referencing properties window

To define folio referencing Label: 

1. `Display`_ project properties PopUP window.
2. Go to **New folio** section.
3. Go to **Folio referencing** tab.
4. Define the desired parameters for each field.
5. Press **OK** button to save the configuration changes and close project properties PopUP window.

.. _Display: ../../../project/properties/display.html
.. _folio: ../../../folio/index.html
.. _folios: ../../../folio/index.html
.. _conductor: ../../../conductor/index.html
.. _schema: ../../../schema/index.html
.. _elements: ../../../element/index.html
.. _workspace: ../../../interface/workspace.html
.. _project properties: ../../../project/properties/index.html
.. _Reference folio following: ../../../element/type/reference_folio_following.html
.. _Previous reference folio: ../../../element/type/previous_reference_folio.html