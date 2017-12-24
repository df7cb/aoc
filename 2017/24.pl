use strict;
use warnings;

my %connector;
while (<DATA>) {
	m!(\d+)/(\d+)! or die;
	die "duplicate" if $connector{$1}->{$2} or $connector{$2}->{$1};
	$connector{$1}->{$2} = 1;
	$connector{$2}->{$1} = 1;
}

my $width = 0;

my $longest = 0;
my $strongest = 0;
sub dfs {
	my ($c1, $length, $strength, @path) = @_;
	if ($length >= $longest) {
		print "New longest at $c1 ($length, $strength) via @path\n";
		$longest = $length;
	}
	if ($strength >= $strongest) {
		print "New strongest at $c1 ($length, $strength) via @path\n";
		$strongest = $strength;
	}
	foreach my $c2 (keys %{$connector{$c1}}) {
		next if $connector{$c1}->{$c2} == 2; # in use
		$connector{$c1}->{$c2} = 2;
		$connector{$c2}->{$c1} = 2;
		dfs($c2, $length + 1, $strength + $c1 + $c2, @path, $c2);
		$connector{$c1}->{$c2} = 1;
		$connector{$c2}->{$c1} = 1;
	}
}

dfs($width, 0, 0, $width);

__DATA__
25/13
4/43
42/42
39/40
17/18
30/7
12/12
32/28
9/28
1/1
16/7
47/43
34/16
39/36
6/4
3/2
10/49
46/50
18/25
2/23
3/21
5/24
46/26
50/19
26/41
1/50
47/41
39/50
12/14
11/19
28/2
38/47
5/5
38/34
39/39
17/34
42/16
32/23
13/21
28/6
6/20
1/30
44/21
11/28
14/17
33/33
17/43
31/13
11/21
31/39
0/9
13/50
10/14
16/10
3/24
7/0
50/50
