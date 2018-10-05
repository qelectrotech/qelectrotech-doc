.. _en/schema/text

=======================
Working with text field
=======================

At the chema from QElectroTech, two different type of text can be found: simple text field and 
text field from element. Depending on the type of text, the user can choose from a different 
list of actions.

Inserting text field
------------------------

``Add a Text field`` tool is provided in the tool bar of the main window. To add a text field into the work space

          (a) Click the ``Add a Text field`` tool and click at a point in the work space, where the text field should be added. 

The text field by default appears as an underscore and it can be either used in association with an element or as an additional field inserted in the work space. 

Some elements are provided with a text field at each of their terminals and / or one for the entire element. Additional text fields can be added any where in the work space by the procedure described earlier. The text field can be edited in the work space by 

         (a) Double left clicking the text field with the mouse and keying in text from keyboard. 

	 (b) To exit editing, click any where else in the workspace. The text field supports multi-line entries and a few formatting options.

Orientation of the text field in workspace
----------------------------------------------

All the text fields are horizontally oriented in the work space by default but, they can be oriented in any direction. The text field can be re-oriented by rotating it as described below:

          (a) Select the text field by left clicking it with the mouse.
	  (b) Rotate it with the ``Rotate`` tool from the tool bar - refer to section on `rotating elements`_. Alternatively the element can be rotated in quantum steps of 90\ :sup:`o` \ by pressing the ``Space`` bar from the keyboard.
	  (c) The text field has special rotation attribute that it can be rotated precisely upto two decimal places of a degree. 

	      (i) Select the text field and press ``Control + Space`` keys from keyboard to pop open a GUI window to rotate the text field in any direction.
	      (ii) The GUI window facilitates rotation in quantum steps of 45\ :sup:`o`\  degrees by clicking the green squares on the yellow circle. 
	      (iii) A double spin box is also provided to manually enter an angle of orientation upto two decimal places. The double spin box can also be interacted with a left mouse, by clicking the up or down arrow keys, to increment or decrement the angles in steps of 1 degree correspondingly with each click.

 
.. _Fig.21:

.. Figure:: graphics/guitextrotate.png
   :width: 400px
   :height: 400px
**Fig.21 Rotate text with orientation pop up window** (The text selected (top right corner) is rotated by -25.75\ :sup:`o`\  degrees)



Moving and editing text field in work place
-----------------------------------------------

Text field can be moved any where in the workspace by 
    (a) Selecting it with a left mouse click and holding it and drag dropping the text to a new position. 
    (b) Text fields that are associated with the elements require ``control key`` to be pressed from the keyboard to permit moving its text field along with the earlier described procedure. 

Moving an element's text field produces a blue colored highlight over the element during relocation as shown in the Fig.22. This feature of QElectroTech helps user to perform such actions in a large diagram and still conspicuously keep track of its parent element.


.. _Fig.22:

.. Figure:: graphics/textmove.png
   :width: 300px
   :height: 150px
**Fig.22 Illustration the step (b), repositioning an element's text label**


Text fields that are not associated with elements have an additional editing options - 
     (a) Select the text field with a left mouse click and use the keyboard short cut ``Control + e`` or from the main menu bar, select ``Edit --> Edit the text field``. A simple text editor window opens up to facilitate some basic text formatting features such as increasing the font size, font color, applying bold / italics / underlining formats to texts and inserting a hyperlink. 

.. note:: The hyperlink is preserved only for the diagrams that are exported to `pdf' format. For other picture exporting formats the hyperlink appears as a underlined text.

.. _edit text:

.. Figure:: graphics/edit_text.png
   :width: 370px
   :height: 400px
**Fig.23 Edit text window for the text field in workspace** This is a WYSIWYG (What You See Is What You Get) editor.


.. _Section.7:

