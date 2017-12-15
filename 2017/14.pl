use warnings;
use strict;
use lib '.';
use Knot;

my $key = 'ljoxqyyw';
my $bits;

for my $i (0 .. 127) {
	my $hash = Knot::knot(sprintf("$key-%d", $i));
	my $bin;
	foreach my $digit (split //, $hash) {
		$bin .= sprintf "%04b", hex($digit);
	}
	$bits += grep { $_ eq '1' } split(//, $bin);
	$bin =~ s/1/#/g;
	$bin =~ s/0/./g;
	print "$bin $bits\n";
}
