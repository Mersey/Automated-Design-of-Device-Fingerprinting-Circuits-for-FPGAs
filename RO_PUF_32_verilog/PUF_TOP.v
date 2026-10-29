//This file was gen automatically by Auto PUF and is licenced by QUB

module RO_Top( 
 input wire          EN,
 input wire          CLK,
 output wire         Finished,
 input  wire [7:0]  sel,
 input  wire         CLR,
 output wire [15:0]  Counter_latch_0_O_0,
 output wire [15:0]  Counter_latch_0_O_1,
 output wire         Response
);

wire [15:0]Counters_0_Counter_0;
wire [15:0]Counters_0_Counter_1;
wire [31:0] Enable_0_EN;
wire [31:0] RO_PUF_Out;
wire to_counter_0;
wire to_counter_1;
wire [4:0] enable_0;
wire [4:0] enable_1;
reg En_master;

always @ (posedge CLK) begin
    if (EN)
        if (!Finished)
            En_master <= 1;
        else
            En_master <= 0;
else
        En_master <= 0;
end 

pair_selector_oneinput pair_0(
    .data_in(RO_PUF_Out),
    .pair_index(sel),
    .data_out_0(to_counter_0),
    .data_out_1(to_counter_1),
    .enable_0(enable_0),
    .enable_1(enable_1)
);

DEMUX DEMUX_0 (
    .in(En_master),
    .enable_0(enable_0),
    .enable_1(enable_1),
    .out(Enable_0_EN)
);

Counters Counter_0 (
    .RO(to_counter_0),
   .CE(1'b1),
    .CLR(CLR),
    .Counter_0(Counters_0_Counter_0)
);

Counters_1 Counter_1 (
    .RO(to_counter_1),
    .CE(1'b1),
    .CLR(CLR),
    .Counter_0(Counters_0_Counter_1)
);

Comparator Comparator_0 (
    .A(Counter_latch_0_O_0),
    .B(Counter_latch_0_O_1),
    .A_is_larger(Response)
);

Counter_latch Counter_latch_0
(.A(Counters_0_Counter_0),
    .B(Counters_0_Counter_1),
    .CLK(CLK),
    .EN(En_master),
    .Finished(Finished),
    .O_0(Counter_latch_0_O_0),
    .O_1(Counter_latch_0_O_1)
);

ROs ROs_0 (
    .Enable(Enable_0_EN),
    .RO_PUF_Out(RO_PUF_Out)
);

counter_16_bit counter_16_bit_0 (
    .CE(1'b1),
    .CLK(CLK),
    .CLR(CLR),
    .EN(En_master),
    .finished(Finished)
);

endmodule
