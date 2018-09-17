.. users/manual/element_editor


Element Editor
===================================

Element can be viewed as a physical object (component) that is symbolically represented. An electrical, electronic, process or an instrumentation diagram employs a large number of symbols that are linked to each other that forms a system. Symbols can be standard, like those issued by ISA (International Society of Automation), or a custom defined by a design house. In QElectroTech such symbols are called elements. They can be given names to describe them and saved either in a \*.elmt or a \*.xml format. 


Creating a new element
---------------------------

Elements in QElectroTech exist in "xml" format. The ``QET Collection`` of elements provided with default QElectroTech installation parameters, are saved in a invisible folder ``$HOME/.qet/elements``. User may however save his/her elements anywhere on the disk. But, QElectroTech detects its elements only from this default folder whenever ``Reload`` is executed from the ``Element's panel tool bar``. Alternatively, users are also provided with a tool in element's panel tool bar, to import elements from a different folder. Refer to animation tutorial `Fig.36`_ of `Section.10`_.

Elements provided in the QET collection are read only and cannot be edited. However, they can be added to "User collection" and subsequently edited and saved. The animation graphic presented at `Fig.36`_ of `Section.10`_  will explain the steps in creating a new element.

Creating a new category
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        1. Select the ``User collection`` with a left mouse click. The elements can be directly created under it. However, it is a good practice to first create a ``category`` under the ``User collection``. 
	2. Left click the shortcut icon ``New category``. ``Add a new category`` wizard pops open, which will prompt the user of further steps to create a new category. ``Category`` is analogous to folders on a disk. Each new category will create a folder under ``$HOME/.qet/elements``.
	3. Enter a name to the new category field (internal name); the field takes only small letters, numbers and `-', `_' and `.'. 
	4. The field displays ``Name of the new category`` and language as ``en`` for English versions. Additional languages can also be added by left clicking the ``Add a line`` button. Double left click the text field and enter a name that the category should display. Hit ``enter`` from keyboard. Now left click ``Ok`` button to add the category to the user collection. 

The new category is added and appears under the ``User collection``. Point the cursor to the new category, its internal name is displayed in the tool tip and the text entered in the text field (explained in step 4) will be displayed as its name. 

