.. _en/schema/conductor/conductor_creation

================
Create conductor
================

.. note::

    Before creating a `conductor`_, selecting the `auto numbering pattern`_ is necessary. This selection 
    can only be done from `Auto Numbering Select panel`_. 

        .. figure:: graphics/qet_conductor_autonumbering_panel.png
            :align: center

            Figure: QElectroTech Auto Numbering Select panel

    If the `Auto Numbering Select panel`_ is not displayed, it can be displayed from **Settings > 
    Display > Auto Numbering Select**.

Manual conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~

To create manually a `conductor`_:

    1. Click on the initial `terminal`_ from the `conductor`_.
    2. Without releasing, move the mouse to the end `terminal`_ of the `conductor`_.
    3. Once the end `terminal`_ is automatically identified by QElectroTech, release the mouse to create the `terminal`_.

        .. figure:: graphics/qet_conductor_create_manual.png
            :align: center

            Figure: QElectroTech manual conductor creation

Automatic conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To increase the working eficiency, QElectroTech can create automatically `conductors`_ when an 
`element`_ is added to the `workspace`_.

To create automatically a `conductor`_:

    1. Check that the icon |icon_automatic_conductor| from the `toolbar`_ is selected. If it is not selected, select the icon.
    2. `Add element`_ to the `workspace`_. Take care that the `element`_ is at the right position for the `conductor`_, the initial `terminal`_ and the end `terminal`_ have to be at the same vertical or horizontal line.

        .. figure:: graphics/qet_conductor_create_automatic.png
            :align: center

            Figure: QElectroTech automatic conductor creation

.. |icon_automatic_conductor| image:: graphics/qet_conductor_automatic_creation_icon.png

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Tools**.

.. warning::

    At the case that the initial and end `terminal`_ are different potentials, QElectroTech considers 
    two `terminals`_ from the same `element`_ as different potentials, QElectrotech will inform you by a 
    warning PopUP window.

            .. figure:: graphics/qet_conductor_error_potentials.png
            :align: center

            Figure: QElectroTech different potentials warning
    
    Nevertheless, QElectroTech will create the `conductor`_ and is responsibility of the designer to 
    take care on deleting the `conductor`_. 

.. _Add element: ../../../en/schema/element/element_add.html
.. _auto numbering pattern: ../../../en/conductor/properties/conductor_numbering.html
.. _Auto Numbering Select panel: ../../../en/interface/panels/autonumbering_panel.html
.. _toolbar: ../../../en/interface/toolbars.html
.. _element: ../../../en/element/index.html
.. _conductor: ../../../en/conductor/index.html
.. _conductors: ../../../en/conductor/index.html
.. _workspace: ../../../en/interface/workspace.html
.. _terminal: ../../../en/element/element_parts/terminal.html
.. _terminals: ../../../en/element/element_parts/terminal.html
