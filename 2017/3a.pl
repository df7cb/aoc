#!/usr/bin/perl
use strict;
use warnings;

my $addr = 312051;

my $x = 0;
my $y = 0;

my $i = 1;
my $l = 1;
while (1) {
	$x += $l;
	$i += $l;
	last if $i >= $addr;

	$y += $l;
	$i += $l;
	last if $i >= $addr;
	$l++;

	$x -= $l;
	$i += $l;
	last if $i >= $addr;

	$y -= $l;
	$i += $l;
	last if $i >= $addr;
	$l++;
}

print "x $x y $y i $i l $l\n";
print "addr $addr diff " . ($i - $addr) . "\n";
