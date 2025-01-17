.. _element/element_parts/terminal:

========
Terminal
========

A terminal is a part from the `element`_ that will allow a connection with one `conductor`_ 
during the schema creation.

Create terminal
~~~~~~~~~~~~~~~

The terminal can only be added to `workspace`_ from `toolbar`_.

    1. Select the icon |icon_terminal| from `toolbar`_ to add a terminal.
    2. Click on the initial point from the terminal in the `workspace`_ to add the terminal.

.. |icon_terminal| image:: /_external/_images/_site-assets/user/ico/22x22/terminal/terminal.png
    

.. note::

   If the `toolbar`_ is not displayed, it can be displayed from **Settings > Display > Parts**.

Terminal properties
~~~~~~~~~~~~~~~~~~~

Element part proterties can be displayed from `information panel`_ when the part is 
selected.

.. note::

   If the `information panel`_ is not displayed, it can be displayed from **Settings > Display > Information**.

.. figure:: /_external/_images/en/qet_element/qet_element_part_terminal.png
   :align: center

   Figure: QElectroTech terminal part from element

QElectroTech allows customizing different terminal properties:

:Position:

    The start point coordinates (x, y) can be defined.

:Orientation:

    The exit direction from the connector can be defined. The four possible orientations are *North*, *East*, *South* and *West*.

:Name:

    Terminal uuid.

.. _element: ../../element/index.html
.. _conductor: ../../conductor/index.html
.. _workspace: ../../element/element_editor/interface/workspace.html
.. _toolbar: ../../element/element_editor/interface/toolbars.html
.. _information panel: ../../element/element_editor/interface/panels/selection_properties.html