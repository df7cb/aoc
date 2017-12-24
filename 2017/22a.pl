use strict;
use warnings;

my @grid = map { chomp; [ split // ] } <DATA>;
print map { "@$_\n" } @grid;

# convert to hash so we have arrays with negative indexes
my %grid;
for my $x (0 .. @grid - 1) {
	for my $y (0 .. @grid - 1) {
		$grid{$y}->{$x} = $grid[$y]->[$x];
	}
}

my $x = (@grid-1) / 2;
my $y = $x;
my $dx = 0;
my $dy = -1;

my ($min_x, $max_x, $min_y, $max_y) = (0, 0, 0, 0);
my $step = 0;
my $infects = 0;
while (++$step <= 10_000) {
	print "step $step: $x $y\n";
	$grid{$y}->{$x} //= '.';
	if ($grid{$y}->{$x} eq '#') { # infected
		($dx, $dy) = (-$dy, $dx); # turn right
		$grid{$y}->{$x} = '.';
	} else {
		($dx, $dy) = ($dy, -$dx); # turn left
		$grid{$y}->{$x} = '#';
		$infects++;
	}
	$x += $dx;
	$y += $dy;
	$min_x = $x if $x < $min_x;
	$max_x = $x if $x > $max_x;
	$min_y = $y if $y < $min_y;
	$max_y = $y if $y > $max_y;
}

for my $y ($min_y .. $max_y) {
	for my $x ($min_x .. $max_x) {
		$grid{$y}->{$x} //= '.';
		print $grid{$y}->{$x};
	}
	print "\n";
}

print "infects: $infects\n";

__DATA__
##.###.....##..#.####....
##...#.#.#..##.#....#.#..
...#..#.###.#.###.##.####
..##..###....#.##.#..##.#
###....#####..###.#..#..#
.....#.#...#..##..#.##...
.##.#.###.#.#...##.#.##.#
......######.###......###
#.....##.#....#...#......
....#..###.#.#.####.##.#.
.#.#.##...###.######.####
####......#...#...#..#.#.
###.##.##..##....#..##.#.
..#.###.##..#...#######..
...####.#...###..#..###.#
..#.#.......#.####.#.....
..##..####.######..##.###
..#..#..##...#.####....#.
.#..#.####.#..##..#..##..
......#####...#.##.#....#
###..#...#.#...#.#..#.#.#
.#.###.#....##..######.##
##.######.....##.#.#.#..#
..#..##.##..#.#..###.##..
#.##.##..##.#.###.......#
