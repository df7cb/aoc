use strict;
use warnings;

my @prg = map { chomp; $_; } <DATA>;
my %reg;
$reg{a} = 1; # flip on debug mode
my $pc = 0;
my $tick = 0;

sub reg ($) {
	my $arg = shift;
	return $arg if $arg =~ /^-?\d+$/;
	return $reg{$arg} // 0;
}

sub dump_state ()
{
	my $instr = $prg[$pc];
	print "$tick:   ";
	print join ' ', map { "$_: $reg{$_}" } sort keys %reg;
	print "\n$pc $instr\n";
}

while (1) {
	$tick++;
	die "segv" if $pc < 0 or $pc >= @prg;
	dump_state if ($tick % 100_000 == 0);
	my $instr = $prg[$pc];
	if ($instr =~ /set (\w) (\S+)/) {
		my $reg = $1;
		$reg{$1} = reg($2);
		dump_state() if $reg eq 'd';
	} elsif ($instr =~ /add (\w) (\S+)/) {
		$reg{$1} += reg($2);
	} elsif ($instr =~ /sub (\w) (\S+)/) {
		$reg{$1} -= reg($2);
	} elsif ($instr =~ /mul (\w) (\S+)/) {
		$reg{$1} //= 0;
		$reg{$1} *= reg($2);
	} elsif ($instr =~ /mod (\w) (\S+)/) {
		$reg{$1} %= reg($2);
	} elsif ($instr =~ /jgz (\S+) (\S+)/) {
		if (reg($1) > 0) {
			$pc += reg($2);
			next; # skip $pc++ below
		}
	} elsif ($instr =~ /jnz (\S+) (\S+)/) {
		if (reg($1) != 0) {
			$pc += reg($2);
			next; # skip $pc++ below
		}
	} elsif ($instr =~ /^ /) {
	} else {
		die "invalid instruction $instr";
	}
	$pc++;
}

__DATA__
set b 81  #             b = 81
set c b   #             c = 81
jnz a 2   # debug
jnz 1 5   # nodebug
mul b 100 # debug       b = 8100
sub b -100000 #         b = 108100
set c b                 c = 108100
sub c -17000      const c = 125100
                     while (1) {
set f 1   # nodebug l7  f = 1
set d 2   #             d = 2
set e 2   # l4          do { e = 2
set g d   # l8               do { g = d*g - b
mul g e   #
sub g b   #
jnz g 2   # l3                    if (g == 0)
set f 0   #                         f = 0
sub e -1  # l3                    e++
set g e   #                       g = e - b
sub g b   #
jnz g -8  # l8               } while (g!=0);
sub d -1  #                  d++
set g d   #                  g = d - b
sub g b
jnz g -13 # l4          } while (g!=0);
jnz f 2   # l5          if (f==0)
sub h -1  #               h++
set g b   # l5          g = b - c
sub g c
jnz g 2   # l6          if (g==0)
jnz 1 3   # segv          exit
sub b -17 # l6          b += 17
jnz 1 -23 # l7      }
