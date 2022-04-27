module fulladder (input [63:0] a,  
                  input [63:0] b,  
                  input c_in,  
                  output c_out,  
                  output [63:0] sum);
   assign {c_out, sum} = a + b + c_in;  
endmodule