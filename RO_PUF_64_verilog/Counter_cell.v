//This file was gen automatically by Auto PUF and is licenced by QUB

module Counter_cell(
input   wire        CE, 
input   wire        CLR, 
input   wire        Oscillator, 
output  wire [15:0] Counter_value, 
); 

(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire Q[15:0]
(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire Q_inv[15:0]

assign Counter_value = Q 

(* BEL = "CFF" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_0 ( 
    .Q(Q[0]),
    .C(Oscillator),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[0])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_0_inver (
    .O(Q_inv[0]),
    .I0(Q[0])
);

(* BEL = "CFF" *)(* RLOC = "X0Y1" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_1 ( 
    .Q(Q[1]),
    .C(Q[0]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[1])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y1" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_1_inver (
    .O(Q_inv[1]),
    .I0(Q[1])
);

(* BEL = "CFF" *)(* RLOC = "X0Y2" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_2 ( 
    .Q(Q[2]),
    .C(Q[1]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[2])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y2" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_2_inver (
    .O(Q_inv[2]),
    .I0(Q[2])
);

(* BEL = "CFF" *)(* RLOC = "X0Y3" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_3 ( 
    .Q(Q[3]),
    .C(Q[2]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[3])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y3" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_3_inver (
    .O(Q_inv[3]),
    .I0(Q[3])
);

(* BEL = "CFF" *)(* RLOC = "X0Y4" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_4 ( 
    .Q(Q[4]),
    .C(Q[3]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[4])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y4" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_4_inver (
    .O(Q_inv[4]),
    .I0(Q[4])
);

(* BEL = "CFF" *)(* RLOC = "X0Y5" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_5 ( 
    .Q(Q[5]),
    .C(Q[4]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[5])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y5" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_5_inver (
    .O(Q_inv[5]),
    .I0(Q[5])
);

(* BEL = "CFF" *)(* RLOC = "X0Y6" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_6 ( 
    .Q(Q[6]),
    .C(Q[5]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[6])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y6" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_6_inver (
    .O(Q_inv[6]),
    .I0(Q[6])
);

(* BEL = "CFF" *)(* RLOC = "X0Y7" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_7 ( 
    .Q(Q[7]),
    .C(Q[6]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[7])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y7" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_7_inver (
    .O(Q_inv[7]),
    .I0(Q[7])
);

(* BEL = "CFF" *)(* RLOC = "X0Y8" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_8 ( 
    .Q(Q[8]),
    .C(Q[7]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[8])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y8" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_8_inver (
    .O(Q_inv[8]),
    .I0(Q[8])
);

(* BEL = "CFF" *)(* RLOC = "X0Y9" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_9 ( 
    .Q(Q[9]),
    .C(Q[8]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[9])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y9" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_9_inver (
    .O(Q_inv[9]),
    .I0(Q[9])
);

(* BEL = "CFF" *)(* RLOC = "X0Y10" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_10 ( 
    .Q(Q[10]),
    .C(Q[9]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[10])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y10" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_10_inver (
    .O(Q_inv[10]),
    .I0(Q[10])
);

(* BEL = "CFF" *)(* RLOC = "X0Y11" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_11 ( 
    .Q(Q[11]),
    .C(Q[10]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[11])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y11" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_11_inver (
    .O(Q_inv[11]),
    .I0(Q[11])
);

(* BEL = "CFF" *)(* RLOC = "X0Y12" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_12 ( 
    .Q(Q[12]),
    .C(Q[11]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[12])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y12" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_12_inver (
    .O(Q_inv[12]),
    .I0(Q[12])
);

(* BEL = "CFF" *)(* RLOC = "X0Y13" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_13 ( 
    .Q(Q[13]),
    .C(Q[12]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[13])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y13" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_13_inver (
    .O(Q_inv[13]),
    .I0(Q[13])
);

(* BEL = "CFF" *)(* RLOC = "X0Y14" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_14 ( 
    .Q(Q[14]),
    .C(Q[13]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[14])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y14" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_14_inver (
    .O(Q_inv[14]),
    .I0(Q[14])
);

(* BEL = "CFF" *)(* RLOC = "X0Y15" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
FDCE #( 
    .INIT(1'b0) 
) DFF_15 ( 
    .Q(Q[15]),
    .C(Q[14]),
    .CE(CE),
    .CLR(CLR),
    .D(Q_inv[15])
);

(* BEL = "C6LUT" *)(* RLOC = "X0Y15" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) 
LUT1 #(
    .INIT(64'h1) 
) FF_15_inver (
    .O(Q_inv[15]),
    .I0(Q[15])
);


endmodule
