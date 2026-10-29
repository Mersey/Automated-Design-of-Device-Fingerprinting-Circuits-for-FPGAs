import numpy as np


def make_RO_cell(Folder_loc):

    RO_cell = open((Folder_loc + "RO_cell.v"), "w")

    RO_cell.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    RO_cell.write("module RO_Cell(\n")
    RO_cell.write("input wire En,\n")
    RO_cell.write("output wire Oscil\n")
    RO_cell.write("); \n")
    RO_cell.write("\n")
    RO_cell.write('(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire A[3:0];\n')
    RO_cell.write("\n")
    RO_cell.write('assign Oscil = A[0];\n')
    RO_cell.write("\n")

    RO_cell.write('(* BEL = "A6LUT" *)(* LOCK_PINS = "I0:A5, I1:A6" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) \n')
    RO_cell.write("LUT2 #(\n")
    RO_cell.write(" .INIT(64'h4) // Specify LUT Contents\n")
    RO_cell.write(") Enable_Inv_0 (\n")
    RO_cell.write(" .O(A[1]), // 1-bit LUT6 output\n")
    RO_cell.write(" .I0(A[0]),\n")
    RO_cell.write(" .I1(En) \n")
    RO_cell.write(");\n\n")


    RO_cell.write('(* BEL = "B6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) \n')
    RO_cell.write('LUT1 #( \n')
    RO_cell.write(".INIT(64'h2) \n")
    RO_cell.write(') Inv_1 ( \n')
    RO_cell.write(' .O(A[2]), // 1-bit LUT6 output \n')
    RO_cell.write(' .I0(A[1]) \n')
    RO_cell.write('); \n\n')

    RO_cell.write('(* BEL = "C6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) \n')
    RO_cell.write('LUT1 #( \n')
    RO_cell.write(".INIT(64'h2) \n")
    RO_cell.write(') Inv_2 ( \n')
    RO_cell.write(' .O(A[3]), // 1-bit LUT6 output \n')
    RO_cell.write(' .I0(A[2]) \n')
    RO_cell.write('); \n\n')

    RO_cell.write('(* BEL = "D6LUT" *)(* LOCK_PINS = "I0:A5" *)(* RLOC = "X0Y0" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)(*DONT_TOUCH= "true"*) \n')
    RO_cell.write('LUT1 #( \n')
    RO_cell.write(".INIT(64'h2) \n")
    RO_cell.write(') Inv_3 ( \n')
    RO_cell.write(' .O(A[0]), // 1-bit LUT6 output \n')
    RO_cell.write(' .I0(A[3]) \n')
    RO_cell.write('); \n\n')

    RO_cell.write('\nendmodule\n')


