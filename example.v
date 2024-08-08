// Test
		// Test1

module example #(
	parameter x = 5,
	parameter y = 4
)
(
	input clk,
	output clk2,
	output [4:0] count,
	input [4 : 0] counter,
	input [ 4 : 0 ] counter_1,
	output [4: 0] counter_2

);

assign count = 1;


endmodule
