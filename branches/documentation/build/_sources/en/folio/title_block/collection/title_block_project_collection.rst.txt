.. _en/folio/title_block/collection/title_block_project_collection

==============================
Title block project collection
==============================

The project collection is the only `collection`_ which is not part from the software structure. A 
project collection is a `title block collection`_ that is part of the project file, each `project`_ 
has its oun `title block collection`_. 

.. figure:: graphics/qet_project_title_block_collection.png
   :align: center

   Figure: QElectroTech project tree

QElectroTech does not allow to work on this `collection`_, the user cannot add or delete manually 
any `title block`_. The user can use the collection to access to the `title blocks`_ of the `project`_ 
for editing them.

The `title block`_ are copied from `QET`_ or `User`_ collection automatically by QElectroTech when 
the user introduces a new `title block`_ at one `folio`_ of the `project`_. If the `title block`_ has 
already been used previously, QElectroTech does not need to add the `title block`_ again to the 
project collection.

If one `title block`_ is deleted from the `project`_, QElectroTech does not delete the `title block`_ 
automatically from the project collection. The `title block`_ is marked on red as some of the 
`title blocks`_ showed at the figure above. For this reason, is recomended to `clean the project`_ at 
the end. `Cleaning the project`_ delete automatically all the `title block`_ from the project 
collection that are not used inside the `project`_ at the cleaning time and reduce the size of the 
project file. 

.. _title block: ../../../../en/folio/title_block/index.html
.. _title blocks: ../../../../en/folio/title_block/index.html
.. _project: ../../../../en/project/index.html
.. _folio: ../../../../en/folio/index.html
.. _title block collection: ../../../../en/folio/title_block/collection/what_is.html
.. _collection: ../../../../en/folio/title_block/collection/what_is.html
.. _QET: ../../../../en/folio/title_block/collection/title_block_qet_collection.html
.. _User: ../../../../en/folio/title_block/collection/title_block_user_collection.html
.. _clean the project: ../../../../en/project/clean_project.html
.. _Cleaning the project: ../../../../en/project/clean_project.html