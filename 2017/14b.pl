use warnings;
use strict;
use lib '.';
use Knot;

my $key = 'ljoxqyyw';

my @grid;

for my $i (0 .. 127) {
	my $hash = Knot::knot(sprintf("$key-%d", $i));
	my $bin;
	foreach my $digit (split //, $hash) {
		$bin .= sprintf "%04b", hex($digit);
	}
	my @bits = split(//, $bin);
	$grid[$i] = \@bits;
}

my @seen;
my $regions = 0;
for my $next_y (0 .. 127) {
	for my $next_x (0 .. 127) {
		next unless $grid[$next_x]->[$next_y] == 1;
		next if $seen[$next_x]->[$next_y];
		$regions++;
		print "Region $regions found at $next_x, $next_y\n";

		my @queue = ([$next_x, $next_y]);
		BFS: while (my $p = shift @queue) {
			my ($x, $y) = @$p;
			next if $seen[$x]->[$y];
			push @queue, [$x-1, $y] if $grid[$x-1]->[$y];
			push @queue, [$x+1, $y] if $grid[$x+1]->[$y];
			push @queue, [$x, $y-1] if $grid[$x]->[$y-1];
			push @queue, [$x, $y+1] if $grid[$x]->[$y+1];
			$seen[$x]->[$y] = 1;
		}
	}
}

print "$regions\n";
