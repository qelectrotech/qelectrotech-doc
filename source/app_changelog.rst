.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

..
.. SPDX-License-Identifier: GPL-2.0-only
.. _app_changelog:

=============
App Changelog
=============

Releases
--------

Version 0.9
~~~~~~~~~~~

- Diagram editor :

  - Improved QElectroTech speed (launch qet, open project, function)
  - A drop-down list has been added to the toolbar to change the size of the resize handles.
- Element Editor:

  - The "keep visual rotation" property of element texts is editable from the element editor.
  - Thanks to the work of antonioaja it is now possible to import a dxf directly from the element editor in a completely transparent way for the user.
  - In the background QElectroTech uses the `dxf2elmt software. <https://qelectrotech.org/forum/viewtopic.php?id=2265 https://github.com/antonioaja/dxf2elmt>`_
  - Improved responsiveness when multiple shapes are selected or deleted, especially when working on a `large converted DXF element. <https://qelectrotech.org/forum/viewtopic.php?pid=16612#p16612>`_
- Other:

  - Add a "side project" tab in the "about" window.
  - In the general QElectroTech configuration, a drop down list allows to choose the scaling method for hdpi screens.
  - Allow `open polygons (i.e. polylines) when saving in dxf format. <https://qelectrotech.org/forum/viewtopic.php?pid=16611#p16611>`_
  - Added 'Other' option for `slave device contact type. #222 <https://qelectrotech.org/forum/viewtopic.php?id=2264>`_

- Logs:

  - Added a QElapsedTimer to calculate the time used to reload the item collection.
  - Improved QElapsedTimer to calculate the time used to reload the item collection in seconds instead of ms.
  - Added Linux pc.gpu.RAM information, but requires mesa-utils dependency on the Linux OS.
  - Added information about mounted disk volumes.
  - Added CPU architecture for which Qt was compiled in the aboutqetdialog widget and in the logs.
  - Added MSVC support to MachineInfo.
  - Added RAM information on Windows of available RAM.
  - Added QElectroTech version to the log file.
- Elements collection :

  - Improve collection 8274 elements in 1097 categories (i.e. 9371 files).


