.. _reports/summary/create_summary

==============
Create summary
==============

A `project`_ can be a group of `folios`_, QElectroTech provides the possibility to make a summary, project index, which shows the 
information from the different `folios`_. QElectroTech allows creating the project summary automatically.

.. figure:: /_external/_images/en/qet_list_folios.png
        :align: center

        Figure: QElectroTech list of folios

To create a project summary:

1. Activate the folio where the summary table has to be created in the `workspace`_.
2. Select **Project > Add a summary** to display the configuration PopUp window of the summary creator.

.. figure:: /_external/_images/en/qet_menu/qet_menu_project.png
   :align: center

         Figure: QElectroTech project menu
   
3. Go to **Display** tab to define display table properties.
4. Define the **Table name** which will identify the table.
5. Configure the display table settings (header and table cells properties, auto adjustment of table size, etc.).

.. figure:: /_external/_images/en/qet_summary/qet_summary_add_display.png
   :align: center

         Figure: QElectroTech project menu

6. Go to **Content** tab to define table columns.
7. Modify the table content using the following commands:

=================      ===============================      ========================================
Icon                   Action                               Keyboard shortcut
=================      ===============================      ========================================
|go-up|                Move up this field                   
|list-add|             Add field to display list            Double click on field at available list
|list-remove|          Remove field from display list       Double click on field at display list
|go-down|              Move down this field                 
=================      ===============================      ========================================

.. figure:: /_external/_images/en/qet_summary/qet_summary_add_content.png
   :align: center

         Figure: QElectroTech project menu

      .. note::

         The content request configuration can be saved and chosen from **Configuration** section to increase working efficiency.

         QElectroTech is working with SQLite database, summary table content can also be defined by SQL query. 

8. Once the desired configuration is defined, press **OK** to create summary tables.

.. note::

   The project summary can be created, modified and updated at any time. 

.. |go-down| image::/_external/_images/_site-assets/user/ico/16x16/go/go-down.png
.. |go-up| image::/_external/_images/_site-assets/user/ico/16x16/go/go-up.png
.. |list-add| image::/_external/_images/_site-assets/user/ico/16x16/list/list-add.png
.. |list-remove| image::/_external/_images/_site-assets/user/ico/16x16/list/list-remove.png

.. _project: ../../project/index.html
.. _folio: ../../folio/index.html
.. _folios: ../../folio/index.html
.. _workspace: ../../interface/workspace.html
