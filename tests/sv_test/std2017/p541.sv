class C1;
rand integer x;
endclass
class C2;
rand integer y;
endclass
initial begin
	C1 c1 = new();
C2 c2 = new();
integer z;
void'(c1.randomize());
// z = $random;
void'(c2.randomize());
end
