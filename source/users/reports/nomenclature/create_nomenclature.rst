.. _reports/nomenclature/create_nomenclature:

===================
Create nomenclature
===================

A `project`_ is a combination / assembly of `elements`_ / components, QElectroTech provides the feature to create a nomenclature, 
also known as Bill Of Materials (BOM), which shows the information about the different `elements`_ / components. QElectroTech allows 
creating the nomenclature automatically.


.. .. figure:: ../../images/qet_bom.png
        :align: center

        Figure: QElectroTech Bill Of Materials (BOM)


To create a project nomenclature:

1. Activate the folio where the nomenclature table has to be created.
2. Select **Project > Add a nomenclature** to display the configuration PopUp window of the nomenclature creator.

.. figure:: /_external/_images/en/qet_menu/qet_menu_project.png
   :align: center

         Figure: QElectroTech project menu
   
3. Go to **Display** tab to define display table properties.
4. Define the **Table name** which will identify the table.
5. Configure the display table settings (header and table cells properties, auto adjustment of table size, etc.).

.. figure:: /_external/_images/en/qet_nomenclature/qet_nomenclature_add_display.png
   :align: center

         Figure: QElectroTech project menu

6. Go to **Content** tab to define table columns.
7. Modify the list of information to be displayed according the commands of the following table.

+---------------------+-----------------------------------------------------------+---------------------------+
| Icon                |Action                                                     | Keyboard shortcut         |
+=====================+===========================================================+===========================+
|  |go-up|            | Move up this field                                        |  ``Ctrl + shift + Home``  |
+---------------------+-----------------------------------------------------------+---------------------------+
| |list-add|          | Add field to display list                                 |  ``Ctrl + shift + Up``    |
+---------------------+-----------------------------------------------------------+---------------------------+
|  |list-remove|      | Remove field from display list                            |  ``Ctrl + shift + Down``  |
+---------------------+-----------------------------------------------------------+---------------------------+
|  |go-down|          | Move down this field                                      |  ``Ctrl + shift + End``   |
+---------------------+-----------------------------------------------------------+---------------------------+

.. figure:: /_external/_images/en/qet_nomenclature/qet_nomenclature_add_content.png
   :align: center

         Figure: QElectroTech project menu

      .. note::

         The content request configuration can be saved and chosen from **Configuration** section to increase working efficiency.

         QElectroTech is working with SQLite database, nomenclature table content can also be defined by SQL query. 

8. Define the filtering parameters (**Filter by** and type of `elements`_).
9. Once the desired configuration is defined, press **OK** to create nomenclature tables.

.. note::

   The project nomenclature can be created, modified and updated at any time. 

.. |go-down| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-down.png
.. |go-up| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-up.png
.. |list-add| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-add.png
.. |list-remove| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-remove.png

.. _project: ../../project/index.html
.. _folio: ../../folio/index.html
.. _folios: ../../folio/index.html
.. _workspace: ../../interface/workspace.html
.. _elements: ../../element/index.html
