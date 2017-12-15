use strict;
use warnings;

my $ga = 277;
my $gb = 349;

my $round = 1;
my $matches = 0;

while ($round <= 40_000_000) {
	$ga = ($ga * 16807) % 2147483647;
	$gb = ($gb * 48271) % 2147483647;

	if (($ga & 0xffff) == ($gb & 0xffff)) {
		$matches++;
		print "match $matches in round $round: $ga $gb\n";
	}

	$round++;
}

