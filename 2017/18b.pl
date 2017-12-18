use strict;
use warnings;

my @prg = <DATA>;
my %reg;
my $pc = 0;
my ($sntcount, $rcvcount);

my $procno;
pipe P0R, P1W;
pipe P1R, P0W;
if (fork > 0) { # parent
	$procno = 0;
	close P1R;
	close P1W;
	select((select(P0W), $|=1)[0]); # make P0W hot
} else {
	$procno = 1;
	close P0R;
	close P0W;
	select((select(P1W), $|=1)[0]);
}
$reg{p} = $procno;

sub reg ($) {
	my $arg = shift;
	return $arg if $arg =~ /^-?\d+$/;
	return $reg{$arg} // 0;
}

while (1) {
	die "segv" if $pc < 0 or $pc >= @prg;
	my $instr = $prg[$pc];
	chomp $instr;
	#print "   ";
	#print join ' ', map { "$_: $reg{$_}" } sort keys %reg;
	#print "\n$pc $instr\n";
	if ($instr =~ /set (\w) (.+)/) {
		$reg{$1} = reg($2);
	} elsif ($instr =~ /add (\w) (.+)/) {
		$reg{$1} += reg($2);
	} elsif ($instr =~ /mul (\w) (.+)/) {
		$reg{$1} //= 0;
		$reg{$1} *= reg($2);
	} elsif ($instr =~ /mod (\w) (.+)/) {
		$reg{$1} %= reg($2);
	} elsif ($instr =~ /jgz (\w) (.*)/) {
		if (reg($1) > 0) {
			$pc += reg($2);
			next; # skip $pc++ below
		}
	} elsif ($instr =~ /snd (.+)/) {
		if ($procno == 0) {
			print P0W reg($1) . "\n";
		} else {
			print P1W reg($1) . "\n";
		}
		$sntcount++;
		print "proc $procno sent ". reg($1) . " ($sntcount)\n";
	} elsif ($instr =~ /rcv (.+)/) {
		my $rcv;
		if ($procno == 0) {
			$rcv = <P0R>;
		} else {
			$rcv = <P1R>;
		}
		chomp $rcv;
		$rcvcount++;
		print "proc $procno received $rcv ($rcvcount)\n";
		$reg{$1} = $rcv;
	} else {
		die "invalid instruction $instr";
	}
	$pc++;
}

__DATA__
set i 31
set a 1
mul p 17
jgz p p
mul a 2
add i -1
jgz i -2
add a -1
set i 127
set p 952
mul p 8505
mod p a
mul p 129749
add p 12345
mod p a
set b p
mod b 10000
snd b
add i -1
jgz i -9
jgz a 3
rcv b
jgz b -1
set f 0
set i 126
rcv a
rcv b
set p a
mul p -1
add p b
jgz p 4
snd a
set a b
jgz 1 3
snd b
set f 1
add i -1
jgz i -11
snd a
jgz f -16
jgz a -19
