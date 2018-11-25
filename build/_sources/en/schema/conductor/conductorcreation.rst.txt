.. _en/schema/conductor/conductorcreation

================
Create conductor
================

.. note::

    Before creating a conductor, selecting the auto numbering pattern is necessary. This selection can 
    only be done from the **Auto Numbering Select** panel. 

        .. figure:: graphics/qet_conductor_autonumbering_panel.png
            :align: center

            Figure: QElectroTech Auto Numbering Select panel

    If the Auto Numbering Select panel is not displayed, it can be displayed from **Settings > 
    Display > Auto Numbering Select**.

Manual conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~

To create manually a conductor:

    1. Click on the initial terminal from the conductor.
    2. Without releasing, move the mouse to the end terminal of the cnductor.
    3. Once the end terminal is automatically identified by QElectroTech, release the mouse to create the conductor.

        .. figure:: graphics/qet_conductor_create_manual.png
            :align: center

            Figure: QElectroTech manual conductor creation

Automatic conductor creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To increase the working eficiency, QElectroTech can create automatically conductors when an 
element is added to the workspace.

To create automatically a conductor:

    1. Check that the icon |icon_automatic_conductor| from the toolbar is selected. If it is not selected, select the icon.
    2. `Add element <../../schema/element/elementadd.html>`_ to the workspace. Take care that the element is at the right position for the conductor, the initial terminal and the end terminal have to be at the same vertical or horizontal line.

        .. figure:: graphics/qet_conductor_create_automatic.png
            :align: center

            Figure: QElectroTech automatic conductor creation

.. |icon_automatic_conductor| image:: graphics/qet_conductor_automatic_creation_icon.png

.. note::

   If the toolbar is not displayed, it can be displayed from **Settings > Display > Tools**.

.. warning::

    At the case that the initial and end terminal are different potentials, QElectroTech considers 
    two terminals from the same element as different potentials, QElectrotech will inform you by a 
    warning PopUP window.

            .. figure:: graphics/qet_conductor_error_potentials.png
            :align: center

            Figure: QElectroTech different potentials warning
    
    Nevertheless, QElectroTech will create the conductor and is responsibility of the designer to take 
    care on deleting the conductor. 