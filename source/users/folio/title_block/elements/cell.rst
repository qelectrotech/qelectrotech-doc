.. _folio/title_block/elements/cell

====
Cell
====

Definition
~~~~~~~~~~

A cell from the `title block`_ is the most basic storage unit available. The three different 
type of cells are: empty cell, text cell and logo cell.

Empty cell
~~~~~~~~~~

An empty cell is used when the area occupied by the cell should be empty and without any edge displayed. 
This type of cell has no properties. 

.. figure:: ../../../images/qet_title_block_cell_empty_prop.png
   :align: center

   Figure: QElectroTech title block empty cell properties


Text cell
~~~~~~~~~~

An text cell is used when the area occupied by the cell should be filled by string information inside 
a rectangle. This type of cell has different parameters that can be defined.

.. figure:: ../../../images/qet_title_block_cell_text_prop.png
   :align: center

   Figure: QElectroTech title block text cell properties

:Name:

    Name from cell

:Label:

    When the cell should display a variable from the folio or project properties, the label is the text that appears before the variable.

:Text:

    It can be a simple string defined by the user or a variable from the folio or project (Ex: Author, Revision, Date, project name, folio page, etc.).

:Font:

    Font from the label and text of the cell.

:Alignment:

    Vertical and horizontal position of the label and text from the cell inside the cell.

Logo cell
~~~~~~~~~~

A logo cell is used when the area occupied by the cell should be filled by a picture inside a rectangle. 
This type of cell has different parameters that can be defined.

.. figure:: ../../../images/qet_title_block_cell_logo_prop.png
   :align: center

   Figure: QElectroTech title block logo cell properties

:Name:

    Name from cell

:Logo:

    Name of the Scalable Vector Graphic (SVG) file with the logo image.

.. note::

    Many different tools allows you to create Scalable Vector Graphics, SVG files. Inside the 
    Open Source world, `Inkscape`_ is on of the recommended tools.

.. _Inkscape: https://inkscape.org/

.. _title block: ../../../folio/title_block/index.html
.. _title block editor: ../../../folio/title_block/title_block_editor/index.html