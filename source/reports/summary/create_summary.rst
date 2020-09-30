.. _reports/summary/create_summary

==============
Create summary
==============

A `project`_ can be a group of `folios`_, for this reason the possibility to make a summary, project index, which shows some 
information about the different `folios`_ is necessary. QElectroTech allows creating this summary as a 
table automatically.

.. figure:: ../../images/qet_list_folios.png
        :align: center

        Figure: QElectroTech list of folios

To create a project summary:

   1. Activate the folio where the summary table has to be created in the `workspace`_.
   2. Select **Project > Add a summary** to display the configuration PopUp window of the summary creator.

      .. figure:: ../../images/qet_menu_project.png
         :align: center

         Figure: QElectroTech project menu
   
   3. Go to **Display** tab to define display table properties.
   4. Define the **Table name** which will identify the table.
   5. Configure the display table settings (header and table cells properties, auto adjustment of table size, etc.).

      .. figure:: ../../images/qet_summary_add_display.png
         :align: center

         Figure: QElectroTech project menu

   6. Go to **Content** tab to define table columns.

      .. figure:: ../../images/qet_summary_add_content.png
         :align: center

         Figure: QElectroTech project menu
   
   7. Modify the list of information to be displayed according the commands of the following table.

      =================      ===============================      ========================================
      Icon                   Action                               Keyboard shortcut
      =================      ===============================      ========================================
      |go-up|                Move up this field                   
      |list-add|             Add field to display list            Double click on field at available list
      |list-remove|          Remove field from display list       Double click on field at display list
      |go-down|              Move down this field                 
      =================      ===============================      ========================================

   8. Once the desired configuration is defined, press **OK** to create summary tables and close the PopUp window.

.. note::

   The project summary can be created, modified and updated at any time. 

.. |go-down| image:: ../../images/ico/16x16/go-down.png
.. |go-up| image:: ../../images/ico/16x16/go-up.png
.. |list-add| image:: ../../images/ico/16x16/list-add.png
.. |list-remove| image:: ../../images/ico/16x16/list-remove.png

.. _project: ../../project/index.html
.. _folio: ../../folio/index.html
.. _folios: ../../folio/index.html
.. _workspace: ../../interface/workspace.html
