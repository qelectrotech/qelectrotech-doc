.. _en/folio/titleblock/titleblockedtor/edition/columnwidth

======================
Colum width definition
======================

The width from a column can only be defined from the column head, the top cell which is given the  
width value from the corresponding column. The head from the columns is not displaied at the folio, 
it is only displayed at the title block editor. 

    1. Double click on column head to display the column width PopUp window.

        .. figure:: graphics/qet_titleblock_column_prop.png
         :align: center

        Figure: QElectroTech Title block column width PopUP window

    2. Select the clik button corresponding to the desired units to define the column width (Absolute to pixels, relative to total, relative to remainding).
    3. Define the width value.
    4. Press the button **OK**.

.. note::

    The global width from the title block have to be defined at QElectroTech, for this reason, defining 
    one column width as remanding of 100% is recomended.

    .. figure:: graphics/qet_titleblock.png
        :align: center

        Figure: QElectroTech Title block
    
    At the case that a remanding width is not desired, be sure that the global width from the title block 
    matches with the sum of all column widths. At the case that the values are not matching, QElectroTech 
    will display the title block as bellow; part of the title block header will be displayed in red and the 
    width difference will be displayed.  

        .. figure:: graphics/qet_titleblock_width_error.png
            :align: center

            Figure: QElectroTech Title block global width error

.. warning::

    at the case of using **Relative to remainding**, be sure that the value from the width is 100 %. 
    Otherwise, spare area will appear at the title block. 

    .. figure:: graphics/qet_titleblock_columns_width_error.png
        :align: center

        Figure: QElectroTech Title block column width error