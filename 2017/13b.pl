use strict;
use warnings;

my @scanner_depth;
my @layers;

while(<DATA>) {
	/(\d+): (\d+)/ or die;
	$scanner_depth[$1] = $2;
	push @layers, $1;
}

my $delay = -1;

DELAY: while (1) {
	$delay++;

	print "delay $delay\n" if ($delay % 50_000) == 0;

	foreach my $l (@layers) {
		next DELAY if (($l+$delay) % (2*($scanner_depth[$l]-1))) == 0;
	}

	print "no penalty with delay $delay\n";
	exit 0;
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
