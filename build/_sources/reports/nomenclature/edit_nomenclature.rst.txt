.. _reports/nomenclature/edit_nomenclature

=================
Edit nomenclature
=================

The nomenclature properties can only be displayed from `selection properties panel`_ once the summary table 
has been selected at `workspace`_.

.. figure:: ../../images/qet_nomenclature_properties_display.png
   :align: center

   Figure: QElectroTech nomenclature properties panel, display tab

.. note::

   If the `selection properties panel`_ is not displayed, it can be displayed from **Settings > Display > Selection properties**.

Nomenclature geometry and line
##############################

.. figure:: ../../images/qet_summary_properties_geometry_and_lines.png
   :align: center

   Figure: QElectroTech summary geometry and lines properties

The **Geometry and lines** section from the summary properties allows defining:

   * Summary table position (coordinates **X** and **Y**) in the `folio`_.
   * Maximum number of rows of the table.
   * Adjust the size of the tables to the `folio`_, automatic margin definition.
   * Define previous summary table, property to be used if the number of `folios`_ is higher than the maximum number of rows defined. 

.. note::

   If the number of `folios`_ is higher than the maximum number of rows defined, each summary 
   table has to have a **Table name** defined. Without **Table name**, the link between tables 
   cannot be defined.

Header
######

.. figure:: ../../images/qet_summary_properties_header.png
   :align: center

   Figure: QElectroTech summary header properties

The **Header** section from the summary properties allows defining:

   * Top, bottom, left and right margin in the header cells.
   * Text alignment in the header cells.
   * Text font of the table header.

.. figure:: ../../images/qet_summary_properties_font.png
   :align: center

   Figure: QElectroTech summary table text font

Table
#####

.. figure:: ../../images/qet_summary_properties_table.png
   :align: center

   Figure: QElectroTech summary table properties panel

The **Table** section from the summary properties allows defining:

   * Top, bottom, left and right margin in the table cells.
   * Text alignment in the table cells.
   * Text font of the table.

.. figure:: ../../images/qet_summary_properties_font.png
   :align: center

   Figure: QElectroTech summary table text font

Content request
###############

The `folio properties`_ to be displayed at the summary tables, the columns information, can be 
modified and re-organized at any time.

To modify the content request form the summary:

   1. `Select`_ one of the tables from the summary to display the summary properties at `selection properties panel`_.
   2. Go to **Content** tab.

      .. figure:: ../../images/qet_summary_properties_content.png
         :align: center

         Figure: QElectroTech summary properties panel, content tab

   3. Click **Request** button to display the content configuration PopUp window.

      .. figure:: ../../images/qet_summary_properties_content_request.png
         :align: center

         Figure: QElectroTech summary properties content request PopUp window
   
   4. Modify the list of information to be displayed by the commands of the following table.

      =================      ===============================      ========================================
      Icon                   Action                               Keyboard shortcut
      =================      ===============================      ========================================
      |go-up|                Move up this field                   
      |list-add|             Add field to display list            Double click on field at available list
      |list-remove|          Remove field from display list       Double click on field at display list
      |go-down|              Move down this field                 
      =================      ===============================      ========================================

      .. note::

         The content request configuration can be saved and chosen from the configuration section 
         to increase working efficiency. 

   5. Once the desired configuration is defined, press **OK** to apply changes and close the PopUp window.

.. |go-down| image:: ../../images/ico/16x16/go-down.png
.. |go-up| image:: ../../images/ico/16x16/go-up.png
.. |list-add| image:: ../../images/ico/16x16/list-add.png
.. |list-remove| image:: ../../images/ico/16x16/list-remove.png

.. _selection properties panel: ../../interface/panels/selection_properties_panel.html
.. _workspace: ../../interface/workspace.html
.. _folio: ../../folio/index.html
.. _folios: ../../folio/index.html
.. _folio properties: ../../folio/properties/index.html
.. _Select: ../../schema/select/index.html
