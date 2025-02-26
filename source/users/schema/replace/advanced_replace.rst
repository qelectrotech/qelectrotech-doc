.. _schema/replace/advanced_replace:

================
Advanced replace
================

QElectroTech provides the possibility to define a string and replace if for a new defining some conditions:

    a. Type of object.
    b. Object property with the defined value.
    c. Filtering `folio`_, `type of element`_, etc.

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.


To replace text information from project objects:

    1. Press **advanced** button to display advanced replace PopUp window.
    2. Define QElectroTech object type from **Who** combobox (Ex.: `Element`_).

        .. figure:: ../../images/qet_search_menu_advanced_replace_advanced_who.png
            :align: center

            Figure: QElectroTech advanced replace PopUp window

    3. Define object property type from **What** combobox (Ex.: Manufacturer).

        .. figure:: ../../images/qet_search_menu_advanced_replace_advanced_what.png
            :align: center

            Figure: QElectroTech advanced replace PopUp window

    4. Define the property value which should be replaced in the **Replace** text box (Ex.: SIEMENS).
    5. Define the new property value at the replace text box in the **By** text box (Ex.: SCHNEIDER).

        .. figure:: ../../images/qet_search_menu_advanced_replace_advanced.png
            :align: center

            Figure: QElectroTech advanced replace PopUp window

    3. Press **OK** button to storage the desired replacing conditions.
    4. Filter in the object tree the `folios`_ where the action should be applied.

        .. figure:: ../../images/qet_search_menu_advanced_folio_tree.png
            :align: center

            Figure: QElectroTech search menu element properties PopUP window

    6. Press **Replace all** button to apply the replace action.

.. _element: ../../element/index.html
.. _elements: ../../element/index.html
.. _type of element: ../../element/type/index.html
.. _conductors: ../../conductor/index.html
.. _text fields: ../../schema/text/index.html
.. _folios: ../../folio/index.html
.. _folio: ../../folio/index.html
.. _Search: ../../schema/search.html
.. _workspace: ../../interface/workspace.html
.. _search menu: ../../interface/search_menu.html