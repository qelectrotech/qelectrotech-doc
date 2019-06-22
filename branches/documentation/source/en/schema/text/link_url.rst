.. _en/schema/text/link_url

===============
Insert URL link
===============

QElectroTech works with text as html code. This property allows the user introducing at the `workspace`_ 
anything that is possible with HTM code. This section explains how the user can create an URL link for 
a text.

.. note::

   The URL link is only actived at the PDF version of the document. The link is not actived at the 
   native QElectroTech format. 

At the current released version, version 0.7, QElectroTech allows creating an URL link internally or 
using external html code generators.

Insert URL link from QElectroTech text editor
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   
    1. Display the `text editor`_ by editing the desired `text field`_.

        .. figure:: graphics/qet_text_editor_link.png
            :align: center

            Figure: QElectroTech text editor

    2. Press the icon **Insert link** from the Menu bar for displaying the Insert link PopUP window.

        .. figure:: graphics/qet_link_popup_window.png
            :align: center

            Figure: QElectroTech Insert link PopUP window

    3. Define the text which should be displayed at the `workspace`_ and the desired URL where the link should redirect.
    4. Press the button **OK** to close the Insert link PopUP window and add the link to the text field content.
    5. Press the button **OK** to save the text field content and close the `text editor`_.

Insert URL link using external html code generators
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

At the case that something special should be included or any propertie should be different, QElectroTech 
allows creating the html source code using an external code generator and later on introduce the code.

    1. Display the `text editor`_ by editing the desired `text field`_.

        .. figure:: graphics/qet_text_editor_rich_text.png
            :align: center

            Figure: QElectroTech text editor

    2. Select the source Tab.

        .. figure:: graphics/qet_text_editor_source_link.png
            :align: center

            Figure: QElectroTech Text field PopUP window source tab

    3. Copy the html code from the html code generator.
    4. Press the button **OK** to save the text field content and close the `text editor`_.

.. note::

   Many different HTML Table Generator can be found on interned or can be installed at the computer. One 
   internet example is the following:

   https://html-css-js.com/html/generator/

.. _workspace: ../../../en/interface/workspace.html
.. _text editor: ../../../en/schema/text/text_editor.html
.. _text field: ../../../en/schema/text/index.html