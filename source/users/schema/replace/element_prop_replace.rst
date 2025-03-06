.. _schema/replace/element_prop_replace:

========================
Replace element property
========================

QElectroTech provides the feature of automatic searching of `element`_ with an specific property for 
replacing `element properties`_ without the need of searching the `element`_ manually around the 
project. 

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.

To replace some `element properties`_:

1. `Search`_ the property (Manufacturer, Label, etc.) which identifies the `element`_ from which a property has to be changed.

.. figure:: /_external/_images/en/qet_search/qet_search_menu_advanced_element_tree.png
            :align: center

            Figure: QElectroTech search menu

2. Press the **Element** button to display the element properties PopUp window.

.. figure:: /_external/_images/en/qet_search/qet_search_menu_advanced_element_prop.png
            :align: center

            Figure: QElectroTech element properties replace PopUp windows

3. Fill the text line box from the `element properties`_ which should be changed.  

    .. note::

       QElectroTech also allows deleting and making empty a filled property. Click the 
       checkbox button located right from the text which should be deleted

4. Press **Accept**.
5. From the `elements`_ found at the search process, select the `elements`_ where the replace action have to be applied. The selection can be made at the object tree from the `search menu`_.
6. Press **Replace all** button to apply the replace action to all selected `elements`_.

.. note::

    Replacing action can also be applied `element`_ by `element`_. The button **Replace** will only 
    apply the action to the displayed `element`_ at the `workspace`_. The buttons |go-top| and 
    |go-bottom| can be used to display the previous and next `element`_ from the search result. 

.. |go-bottom| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-bottom.png
.. |go-top| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-top.png

.. _element: ../../element/index.html
.. _elements: ../../element/index.html
.. _element properties: ../../element/properties/index.html
.. _Search: ../../schema/search.html
.. _workspace: ../../interface/workspace.html
.. _search menu: ../../interface/search_menu.html