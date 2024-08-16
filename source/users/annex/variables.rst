.. SPDX-FileCopyrightText: 2024 Qelectrotech Team <license@qelectrotech.org>
..
.. SPDX-License-Identifier: GPL-2.0-only

.. _annex/variables:

==============================
Default QElectroTech variables
==============================

To systematize title block templates and allow auto numbering of elements, conductors and folios; 
QElectroTech provides the posibility to work with variables. 

The variables are used to define the content of text field and properties from elements, folios and 
conductors. Depending on the conditions during the creation of the object (folio, element, conductor, 
etc,) The variable of the text or property field is replaced by a different value.

A property is identified as a string which starts with the symbol **%**. The default variables provided 
by ElectroTech can be found at this section.

General project variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following variables are global variables which can be used to create title block templates. 

    * **% {projecttitle}**: Project title
    * **% {projectpath}**: Project path
    * **% {projectfilename}**: Project file name
    * **% {saveddate}**: File saving date
    * **% {filename}**: Project file name
    * **% {savedfilename}**: Registered file name
    * **% {savedfilepath}**: Saved file path
    * **% {savedtime}**: File saving time
    * **% {folio-total}**: Total number of folios in the project
    * **% {version}**: Software version
    * **% {machine}**: Project functional group name

variables related to folio
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following variables are specific variables for each folio. They can be used to create title block 
templates. 

    * **% {folio-id}**: Folio position in the project
    * **% {title}**: Folio title
    * **% {author}**: Folio author
    * **% {date}**: Folio date
    * **% {folio}**: Folio information (Label)
    * **% {indexrev}**: Folio revision index
    * **% {locmach}**: Name of the location in the project functional group    
    * **% {previous-folio-num}**: Number previous folio  
    * **% {next-folio-num}**: Number next folio  

variables related to element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following variables are specific variables for each element. They can be used to create auto 
numbering patterns.

    * **% {F}**: Label from the folio where the element can be found
    * **% {f}**: Number from the folio where the element can be found
    * **% {M}**: Plant variable from the folio where the element can be found
    * **% {LM}**: Location variable of the folio where the element can be found
    * **% {l}**: Folio line number from the workspace where the element can be found
    * **% {c}**: Folio column number from the workspace where the element can be found
    * **% {id}**: Folio position in the project (Schema number)

variables related to conductor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following variables are specific variables for each conductor. They can be used to create auto numbering 
patterns.

    * **% {F}**: Label from the folio where the conductor can be found
    * **% {f}**: Number from the folio where the conductor can be found
    * **% {M}**: Plant variable from the folio where the conductor can be found
    * **% {LM}**: Location variable of the folio where the conductor can be found
    * **% {l}**: Folio line number from the workspace where the conductor can be found
    * **% {c}**: Folio column number from the workspace where the conductor can be found
    * **% {id}**: Folio position in the project (Schema number)