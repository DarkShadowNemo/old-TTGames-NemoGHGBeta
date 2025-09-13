# old-TTGames-NemoGHGBeta

this imports and exports old ttgames ghg file formats into blender 4x, for nemo, twoc, haven and lsw1

as u can see in the img u can see a ghg model but still wip to fill entire face data up


<img width="1234" height="1258" alt="pearlpearlpearl" src="https://github.com/user-attachments/assets/6ee81900-c883-4c84-910c-88363ee12fcb" />

as you can 6 is in strips and tris on below called 0x030200010380XX6D, contains the face data called 0x83C0XX6E

between it contains the weights called 0x05C0XX6E

7th uses and operator 0x10 and 0x0F

the problem when you export ghg, u get flickering models on 0x04020001, not sure how to fix those
not tested 0x03020001

0x03010001 works on ghg

TODO
