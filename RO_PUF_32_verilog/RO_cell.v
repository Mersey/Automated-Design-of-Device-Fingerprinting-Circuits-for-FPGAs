//This file was gen automatically by Auto PUF and is licenced by QUB

module RO_Cell(
input wire En,
output wire Oscil
); 

(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire A[3:0];

assign Oscil = A[0];

(* BEL = "A6LUT" *)(* LOCK_PINS = "I0:A5, I1:A6" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) 
LUT2 #(
 .INIT(64'h4) // Specify LUT Contents
) Enable_Inv_0 (
 .O(A[1]), 
 .I0(A[0]),
 .I1(En) 
);

(* BEL = "B6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) 
LUT1 #( 
.INIT(64'h2) 
) Inv_1 ( 
 .O(A[2]), 
 .I0(A[1]) 
); 

(* BEL = "C6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) 
LUT1 #( 
.INIT(64'h2) 
) Inv_2 ( 
 .O(A[3]), 
 .I0(A[2]) 
); 

(* BEL = "D6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) 
LUT1 #( 
.INIT(64'h2) 
) Inv_3 ( 
 .O(A[0]), 
 .I0(A[3]) 
); 


endmodule
