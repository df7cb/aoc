use strict;
use warnings;

my @banks = qw(11	11	13	7	0	15	5	5	4	4	1	1	7	1	15	11);

my $rounds = 0;
my %seen;

while (1) {
	my $str = join ' ', @banks;
	if ($seen{$str}) {
		print "seen before in round $seen{$str}: $str\n";
		exit;
	}
	$seen{$str} = $rounds;
	$rounds++;
	print "round $rounds: $str ";

	my $slot = 0;
	for (my $i = 1; $i < @banks; $i++) {
		$slot = $i if ($banks[$i] > $banks[$slot]);
	}
	print "redistribution slot $slot\n";

	my $redist = $banks[$slot];
	$banks[$slot] = 0;

	while ($redist) {
		$slot = ($slot + 1) % @banks;
		$banks[$slot]++;
		$redist--;
	}
}
