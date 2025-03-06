.. _schema/search:

======
Search
======

To find information inside a `schema`_ easily, QElectroTech provides a searching feature. This feature 
allows finding automatically `folios`_, `elements`_, `conductors`_ and `text fields (plain text)`_ 
which contains a string at one of the properties.

To find an object which contains a string:

1. Go to `search menu`_.

.. figure:: /_external/_images/en/qet_search/qet_search_menu.png
            :align: center

            Figure: QElectroTech search menu

2. Write the string which should be search over the `project`_ in the text box from the menu.
3. Press ``Enter`` and QElectroTech will zoom and display the first object from the list of matches at the `workspace`_. 
4. Press |icon_next| or |icon_previous| button to zoom the next or previous object from the list of matches.
5. Press |icon_actualize| button to refresh the search.

.. |icon_next| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-bottom.png
.. |icon_previous| image:: /_external/_images/_site-assets/user/ico/16x16/go/go-top.png
.. |icon_actualize| image:: /_external/_images/_site-assets/user/ico/16x16/view/view-refresh.png

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu item or using ``Ctrl + f`` shortcut keyboard.

QElectrotech provides also some advanced properties for searching. Before searching, a filter can be 
defined to reduce the list of matches according the following criteria:

* `Text fields (Plain text)`_.
* Whole words (`Text fields (Plain text)`_, `Conductor properties`_, `Element properties`_, `Folio properties`_)

To create an advanced search:

1. Go to `search menu`_.
2. Press |icon_advanced| button to display the filter tree.

.. figure:: /_external/_images/en/qet_search/qet_search_menu.png
            :align: center

            Figure: QElectroTech advanced search menu

3. Select the type of text to be searched (**Plain text** or **Whole words**) at the combobox from the right side of the text box.
4. Click / unclick the button which selects **Case sensitive**.
5. From here, follow the steps from the standard search.

.. |icon_advanced| image:: /_external/_images/_site-assets/user/ico/16x16/configure/configure-toolbars.png

.. _elements: ../element/index.html
.. _conductors: ../conductor/index.html
.. _conductor properties: ../conductor/properties/index.html
.. _text fields (plain text): ../schema/text/index.html
.. _folios: ../folio/index.html
.. _workspace: ../interface/workspace.html
.. _search menu: ../interface/search_menu.html
.. _project: ../project/index.html
.. _schema: ../schema/index.html
.. _Element properties: ../element/properties/index.html
.. _Folio properties: ../folio/properties/index.html