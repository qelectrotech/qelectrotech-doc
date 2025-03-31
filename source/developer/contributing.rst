.. SPDX-FileCopyrightText: 2024 QElectroTech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _developer/contributing:

============================================
Contributing to the QET source code
============================================

The goal of this page is to teach you basics about the QET source code and how to contribute effectively to the project.

Access the source code
======================

To contribute to QElectroTech (QET), you need to have access to the `source code`_.

Source control is provided by `Git`_.

If you need help to setup Git, please take a look at the `Git Documentation`_.

Access the Code Documentation
=============================


Compile the app from source
===========================

To set up a dev environment and compile the app locally, please refer to the :doc:`Build Guidelines<build>`.

Submit code
===========

To add your additions to the QET codebase, you need to open a `Merge Request`_ in the `source code`_ Git repository. 


Do & Don't of contributing
--------------------------

.. list-table:: 
   :widths: 35, 35
   :header-rows: 1

   * - Do
     - Don't
   * - Always provide log files when opening an issue. Having no logs makes it really difficult to replicate your bug. 
     - 
   * - Make sure to follow the QET Coding style before submitting code 
     - 
   * - After forking the repository, please **create another branch** for your changes. This will allow you to go back if something in the code breaks.
     - Don't use :code:`git pull` when updating your MR, prefer :code:`git rebase`. This will apply all the latest changes and make the commit history more readable, facilitating testing.  
   * - Structure your files so later contributors can easily make changes and additions to your files
     -      





.. _source code: https://github.com/qelectrotech/qelectrotech-source-mirror
.. _Git Documentation: https://git-scm.com/doc
.. _Git: https://git-scm.com/
.. _Merge Request: https://github.blog/developer-skills/github-education/beginners-guide-to-github-merging-a-pull-request/