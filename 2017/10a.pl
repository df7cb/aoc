use strict;
use warnings;

my @list = 0 .. 255;
my @input = (192,69,168,160,78,1,166,28,0,83,198,2,254,255,41,12);
my $pos = 0;
my $skip = 0;

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

print $list[0] * $list[1] . "\n";
