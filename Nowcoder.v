module data_select(
	input clk,
	input rst_n,
	input signed[7:0]a,
	input signed[7:0]b,
	input [1:0]select,
	output reg signed [8:0]c
);
//*************code***********//
always @(posedge clk or negedge rst_n) begin
    if(~rst_n) begin
		c <= 0;
	end else begin
		case(select)
			2'b00: c <= a;
			2'b01: c <= b;
			2'b10: c <= a + b;
			2'b11: c <= a - b;
		endcase
	end
end
//*************code***********//
endmodule
