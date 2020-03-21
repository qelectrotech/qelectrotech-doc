.. _folio/title_block/title_block_delete

==================
Delete title block
==================

The title blocks templates can only be deleted from `project panel`_. QElectroTech does not allow 
deleting templates from any menu item.

.. note::

   If the `project panel`_ is not displayed, it can be displayed from **Settings > Display > Projects**.

It is important to make difference between the `project embedded collection`_ and `QET`_ or `User`_ 
collection. The `project embedded collection`_ is in the project "database", delete information from 
the project does not change anything at QElectroTech or in the computer file system. Deleting information 
from `QET`_ or `User`_ collection deletes information from QElectroTech "database" and in the computer file 
system, the information deleted in these "databases" can never be recovered. 

Delete title block from project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Right click on one title block template from `project embedded collection`_ which should be deleted. 
    2. Click the option **Delete this template** to delete the template form project "database".

        .. figure:: ../../images/qet_title_block_panel_project_embedded_options.png
            :align: center

            Figure: QElectroTech Project panel

Delete title block from collection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    1. Right click on the title block template from `QET`_ or `User`_ collections which should be deleted. 
    2. Click the option **Delete this template** to delete the template form QElectroTech and from the file system.

        .. figure:: ../../images/qet_title_block_panel_project_user_options.png
            :align: center

            Figure: QElectroTech Project panel
    
    3. Press **YES** to confirm the action.

        .. figure:: ../../images/qet_title_block_delete_confirmation.png
            :align: center

            Figure: QElectroTech delete title block confirmation PopUP window

.. warning::

    The template deleted from one collection cannot be recovered, it will be deleted from QElectroTech 
    "dataabse" and from the computer file system. Be sure about the operation.

.. _project panel: ../../interface/panels/projects_panel.html
.. _QET: ../../folio/title_block/collection/title_block_qet_collection.html
.. _User: ../../folio/title_block/collection/title_block_user_collection.html
.. _project embedded collection: ../../folio/title_block/collection/title_block_project_collection.html
