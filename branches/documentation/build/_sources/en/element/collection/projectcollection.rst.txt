.. _en/element/collection/projectcollection

==================
Project collection
==================

The project collection is the only collection which is not part from the software structure. A project 
collection is an element collection that is part of the project file, each project has its oun element 
collection. 

.. figure:: graphics/qet_collection_project.png
   :align: center

   Figure: QElectroTech project collection

QElectroTech does not allow to work on this collection, the user cannot add or delete manually any element, 
category or sub-category. The user can only read the category or sub-category properties and use the 
collection to access to the elements of the project for editing them.

The elements are copied from QET or user collection automatically by QElectroTech when the user 
introduces a new element at one folio of the project. If the element has already been used previously, 
QElectroTech does not need to add the element again to the project collection.

If one element is deleted from the project, QElectroTech does not delete the element automatically from 
the project collection. The element is marked on red as some of the elements showed at the figure above. 
For this reason, is recomended to `clean the project <../../../en/project/cleanproject.html>`_ at 
the end. `Cleaning the project <../../../en/project/cleanproject.html>`_ delete automatically 
all the elements from the project collection that are not used inside the project at the cleaning 
time and reduce the size of the project file. 