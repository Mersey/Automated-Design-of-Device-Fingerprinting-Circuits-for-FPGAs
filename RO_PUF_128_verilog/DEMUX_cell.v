//This file was gen automatically by Auto PUF and is licenced by QUB

module demux_any_size (
    input  wire in,
    input  wire [$clog2(128)-1:0] sel,
    output reg [128-1:0] out
);

    integer i;
    always @(*) begin
        out = {128{1'b0}};
        out[sel] = in;
    end

endmodule