def make_counter_cell(Counter_length, Folder_loc):

    Counter_cell = open((Folder_loc + "Counter_cell.v"), "w")

    Counter_cell.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    Counter_cell.write("module Counter_cell(\n")
    Counter_cell.write("input   wire        CE, \n")
    Counter_cell.write("input   wire        CLR, \n")
    Counter_cell.write("input   wire        Oscillator, \n")
    Counter_cell.write("output  wire ["+str(Counter_length-1)+":0] Counter_value, \n")
    Counter_cell.write("); \n\n")

    Counter_cell.write('(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire Q['+str(Counter_length-1)+':0]\n')
    Counter_cell.write('(*DONT_TOUCH= "true"*)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) wire Q_inv['+str(Counter_length-1)+':0]\n\n')

    Counter_cell.write('assign Counter_value = Q \n\n')
    i = 0

    Counter_cell.write('(* BEL = "CFF" *)(* RLOC = "X0Y'+str(i)+'" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) \n')
    Counter_cell.write('FDCE #( \n')
    Counter_cell.write("    .INIT(1'b0) \n")
    Counter_cell.write(') DFF_0 ( \n')
    Counter_cell.write('    .Q(Q[0]),\n') 
    Counter_cell.write('    .C(Oscillator),\n')  
    Counter_cell.write('    .CE(CE),\n')
    Counter_cell.write('    .CLR(CLR),\n')
    Counter_cell.write('    .D(Q_inv[0])\n')   
    Counter_cell.write(');\n\n')

    Counter_cell.write('(* BEL = "C6LUT" *)(* RLOC = "X0Y'+str(i)+'" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) \n')
    Counter_cell.write('LUT1 #(\n')
    Counter_cell.write("    .INIT(64'h1) \n")
    Counter_cell.write(') FF_0_inver (\n')
    Counter_cell.write('    .O(Q_inv[0]),\n')
    Counter_cell.write('    .I0(Q[0])\n')
    Counter_cell.write(');\n\n')
    
    for i in range(1,Counter_length):

        Counter_cell.write('(* BEL = "CFF" *)(* RLOC = "X0Y'+str(i)+'" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) \n')
        Counter_cell.write('FDCE #( \n')
        Counter_cell.write("    .INIT(1'b0) \n")
        Counter_cell.write(') DFF_'+str(i)+' ( \n')
        Counter_cell.write('    .Q(Q['+str(i)+']),\n') 
        Counter_cell.write('    .C(Q['+str(i-1)+']),\n')  
        Counter_cell.write('    .CE(CE),\n')
        Counter_cell.write('    .CLR(CLR),\n')
        Counter_cell.write('    .D(Q_inv['+str(i)+'])\n')   
        Counter_cell.write(');\n\n')

        Counter_cell.write('(* BEL = "C6LUT" *)(* RLOC = "X0Y'+str(i)+'" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*) (*DONT_TOUCH= "true"*) \n')
        Counter_cell.write('LUT1 #(\n')
        Counter_cell.write("    .INIT(64'h1) \n")
        Counter_cell.write(') FF_'+str(i)+'_inver (\n')
        Counter_cell.write('    .O(Q_inv['+str(i)+']),\n')
        Counter_cell.write('    .I0(Q['+str(i)+'])\n')
        Counter_cell.write(');\n\n')

    Counter_cell.write('\nendmodule\n')

def make_Mux_cell(Num_inputs, width, Folder_loc):
    import math

    MUX_cell = open((Folder_loc + "MUX_cell.v"), "w")

    MUX_cell.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    MUX_cell.write("module mux_any_size(  \n")
    # MUX_cell.write("    parameter N = "+Num_inputs+",    \n")
    # MUX_cell.write("    parameter WIDTH = "+str(Num_inputs)+" \n")             
    MUX_cell.write(")( \n")
    for i in range(width):
        MUX_cell.write("    input  ["+str(Num_inputs-1)+":0] data_in_"+str(i)+",   \n")

    MUX_cell.write("    input  ["+str(Num_inputs-1)+":0] sel,     \n")
    
    for i in range(width):   
        MUX_cell.write("    output reg data_out_"+str(i)+" \n")  

    MUX_cell.write(");\n")
    MUX_cell.write("\n")
    MUX_cell.write("always @(*) begin\n")
    for i in range(width):
        MUX_cell.write("    data_out_"+str(i)+" = data_in_"+str(i)+"[sel];\n")
    MUX_cell.write("end\n")

    MUX_cell.write("endmodule\n")

def make_DEMUX_cell(Num_inputs, Folder_loc):

    DEMUX_cell = open((Folder_loc + "DEMUX_cell.v"), "w")

    DEMUX_cell.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    DEMUX_cell.write("module demux_any_size (\n")
    DEMUX_cell.write("    input  wire in,\n")
    DEMUX_cell.write("    input  wire [$clog2("+str(Num_inputs)+")-1:0] sel,\n")
    DEMUX_cell.write("    output reg ["+str(Num_inputs)+"-1:0] out\n")
    DEMUX_cell.write(");\n")
    DEMUX_cell.write("\n")
    DEMUX_cell.write("    integer i;\n")
    DEMUX_cell.write("    always @(*) begin\n")
    DEMUX_cell.write("        out = {"+str(Num_inputs)+"{1'b0}};\n")
    DEMUX_cell.write("        out[sel] = in;\n")
    DEMUX_cell.write("    end\n")
    DEMUX_cell.write("\n")
    DEMUX_cell.write("endmodule\n")


