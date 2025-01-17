.. _element/cross_reference/cross_reference_slave:

=================================
Cross reference at slave element
=================================

A slave element can only have one master element linked. QElectroTech does not allow that one slave element 
has more than one cross reference defined. 

.. figure:: /_external/_images/en/qet_element/qet_element_slave_linked.png
   :align: center

   Figure: QElectroTech slave element cross reference

An slave element has only the properties which defines how the element should be represented, the information 
from the element is not necessary, the master element is the element which defines the device and the element 
which appear at the bill of materials (BOM), The information about the devce can only be found at the master 
elemnt. 