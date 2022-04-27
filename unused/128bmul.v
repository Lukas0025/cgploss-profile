module mul (input [127:0] a,  
            input [127:0] b,  
            output [255:0] mul);
   assign mul = a * b;  
endmodule