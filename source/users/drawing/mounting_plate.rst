.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _drawing/mounting_plate:

=====================
Design mounting plate
=====================

QElectroTech is not only a tool for diagrams and shemas, QElectroTech allows also drawing 2D drawings. 
Electrical boxes, buttons, switches, screens and any other type of components can be drawn at the 
`workspace`_.

2D drawings from electrical component can be created at the `element editor`_ as
`elements`_. After the creation of component drawings, assembled panel drawings can be created 
introducing the `elements`_ at the `workspace`_. At the category **Graphics** from 
`QET collection`_ some common electrical components front views are provided as `elements`_.

.. note::

   For more information about how to create `elements`_, refer to `Create or edit element`_ 
   section.
   
   For more information about how to introduce `elements`_ at `workspace`_, refer 
   to `Working with element`_ section.

The advantage of drawing mounting plates using QElectroTech and not with a different CAD tool is the 
posibility to create links between the `elements`_. A link between the `elements`_ which represents 
the electrical component at the `schema`_ and the `elements`_ which represents the component at the 
drawing will reduce the future effort; the effort from the manufacturing, intallation and maintenace 
phase of the project.

.. figure:: /_external/_images/en/qet_mounting_plate.png
   :align: center

   Figure: QElectroTech Mounting plate example

.. _workspace: ../interface/workspace.html
.. _element: ../element/index.html
.. _elements: ../element/index.html
.. _schema: ../schema/index.html
.. _QET collection: ../element/collection/default_collection.html
.. _element editor: ../element/element_editor/index.html
.. _Create or edit element: ../element/element_editor/edition/index.html
.. _Working with element: ../schema/element/index.html