module mul (input [31:0] a,  
            input [31:0] b,  
            output [63:0] mul);
   assign mul = a * b;  
endmodule