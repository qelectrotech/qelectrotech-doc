.. _en/schema/search

======
Search
======

To find information inside a `schema`_ easily, QElectroTech provides the search feature. This feature 
allows finding automatically `Folios`_, `Elements`_, `Conductors`_ and `Text fields (plain text)`_ 
which contains an string at one of the properties.

To find an object which contains an string:

    1. Go to `search menu`_.

        .. figure:: graphics/qet_search_menu.png
            :align: center

            Figure: QElectroTech search menu

    2. Write at the text box from the menu the string which should be search over the `project`_.
    3. Press ``Intro`` and QElectroTech will zoom and display the first object from the list of matches at the `workspace`_ after the seach process. 
    4. Press |icon_next| or |icon_previous| button to zoom the next or previous object from the list of matches.
    5. Press |icon_actualize| button to clean the search.

.. |icon_next| image:: graphics/qet_search_next_match_button.png
.. |icon_previous| image:: graphics/qet_search_previous_match_button.png
.. |icon_actualize| image:: graphics/qet_search_actualize_button.png

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu item.

QElectrotech provides also some advanced properties for searching. Before searching, a filter can be 
dedined to reduce the list of matches according the following criteria:

    * `Text fields (Plain text)`_.
    * Whole words (`Text fields (Plain text)`_, `Conductor properties`_, `Element properties`_, `Folio properties`_)

To create an advanced search:

    1. Go to `search menu`_.
    2. Press |icon_advanced| button to display the filter tree.

        .. figure:: graphics/qet_advanced_search_menu.png
            :align: center

            Figure: QElectroTech advanced search menu

    3. Select the type of text to be searched (**Plain text** or **Whole words**) at the combobox from the right side of the text box.
    4. Click / unclick the button which selects **Case sensitive**.
    5. From here, follow the steps from the standard search.

.. |icon_advanced| image:: graphics/qet_search_advanced_button.png

.. _elements: ../../en/element/index.html
.. _conductors: ../../en/conductor/index.html
.. _conductor properties: ../../en/conductor/properties/index.html
.. _Text fields (plain text): ../../en/schema/text/index.html
.. _folios: ../../en/folio/index.html
.. _workspace: ../../en/interface/workspace.html
.. _search menu: ../../en/interface/search_menu.html
.. _project: ../../en/project/index.html
.. _schema: ../../en/schema/index.html
.. _Element properties: ../../en/element/properties/index.html
.. _Folio properties: ../../en/folio/properties/index.html