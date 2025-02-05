.. _folio/title_block/title_block_editor/edition/cells_value

===================
Define cell content
===================

QElectroTech `title block editor`_ allows defining two different types of content in a `text cell`_ 
type: 

    * **Plain text**
    * **Variable**

QElectroTech works managing different database, the content of the `cells`_ are storage in the project 
database. QElectroTech provides the feature of defining the cell content in different languages, 
the cell content is defined in a cell value table. The content from the different `cells`_ of the 
`title block`_ are automatically displayed in the language defined.

.. note::

   The working language from QElectroTech is defined at **Setting > Configure QElectroTech**. 

Add text to cell
~~~~~~~~~~~~~~~~

    1. Select the `cell`_ where the text should be introduced.
    2. Press **Edit** button from text field and the cell value PopUP window will be displayed.
    3. Press the button **Add a line** to add a new row in the cell value table.
    4. Define the 2 letter code that identifies the language from the text at **Language** column.
    5. Define the text at **Text** column.
    6. Press **OK**

.. note:: 

    QElectroTech works according `ISO 639-1`_ norm. The text language is defined using 2 letter code which 
    should be used at the language column from the cell value table.
        
    .. figure:: ../../../../images/qet_title_block_editor_cell_label.png
        :align: center

        Figure: QElectroTech title block editor, cell label PopUP window

Add variable to cell
~~~~~~~~~~~~~~~~~~~~

A title block variable is the value of a project or folio property. At QElectroTech, a variable is 
called using the percent symbol before the variable name (``%{variable-name}``).  

.. note::

    QElectroTech has some default variables that the user does not need to create (ex.: ``%{author}``, 
    ``%{date}``, ``%{title}``, ``%{folio}``, ``%{projecttitle}``, etc.). 
   
    QElectroTech also allows the user defining extra variables:

        * Go to **Project > Project properties > General** to define customized project variables.
        * Go to **Edit > Folio properties > Title block information > Costum**  to define customized folio variables. 

QElectroTech allows that the cell has a **Label** for the variable.

To define the label:
   
    1. Select the `cell`_ where the variable should be introduced.
    2. Click the button **Display a label** to introduce a label in the cell. Click on the button and go to variable definition if the **Label** should not be displayed.

        .. figure:: ../../../../images/qet_title_block_editor_cell_prop_text.png
            :align: center

            Figure: QElectroTech Title block text cell properties

    3. Press **Edit** button from label field and the label value PopUP window will be displayed.

        .. figure:: ../../../../images/qet_title_block_editor_cell_label.png
            :align: center

            Figure: QElectroTech title block editor, cell value PopUP window

    4. Press the button **Add a line** to add a new row in the Label value table.
    5. Define the 2 letter code that identifies the language from the text at **Language** column.
    6. Define the text at **Text** column.
    7. Press **OK**

To define the variable:

    8. Press **Edit** button from text field and the cell value PopUP window will be displayed.
    9. Press the button **Add a line** to add a new row in the cell value table.
    10. Define the 2 letter code that identifies the language from the text at **Language** column. Defining only one language is enough for default variables.
    11. Define the variable at **Text** column. A variable is defined as ``%{variable-name}``. The default variables can be copied to clipboard at the right bottom Combo Box and pasted (``Ctrl + c``) in **Text** column cell.

        .. figure:: ../../../../images/qet_title_block_editor_cell_prop_variable.png
            :align: center

            Figure: QElectroTech title block editor, cell value PopUP window

    12. Press **OK**

.. seealso::

    For more information about default variables, refer to `default QElectroTech variables`_ 
    section.

.. _ISO 639-1: https://www.iso.org/iso-639-language-codes.html

.. _Title Block editor: ../../../../folio/title_block/title_block_editor/index.html
.. _Title Block: ../../../../folio/title_block/index.html
.. _text cell: ../../../../folio/title_block/elements/cell.html
.. _cells: ../../../../folio/title_block/elements/cell.html
.. _cell: ../../../../folio/title_block/elements/cell.html
.. _Default QElectroTech variables: ../../../../annex/variables.html