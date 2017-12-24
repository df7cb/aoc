use strict;
use warnings;

my @prg = map { chomp; $_; } <DATA>;
my %reg;
my $pc = 0;

sub reg ($) {
	my $arg = shift;
	return $arg if $arg =~ /^-?\d+$/;
	return $reg{$arg} // 0;
}

my $muls = 0;
while (1) {
	die "segv after $muls muls" if $pc < 0 or $pc >= @prg;
	my $instr = $prg[$pc];
	print "   ";
	print join ' ', map { "$_: $reg{$_}" } sort keys %reg;
	print "\n$pc $instr\n";
	if ($instr =~ /set (\w) (.+)/) {
		$reg{$1} = reg($2);
	} elsif ($instr =~ /add (\w) (.+)/) {
		$reg{$1} += reg($2);
	} elsif ($instr =~ /sub (\w) (.+)/) {
		$reg{$1} -= reg($2);
	} elsif ($instr =~ /mul (\w) (.+)/) {
		$reg{$1} //= 0;
		$reg{$1} *= reg($2);
		$muls++;
	} elsif ($instr =~ /mod (\w) (.+)/) {
		$reg{$1} %= reg($2);
	} elsif ($instr =~ /jgz (\w) (.*)/) {
		if (reg($1) > 0) {
			$pc += reg($2);
			next; # skip $pc++ below
		}
	} elsif ($instr =~ /jnz (\w) (.*)/) {
		if (reg($1) != 0) {
			$pc += reg($2);
			next; # skip $pc++ below
		}
	} else {
		die "invalid instruction $instr";
	}
	$pc++;
}

__DATA__
set b 81
set c b
jnz a 2
jnz 1 5
mul b 100
sub b -100000
set c b
sub c -17000
set f 1
set d 2
set e 2
set g d
mul g e
sub g b
jnz g 2
set f 0
sub e -1
set g e
sub g b
jnz g -8
sub d -1
set g d
sub g b
jnz g -13
jnz f 2
sub h -1
set g b
sub g c
jnz g 2
jnz 1 3
sub b -17
jnz 1 -23