Creating a new element
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	1. Click on the shortcut icon on the tool bar to create a ``New element``.

	2. A wizard pops open prompting the user for subsequent inputs to ``Create a new element``. Select the category in which the new element has to be created.

	3. Click the ``Next`` button. The action prompts for assigning a file name to the element. It is the name of the file on the disk in ``$HOME/.qet/elements``. Overwrite the default filename ``new_element`` and click ``Next`` to continue. The field accepts only small letters, numbers and `-‘, `_’ and `.’.

        4. The action leads to a elements name field; double click the text field to enter a name by which the element is displayed. The default language is ``en`` (english). More languages can be added and corresponding names set by clicking ``Add a line`` button. The fields can be edited by a double click. After completing entering the name click ``Finish`` to begin drawing the element in the elements' editor. 

	5. The element will be displayed under the ``User collection`` under the ``category`` chosen after it is drawn and saved in the elements' editor. However, a ``reload`` of the collection of elements is required. Refer to the graphic `Fig.36`_ of `Section.10`_.  

The element editor facilitates drawing of a new element or editing imported elements.  The element editor has a plain drawing area with two thin red colored reference cross hairs, whose center is origin with coordinates (0,0). The cross hair is basically a set of coordinate axes, that helps in dimensioning, positioning and scaling of drawings. However, it does not appear in the finished element. Refer `Section.9.2`_ for a description on elements' editor.

.. _section.9.2:

Description of Element editor
---------------------------------

.. image:: graphics/elements_editor.png
   :height: 500 px
   :width: 900 px

**Fig.27 Elements Editor Main Window**

.. _main menu bar:

Main Menu bar:
~~~~~~~~~~~~~~~~
The Main menu bar has the standard set of windows options like ``File``, ``Edit``, ``Display``, ``Settings`` and ``Help``. 

+------------+------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
| Menu bar   | Options          | Function                                                         | Keyboard shortcut         | Notes                            |
+============+==================+==================================================================+===========================+==================================+
| **File**   | New              | Creates a new file                                               |   ``Ctrl + n``            | Same as ``New`` on tool bar      |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Open             | Opens an existing element from user collection or imported list  |   ``Ctrl + o``            | Same as ``Open`` on tool bar     |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Open from a file | Opens a file, usually a *.elmt file on disk                      |   ``Ctrl + Shift +  n``   |                                  |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Recently opened  | History of recently opened item                                  |                           |                                  |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Save             | Saves the current changes to the drawing / element (overwrites)  |   ``Ctrl + s``            |  Same as ``Save`` on tool bar    |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Save as          | Saves the current drawing / element under a category             |                           |  Same as ``Save as`` on tool bar |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Save to a file   | Saves the current drawing / element as a file on disk            |   ``Ctrl + shift + s``    |                                  |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Reload           |  Reloads the element / drawing, can be used to revert changes    |   ``F5``                  |  Same as ``Reload`` on tool bar  |
+            +------------------+------------------------------------------------------------------+---------------------------+----------------------------------+
|            | Quit             |  Quit the elements editor window                                 |   ``Ctrl + q``            |                                  |
+------------+------------------+------------------------------------------------------------------+---------------------------+----------------------------------+


|


+--------------+-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
| Menu bar     | Options                                   | Function                                             | Keyboard shortcut         | Notes                      |
+==============+===========================================+======================================================+===========================+============================+
| **Edit**     |  Undo                                     | Undo the last action                                 |  ``Ctrl + z``             | Same as Undo on tool bar   |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Redo                                     | Repeat the last action                               |  ``Ctrl + Shift + z``     | Same as Redo on tool bar   |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Select All                               | Selects all objects in the drawing area              |  ``Ctrl + a``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Select none                              | Removes all current selections                       |  ``Ctrl + Shift + a``     |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Invert selection                         | Inverts selection of objects in workspace            |  ``Ctrl + i``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Cut                                      | Equivalent to copy + delete the object               |  ``Ctrl + x``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Copy                                     | Copies the object selected                           |  ``Ctrl + c``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Paste                                    | Pastes the object from last copy or cut              |  ``Ctrl + v``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Paste in the area                        | Pastes object in the area specified by a mouse click |  ``Ctrl + Shift + v``     |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Paste from                               | Pastes objects from a file or element in collection  |                           |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Delete                                   | Deletes the selected object                          |  ``Del``                  | Same as Delete on tool bar |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Edit name and information of the element | Opens dialogue to change name or language            |  ``Ctrl + e``             | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Edit author information                  | Opens dialogue to credit author                      |  ``Ctrl + y``             |                            |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Edit element properties                  | Sets attributes for dependency or referencing        |                           | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Bring forward                            | Sets the selected object to be the top most part     |  ``Ctrl + Shift + Home``  | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Raise                                    | Sends up the selected object(s) by one level         |  ``Ctrl + Shift + Up``    | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Lower                                    | Sends down the selected object(s) by one level       |  ``Ctrl + Shift + Down``  | Same as in tool bar        |
+              +-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+
|              |  Send backward                            | Sets the selected object at the lowest level         |  ``Ctrl + Shift + End``   | Same as in tool bar        |
+--------------+-------------------------------------------+------------------------------------------------------+---------------------------+----------------------------+


|


+---------------+------------------+-------------------------------+---------------------------+
| Menu bar      | Options          | Function                      | Keyboard shortcut         |
+===============+==================+===============================+===========================+
| **Display**   | Zoom in          | Enlarges drawing              | ``Ctrl + +``              | 
+               +------------------+-------------------------------+---------------------------+
|               | Zoom out         | Gets a wider view of drawing  | ``Ctrl + -``              |
+               +------------------+-------------------------------+---------------------------+
|               | Fit in view      | Fits drawing in window        | ``Ctrl + 9``              | 
+               +------------------+-------------------------------+---------------------------+
|               | Reset zoom       | Sets zoon level to zero       | ``Ctrl + 0``              |
+---------------+------------------+-------------------------------+---------------------------+

|


+---------------+--------------------------------+-------------------------------------------------+--------------------------------------------+
| Menu bar      | Options                        | Function                                        | Notes                                      |
+===============+================================+=================================================+============================================+
| **Settings**  | Display                        | View or hide options in the editor window       | Hides or shows information window etc.,    |
+               +--------------------------------+-------------------------------------------------+--------------------------------------------+
|               | Full screen mode               | Spreads the window to fill the screen           | Entire screen gets occupied by the window  |
+               +--------------------------------+-------------------------------------------------+--------------------------------------------+
|               | Configure QElectroTech         | Opens the configure QElectroTech window         | Same as described in `Section.4`_          |
+---------------+--------------------------------+-------------------------------------------------+--------------------------------------------+

|

+---------------+--------------------------------+-----------------------------------------------------------------------------+---------------------------+
| Menu bar      | Options                        | Function                                                                    | Keyboard shortcut         |
+===============+================================+=============================================================================+===========================+
| **Help**      | What is this ?                 | Enquires main menu options                                                  | ``Shift + F1``            | 
+               +--------------------------------+-----------------------------------------------------------------------------+---------------------------+
|               | About QElectroTech             | Displays information about authors, contributors, translators and Licensing |                           |
+               +--------------------------------+-----------------------------------------------------------------------------+---------------------------+
|               | About Qt                       | Displays information about Qt, a C++ toolkit for cross platform applications|                           |
+---------------+--------------------------------+-----------------------------------------------------------------------------+---------------------------+


|



Drawing area:
~~~~~~~~~~~~~~~~~~~
This is the dotted grid area over which the elements are drawn. The grid area has two kinds of markings ``.`` and ``+``. The distance between two consecutive ``+`` is 10px and between two consecutive ``.`` is 5px. 

User can pick up a drawing tool from the drawing tools with a single click. A faded gray cross hair mark now appears with cursor, with its intersecting point at the cursor position. These reference marks assist in the drawing. The ``information`` window describes the properties of individual part in the drawing and it is accessible only when the part is selected. The interactive behaviour with mouse in the drawing editor window on a macro level includes :

        (a) Selection of drawing parts is possible using left mouse button, in a manner described for selection of elements; refer `Selection properties`_. Individual parts can be selected with a left mouse click.
        (b) Mouse middle button can be used to zoom in and out.
        (c) Right mouse button click in the window gives access to many interesting functions, that includes most of the keyboard shortcuts described under `main menu bar`_.


Undo & Parts:
~~~~~~~~~~~~~~~~~~~
``Undo`` & ``Parts`` windows are related to each other, in the sense ``Undo`` keeps a record of each of the user's action in the drawing and ``Parts`` keep inventory of the parts. A brief use of these tabs are explained here - 

       (a) User may go back to any previous state by selecting the point in the ``Undo`` window. The states are listed in the chronological order with the latest state highlighted at the bottom of the list.
       (b) ``Parts`` window will show the inventory of the parts in the state specified by ``Undo``. Reverting to a previous state from ``Undo`` (*by point (a)*) will also update the corresponding inventory in the ``Parts`` window.
       (c) By default the parts tab is displayed. It contains all the individual parts that make up the drawing.
       (d) As the complexity of the drawing or element increases, it become easier to define properties of individual parts from the parts window. Select a part from the parts window, its referencing component in the drawing is highlighted in red color (other than texts). User can now define its attributes such as position, color, fill, thickness etc., in the ``information`` window.
       (e) User can also exploit keyboard shortcuts  ``Del`` (delete), ``Ctrl + c`` (copy), ``Ctrl + x`` (cut), ``Ctrl + v`` (paste) and ``Ctrl + z`` (undo) after selecting a part from the parts window, to speed up his/her work in the elements editor.


Information window:
~~~~~~~~~~~~~~~~~~~~~~~~
Information window displays the properties (attributes) of the selected individual part in the drawing. The properties of each part is its type dependent. However, a few things are common to some common shapes and they are described here.

.. _Appearance:

**Appearance** (For Line, Square, Ellipse and Arc tools)
     The appearance properties for a part are line style, outline color, weight (thickness of lines), filling color for closed geometry like rectangle, square etc., and antialiasing, which is to remove distortions of the skectches and smoothem for better smoother appearance.

     (a) Outline color specifies a color for the lines of the part selected. The selected part can be any geometry such as an ellipse, a curve, a straight line or a rectangle etc.,. There are five colors that a user can choose from namely -  Black, White, Green, Red and Blue.

     (b) Filling lets user to fill colors in the area bounded by the part's closed geometry such as a triangle, square, ellipse etc., User can keep the bounded area transparent by assigning ``None`` as the filling option or choose a color from Black, White, Green, Red and Blue.

     (c) Line style describes how line(s) should be displayed for the part selected. Options include 

	 (1) Normal: Straight continuous lines
	 (2) Dashed: Dashed lines 
	 (3) Dotted: Dotted lines
	 (4) Dots and dashes: One dot followed by a dash and repeated.

     (d) Weight defines the thickness of the line segments of the selected part. The options are qualitatively provided in QElectroTech such as None, Thin, Normal, Strong and High.
     
     (e) Antialiasing is an option to remove distortions from the selected part. Some lines (especially slanting) appear with stairstep-like distortions at the edges, referred to as jaggies in computer graphics. These distortions can be minimized by choosing this option.

.. _Geometry:

**Geometry**
     Geometrical properties for a part varies with the part selected. A simple line, a square or a rectangle, a circle, text fields, a terminal and an arc will have their own set of specific parameters, which are displayed in the information panel. Try drawing each of the drawing tools in the work area and select them to check the information area. Watch how the parameters change with each geometry. Try changing the parameters from the ``information`` window to note their effect on the part in the drawing. 

+---------------+--------------------------------+------------------------------------+ 
| Tool          | Geometry defined by            | Options in Information window      |
+===============+================================+====================================+
| **Line**      | Start position                 | x1, y1  (spin box)                 | 
+               +--------------------------------+------------------------------------+
|               | End position                   | x2, y2  (spin box)                 |
+               +--------------------------------+------------------------------------+
|               | Start arrow                    | End 1 and arrow size (value in px) |
+               +--------------------------------+------------------------------------+
|               | End arrow                      | End 2 and arrow size (value in px) |              
+---------------+--------------------------------+------------------------------------+

|

+---------------+--------------------------------+------------------------------------+
| Tool          | Geometry defined by            | Options in Information window      |
+===============+================================+====================================+
| **Rectangle** | Top left corner position       | x, y (spin box)                    | 
+               +--------------------------------+------------------------------------+
|               | Width  (Horizontal spread)     | value in px                        |
+               +--------------------------------+------------------------------------+
|               | Height (Vertical spread)       | value in px                        |
+---------------+--------------------------------+------------------------------------+

|

+---------------+--------------------------------+------------------------------------+
| Tool          | Geometry defined by            | Options in Information window      |
+===============+================================+====================================+
| **Ellipse**   | Center position                | x, y  (spin box)                   | 
+               +--------------------------------+------------------------------------+
|               | Diameter Horizontal            | value in px                        |
+               +--------------------------------+------------------------------------+
|               | Diameter Vertical              | value in px                        |
+---------------+--------------------------------+------------------------------------+

|

+---------------+--------------------------------+------------------------------------+
| Tool          | Geometry defined by            | Options in Information window      |
+===============+================================+====================================+
| **Polygon**   | Each coordinate in tabular     | x, y  columns                      | 
+               +                                +                                    +
|               | form; double click to change   |                                    |
+               +--------------------------------+------------------------------------+
|               | Closed polygon                 | Selection box                      |
+---------------+--------------------------------+------------------------------------+

|

+----------------+--------------------------------+------------------------------------+ 
| Tool           | Geometry defined by            | Options in Information window      |
+================+================================+====================================+
| **Add a Text** | Position                       | x, y (spin box)                    | 
+                +--------------------------------+------------------------------------+
|                | Size                           | Value in px (spin box)             |
+                +--------------------------------+------------------------------------+
|                | Color                          | Black or White as options          |
+                +--------------------------------+------------------------------------+
|                | Text                           | Text field (default text is ``T``) |
+                +--------------------------------+------------------------------------+
|                | Rotation angle                 | Graphic selection or input field   |          
+----------------+--------------------------------+------------------------------------+


|

+----------------+--------------------------------+------------------------------------+ 
| Tool           | Geometry defined by            | Options in Information window      |
+================+================================+====================================+
| **Arc**        | Center                         | x, y                               | 
+                +--------------------------------+------------------------------------+
|                | Diameter horizontal            | Value in px (spin box)             |
+                +--------------------------------+------------------------------------+
|                | Diameter vertical              | Value in px (spin box)             |
+                +--------------------------------+------------------------------------+
|                | Starting angle (begin of arc)  | Value in px (spin box)             |
+                +--------------------------------+------------------------------------+
|                | Angle (Arc termination angle)  | Value in px (spin box)             |             
+----------------+--------------------------------+------------------------------------+

|

+---------------+--------------------------------+------------------------------------+
| Tool          | Geometry defined by            | Options in Information window      |
+===============+================================+====================================+
| **Terminal**  | Position of blue tip           | x, y (spin box)                    | 
+               +--------------------------------+------------------------------------+
|               | Orientation                    | North, South, East or West         |
+---------------+--------------------------------+------------------------------------+

|

+----------------+--------------------------------+-----------------------------------------+ 
| Tool           | Geometry defined by            | Options in Information window           |
+================+================================+=========================================+
| **Text field** | Position                       | x, y (spin box)                         | 
+                +--------------------------------+-----------------------------------------+
|                | Size (Font size)               | Value in px (spin box)                  |
+                +--------------------------------+-----------------------------------------+
|                | Default text                   | Text field (default text is ``_``)      |
+                +--------------------------------+-----------------------------------------+
|                | Tagg (element requires 1 label)| None or Label (Combo box)               |
+                +--------------------------------+-----------------------------------------+
|                | Default rotation angle         | Graphic selection or input field        |
+                +--------------------------------+-----------------------------------------+
|                | Donot follow parent rotations  | Lock text field orientation (check box) |    
+----------------+--------------------------------+-----------------------------------------+

|

Active area:
~~~~~~~~~~~~~~~~~~
Active area is the part of the element that is selected with a left mouse click. The active area attributes (properties) are displayed in the ``information`` window and the segment will be highlighted in the ``parts`` window.

.. _working with drawing tools:

Working with drawing tools:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The following actions will describe a general behaviour in the elements editor. An instance of usage of a drawing tool is referred to as a part in the elements' editor. 

      (a) Drawing tools can be selected by a single click on the tool from the drawing and labelling tool bar.

      (b) Deselecting the tool is possible either by pressing ``Esc`` key from the keyboard or using a ``right click`` with the mouse.

      (c) The entire element or each drawing part can be selected using left mouse button. Single part can be selected by left clicking it (no drawing tool should be active). Multiple parts can be selected as described earlier under `Selection properties`_.  Selecting the part(s) creates a rectangular dotted box with small square handles around the object(s) (part(s)), which can be dragged (click + hold and move) with mouse to scale its size. The selected part(s) can be repositioned anywhere in the drawing area by drag dropping with mouse.

      (d) While working with the ``Add a polygon`` tool the following points should be kept in mind:  
 
	  (1) User must use a double click to complete one instance of drawing. 
	  (2) User must checkout the ``closed polygon`` option in the ``information`` panel, after completing a geometry to achieve a truly closed geometry. Options like ``filling`` with a color is possible only with closed geometry.
	  (3) A right click un-does the last action.
          (4) The option ``closed polygon`` can produce a closing line. For example, While drawing a triangle, a user can actually leave the tool after drawing a "V" shaped geometry and click closed polygon to complete the third side.

      (e) There are two tools for adding text to the drawing - ``Add a text`` and ``Add a text field``. ``Add a text field`` has few additional options, namely  ``Tag`` and ``Do not follow parent element rotations`` and a ``default text`` field. The specific purpose they serve are enumerated here 

	  (1) Every drawing or element requires at least one text label, which is achieved with ``Add a text field`` tool and then tagging the field as label from the combo-box in the ``Information`` window. 
	  (2) ``Add a text field`` provides a text field with the element which is editable in the QElectroTech main drawing window. But, the ``Add a text`` field is used to add permanent text to the element. This field is not editable during the element usage in the main drawing window.
	  (3) Checking out the option ``Do not follow parent element rotations`` will fix the alignment of the text field during its usage in the QElectroTech main drawing window i.e. if the element is rotated in the QElectroTech drawing area, the text field orientation remains fixed and does not follow the element. 
          (4) The text fields cannot be resized by dragging the selection handles. However, the font can be adjusted from the ``information`` window, by choosing a font size.



Element editor tool bar:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The tool bar is a collection of quickly accessible shortcuts to the features available in ``Main menu`` under ``File``, ``Edit``, ``Display``, ``Settings`` and ``Help``. Refer to tables listed in `main menu bar`_.


Drawing bar:
~~~~~~~~~~~~~~~~~~

The drawing bar has a set of tools like a line, rectangle, ellipse etc., for constructing an element. Each instance of usage of a tool is called a part. Each tool has its characteristic properties displayed in the ``Information`` window. Refer to section on `Geometry`_ to know in detail about specific features of the corresponding tool. In the following topics, detailed procedure to apply each tool is described.


(A) Line tool:
>>>>>>>>>>>>>>>>>>>>

Use a left mouse click to select and activate the ``Add a line`` tool from the drawing bar. From basics of geometry we know that a straight line is defined between atleast two coordinates. In the elements editor, we use left mouse clicks in the drawing area to select two coordinates to define the line segment. The line segment can be re-sized either from its ``information`` panel or using the sizing handles from its ``active area``. Drag dropping a line segment, to move it to another location in the drawing is also possible.

|

.. _Fig.28:
.. figure:: graphics/line_tool_info.png
  :width: 800px
  :height: 400px
  :alt: line tool in QElectroTech
**Fig.28 Line tool and formatting:**
The line segment information is shown here in `Fig.28`_ . The line segment geometry can be defined by a start coordinate and ending coordinate. The default end style is ``normal``; optionally the endings can be set as a ``simple arrow``, ``triangle arrow``, ``circle arrow`` or a ``diamond arrow``. End 1 is the initial point from where the line segment is drawn and End 2 is the ending point of the line segment. The triangle, circle and diamond arrow spaces can be filled with a color using the ``Filling`` combo box; the default is set as ``None`` indicating transparent. The line color can be set from the outline combobox. The options available are ``black``, ``white``, ``green``, ``red`` or ``blue``. The line style can be ``normal`` (continuous black line), ``dashed``, ``dotted`` or ``dashed & dotted``. The thickness of the line segment can be defined from the ``weight`` combo box. A slanted line can have rough outline with stairstep-like distortions, which can be smoothed by selecting the ``anti-aliasing`` option.
 
|


(B) Rectangle tool:
>>>>>>>>>>>>>>>>>>>>>>>>>

Select ``Add a rectangle`` icon with a left mouse click from the drawing bar to activate it. Use left mouse clicks to select two points that would become to top left corner coordinate and bottom right coordinate in the drawing area for the rectangle. The rectangle would be generated and it can be also be re-sized from its information panel or by using the resizing handles from its ``active area``. The rectangle can be shifted to a different position in the drawing area by drag dropping it to the other position.  

|

.. _Fig.29:

.. Figure:: graphics/rectangle_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Rectangle tool in QElectroTech         
**Fig.29 Rectangle tool and formatting:**
The Rectangle tool permits drawing of rectangular geometry in the element editor. Formatting options that are provided (``information`` window) for a rectangle are tabulated under `Appearance`_ and `Geometry`_. The geometry is defined by a point and the size of the rectangle (length and breadth). The appearance options are similar to those available for line tool.

|


(C) Terminal tool:
>>>>>>>>>>>>>>>>>>>>>>>>

 Elements require terminals to provide for connections with other elements in a circuit. Terminals offer an interactive point in the QElectroTech main drawing area, to create conductors between other terminals of either the same element or another element. The terminal tool in the elements editor provides for creating or rather adding terminals to elements. Click the red-blue (colored) terminal tool from the drawing tools bar to select it. A terminal is created at a point in the drawing area with a left mouse click. Several elements can be added with subsequent left clicks as long as the tool is selected (active). The terminal is not scalable but its orientation can be changed from the ``information`` panel. The blue colored square on the terminal corresponds to its position in the drawing. 

|

.. _Fig.30:

.. Figure:: graphics/terminal_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Terminal tool in QElectroTech
**Fig.30 Terminal tool information:** 
A terminal has a fixed set of dimensions and cannot be changed. It has a special directional property (orientation) and is specified as ``North``, ``South``, ``East`` and ``West``, from the ``information`` panel. This direction is determined by the blue square of the terminal, in the direction that it points relative to its red tail. It is described in the working area by a single coordinate, the point where it is added (blue square). The red tail of the terminal should be placed inside the element geometry. The terminal gives the element an interactive property in QElectroTech main drawing area. Refer to the animation describing creation of connections in `Fig.24`_.

|


(D) Ellipse tool: 
>>>>>>>>>>>>>>>>>>>>>>>>

Select the ``Add an ellipse`` icon from the drawing bar to activate it. Use a left mouse click in the drawing area to select a point to start drawing with the tool, click a second point to form an ellipse. The ellipse can be re-sized either by using re-sizing handles from its ``active area`` or using its ``information`` panel. Drag dropping the ellipse to shift to another position in the drawing area is possible.

|

.. _Fig.31:

.. Figure:: graphics/ellipse_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Ellipse tool in QElectroTech

**Fig.31 Ellipse tool with different format options:**
Ellipse tool permits drawing ellipses and circles in the drawing editor. The geometry of an ellipse is defined by the center point coordinate and its horizontal and vertical diameters. Standard line formatting styles are possible with ellipse tool. Some of them are illustrated in the `Fig.31`_ . Anti-Aliasing option  can be applied to smooothen the ellipse. This option is deselected for some of the illustrations shown in `Fig.31`_ (zoom to view closely). For a range of ellipse properties in the elements editor refer to `Appearance`_ and `Geometry`_.

|


(E) Polygon tool:
>>>>>>>>>>>>>>>>>>>>>>>

Select the ``Add a polygon`` tool with a left mouse click to activate. With the tool activated, use left mouse clicks to select a number of points that define the polygon in the drawing area. A polygon is formed by straight lines forming between to consecutive clicks. To finalize the geometry, use a right mouse click. To deselect the tool press ``Esc`` from keyboard. User may subsequently re-size the polygon using the handles from its ``active area`` or from its ``information`` panel. A seemingly closed geometry created using mouse clicks may not be a truly closed geometry. The option ``closed polygon`` should be checked-out in the ``information`` panel to achieve a bounded figure. Refer to the topic `working with drawing tools`_ to know more about using this tool. 

|

.. _Fig.32:

.. Figure:: graphics/polygon_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Polygon tool in QElectroTech

**Fig.32 Polygon tool in different formats:**
``Add a polygon`` tool is flexible tool to create varied geometry. It is a handy tool for creative users trying to sketch complicated symbols using the elements editor. Some sample sketches are drawn in `Fig.32`_ to display some of its capabilities. The geometry of a polygon is defined by two columns of coordinates for x and y, which are created for every left mouse click in the drawing area. The appearance properties are same as that of a line tool. For more information about using this tool refer to `working with drawing tools`_ , `Appearance`_ and `Geometry`_.

|


(F) Arc tool:
>>>>>>>>>>>>>>>>>>>

Select the ``Add an arc`` tool with a left mouse click to activate. With the tool activated, use left mouse click to select two points between which an arc is created. The arc tool draws an ellipse and crops it between the two points that were selected with mouse. Its geometry in elements editor is described by a center point, horizontal diameter along x-axis and a vertical diameter along y-axis and the angle between the first and the second clicks between which it is cropped. The arc may be re-sized using the handles from its ``active area`` or from its ``information`` panel. Arc tool has anti-aliasing as its default option for smoothness.

|

.. _Fig.33:

.. Figure:: graphics/arc_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Polygon tool in QElectroTech

**Fig.33 Arc tool with some formatted styles:**
The arc tool permits creation of an arc along an elliptical path. Some samples using arc tool are drawn in the `Fig.33`_. The appearance properties for arc are same as that of a line tool. Drag and drop functions are possible to move the arc in the drawing area. Refer to sections on `Appearance`_ and `Geometry`_ for more explanation.

|


(G) Add text: 
>>>>>>>>>>>>>>>>>>>>

Some elements require a name to be associated with it. ``Add a text`` tool permits inserting such text with an element. It can be activated by a single left click on the ``Add a text`` the tool in the drawing bar. Select a point in the drawing area by a left mouse click to insert the text field. Text can be entered from its ``information`` panel. Few basic formatting options are also included such as font size, color, orientation etc.,. The add text field is used to label the element or its components and it cannot be edited during the elements use in QElectroTech main drawing window. Also refer to sections on `working with drawing tools`_ , `Appearance`_ and `Geometry`_ for more information.

|

.. _Fig.34:

.. figure:: graphics/text_tool_info.png
  :width: 800px
  :height: 400px
  :alt: Polygon tool in QElectroTech

**Fig.34 Text tool and information:**
``Add a text`` tool permits fixed naming of the element or its parts at the time of its drawing in elements editor. Add text appears as a text box with a default text ``T``. The text can be resized from the font size field in its ``information`` panel. Drag and drop functions to reposition it in the elements editor drawing area are provided. The information panel describes the text box position by a single point coordinate, font size, color, text to display and orientation. Text can be set in any direction from 0 to 359.99\ :sup:`o`\  (degrees). The `Fig.34`_ shows text ``QET`` added to rectangles filled with different colors for demonstration.

|


(H) Add a text field:
>>>>>>>>>>>>>>>>>>>>>>>>>>>

Select the ``Add a text field`` tool with a left mouse click to activate it. Use left mouse click to select a point in the drawing area to add a text label. A text box with a default font ``_``, appears at the point selected. The field size is defined by the font size and can be set from its ``information`` panel. The add text field should be included as a label to the element or its components. The field is editable during its use in the QElectroTech drawings unlike the ``Add a text`` field. User may add information to the element using the field, while working with it in the QElectroTech main drawings. Also refer to sections on `working with drawing tools`_ , `Appearance`_ and `Geometry`_ for more information.

|

.. _Fig.35:

.. figure:: graphics/text_field_info.png
  :width: 800px
  :height: 400px
  :alt: Polygon tool in QElectroTech

**Fig.35 Text field inserted for an element:**
Every element requires at least one ``Add a text field``, which is tagged as a label from its ``information`` window. Drag and drop functions are possible for this field in both elements editor and in the QElectroTech drawing window independent of the parent element. The information panel describes the text box position by a single point coordinate, font size, default text as ``_``. Add a text field can be oriented in any direction possible from 0 to 359.99. The `Fig.35`_ shows the Add a text field in its default appearance. The tool has an additional option of ``Do not follow parent element rotations`` to lock its orientation in the QElectroTech drawing window. With this option selected, the text field does not rotate even when the parent element to which it is associated is rotated in the QElectroTech drawing.

|

.. _Section.10:

