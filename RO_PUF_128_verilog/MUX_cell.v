//This file was gen automatically by Auto PUF and is licenced by QUB

module mux_any_size(  
)( 
    input  [127:0] data_in_0,   
    input  [127:0] sel,     
    output reg data_out_0 
);

always @(*) begin
    data_out_0 = data_in_0[sel];
end
endmodule
