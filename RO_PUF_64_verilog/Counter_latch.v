//This file was gen automatically by Auto PUF and is licenced by QUB

module Counter_latch(
    input wire [15:0] A,
    input wire [15:0] B,
    input wire CLK,
    input wire EN,
    input wire Finished, 
    output reg [15:0] O_0,
    output reg [15:0] O_1
    );

always @ (posedge CLK) begin
    if (Finished == 1'b1) begin 
        if (EN == 1) begin
            O_0 <= A;
            O_1 <= B;
        end
    end
end

endmodule
