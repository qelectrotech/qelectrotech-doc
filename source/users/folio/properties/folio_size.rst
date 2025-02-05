.. _folio/properties/folio_size

==========
Folio size
==========

The working area from the `workspace`_ is defined as a grid of columns and rows. All columns 
have the same width and all rows have the same height.

.. figure:: ../../images/qet_workspace.png
   :align: center


   Figure: QElectroTech folio with 17 columns (0 to 16) and 8 rows (A to H) is shown

The parameters that can be customized from **Dimensions of folio** section from
the `folio properties PopUp window`_ are:

    1. Number of columns.
    2. Width from columns.
    3. Column headers display or hidden.
    4. Number of rows.
    5. Height from rows.
    6. Row headers display or hidden.

.. figure:: ../../images/qet_folio_dimensions_pop.png
   :align: center

   Figure: QElectroTech dimensions of folios section

The version 0.7 from QElectroTech works with pixels and there is no pre-defined folio sizes. The 
pixels dimensions according `ISO 216`_ are: 

.. table::
    :align: center

    +----------+-------------+---------------+
    | ISO 216  |             A-              |
    |          +-------------+---------------+
    |          |      mm     |     pixels    |
    +==========+=============+===============+
    |    -0    |  841 x 1189 |  3178 x 4494  |
    +----------+-------------+---------------+
    |    -1    |  594 x 841  |  2245 x 3178  |
    +----------+-------------+---------------+
    |    -2    |  420 x 594  |  1587 x 2245  |
    +----------+-------------+---------------+
    |    -3    |  297 x 420  |  1122 x 1587  |
    +----------+-------------+---------------+
    |    -4    |  210 x 297  |   794 x 1122  |
    +----------+-------------+---------------+
    |    -5    |  148 x 210  |   559 x 794   |
    +----------+-------------+---------------+
    |    -6    |  105 x 148  |   397 x 559   |
    +----------+-------------+---------------+
    |    -7    |   74 x 105  |   280 x 397   |
    +----------+-------------+---------------+
    |    -8    |   52 x 74   |   196 x 280   |
    +----------+-------------+---------------+
    |    -9    |   37 x 52   |   140 x 196   |
    +----------+-------------+---------------+
    |   -10    |   26 x 37   |    98 x 140   |
    +----------+-------------+---------------+

.. seealso::
  
    For more information about how to display folio properties, refer to 
    `display folio properties`_ section.

.. _workspace: ../../interface/workspace.html
.. _display folio properties: ../../folio/properties/display.html
.. _folio properties PopUp window: ../../folio/properties/display.html
.. _ISO 216: https://www.iso.org/standard/36631.html