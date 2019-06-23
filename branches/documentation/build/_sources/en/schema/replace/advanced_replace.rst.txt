.. _en/schema/replace/advanced_replace

================
Advanced replace
================

QElectroTech provides the feature of searching and replacing text information automatically.

.. warning::

    QElectroTech only provides the feature of replacing all text field or property content, changing 
    the `text fields`_ content or any `folio`_, `elements`_ or `conductors`_ property partly is not 
    possible.

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.


To replace text information from project objects:

    1. `Search`_ the text content which should be replaced (Ex.: SIEMENS).

        .. figure:: graphics/qet_advanced_search_menu_siemens.png
            :align: center

            Figure: QElectroTech search menu

    2. Define the new text content at the replace text box (Ex.: SCHNEIDER).

        .. figure:: graphics/qet_advanced_search_menu_replace_schneider.png
            :align: center

            Figure: QElectroTech search menu

    3. Press the folio properties button and select the properties which should be replaced (Ex.: Revision item).

        .. figure:: graphics/qet_replace_options_folio.png
            :align: center

            Figure: QElectroTech search menu folio properties PopUP window

    4. Press the element button and select the properties which should be replaced (Ex.: Manufacturer)

        .. figure:: graphics/qet_replace_options_element.png
            :align: center

            Figure: QElectroTech search menu element properties PopUP window

    5. From the objets found at the search process, select the objets where the replace action have to be applied. The selection can be made at the object tree.
    6. Press **Replace all** button to apply the replace action.

.. note::

    Replace action can also be applied `element`_ by `element`_. The button **Replace** will only 
    apply the action to the displayed object at the `workspace`_ and the buttons |icon_previous| and 
    |icon_next| can be used to display the previous and next object from the search. 

.. |icon_next| image:: graphics/qet_search_next_match_button.png
.. |icon_previous| image:: graphics/qet_search_previous_match_button.png

.. _element: ../../en/element/index.html
.. _elements: ../../en/element/index.html
.. _conductors: ../../en/conductor/index.html
.. _text fields: ../../en/schema/text/index.html
.. _folio: ../../en/folio/index.html
.. _Search: ../../en/schema/search.html
.. _workspace: ../../en/interface/workspace.html
.. _search menu: ../../en/interface/search_menu.html