def pair_selector(Folder_loc, NUM_ROs):

    pair_selector = open((Folder_loc + "pair_selector.v"), "w")

    pair_selector.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    pair_selector.write("module pair_selector_oneinput (\n")
    pair_selector.write("    input  wire ["+str(NUM_ROs-1)+":0] data_in,\n")
    pair_selector.write("    input  wire ["+str(int(np.log2((NUM_ROs*(NUM_ROs-1)/2))-1))+":0] pair_index,\n")
    pair_selector.write("    output wire data_out_0,\n")
    pair_selector.write("    output wire data_out_1,\n")
    pair_selector.write("    output wire ["+str(int(np.log2((NUM_ROs))-1))+":0] enable_0,\n")
    pair_selector.write("    output wire ["+str(int(np.log2((NUM_ROs))-1))+":0] enable_1,\n")
    pair_selector.write(");\n")
    pair_selector.write("    integer i, j;\n")
    pair_selector.write("    integer count;\n")
    pair_selector.write("    reg ["+str(int(np.log2((NUM_ROs))-1))+":0] idx_i;\n")
    pair_selector.write("    reg ["+str(int(np.log2((NUM_ROs))-1))+":0] idx_j;\n")
    pair_selector.write("\n")
    pair_selector.write("    always @* begin\n")
    pair_selector.write("        count = 0;\n")
    pair_selector.write("        idx_i = 0;\n")
    pair_selector.write("        idx_j = 1;\n")
    pair_selector.write("        for (i = 0; i < "+str(NUM_ROs-1)+"; i = i + 1) begin\n")
    pair_selector.write("           for (j = i + 1; j < "+str(NUM_ROs)+"; j = j + 1) begin\n")
    pair_selector.write("                if (count == pair_index) begin\n")
    pair_selector.write("                    idx_i = i;\n")
    pair_selector.write("                    idx_j = j;\n")
    pair_selector.write("                end\n")
    pair_selector.write("                count = count + 1;\n")
    pair_selector.write("           end\n")
    pair_selector.write("        end\n")
    pair_selector.write("    end\n")
    pair_selector.write("\n")
    pair_selector.write("    assign data_out_0 = data_in[idx_i];\n")
    pair_selector.write("    assign data_out_1 = data_in[idx_j];\n")
    pair_selector.write("    assign enable_0 = idx_i;\n")
    pair_selector.write("    assign enable_0 = idx_i;\n")
    pair_selector.write("\n")
    pair_selector.write("endmodule\n")

def Make_Counter_latch(Counter_length,Folder_loc):
    Counter_latch = open((Folder_loc + "Counter_latch.v"), "w")
    Counter_latch.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")
    Counter_latch.write("module Counter_latch(\n")
    Counter_latch.write("    input wire ["+str(Counter_length-1)+":0] A,\n")
    Counter_latch.write("    input wire ["+str(Counter_length-1)+":0] B,\n")
    Counter_latch.write("    input wire CLK,\n")
    Counter_latch.write("    input wire EN,\n")
    Counter_latch.write("    input wire Finished, \n")
    Counter_latch.write("    output reg ["+str(Counter_length-1)+":0] O_0,\n")
    Counter_latch.write("    output reg ["+str(Counter_length-1)+":0] O_1\n")
    Counter_latch.write("    );\n\n")
        

    Counter_latch.write("always @ (posedge CLK) begin\n")
    Counter_latch.write("    if (Finished == 1'b1) begin \n")
    Counter_latch.write("        if (EN == 1) begin\n")
    Counter_latch.write("            O_0 <= A;\n")
    Counter_latch.write("            O_1 <= B;\n")
    Counter_latch.write("        end\n")
    Counter_latch.write("    end\n")
    Counter_latch.write("end\n\n")

    Counter_latch.write("endmodule\n")

