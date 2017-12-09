use strict;
use warnings;
use Switch;

open F, "9.txt";
my $input = <F>;
close F;
my @input = split //, $input;

my $nesting = 0;
my $score = 0;
my $garbage = 0;

while (my $c = shift @input) {
	switch ($c) {
		case '!' { shift @input; }
		case '{' { $nesting++; $score += $nesting; print "now level $nesting\n"; }
		case '}' { $nesting--; }
		case '<' {
			GARBAGE: while (my $c = shift @input) {
				switch ($c) {
					case '!' { shift @input }
					case '>' { last GARBAGE; }
					else { $garbage++; }
				}
			}
		}
	}
}

print "nesting $nesting, score $score, garbage $garbage\n";
