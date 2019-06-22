.. _en/folio/title_block/elements/cell

====
Cell
====

Definition
~~~~~~~~~~

As in a table, a cells from the title block is the most basic storage unit avaliable. At the title 
block editor from QElectroTech, three different type of cells can be found: Empty cell, text cell and 
logo cell.

Empty cell
~~~~~~~~~~

An empty cell is used when the area occupied by the cell should be empty and without any edge displayed. 
This type of cell has no properties. 

.. figure:: graphics/qet_titleblock_emptycell_prop.png
   :align: center

   Figure: QElectroTech Title block empty cell properties


Text cell
~~~~~~~~~~

An text cell is used when the area occupied by the cell should be filled by an string information inside 
a rectangle. This type of cell has different parameters that can be defined.

.. figure:: graphics/qet_titleblock_textcell_prop.png
   :align: center

   Figure: QElectroTech Title block text cell properties

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

.. figure:: graphics/qet_titleblock_logocell_prop.png
   :align: center

   Figure: QElectroTech Title block logo cell properties

:Name:

    Name from cell

:Logo:

    Name of the Scalable Vector Graphic (SVG) file with the logo image.

.. note::

    Many different tools allows you to create Scalable Vector Graphics, SVG files. Inside the 
    Open Source world, `Inkscape`_ is on of the recomended tools.

.. _Inkscape: https://inkscape.org/