.. _users/manual/connectors


Connector
===================================

Elements have terminals, a conductor generating extension to elements to connect them with other elements or connectors. Making connections between terminals can be summarized as follows:
         
        1. Position the cursor on the element connector or terminal you want to connect; you will see that a blue dot appearing on the terminals you want to join.
        2. Left click the blue dot and hold and drag the pointer to the connector or terminal to join the other element you want to connect. If a green dot appears on the target terminals, it means that the conductor path between them is complete. A red dot means a ``forbidden connection".
	3. Release the left mouse button and the conductor will be completed. The conductor assumes a path between the two elements. However, the connectors can be edited by selecting the conductor with a left mouse click and dragging the green squares on it. Refer to `Section.8`_ for more operations with conductors.

.. _Fig.24:

.. Figure:: graphics/insert-wires_1.gif

.. youtube:: p5HKZyL2nPo
	:width: 500
	:height: 300           
   
**Fig.24 Animated graphics showing making of connection (by way of conductors) between two elements**  **(Top)** Graphic illustrates that for a connection to be made between the two terminals, blue dot should be selected and cursor should be dragged to the other terminal in a fashion shown by arrows. **(Bottom)** graphic animates connection between a relay and a push button. When a terminal of the coil is pointed with the mouse, a blue colored dot develops at the terminal tip. The dot turns red upon clicking and holding it. Holding and dragging the dot to the terminal of the push button causes a green colored dot to appear at the terminal of the push button, indicating that the connection is permitted. Releasing the mouse button at this point creates a conductor between the two terminals.


.. _Section.8:

Resizing conductors (connectors)
==================================

Adjusting conductors by moving elements
-------------------------------------------

          1. Select an element in a circuit by left clicking it and hold it in the work  space.
	  2. Drag the selected element in the circuit, the connectors linking the element to the rest of the circuit also moves.

.. _Fig.25:

.. youtube:: s1Wx2bM87SA
	:width: 500
	:height: 300 

**Fig.25 Adjusting conductors by repositioning elements**

Adjusting conductors with handles
-------------------------------------

        1. Select a connector with a left mouse click. The segment of the selected connector between two elements turns red, indicating that the conductor is selected.
	2. Position the cursor over the selected connector; you will find thick green colored squares appear over this segment, one each in a bend.
	3. The connector can now be adjusted as per the users demands by left clicking these thick little squares and holding and dragging to a new position. The connector changes its path during this action.
	4. To reset the altered path, left click the short cut icon `Reset conductors' provided in the tool bar with the connector selected (highlighted red). This action will undo all the earlier changes effected to the connector.

.. _Fig.26:

.. youtube:: XpVBM3Xq-74
	:width: 500
	:height: 300

**Fig.26 Animation showing adjusting conductors with handles and reset tool**

Adding text to connectors
-----------------------------

Connectors are provided with text fields, which can be configured from the new project option and conductor tab. Additional text fields can be inserted at desired locations. Text fields for connectors have the same behavior as the text fields for elements discussed under creating a new diagram. Double left click a connector text field and enter the text. The text can orient horizontally or vertically depending on the section of the connector where the test field is provided. The text fields can be rotated and re-positioned as required. Refer section on `configure conductor`_ for a complete list of configuration options.

Connector properties window
--------------------------------

A connector's properties window can be activated by double left clicking it. The connector and its text field properties can be set from this window. Only multiline connectors have text fields. Selecting the ``single line`` radio button deactivates the text field. The single line option has further options to format the connector as an earth, phase or a neutral conductor or a combination of any. Selecting the ``neutral`` option further facilitates formatting the conductor as ``Protective Earth Neutral`` (PEN). Number of phases can also be set upto 3 by selecting the ``phase`` radio button and using the slider or keying a value into the double spin field. Color and styles to a connector can be applied irrespective of other choices. Refer section on `configure conductor`_.

.. _Section.9:



