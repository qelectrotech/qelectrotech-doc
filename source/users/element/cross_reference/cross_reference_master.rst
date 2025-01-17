.. _element/cross_reference/cross_reference_master:

=================================
Cross reference at master element
=================================

A master element can have many slave element linked. QElectroTech allows that one master element 
has more than one cross reference defined. This characteristic is similar to the physical devices, 
the component which manage the control signal can define the action from many different components of 
the device.

.. figure:: /_external/_images/en/qet_element/qet_element_master_reference.png
   :align: center

   Figure: QElectroTech master element cross reference

The master element is the element which should appear at the Bill of Materials (BOM), it s the element 
with all the information. All slave element linked are following the master element.