def Write_RO_placement(Folder_loc, Number_of_ROs_wanted, x_locs, y_locs):

    RO_placement = open((Folder_loc + "RO_placement_PUF.v"), "w")
    RO_placement.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")
    RO_placement.write("module ROs (\n")
    RO_placement.write("    input  wire ["+str(Number_of_ROs_wanted-1)+":0]  Enable,\n")

    RO_placement.write("    output wire ["+str(Number_of_ROs_wanted-1)+":0]  RO_PUF_Out\n")
    # RO_placement.write("    output wire ["+str(number_of_pairs_wanted-1)+":0]  RO_PUF_Out_1\n")
    RO_placement.write(");\n\n")

    count = 0
    i = 0

    for i2 in range(Number_of_ROs_wanted):

        RO_placement.write('(*RLOC_ORIGIN = "X'+str(x_locs[i,i2])+'Y'+str(y_locs[i,i2])+'", KEEP_HIERARCHY = "YES" *)(*DONT_TOUCH = "true" *)(*ALLOW_COMBINATORIAL_LOOPS= "true"*)\n')
        RO_placement.write('RO_Cell RO_pair_'+str(i2)+'_'+str(i)+' (\n')
        RO_placement.write('    .En(Enable['+str(count)+']),\n')
        RO_placement.write('    .Oscil(RO_PUF_Out['+str(i2)+'])\n')
        RO_placement.write(');\n\n')

        count += 1

    RO_placement.write("\n")
    RO_placement.write("endmodule\n")


def get_data():
    import pandas as pd

    Number_of_devices = 20 + 19 + 20 + 20 + 18 
    Num_of_ROs = 2200

    print("Number of devices:", Number_of_devices)

    Results_2 = np.zeros((Number_of_devices, Num_of_ROs, 4))
    temperature = 23

    count = 0
    panel = 1
    for c in range(20):
        if c != 99:

            File_name_Results = "Data/Frequency_test_32768_panel_" + str(panel) + "_" + str(c) + "_Temp_" + str(temperature) + "C.csv"

            Results_2[count] = pd.read_csv(File_name_Results).values
            count += 1

    panel = 2
    for c in range(19):
        if c != 99:
            File_name_Results = "Data/Frequency_test_32768_panel_" + str(panel) + "_" + str(c) + "_Temp_" + str(temperature) + "C.csv"

            Results_2[count] = pd.read_csv(File_name_Results).values
            count += 1

    panel = 3
    for c in range(20):
        if c != 99:
            File_name_Results = "Data/Frequency_test_32768_panel_" + str(panel) + "_" + str(c) + "_Temp_" + str(temperature) + "C.csv"
            Results_2[count] = pd.read_csv(File_name_Results).values
            count += 1

    panel = 4
    for c in range(20):
        if c != 99:
            File_name_Results = "Data/Frequency_test_32768_panel_" + str(panel) + "_" + str(c) + "_Temp_" + str(temperature) + "C.csv"

            Results_2[count] = pd.read_csv(File_name_Results).values
            count += 1

    panel = 5
    for c in range(18):
        if c != 99:
            File_name_Results = "Data/Frequency_test_32768_panel_" + str(panel) + "_" + str(c) + "_Temp_" + str(temperature) + "C.csv"

            Results_2[count] = pd.read_csv(File_name_Results).values
            count += 1

    Data = Results_2[:,:,1:]
    
    Averaged = np.mean(Data, axis=(2))
    Averaged_count_of_each_loc = np.mean(Averaged, axis=0)

    return Averaged_count_of_each_loc

