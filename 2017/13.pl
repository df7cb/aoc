use strict;
use warnings;

my @scanner_depth;

while(<DATA>) {
	/(\d+): (\d+)/ or die;
	@scanner_depth[$1] = $2;
}

my $delay = -1;

DELAY: while (1) {
	$delay++;
	my @scanner_state;
	my @scanner_dir;
	my $penalty = 0;
	#next if $delay % 4 == 0; # layer 0
	#next if $delay % 2 == 1; # layer 1

	# reset
	foreach my $l2 (0 .. $#scanner_depth) {
		@scanner_dir[$l2] = 1;
		@scanner_state[$l2] = 0;
	}

	# try a run
	for my $tick (0 .. $#scanner_depth + $delay) {
		my $layer = $tick - $delay;
		#foreach my $l2 (0 .. $#scanner_depth) {
		#	next if $layer < 0;
		#	if ($scanner_depth[$l2]) {
		#		print "$l2: $scanner_state[$l2]/$scanner_depth[$l2] ";
		#		print " *** " if $l2 == $layer;
		#	} else {
		#		print "$l2 *** " if $l2 == $layer;
		#	}
		#}
		#print "\n";

		if ($layer >= 0 and $scanner_depth[$layer] and $scanner_state[$layer] == 0) {
			$penalty += $layer * $scanner_depth[$layer];
			print "with delay $delay, got hit in layer $layer by $scanner_depth[$layer], penalty is now $penalty\n";
			#next DELAY;
		}
		foreach my $l2 (0 .. $#scanner_depth) {
			if ($scanner_depth[$l2]) {
				$scanner_dir[$l2] = 1 if ($scanner_state[$l2] == 0);
				$scanner_dir[$l2] = -1 if ($scanner_state[$l2] == $scanner_depth[$l2] - 1);
				$scanner_state[$l2] += $scanner_dir[$l2];
			}
		}
		#print "\n";
	}
	print "with delay $delay, final penalty: $penalty\n";
	last if $penalty == 0;
}

__DATA__
0: 3
1: 2
2: 4
4: 6
6: 4
8: 6
10: 5
12: 8
14: 8
16: 6
18: 8
20: 6
22: 10
24: 8
26: 12
28: 12
30: 8
32: 12
34: 8
36: 14
38: 12
40: 18
42: 12
44: 12
46: 9
48: 14
50: 18
52: 10
54: 14
56: 12
58: 12
60: 14
64: 14
68: 12
70: 17
72: 14
74: 12
76: 14
78: 14
82: 14
84: 14
94: 14
96: 14
