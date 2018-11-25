.. _en/folio/titleblock/titleblockedtor/edition/cellsvalue

===================
Define cell content
===================

QElectroTech title block editor allows defining two differen type of content at the text cell 
type: simple text and variables.

Regardless of the content type, QElectroTech reads the infromation from the title block at a different 
database adress depending on the languaje selected at **Setting > Configure QElectroTech**. This means 
that the user have always to define the languaje of the content before introduce it.

QElectroTech allows defining the cell content in some languajes at the same time, this option reduce the 
project translation work. Once the project is ready, only changing the languaje at QElectroTech settings 
is enougth to display all project information at the different languajes. Defining all element and title 
block content of the text fields at the different languajes is necessary to take advantage of this option 
provided by QElectroTech.

.. note::

   At QElectroTech, all title block information and element names are storage at the databae. This is the 
   information that the user have to define indicating the languaje of the content.

   QElectroTech still does not storage the content of simple text fields at any database, this information 
   cannot be displayed at different languaje by a simple languaje selection at QElectroTech settings.

QElectroTech works according `ISO 639-1`_ norm. The text language is defined using 2 letter code which 
should be used at the language column from the cell value table.

.. figure:: graphics/qet_titleblock_cell_value.png
    :align: center

    Figure: QElectroTech title block editor, cell value PopUP window

.. _ISO 639-1: https://www.iso.org/iso-639-language-codes.html

Add text to cell
~~~~~~~~~~~~~~~~

    1. Select cell where the text should be introduced.
    2. Press the button **Edit** from text field and the cell value PopUP window will be displayed.
    
        .. figure:: graphics/qet_titleblock_textcell_prop.png
            :align: center

            Figure: QElectroTech title block editor, cell properties

    3. Press the button **Add a line** to add a new row in the cell value table.
    4. Define the 2 letter code that identifie the languaje from the text at the Languaje column.
    5. Define the text at the Text column.
    6. Press the button **OK**

Add variable to cell
~~~~~~~~~~~~~~~~~~~~

A title block variable is the name of a project or folio property. At QElectroTech, a variable is called 
using the percent symbol before the variable name (%{variable-name}).  

.. note::

   QElectroTech has some default variables that the user does not need to create (ex.: %author, %date, 
   %title, %folio, %projecttitle, etc.), QElectorTech provides a list with all the defaul variables at 
   the bottom cell value PopUP window.
   
   QElectroTech allows also the user the posibility to define extra variables

        * Go to **Project > Project properties > General** to define costumized project variables.
        * Go to **Edit > Folio properties > Title block informations > Costum**  to define costumized folio variables. 

|
    1. Select cell where the cariable should be introduced.
|
    2. Press the button **Edit** from text field and the cell value PopUP window will be displayed.
    
        .. figure:: graphics/qet_titleblock_textcell_prop.png
            :align: center

            Figure: QElectroTech title block editor, cell properties
|
    3. Press the button **Add a line** to add a new row in the cell value table.
|
    4. Define the 2 letter code that identifie the languaje from the text at the Languaje column.
|
    5. Define the variable at the Text column. A variable is defined using the percent symbol (%) and the name of the variable, all together. 
|
    6. Press the button **OK**

.. note::

   QElectroTech allows combining text with variable at one cell. For example, QElectroTech allows 
   introducing at the same cell the label 'Date' and the variable date (%date).

        1. Click the button **Display a label** to introduce a label at the cell.
        2. Press the button **Edit** and define the label according the text procedure
        3. Define the variable at the text field according the variable procedure
