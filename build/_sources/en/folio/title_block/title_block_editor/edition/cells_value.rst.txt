.. _en/folio/title_block/title_block_editor/edition/cells_value

===================
Define cell content
===================

QElectroTech `Title Block editor`_ allows defining two differen type of content at the `text cell`_ 
type: 

    * **Plain text**
    * **Variable**

QElectroTech works managing different database, the content of the `cells`_ are storage in the project 
database. QElectroTech provides the feature of defining the cell content in different languages, 
the cell content is defined at a cell value table. The content from the different `cells`_ of the 
`Title Block`_ are automatically displayed in the language defined.

.. note::

   The working language from QElectroTech is defined at **Setting > Configure QElectroTech**. 

QElectroTech works according `ISO 639-1`_ norm. The text language is defined using 2 letter code which 
should be used at the language column from the cell value table.

.. figure:: graphics/qet_titleblock_cell_label.png
    :align: center

    Figure: QElectroTech title block editor, cell label PopUP window

Add text to cell
~~~~~~~~~~~~~~~~

    1. Select `cell`_ where the text should be introduced.
    2. Press the button **Edit** from text field and the cell value PopUP window will be displayed.
    
        .. figure:: graphics/qet_titleblock_cell_plain_text.png
            :align: center

            Figure: QElectroTech title block editor, cell value PopUP window

    3. Press the button **Add a line** to add a new row in the cell value table.
    4. Define the 2 letter code that identifie the language from the text at the **Language** column.
    5. Define the text at the **Text** column.
    6. Press the button **OK**

Add variable to cell
~~~~~~~~~~~~~~~~~~~~

A title block variable is the value of a project or folio property. At QElectroTech, a variable is 
called using the percent symbol before the variable name (``%{variable-name}``).  

.. note::

    QElectroTech has some default variables that the user does not need to create (ex.: ``%{author}``, 
    ``%{date}``, ``%{title}``, ``%{folio}``, ``%{projecttitle}``, etc.). 
   
    QElectroTech allows also the user the posibility to define extra variables

        * Go to **Project > Project properties > General** to define costumized project variables.
        * Go to **Edit > Folio properties > Title block informations > Costum**  to define costumized folio variables. 

When the content cell would be a variable, QElectroTech allos that the cell has a **Label** for the 
variable.

To define the label:
   
    1. Select `cell`_ where the variable should be introduced.
    2. Click the button **Display a label** to introduce a label at the cell. Click of the button and go to variable definition if the Label should not be displayed.

        .. figure:: graphics/qet_titleblock_textcell_prop.png
            :align: center

            Figure: QElectroTech Title block text cell properties

    3. Press the button **Edit** from label field and the label value PopUP window will be displayed.

        .. figure:: graphics/qet_titleblock_cell_plain_text.png
            :align: center

            Figure: QElectroTech title block editor, cell value PopUP window

    4. Press the button **Add a line** to add a new row in the Label value table.
    5. Define the 2 letter code that identifie the language from the text at the **Language** column.
    6. Define the text at the **Text** column.
    7. Press the button **OK**

To define the variable:

    8. Press the button **Edit** from text field and the cell value PopUP window will be displayed.
    9. Press the button **Add a line** to add a new row in the cell value table.
    10. Define the 2 letter code that identifie the language from the text at the **Language** column. Defining only one languaje is enough for default variables.
    11. Define the variable at the **Text** column. A variable is defined as ``%{variable-name}``. The default variables can be copied to clipboard at the right bottom Combo Box and pasted (``Ctrl + c``) at the **Text** column.

        .. figure:: graphics/qet_titleblock_cell_variable.png
            :align: center

            Figure: QElectroTech title block editor, cell value PopUP window

    12. Press the button **OK**

.. seealso::

    For more information about default variables, please refer to `Default QElectroTech variables`_ 
    section.

.. _ISO 639-1: https://www.iso.org/iso-639-language-codes.html

.. _Title Block editor: ../../../../../en/folio/title_block/title_block_editor/index.html
.. _Title Block: ../../../../../en/folio/title_block/index.html
.. _text cell: ../../../../../en/folio/title_block/elements/cell.html
.. _cells: ../../../../../en/folio/title_block/elements/cell.html
.. _cell: ../../../../../en/folio/title_block/elements/cell.html
.. _Default QElectroTech variables: ../../../../../en/annex/variables.html