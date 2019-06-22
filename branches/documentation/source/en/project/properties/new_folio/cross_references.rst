.. _en/project/properties/new_folio/cross_references

===========================
Cross references properties
===========================

The main advantage of using `Master`_ and `Slave`_ elements is the posibility to create 
`cross references (links)`_ between `elements`_. At the case of `cross references definition`_, 
QElectroTech provides the posbility to display automatically at the `workspace`_ some information from 
the `Master`_ or `Slave`_ element linked.

The definition or cross references properties inside a project can be costumized by the user at 
`project properties`_.

.. note ::

    QElectroTech allows defining automatically `cross references properties`_ during `project creation`_. 
    For more  information about how to standarize some `cross references properties`_ from `project`_ 
    to `project`_, please refers to the `QElectroTech cross references settings`_ section.

The **Cross references** tab from **New folio** settings section allows pre-defining some 
`cross references properties`_:

    * Cross references `Master element`_ type (Coil, organ of protection or Switch/button).
    * Cross references label (Master and slave cross references label to be display at the `workspace`_)
    * Representation position from the cross references label (Under the element label or Footer).
    * Display option from `cross references`_

.. note ::

    The cross reference label can be created using the general variables from `Master`_ and `Slave`_ elements.

.. figure:: graphics/qet_project_cross_references_prop.png
   :align: center

   Figure: Project cross referencing properties window

To define cross references settings: 

    1. `Display`_ project properties PopUP window.
    2. Go to **New folio** section.
    3. Go to **Cross references** tab.
    4. Define the desired parameters for each field.
    5. Press **OK** button to save the configuration changes and close project properties PopUP window.

.. note::

    All pre-defined cross references properties defined at QElectroTech settings PopUP window will 
    be automatically defined during `project creation`_ at `project properties`_. The cross references 
    properties can be found at `Cross references tab`_ tab from `New folio`_ section.  

.. _Display: ../../../../en/project/properties/display.html
.. _folio properties: ../../../../en/folio/properties/index.html
.. _conductor properties: ../../../../en/conductor/properties/index.html
.. _cross references properties: ../../../../en/element/properties/index.html
.. _project creation: ../../../../en/project/new_project.html
.. _project properties: ../../../../en/project/properties/index.html
.. _Cross references tab: ../../../../en/project/properties/new_folio/cross_references.html
.. _New folio: ../../../../en/project/properties/new_folio/index.html
.. _QElectroTech cross references settings: ../../../../en/preferences/new_project/cross_references_settings.html
.. _project: ../../../../en/project/index.html
.. _project creation: ../../../../en/project/new_project.html
.. _Master: ../../../../en/element/type/element_master.html
.. _Master element: ../../../../en/element/type/element_master.html
.. _Slave: ../../../../en/element/type/element_slave.html
.. _workspace: ../../../../en/interface/workspace.html
.. _cross references (links): ../../../../en/element/cross_reference/index.html
.. _cross references: ../../../../en/element/cross_reference/index.html
.. _cross references definition: ../../../../en/schema/element/references/index.html
.. _elements: ../../../../en/element/index.html