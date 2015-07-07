Hardware devices
================

This section contains information about ethernet connected devices, their connection and VLANs (if applicable).

Switch01
---------

:Device type: switch
:Model: HP procurve 1810

=========	===================     ===========     ========= ==========
Interface	VLANs                   Connected       Interface Comments
									device    
=========	===================     ===========     ========= ==========
1		Default, SRV (T),       Switch02        1
		USR (T), WAN (T)     
2		SRV
=========	===================     ===========     ========= ==========


Switch02
---------

:Device type: switch
:Model: HP procurve 1810


=========       ===================     ===========     ========= ==========
Interface       VLANs                   Connected       Interface Comments
                                        device    
=========       ===================     ===========     ========= ==========
1               Default, SRV (T),       Switch01	    6	
                USR (T), WAN(T)
2               SRV
=========       ===================     ===========     ========= ==========
