.. _schema/replace/conductor_prop_replace:

==========================
Replace conductor property
==========================

QElectroTech provides the feature of automatic searching of `conductor`_ with an specific property for 
replacing `conductor properties`_ without the need of searching the `conductor`_ manually arround the 
project. 

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.

To replace some `conductor properties`_:

    1. `Search`_ the property (Manufacturer, Lable, etc.) which identifies the `conductor`_ from which a property has to be changed.

        .. figure:: ../../images/qet_search_menu_advanced_conductor_tree.png
            :align: center

            Figure: QElectroTech search menu

    2. Press the **Conductor** button to display the conductor properties PopUp window.

        .. figure:: ../../images/qet_search_menu_advanced_conductor_prop.png
            :align: center

            Figure: QElectroTech conductor properties replace PopUp windows

    3. Fill the text line box from the `conductor property/ies`_ which should be changed.  

        .. note::

            QElectroTech also allows deleting and making empty a filled property. Click at the 
            cliked button from the `conductor property/ies`_ which should be deleted. 

    4. Press **Accept**.
    5. From the `conductors`_ found at the search process, select the `conductors`_ where the replace action have to be applied. The selection can be made at the object tree from the `search menu`_.
    6. Press **Replace all** button to apply the replace action to all selected `conductors`_.

.. note::

    Replacing action can also be applied `conductor`_ by `conductor`_. The button **Replace** will only 
    apply the action to the displayed `conductor`_ at the `workspace`_. The buttons |go-top| and 
    |go-bottom| can be used to display the previous and next `conductor`_ from the search result. 

.. |go-bottom| image:: ../../images/ico/16x16/go-bottom.png
.. |go-top| image:: ../../images/ico/16x16/go-top.png

.. _conductor: ../../conductor/index.html
.. _conductors: ../../conductor/index.html
.. _conductor properties: ../..//conductor/properties/index.html
.. _conductor property/ies: ../../conductor/properties/index.html
.. _Search: ../../schema/search.html
.. _workspace: ../../interface/workspace.html
.. _search menu: ../../interface/search_menu.html