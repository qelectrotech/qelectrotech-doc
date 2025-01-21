.. _preferences/settings_element:

=================
Element settings
=================

.. figure:: /_external/_images/en/qet_configure/qet_configure_collections.png
   :align: center

   Figure: QElectroTech elements settings

Collection settings
~~~~~~~~~~~~~~~~~~~

QElectroTech allows choosing the path from the `QET (Common)`_ and `User`_ element collection. The 
path from `User Title Block`_ collection can also be choosed. The collections directory can be 
at the local Hard Disk, common users, or at local servers, common for companies. 

The default element collection paths depend on the installation settings choosed during the 
installation process.

.. admonition:: Example

    :QET collection:
        :Windows:
            ``C/Program Files/QElectroTech/elements``
        :Linux:
            ``/usr/share/qelectrotech/elements``
        :Mac:

    :User collection:
        :Windows:
            ``C/users/user_name/Application Data/qet/elements``   
        :Linux:
            ``/Home/user_name/QElectroTech/collections/elements``
        :Mac:

For changing the element collection paths of QElectroTech:

1. `Display`_ QElectroTech settings PopUP window.
2. Go to **Elements** section.
3. Search and choose the folder directory from the `QET (Common)`_ and `User`_ element collection at the **Collection of elements** section.
4. Press **OK** button to save the configuration changes and close settings PopUP window. 

.. note::

    QElectroTech has to be restarted to implement the changes.

Element management settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~

QElectroTech provides the possibility to predefine the `element author`_. In this way; when a new 
`element`_ is created, QElectroTech defines automatically this `element property`_. 

For pre-defining the `element author`_ information:

1. `Display`_ QElectroTech settings PopUP window.
2. Go to **Elements** section.
3. Defines the element author and license information at the text box from **Elements management** section.
4. Press **OK** button to save the configuration changes and close settings PopUP window. 

.. _QET (Common): ../element/collection/default_collection.html
.. _User: ../element/collection/user_collection.html
.. _Display: ../preferences/display_settings.html
.. _element author: ../element/element_editor/edition/define_element_author.html
.. _element: ../../en/element/index.html
.. _element property: ../element/properties/index.html
.. _User Title Block: ../folio/title_block/collection/title_block_user_collection.html