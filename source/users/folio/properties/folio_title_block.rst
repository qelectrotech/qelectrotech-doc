.. _folio/properties/folio_title_block:

===============================
Title block properties section
===============================

The title block section from the `folio properties`_ is the section used to define the `title block`_ 
template used at the `folio`_. The folio variables can also be managed from this section.

.. note::

   To reduce the creation time, QElectroTech allows creating some pre-setting for all future 
   folios that will be created in the project. The folio variable values and the `folio title block`_ 
   can be predefined at the project properties. For more information about how to pre-define folio 
   properties, refer to `project properties`_ section.

The title block section is organized on three different areas: title block selection area, main 
variable tab and custom variable tab.

Title block selection area
~~~~~~~~~~~~~~~~~~~~~~~~~~

The title block selection area is used to define the `folio title block`_. The actions that can be 
managed from this section are:

1. Select the `folio title block`_ from the `project title block collection`_.
2. Select the position of the title block in the folio, bottom |titleblock-bottom| or right |titleblock-right| side.
3. Edit the `title block`_ pressing the button |edit-rename| and choosing the option **Edit this template**.
4. Duplicate the `title block`_ in the `project title block collection`_ pressing the button |edit-rename| and choosing the option **Duplicate and edit this template**. 

.. figure:: /_external/_images/en/qet_folios/qet_folio_prop_title_block_selection_area.png
   :align: center

   Figure: Folio title block selection area

.. seealso::
  
    For more information about QElectroTech title block, refer to `title block`_ section.

.. |titleblock-bottom| image:: /_external/_images/_site-assets/user/ico/22x22/titleblock/titleblock-bottom.png
.. |titleblock-right| image:: /_external/_images/_site-assets/user/ico/22x22/titleblock/titleblock-right.png
.. |edit-rename| image:: /_external/_images/_site-assets/user/ico/22x22/edit/edit-rename.png

Main folio properties tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Main** tab provides these default folio variables.

.. figure:: /_external/_images/en/qet_folios/qet_folio_prop_title_block_main.png
   :align: center

   Figure: Folio title block main tab

The default folio variables are:

* **Title**: Title from the folio.
* **Author**: Author from the folio.
* **Date**: Date of creation of the folio.
* **File**: 
* **Folio**: Folio information (Label).
* **Plant**: Folio variable named Plant.
* **Location**: Folio variable named Location.
* **Rev index**: Revision index from the folio.
* **Page Num**: Auto numbering pattern from the folio.

.. seealso::
  
    For more information about default variables, refer to `variables`_ section.

Custom properties folio tab
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The **Custom** tab is the section where custom variables can be defined.

.. figure:: /_external/_images/en/qet_folios/qet_folio_prop_title_block_custom.png
   :align: center

   Figure: Folio title block custom tab

To define a user folio variable:

1. Define variable name at the **Name** column from the variables table.
2. Define variable value at the **Value** column from the variables table.

.. _workspace: ../../interface/workspace.html
.. _title block: ../../folio/title_block/index.html
.. _Display folio properties: ../../folio/properties/display.html
.. _folio: ../../folio/index.html
.. _project: ../../project/index.html
.. _folio properties: ../../folio/properties/index.html
.. _Project properties: ../../project/properties/folio_prop.html
.. _folio title block: ../../folio/title_block/index.html
.. _title block editor: ../../folio/title_block/title_block_editor/index.html
.. _project title block collection: ../../folio/title_block/collection/title_block_project_collection.html
.. _variables: ../../annex/variables.html