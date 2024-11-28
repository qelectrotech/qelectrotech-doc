.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _interface/panels/undo_panel:

==========
Undo panel
==========

The Undo panel displays the history since the last time that the document was saved. 
Once the `project`_ is saved, undo panel is automatically cleared.

.. figure:: /_external/_images/en/qet_panel/qet_panel_undo.png
        :align: center

        Figure: QElectroTech Undo panel

To display or hidden the undo panel:

* Select **Settings > Display > Undo** menu item.

The undo panel is used to return the `project`_ to the status after one of the actions made after last save. By one 
click on one of the actions listed at undo panel, the `project`_ will return to the status after the 
action choosed at the panel. While the `project`_ is not saved again, the user can go to the different 
status as many times he wants.

.. warning::

    If you play with the panel, be sure that you are at the correct history status before continue working, 
    saving `project`_ or any irreversible action like `delete folio`_. Once the `project`_ is saved or an 
    irreversible action is made, the history is cleared.

Using the undo panel allow you to:

* Come back to previous steps with a click.
* Recovering an object which was deleted before. The object can be recovered going one step back before the deletion, `copying the object`_  and `pasting the object`_ when on the latest version.
* Checking the `project`_ status between versions.
* Etc.

.. _project: ../../project/index.html
.. _delete folio: ../../folio/delete_folio.html
.. _copying the object: ../../schema/copy.html
.. _pasting the object: ../../schema/paste.html
