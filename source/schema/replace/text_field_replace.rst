.. _schema/replace/text_field_replace

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

        .. figure:: ../../images/qet_search_menu_advanced_folio.png
            :align: center

            Figure: QElectroTech search menu

    2. Define the new text content at the replace text box (Ex.: Sheet reserve).

        .. figure:: ../../images/qet_search_menu_advanced_replace_sheet.png
            :align: center

            Figure: QElectroTech search menu

    3. Select at the objects tree the `text fields`_ which content should be replaced.
    4. Press **Replace all** button to replace the content from the selected `text fields`_.
    5. Press actualize |view-refresh| button to refresh the search.

.. note::

    Replacing action can also be applied object by object. The button **Replace** will only 
    apply the action to the displayed object at the `workspace`_. The buttons |go-top| and 
    |go-bottom| can be used to display the previous and next `text field`_ from the search result. 

.. warning::

    The replacing feature from QElectroTech replaces the `text field`_ content completely. Changing 
    the `text field`_ content partly cannot be done.

.. |go-bottom| image:: ../../images/ico/16x16/go-bottom.png
.. |go-top| image:: ../../images/ico/16x16/go-top.png
.. |view-refresh| image:: ../../images/ico/22x22/view-refresh.png

.. _text field: ../../schema/text/index.html
.. _text fields: ../../schema/text/index.html
.. _Search: ../../schema/search.html
.. _search menu: ../../interface/search_menu.html
.. _project: ../../project/index.html
.. _workspace: ../../interface/workspace.html