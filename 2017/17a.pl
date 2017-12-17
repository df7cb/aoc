use strict;
use warnings;

my $input = 369;
my @buffer = (0);
my $pos = 0;

for my $value (1 .. 2017) {
	$pos = ($pos + $input) % $value;
	splice @buffer, $pos + 1, 0, ($value);
	$pos = ($pos + 1) % ($value + 1);

	printf "%4d: (%4d): ", $value, $pos;
	print "@buffer[0 .. $pos-1]";
	print "($buffer[$pos])";
	print "@buffer[$pos + 1 .. $value]";
	print "\n";
}

print "$pos: $buffer[$pos], $pos + 1: $buffer[$pos+1]\n";
