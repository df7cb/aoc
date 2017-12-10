use strict;
use warnings;

my @list = 0 .. 255;
my $pos = 0;
my $skip = 0;
my $input = "192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12";
my @input = map { ord } split //, $input;
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
		print "$len: @rep\n";
		print "  @list\n";
		$pos = ($pos + $len + $skip) % 256;
		$skip++;
	}
}

for my $block (0 .. 15) {
	my @block = splice @list, 0, 16;
	my $h = 0;
	$h ^= $_ foreach @block;
	printf "%02x", $h;
}
print "\n";
