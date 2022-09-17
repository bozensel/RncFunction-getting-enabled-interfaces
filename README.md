# RncFunction-getting-enabled-interfaces
how to set enabled interfaces from "st RncFunction=1,IubLink=Iub_" along with proxy id 

The following sample outputs under xxx.log files have been found and oper state == ENABLED proxy ids have been found out: 

BRP1R06> st RncFunction=1,IubLink=Iub_

210407-11:42:59 10.174.28.173 21.0a RNC_NODE_MODEL_V_21_436 stopfile=/tmp/23979
===================================================================================
Proxy  Adm State     Op. State     MO
===================================================================================
101137  0 (LOCKED)    0 (DISABLED)  RncFunction=1,IubLink=Iub_ADGUBR
14618  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_AYVAP
24295  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_AYVAPR
77144  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BAANF
31936  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BAANFQ
31939  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BAANFR
31942  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BAANFS
77147  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABBD
38585  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABBDQ
38588  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABBDR
77150  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABEV
39173  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABEVQ
39176  1 (UNLOCKED)  1 (ENABLED)   RncFunction=1,IubLink=Iub_BABEVR
===================================================================================


BRP1R06> q
Bye...
Output has been logged to file /home/shared/EUNVAN/script/lisans_alarm_hgenm_nodeb/lisans/rnc_log/BRP1R06.log

Sample output, including devide name: 

![image](https://user-images.githubusercontent.com/94804863/190860023-deddfdec-74b8-4395-a3fb-5d72e4448ccb.png)
