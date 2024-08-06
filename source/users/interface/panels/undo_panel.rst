.. _interface/panels/undo_panel:

==========
Undo panel
==========

The Undo panel displays the history since the last time that the document was saved. 
Once the `project`_ is saved, undo panel is automatically cleared.

.. figure:: ../../images/qet_panel_undo.png
        :align: center

        Figure: QElectroTech Undo panel

To display or hidden the undo panel:

    1. Select **Settings > Display > Undo** menu item.

The undo panel is used to return the `project`_ to the status after one of the actions made after last save. By one 
click on one of the actions listed at undo panel, the `project`_ will return to the status after the 
action choosed at the panel. While the `project`_ is not saved again, the user can go to the different 
status as many times he wants.

.. warning::

    If you play with the panel, be sure that you are at the correct history status before continue working, 
    saving `project`_ or any irreversible action like `delete folio`_. Once the `project`_ is saved or an 
    irreversible action is made, the history is cleared.

Using the undo panel is interested for:

    * Coming back some steps with a click.
    * Recovering an object which was deleted some steps before. The object can be recovered coming back one step before the elimination, `copying the object`_, coming back to the last history status and `pasting the object`_.
    * Checking the status from the `project`_ some steps before.
    * Etc.

.. _project: ../../project/index.html
.. _delete folio: ../../folio/delete_folio.html
.. _copying the object: ../../schema/copy.html
.. _pasting the object: ../../schema/paste.html
