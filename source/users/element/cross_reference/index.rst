.. _element/cross_reference/index:

=======================
Element cross reference
=======================

E-CAD softwares like QElectroTech allow creating projects where different type of subsystems or/and 
disciplines are combinated. This means that one device can be represented many times. 

An example of combining subsystems is an electrical control system where the command system and 
the power system are combined. The control coil from a power contactor is represented at the control 
command system and the electrical contactors are represented at the electrical power system.

An example of combining different disciplines is the representation of an hydraulic valve at the electrical 
schema and at the hydraulic schema. 

The examples mentioned before are situations where different QElectroTech elements introduced at the project 
are representing the same device and later on they have to be listed as one item at the Bill Of Materials 
(BOM). For this reason, QElectroTech allow defining Master and Slave elements that later on will be linked.
The link between master and slave elements is known at QElectroTech as cross reference.

.. toctree::
   :maxdepth: 2

   cross_reference_master
   cross_reference_slave