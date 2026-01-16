.. _element/collection/project_collection:

==================
Project collection
==================

The project collection is the only collection which is not part from the software structure. A project 
collection is an element collection that is part of the project file, each `project`_ has its own element 
collection. 

.. figure:: /_external/_images/en/qet_element/qet_element_collection_project.png
   :align: center

   Figure: QElectroTech project collection

QElectroTech does not allow working in this collection, the user cannot add or delete any element, 
category or sub-category manually. The user can only read the category or sub-category properties and use the 
collection to access to the `elements`_ of the `project`_ to edit them.

The elements are copied from `QET`_ or `User`_ collection by QElectroTech automatically when the user 
introduces a new `element`_ at one `folio`_ of the `project`_. If the `element`_ has already been used previously, 
QElectroTech does not add the `element`_ to the project collection again.

If one `element`_ is deleted from the `project`_, QElectroTech does not delete the `element`_ from the 
project collection automatically, the `element`_ is remarked in red. `Cleaning the project`_ deletes 
all elements from the project collection that are not used inside the project and reduces the size of 
the project file. 

.. _project: ../../project/index.html
.. _element: ../../element/index.html
.. _elements: ../../element/index.html
.. _folio: ../../folio/index.html
.. _QET: ../../element/collection/default_collection.html
.. _User: ../../element/collection/user_collection.html
.. _Cleaning the project: ../../project/clean_project.html