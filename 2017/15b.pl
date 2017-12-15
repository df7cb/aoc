use strict;
use warnings;

my $ga = 277;
my $gb = 349;

my $round = 1;
my $matches = 0;

while ($round <= 5_000_000) {
	do {
		$ga = ($ga * 16807) % 2147483647;
	} while (($ga & 0x03) != 0);
	do {
		$gb = ($gb * 48271) % 2147483647;
	} while (($gb & 0x07) != 0);

	if (($ga & 0xffff) == ($gb & 0xffff)) {
		$matches++;
		print "match $matches in round $round: $ga $gb\n";
	}

	$round++;
}

