.. _en/project/properties/general_prop

==================
General properties
==================

The general properties section from the `project properties`_ PopUP windows is the area where the user 
can define global project variables that later on can be used at the `folios title block templates`_ 
to automate the filling of the `title block`_.

Creating general project variables is recomended, it increase the working eficiency. By default, the 
variables which can be found at this section are the following:

    * **% {projecttitle}**: Project title
    * **% {saveddate}**: File saving date
    * **% {savedfilename}**: Registered file name
    * **% {savedfilepath}**: Saved file path
    * **% {savedtime}**: File saving time

.. figure:: graphics/qet_project_general_prop.png
   :align: center

   Figure: General project properties window

To create new project variables:

    1. `Display project properties`_ PopUp window.
    2. Go to **General** project properties section.
    3. Define the variable name at the left cell from the last row of the project variables table.
    4. Define the value of the variable at the right cell from the variable row.
    5. Press the button **OK** to save the changes and close the PopUp window.

.. seealso::

    For more information about QElectroTech default variables, please refers to `Default QElectroTech variables`_ section.

.. _Display project properties: ../../../en/project/properties/display.html
.. _project properties: ../../../en/project/properties/index.html
.. _title block: ../../../en/folio/titleblock/index.html
.. _folios title block templates: ../../../en/folio/titleblock/index.html
.. _Default QElectroTech variables: ../../../en/annex/variables.html