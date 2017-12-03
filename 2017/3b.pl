#!/usr/bin/perl
use strict;

my $addr = 312051;

my $x = 0;
my $y = 0;

my $grid;
$grid->{$x}->{$y} = 1;

sub grid_sum
{
	$grid->{$x}->{$y} =
		$grid->{$x-1}->{$y-1} +
		$grid->{$x+0}->{$y-1} +
		$grid->{$x+1}->{$y-1} +
		$grid->{$x-1}->{$y} +
		$grid->{$x+1}->{$y} +
		$grid->{$x-1}->{$y+1} +
		$grid->{$x+0}->{$y+1} +
		$grid->{$x+1}->{$y+1};
	if ($grid->{$x}->{$y} > $addr) {
		print "$grid->{$x}->{$y} at $x $y\n";
		exit 0;
	}
}

my $i;
my $l = 1;
while (1) {
	for $i (0 .. $l - 1) {
		$x += 1;
		grid_sum();
	}
	for $i (0 .. $l - 1) {
		$y += 1;
		grid_sum();
	}
	$l++;
	for $i (0 .. $l - 1) {
		$x -= 1;
		grid_sum();
	}
	for $i (0 .. $l - 1) {
		$y -= 1;
		grid_sum();
	}
	$l++;
}
