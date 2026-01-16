.. _project/properties/new_folio/cross_references:

===========================
Cross references properties
===========================

The main advantage of using `Master`_ and `Slave`_ elements is the possibility to create 
`cross references (links)`_ between `elements`_. At the case of `cross references definition`_, 
QElectroTech allows you to display automatically at the `workspace`_  information from 
the `Master`_ or `Slave`_ linked element.

The definition or cross references properties inside a project can be customized by the user at 
`project properties`_.

.. note ::

    QElectroTech allows defining automatically `cross references properties`_ during `project creation`_. 
    For more  information about how to standardize some `cross references properties`_ from `project`_ 
    to `project`_, please refers to the `QElectroTech cross references settings`_ section.

The **Cross references** tab from **New folio** settings section allows pre-defining some 
`cross references properties`_:

* Cross references `Master element`_ type (Coil, organ of protection or Switch/button).
* Cross references label (Master and slave cross references label to be display at the `workspace`_)
* Representation position from the cross references label (Under the element label or Footer).
* Display option from `cross references`_

.. note ::

    The cross reference label can be created using the general variables from `Master`_ and `Slave`_ elements.

.. figure:: /_external/_images/en/qet_project/qet_project_cross_references_prop.png
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

.. _Display: ../../../project/properties/display.html
.. _folio properties: ../../../folio/properties/index.html
.. _conductor properties: ../../../conductor/properties/index.html
.. _cross references properties: ../../../element/properties/index.html
.. _project creation: ../../../project/new_project.html
.. _project properties: ../../../project/properties/index.html
.. _Cross references tab: ../../../project/properties/new_folio/cross_references.html
.. _New folio: ../../../project/properties/new_folio/index.html
.. _QElectroTech cross references settings: ../../../preferences/new_project/cross_references_settings.html
.. _project: ../../../project/index.html
.. _project creation: ../../../project/new_project.html
.. _Master: ../../../element/type/element_master.html
.. _Master element: ../../../element/type/element_master.html
.. _Slave: ../../../element/type/element_slave.html
.. _workspace: ../../../interface/workspace.html
.. _cross references (links): ../../../element/cross_reference/index.html
.. _cross references: ../../../element/cross_reference/index.html
.. _cross references definition: ../../../schema/element/references/index.html
.. _elements: ../../../element/index.html