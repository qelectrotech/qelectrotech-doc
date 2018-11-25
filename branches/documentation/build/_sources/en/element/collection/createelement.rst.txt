.. _en/element/collection/createelement

==============
Create element
==============

Working with collections can only be done from the collections panel. Before starting to work with 
collections, the collections panel has to be displayed. 

.. note::

   Select **Settings > Display > Collections** menu item to display the Collections panel.

QElectroTech allows creating element at some collection. The user has only read rights at QET element 
collection, the user can create element at all collections except QET collection.

There is two different ways to create a new eleemnt at the user collection. A new element can be 
created from cero or from an already existing element from the QET or user collection.

Create element from cero
~~~~~~~~~~~~~~~~~~~~~~~~

1. Right click on the user collection or at the category / sub-category from the collection where the new element should be added.

    .. figure:: graphics/qet_right_click_folder.png
        :align: center

        Figure: Options at folder

2. Click the option **New element** to start the element creation.
3. Confirm or change the category from the element.

    .. figure:: graphics/qet_element_parent_category.png
        :align: center

         Figure: Category election PopUP window

4. Define the element file name.

    .. figure:: graphics/qet_element_file_name.png
        :align: center

        Figure: File name definition PopUP window

5. Define the element name for the collection and project tree. It can be defined in many languajes.

    .. figure:: graphics/qet_element_name.png
        :align: center

        Figure: Element name definition PopUP window
    
.. note::

    QElectroTech works according `ISO 639-1`_ norm. The element name languaje is defined using 2 letter 
    code which should be used at the languaje column from the folder internal name table.

.. _ISO 639-1: https://www.iso.org/iso-639-language-codes.html

6. Once the element editor PopUP window is opened, design the symbol element and define the properties.
7. Save the element and it will appear at the collection.

.. seealso::

   For more information about the element editor, please refers to `Element editor <../../../en/element/elementeditor/index.html>`_ section.

Create an element from an existing element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Right click on the element which will be used as base for the new element.

    .. figure:: graphics/qet_right_click_element.png
        :align: center

        Figure: Options at element

2. Click the option **Edit element** to open the element at the element editor.
3. Select **File > Save as** menu item to open the save window.

    .. figure:: graphics/qet_element_editor_file_menu.png
        :align: center

         Figure: Element editor File menu

4. Choose the element category at the collection tree.
5. Define the file name for the element.
6. Press the button **Save**.

    .. figure:: graphics/qet_element_save_as.png
        :align: center

         Figure: Element editor Save as PopUP window