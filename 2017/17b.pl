use strict;
use warnings;

my $input = 369;
my $pos = 0;
my $col1 = undef;

for my $value (1 .. 50_000_000) {
	$pos = ($pos + $input) % $value;
	$col1 = $value if ($pos == 0);
	$pos = ($pos + 1) % ($value + 1);
}

print "$col1\n";
