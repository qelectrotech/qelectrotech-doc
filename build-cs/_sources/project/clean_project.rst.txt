.. _project/clean_project

=============
Clean project
=============

QElectroTech stores on the project database every `title block`_, `conductor`_, `element`_, etc. 
which is introduced by the user. If the user deletes one `element`_ or replace the `title block`_ 
from the `folio`_, the `element`_ or `title block`_ will be deleted from the `folio`_ but it will 
still be storage at the project database. 

QElectroTech allows cleaning the project database from `menu bar`_. 

    1. Select **Project > Clean project** menu item to open the cleaning project PopUP window.

    .. figure:: ../images/qet_menu_project.png
        :align: center

        Figure: QElectroTech cleaning project PopUP window 

    2. Select the check buttons desired (templates, elements, categories).
    3. Press the button **OK** to clean the `project`_ and close the cleaning project PopUP window.

    .. figure:: ../images/qet_project_clean.png
        :align: center

         Figure: QElectroTech Project menu 

.. note::

   Cleaning the `project`_ is recomended to reduce the size of the project file and inclease the 
   loading speed.

.. _project: ../project/index.html
.. _folio: ../folio/index.html
.. _title block: ../folio/title_block/index.html
.. _element: ../element/index.html
.. _conductor: ../conductor/index.html
.. _Menu bar: ../interface/menu_bar.html