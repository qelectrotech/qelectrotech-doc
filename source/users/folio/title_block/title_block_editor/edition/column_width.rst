.. _folio/title_block/title_block_editor/edition/column_width:

=======================
Column width definition
=======================

The width from a `column`_ can only be defined from the column head, the top cell from the `drawing area`_ 
which gives the width value from the corresponding `column`_. The head from the `columns`_ is not 
displayed in the `folio`_, it is only displayed at `title block editor`_. 

1. Double click on column head to display the column width PopUp window.

.. figure:: /_external/_images/en/qet_title/qet_title_block_column_prop.png
        :align: center

        Figure: QElectroTech Title block column width PopUP window

2. Select the click button corresponding to the desired units to define the column width (Absolute, relative to total, relative to remainding).
3. Define the width value.
4. Press **OK**.

.. note::

    The global width from the `title block`_ has to be defined at QElectroTech, for this reason, 
    defining one column width as remanding of 100% is recommended.

.. figure:: /_external/_images/en/qet_title/qet_title_block_editor_workspace.png
    :align: center

    Figure: QElectroTech Title block
    

    At the case that a remanding width is not desired, be sure that the global width from the 
    `title block`_ matches with the sum of all column widths. At the case that the values are not 
    matching, QElectroTech will display the `title block`_ as shown below; part of the title block header 
    will be displayed in red and the width difference will be displayed.  

.. figure:: /_external/_images/en/qet_title/qet_title_block_editor_column_width_error_relative_total.png
    :align: center

    Figure: QElectroTech Title block global width error

.. warning::

    At the case of using **Relative to remainding**, be sure that the value from the width is 100 %. 
    Otherwise, spare area will appear in the `title block`_. 

.. figure:: /_external/_images/en/qet_title/qet_title_block_editor_column_width_error_relative_remainding.png
        :align: center

        Figure: QElectroTech Title block column width error

.. _Title Block editor: ../../../../folio/title_block/title_block_editor/index.html
.. _Title Block: ../../../../folio/title_block/index.html
.. _column: ../../../../folio/title_block/elements/column.html
.. _columns: ../../../../folio/title_block/elements/column.html
.. _Drawing area: ../../../../folio/title_block/title_block_editor/interface/workspace.html
.. _folio: ../../../../folio/index.html