//This file was gen automatically by Auto PUF and is licenced by QUB

module pair_selector_oneinput (
    input  wire [63:0] data_in,
    input  wire [9:0] pair_index,
    output wire data_out_0,
    output wire data_out_1,
    output wire [5:0] enable_0,
    output wire [5:0] enable_1,
);
    integer i, j;
    integer count;
    reg [5:0] idx_i;
    reg [5:0] idx_j;

    always @* begin
        count = 0;
        idx_i = 0;
        idx_j = 1;
        for (i = 0; i < 63; i = i + 1) begin
           for (j = i + 1; j < 64; j = j + 1) begin
                if (count == pair_index) begin
                    idx_i = i;
                    idx_j = j;
                end
                count = count + 1;
           end
        end
    end

    assign data_out_0 = data_in[idx_i];
    assign data_out_1 = data_in[idx_j];
    assign enable_0 = idx_i;
    assign enable_0 = idx_i;

endmodule
