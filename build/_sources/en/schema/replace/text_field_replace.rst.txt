.. _en/schema/replace/text_field_replace

==========================
Replace text field content
==========================

QElectroTech provides the feature of searching and replacing `text field`_ content automatically. 
This option allows replacing the complete content from a `text field`_ which contains the string 
searched. The string searched can be the complete `text field`_ content or part of the `text field`_ 
content.

.. note::

   If the `search menu`_ is not displayed, it can be displayed from **Edit > Search / Replace** menu 
   item.

To replace `text field`_ content over a `project`_:

    1. `Search`_ the string which should be replaced (Ex.: Folio).

        .. figure:: graphics/qet_advanced_search_menu_folio.png
            :align: center

            Figure: QElectroTech search menu

    2. Define the new text content at the replace text box (Ex.: Sheet reserve).

        .. figure:: graphics/qet_advanced_search_menu_replace_sheet.png
            :align: center

            Figure: QElectroTech search menu

    3. Select at the objects tree the `text field`_ which content should be replaced.
    4. Press **Replace all** button to replace the content from the selected `text field`_.
    5. Press actualize |icon_actualize| button to refresh the search.

.. note::

    Replace action can also be applied object by object. The button **Replace** will only 
    apply the action to the displayed object at the `workspace`_. the buttons |icon_previous| and 
    |icon_next| can be used to display the previous and next `text field`_ from the search result. 

.. warning::

    The replacing feature from QElectroTech replaces the `text field`_ content completely. Changing 
    the `text field`_ content partly cannot be done.

.. |icon_next| image:: graphics/qet_search_next_match_button.png
.. |icon_previous| image:: graphics/qet_search_previous_match_button.png
.. |icon_actualize| image:: graphics/qet_search_actualize_button.png

.. _text field: ../../../en/schema/text/index.html
.. _Search: ../../../en/schema/search.html
.. _search menu: ../../../en/interface/search_menu.html
.. _project: ../../../en/project/index.html
.. _workspace: ../../../en/interface/workspace.html