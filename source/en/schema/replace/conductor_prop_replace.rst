.. _en/schema/replace/conductor_prop_replace

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

        .. figure:: graphics/qet_object_tree_conductor_prop_replace.png
            :align: center

            Figure: QElectroTech search menu

    2. Press the **Conductor** button to display the conductor properties PopUp window.

        .. figure:: graphics/qet_conductor_prop_replace.png
            :align: center

            Figure: QElectroTech search menu

    3. Fill the text line box from the `conductor property/ies`_ which should be changed.  

        .. note::

            QElectroTech also allows deleting and making empty a filled property. Click at the 
            cliked button from the `conductor property/ies`_ which should be deleted. 

    4. Press **Accept**.
    5. From the `conductors`_ found at the search process, select the `conductors`_ where the replace action have to be applied. The selection can be made at the object tree from the `search menu`_.
    6. Press **Replace all** button to apply the replace action to all selected `conductors`_.

.. note::

    Replace action can also be applied `conductor`_ by `conductor`_. The button **Replace** will only 
    apply the action to the displayed `conductor`_ at the `workspace`_. the buttons |icon_previous| and 
    |icon_next| can be used to display the previous and next `conductor`_ from the search result. 

.. |icon_next| image:: graphics/qet_search_next_match_button.png
.. |icon_previous| image:: graphics/qet_search_previous_match_button.png

.. _conductor: ../../en/conductor/index.html
.. _conductors: ../../en/conductor/index.html
.. _conductor properties: ../../../en/conductor/properties/index.html
.. _conductor property/ies: ../../../en/conductor/properties/index.html
.. _Search: ../../../en/schema/search.html
.. _workspace: ../../../en/interface/workspace.html
.. _search menu: ../../../en/interface/search_menu.html