def Make_PUF_top(Number_of_ROs_wanted, Counter_length, Folder_loc):

    PUF_TOP = open((Folder_loc + "PUF_TOP.v"), "w")
    PUF_TOP.write("//This file was gen automatically by Auto PUF and is licenced by QUB\n\n")

    PUF_TOP.write("module RO_Top( \n")
    PUF_TOP.write(" input wire          EN,\n")
    PUF_TOP.write(" input wire          CLK,\n")             
    PUF_TOP.write(" output wire         Finished,\n")
    PUF_TOP.write(" input  wire ["+str(int(np.log2((Number_of_ROs_wanted*(Number_of_ROs_wanted-1)/2))-1))+":0]  sel,\n")
    PUF_TOP.write(" input  wire         CLR,\n")
    PUF_TOP.write(" output wire ["+str(Counter_length-1)+":0]  Counter_latch_0_O_0,\n")
    PUF_TOP.write(" output wire ["+str(Counter_length-1)+":0]  Counter_latch_0_O_1,\n")
    PUF_TOP.write(" output wire         Response\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("wire ["+str(Counter_length-1)+":0]Counters_0_Counter_0;\n")
    PUF_TOP.write("wire ["+str(Counter_length-1)+":0]Counters_0_Counter_1;\n")
    PUF_TOP.write("wire ["+str(Number_of_ROs_wanted-1)+":0] Enable_0_EN;\n")
    PUF_TOP.write("wire ["+str(Number_of_ROs_wanted-1)+":0] RO_PUF_Out;\n")
    PUF_TOP.write("wire to_counter_0;\n")
    PUF_TOP.write("wire to_counter_1;\n")
    PUF_TOP.write("wire ["+str(int(np.log2((Number_of_ROs_wanted))-1))+":0] enable_0;\n")
    PUF_TOP.write("wire ["+str(int(np.log2((Number_of_ROs_wanted))-1))+":0] enable_1;\n")
    PUF_TOP.write("reg En_master;\n\n")

    PUF_TOP.write("always @ (posedge CLK) begin\n")
    PUF_TOP.write("    if (EN)\n")
    PUF_TOP.write("        if (!Finished)\n")
    PUF_TOP.write("            En_master <= 1;\n")
    PUF_TOP.write("        else\n")
    PUF_TOP.write("            En_master <= 0;\n")
    PUF_TOP.write("else\n")
    PUF_TOP.write("        En_master <= 0;\n")
    PUF_TOP.write("end \n\n")

    PUF_TOP.write("pair_selector_oneinput pair_0(\n")
    PUF_TOP.write("    .data_in(RO_PUF_Out),\n")
    PUF_TOP.write("    .pair_index(sel),\n")
    PUF_TOP.write("    .data_out_0(to_counter_0),\n")
    PUF_TOP.write("    .data_out_1(to_counter_1),\n")
    PUF_TOP.write("    .enable_0(enable_0),\n")
    PUF_TOP.write("    .enable_1(enable_1)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("DEMUX DEMUX_0 (\n")
    PUF_TOP.write("    .in(En_master),\n")
    PUF_TOP.write("    .enable_0(enable_0),\n")
    PUF_TOP.write("    .enable_1(enable_1),\n")
    PUF_TOP.write("    .out(Enable_0_EN)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("Counters Counter_0 (\n")
    PUF_TOP.write("    .RO(to_counter_0),\n")
    PUF_TOP.write("   .CE(1'b1),\n")
    PUF_TOP.write("    .CLR(CLR),\n")
    PUF_TOP.write("    .Counter_0(Counters_0_Counter_0)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("Counters_1 Counter_1 (\n")
    PUF_TOP.write("    .RO(to_counter_1),\n")
    PUF_TOP.write("    .CE(1'b1),\n")
    PUF_TOP.write("    .CLR(CLR),\n")
    PUF_TOP.write("    .Counter_0(Counters_0_Counter_1)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("Comparator Comparator_0 (\n")
    PUF_TOP.write("    .A(Counter_latch_0_O_0),\n")
    PUF_TOP.write("    .B(Counter_latch_0_O_1),\n")
    PUF_TOP.write("    .A_is_larger(Response)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("Counter_latch Counter_latch_0\n")
    PUF_TOP.write("(.A(Counters_0_Counter_0),\n")
    PUF_TOP.write("    .B(Counters_0_Counter_1),\n")
    PUF_TOP.write("    .CLK(CLK),\n")
    PUF_TOP.write("    .EN(En_master),\n")
    PUF_TOP.write("    .Finished(Finished),\n")
    PUF_TOP.write("    .O_0(Counter_latch_0_O_0),\n")
    PUF_TOP.write("    .O_1(Counter_latch_0_O_1)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("ROs ROs_0 (\n")
    PUF_TOP.write("    .Enable(Enable_0_EN),\n")
    PUF_TOP.write("    .RO_PUF_Out(RO_PUF_Out)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("counter_16_bit counter_16_bit_0 (\n")
    PUF_TOP.write("    .CE(1'b1),\n")
    PUF_TOP.write("    .CLK(CLK),\n")
    PUF_TOP.write("    .CLR(CLR),\n")
    PUF_TOP.write("    .EN(En_master),\n")
    PUF_TOP.write("    .finished(Finished)\n")
    PUF_TOP.write(");\n\n")

    PUF_TOP.write("endmodule\n")

              
def Auto_PUF(Number_of_ROs_wanted, Folder_loc, Counter_length):

    Averaged_count_of_each_loc = get_data()

    Sorted_and_loc_vector = np.zeros((len(Averaged_count_of_each_loc),2))

    Sorted_and_loc_vector[:,0] = Averaged_count_of_each_loc
    Sorted_and_loc_vector[:,1] = np.arange(len(Averaged_count_of_each_loc))

    Sorted_and_loc_vector = Sorted_and_loc_vector[Sorted_and_loc_vector[:,0].argsort()]
    Sorted_and_loc_vector = Sorted_and_loc_vector[Sorted_and_loc_vector[:,0]>18500]

    np.savetxt("data.cvs", Sorted_and_loc_vector, delimiter=",")

    number_of_pairs_wanted = 1

    Soultions = np.zeros((number_of_pairs_wanted, Number_of_ROs_wanted, 2))

    for a in range(number_of_pairs_wanted):

        temp = np.inf
        solution = 0

        for i in range(len(Sorted_and_loc_vector) - Number_of_ROs_wanted):
            if (Sorted_and_loc_vector[i,1] not in Soultions and Sorted_and_loc_vector[i+1, 1] not in Soultions):
                if np.mean(np.abs(Sorted_and_loc_vector[i:i+Number_of_ROs_wanted, 0] - np.mean(Sorted_and_loc_vector[i:i+Number_of_ROs_wanted, 0]))) < temp:
                    temp = np.mean(np.abs(Sorted_and_loc_vector[i:i+Number_of_ROs_wanted, 0] - np.mean(Sorted_and_loc_vector[i:i+Number_of_ROs_wanted, 0])))
                    solution = Sorted_and_loc_vector[i:i+Number_of_ROs_wanted]

        # print(solution)
        Soultions[a] = solution
        # print(Soultions)

    # print(Soultions)

    Soultions = Soultions.reshape((number_of_pairs_wanted*Number_of_ROs_wanted), 2).astype(int)

    # print(Soultions)

    loc = (Soultions[:,1])
    loc = loc.reshape((len(loc)//Number_of_ROs_wanted,Number_of_ROs_wanted)).astype(int)

    x_locs = loc // 100 
    y_locs = loc - x_locs * 100

    x_locs = x_locs + 22

    Write_RO_placement(Folder_loc, Number_of_ROs_wanted, x_locs, y_locs)
    pair_selector(Folder_loc, Number_of_ROs_wanted)
    make_DEMUX_cell(Number_of_ROs_wanted, Folder_loc)
    make_Mux_cell(Number_of_ROs_wanted, 1, Folder_loc)
    make_counter_cell(Counter_length, Folder_loc)
    make_RO_cell(Folder_loc)
    Make_PUF_top(Number_of_ROs_wanted, Counter_length, Folder_loc)
    Make_Counter_latch(Counter_length, Folder_loc)

    return "Done"


Auto_PUF(128, "RO_PUF_128_verilog/", 16)