.. _schema/conductor/conductor_creation

================
Create conductor
================

Manual conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~

To create a `conductor`_ manually:

    1. Select `auto numbering pattern`_ at the `Auto numbering selection panel`_.

        .. figure:: ../../images/qet_panel_auto_numbering_conductor_pattern.png
            :align: center

            Figure: QElectroTech Auto numbering selection panel
        
        .. note::

            If the `Auto numbering selection panel`_ is not displayed, it can be displayed from **Settings > 
            Display > Auto numbering selection**.

    2. Click on the initial `terminal`_ from the `conductor`_.
    3. Without releasing, move the mouse up to the end `terminal`_ of the `conductor`_.
    4. Once the end `terminal`_ is automatically identified by QElectroTech, release the mouse to create the `conductor`_.

        .. figure:: ../../images/qet_conductor_create_manual.png
            :align: center
            :scale: 50%

            Figure: QElectroTech manual conductor creation

Automatic conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To increase the working eficiency, QElectroTech can create `conductors`_ automatically when an 
`element`_ is added to the `workspace`_.

To create a `conductor`_ automatically:

    1. Select `auto numbering pattern`_ at the `Auto numbering selection panel`_.

        .. figure:: ../../images/qet_panel_auto_numbering_conductor_pattern.png
            :align: center

            Figure: QElectroTech Auto numbering selection panel
        
        .. note::

            If the `Auto numbering selection panel`_ is not displayed, it can be displayed from **Settings > 
            Display > Auto numbering selection**.

    2. Select the icon |autoconnect| from `toolbar`_, if it is not selected.
    3. `Add element`_ to `workspace`_ taking care of the `element`_ position, the initial `terminal`_ and the end `terminal`_ have to be at the same vertical or horizontal line.

        .. figure:: ../../images/qet_conductor_create_automatic.png
            :align: center

            Figure: QElectroTech automatic conductor creation

.. |autoconnect| image:: ../../images/ico/22x22/autoconnect.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Tools**.

.. warning::

    At the case that the initial and end `terminal`_ are different potentials, QElectroTech considers 
    two `terminals`_ from the same `element`_ as different potentials, QElectroTech will inform by a 
    warning PopUP window. Nevertheless, QElectroTech will create the `conductor`_

            .. figure:: ../../images/qet_select_electric_potential_message.png
                :align: center

                Figure: QElectroTech different potentials warning

.. _Add element: ../../schema/element/element_add.html
.. _auto numbering pattern: ../../conductor/properties/conductor_numbering.html
.. _Auto numbering selection panel: ../../interface/panels/autonumbering_panel.html
.. _toolbar: ../../interface/toolbars.html
.. _element: ../../element/index.html
.. _conductor: ../../conductor/index.html
.. _conductors: ../../conductor/index.html
.. _workspace: ../../interface/workspace.html
.. _terminal: ../../element/element_parts/terminal.html
.. _terminals: ../../element/element_parts/terminal.html
