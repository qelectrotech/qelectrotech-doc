.. _en/folio/title_block/title_block_editor/edition/column_width

======================
Colum width definition
======================

The width from a `column`_ can only be defined from the column head, the top cell from the `Drawing area`_ 
which is given the  width value from the corresponding `column`_. The head from the `columns`_ is not 
displaied at the `folio`_, it is only displayed at the `Title Block editor`_. 

    1. Double click on column head to display the column width PopUp window.

        .. figure:: graphics/qet_titleblock_column_prop.png
         :align: center

        Figure: QElectroTech Title block column width PopUP window

    2. Select the click button corresponding to the desired units to define the column width (Absolute to pixels, relative to total, relative to remainding).
    3. Define the width value.
    4. Press the button **OK**.

.. note::

    The global width from the `Title Block`_ has to be defined at QElectroTech, for this reason, 
    defining one column width as remanding of 100% is recomended.

    .. figure:: graphics/qet_titleblock.png
        :align: center

        Figure: QElectroTech Title block
    
    At the case that a remanding width is not desired, be sure that the global width from the 
    `Title Block`_ matches with the sum of all column widths. At the case that the values are not 
    matching, QElectroTech will display the `Title Block`_ as bellow; part of the title block header 
    will be displayed in red and the width difference will be displayed.  

        .. figure:: graphics/qet_titleblock_width_error.png
            :align: center

            Figure: QElectroTech Title block global width error

.. warning::

    At the case of using **Relative to remainding**, be sure that the value from the width is 100 %. 
    Otherwise, spare area will appear at the `Title Block`_. 

    .. figure:: graphics/qet_titleblock_columns_width_error.png
        :align: center

        Figure: QElectroTech Title block column width error

.. _Title Block editor: ../../../../../en/folio/title_block/title_block_editor/index.html
.. _Title Block: ../../../../../en/folio/title_block/index.html
.. _column: ../../../../../en/folio/title_block/elements/column.html
.. _columns: ../../../../../en/folio/title_block/elements/column.html
.. _Drawing area: ../../../../../en/folio/title_block/title_block_editor/interface/workspace.html
.. _folio: ../../../../../en/folio/index.html