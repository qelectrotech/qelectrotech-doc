.. _en/schema/replace/element_prop_replace

========================
Replace element property
========================

QElectroTech provides the feature of automatic searching of `element`_ with an specific property for 
replacing `element properties`_ without the need of searching the `element`_ manually arround the 
project. 

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.

To replace some `element properties`_:

    1. `Search`_ the property (Manufacturer, Lable, etc.) which identifies the `element`_ from which a property has to be changed.

        .. figure:: graphics/qet_object_tree_element_prop_replace.png
            :align: center

            Figure: QElectroTech search menu

    2. Press the **Element** button to display the element properties PopUp window.

        .. figure:: graphics/qet_element_prop_replace.png
            :align: center

            Figure: QElectroTech search menu

    3. Fill the text line box from the `element property/ies`_ which should be changed.  

        .. note::

            QElectroTech also allows deleting and making empty a filled property. Click at the 
            cliked button from the `element property/ies`_ which should be deleted. 

    4. Press **Accept**.
    5. From the `elements`_ found at the search process, select the `elements`_ where the replace action have to be applied. The selection can be made at the object tree from the `search menu`_.
    6. Press **Replace all** button to apply the replace action to all selected `elements`_.

.. note::

    Replace action can also be applied `element`_ by `element`_. The button **Replace** will only 
    apply the action to the displayed `element`_ at the `workspace`_. the buttons |icon_previous| and 
    |icon_next| can be used to display the previous and next `element`_ from the search result. 

.. |icon_next| image:: graphics/qet_search_next_match_button.png
.. |icon_previous| image:: graphics/qet_search_previous_match_button.png

.. _element: ../../../en/element/index.html
.. _elements: ../../../en/element/index.html
.. _element properties: ../../../en/element/properties/index.html
.. _element property/ies: ../../../en/element/properties/index.html
.. _Search: ../../../en/schema/search.html
.. _workspace: ../../../en/interface/workspace.html
.. _search menu: ../../../en/interface/search_menu.html