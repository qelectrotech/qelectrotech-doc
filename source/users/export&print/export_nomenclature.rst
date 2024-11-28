.. _export&print/export_nomenclature:

Export nomenclature
===================

QElectroTech allows creating a CSV file which contains a list of all `elements`_ from the active project. 
The CSV file can be opened and edited with tools as `LibreOffice Calc`_.  

The different field properties are listed by columns and the `elements`_ are ordered by `folio`_.

To export the nomenclature list to CSV file:

1. Select **Project > Export to CSV** menu item to open the exporting parameter PopUP window.

.. figure:: /_external/_images/en/qet_menu/qet_menu_project.png  
            :align: center

            Figure: QElectroTech project menu

2. Modify the list of information to be exported by the commands of the following table.

=================      ===============================      ========================================
Icon                   Action                               Keyboard shortcut
=================      ===============================      ========================================
|go-up|                Move up this field                   
|list-add|             Add field to export list             Double click on field at available list
|list-remove|          Remove field from export list        Double click on field at export list
|go-down|              Move down this field                 
=================      ===============================      ========================================

.. figure:: /_external/_images/en/qet_export/qet_export_nomenclature.png
            :align: center

            Figure: QElectroTech export nomenclature PopUp window

3. Define the filtering parameters (**Filter by** and type of `elements`_).

.. note::

         The content and filtering request configuration can be saved and chosen from **Configuration** section to increase working efficiency.

         QElectroTech is working with SQLite database, summary table content can also be defined by SQL query. 
    
4. Define page layout parameters (include table header and type of format).
5. Press **OK** button to apply exporting parameters and display the **Save As** PopUp window.
6. Choose target directory and file name.
7. Press **Save** button to create the file with extension ``.csv``.


.. _LibreOffice Calc: https://www.libreoffice.org/

.. |go-down| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-down.png
.. |go-up| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-up.png
.. |list-add| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-add.png
.. |list-remove| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-remove.png

.. _elements: ../element/index.html
.. _folio: ../folio/index.html
