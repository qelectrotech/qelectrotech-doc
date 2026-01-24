.. SPDX-FileCopyrightText: 2026 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _folio/title_block/collection/title_block_project_collection:

==============================
Title block project collection
==============================

The project collection is the only `collection`_ which is not part from the software structure. A 
project collection is a `title block collection`_ that is part of the project file, each `project`_ 
has its own `title block collection`_. 

.. figure:: /_external/_images/en/qet_title/qet_title_block_collection_project.png
   :align: center

   Figure: QElectroTech project tree

QElectroTech does not allow working on this `collection`_, the user cannot add or delete any 
`title block`_ manually. The user can only edit `title blocks`_ used in the project without 
modifying the original `title block`_ from `QET`_ or `User`_ collection.

The `title block`_ is copied from `QET`_ or `User`_ collection automatically by QElectroTech when 
the user introduces a new `title block`_ in one `folio`_ of the `project`_. If the `title block`_ has 
already been used previously, QElectroTech does not need to add again the `title block`_ to the 
project collection.

If one `title block`_ is deleted from the `project`_, QElectroTech does not delete the `title block`_ 
from the project collection automatically, the `title block`_ is marked in red. 
`Cleaning the project`_ deletes all `title block`_ from the project collection that 
are not used inside the `project`_ automatically at the cleaning time. 

.. _title block: ../../../folio/title_block/index.html
.. _title blocks: ../../../folio/title_block/index.html
.. _project: ../../../project/index.html
.. _folio: ../../../folio/index.html
.. _title block collection: ../../../folio/title_block/collection/what_is.html
.. _collection: ../../../folio/title_block/collection/what_is.html
.. _QET: ../../../folio/title_block/collection/title_block_qet_collection.html
.. _User: ../../../folio/title_block/collection/title_block_user_collection.html
.. _clean the project: ../../../project/clean_project.html
.. _Cleaning the project: ../../../project/clean_project.html