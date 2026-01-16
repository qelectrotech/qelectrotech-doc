.. _reports/summary/edit_summary:

============
Edit summary
============

The summary properties can only be displayed from `selection properties panel`_ once the summary table 
has been selected at `workspace`_.

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_display.png
   :align: center

   Figure: QElectroTech summary properties panel, display tab

.. note::

   If the `selection properties panel`_ is not displayed, it can be displayed from **Settings > Display > Selection properties**.

Summary geometry and line
#########################

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_geometry_and_lines.png
   :align: center

   Figure: QElectroTech summary geometry and lines properties

The **Geometry and lines** section from the summary properties allows defining:

* Summary table position (coordinates **X** and **Y**) in the `folio`_.
* Maximum number of table rows.
* Adjust the size of the table to the `folio`_, automatic margin definition.
* Define previous summary table, property to be used if the number of `folios`_ is higher than the maximum number of rows defined. 

.. note::

   If the number of `folios`_ is higher than the maximum number of rows defined, each summary 
   table has to have a **Table name** defined. Without **Table name**, the link between tables 
   cannot be defined.

Header
######

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_header.png
   :align: center

   Figure: QElectroTech summary header properties

The **Header** section from the summary properties allows defining:

* Top, bottom, left and right margin in the header cells.
* Text alignment in the header cells.
* Text font of the table header.

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_font.png
   :align: center

   Figure: QElectroTech summary table text font

Table
#####

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_table.png
   :align: center

   Figure: QElectroTech summary table properties panel

The **Table** section from the summary properties allows defining:

* Top, bottom, left and right margin in the table cells.
* Text alignment in the table cells.
* Text font of the table.

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_font.png
   :align: center

   Figure: QElectroTech summary table text font

Content request
###############

The `folio properties`_ to be displayed at the summary tables, the columns information, can be 
modified and re-organized at any time.

To modify the content request form the summary:

1. `Select`_ one of the tables from the summary to display the summary properties at `selection properties panel`_.
2. Go to **Content** tab.

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_content.png
   :align: center

   Figure: QElectroTech summary properties panel, content tab

3. Click **Request** button to display the content configuration PopUp window.
4. Modify the table content using the following commands:

   =================      ===============================      ========================================
   Icon                   Action                               Keyboard shortcut
   =================      ===============================      ========================================
     |go-up|                Move up this field                   
     |list-add|             Add field to display list           Double click on field at available list
     |list-remove|         Remove field from display list       Double click on field at display list
     |go-down|              Move down this field                 
   =================      ===============================      ========================================

.. figure:: /_external/_images/en/qet_summary/qet_summary_properties_content_request.png
   :align: center

   Figure: QElectroTech summary properties content request PopUp window

   .. note::

         The content request configuration can be saved and chosen from **Configuration** section to increase working efficiency.

         QElectroTech is working with SQLite database, summary table content can also be defined by SQL query. 

5. Once the desired configuration is defined, press **OK** to apply changes.

.. |go-down| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-down.png
.. |go-up| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-up.png
.. |list-add| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-add.png
.. |list-remove| image:: /_external/_images/_site-assets/user/ico/16x16/list/list-remove.png

.. _selection properties panel: ../../interface/panels/selection_properties_panel.html
.. _workspace: ../../interface/workspace.html
.. _folio: ../../folio/index.html
.. _folios: ../../folio/index.html
.. _folio properties: ../../folio/properties/index.html
.. _Select: ../../schema/select/index.html
