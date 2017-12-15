package Knot;

use strict;
use warnings;

sub knot ($)
{
	my @list = 0 .. 255;
	my $pos = 0;
	my $skip = 0;
	my @input = map { ord } split //, $_[0];
	@input = (@input, 17, 31, 73, 47, 23);

	for my $round (0 .. 63) {
		foreach my $len (@input) {
			my @rep = reverse ((@list, @list)[$pos .. $pos + $len - 1]);
			die unless @rep == $len;
			if ($pos + $len > 255) {
				@list = (@rep[256 - $pos .. $len - 1], @list[$pos + $len - 256 .. $pos - 1], @rep[0 .. 255 - $pos]);
			} else {
				@list = (@list[0 .. $pos - 1], @rep, @list[$pos + $len .. 255]);
			}
			die scalar(@list) unless @list == 256;
			$pos = ($pos + $len + $skip) % 256;
			$skip++;
		}
	}

	my $output;
	for my $block (0 .. 15) {
		my @block = splice @list, 0, 16;
		my $h = 0;
		$h ^= $_ foreach @block;
		$output .= sprintf "%02x", $h;
	}

	return $output;
}

1;
