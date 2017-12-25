use strict;
use warnings;

my $state;
my %config;
my $checksum_steps;

my $s;
my $v;
while (<DATA>) {
	if (/^Begin in state (.)/) {
		$state = $1;
	} elsif (/Perform a diagnostic checksum after (\d+) steps/) {
		$checksum_steps = $1;
	} elsif (/In state (.):/) {
		$s = $1;
	} elsif (/If the current value is (\d):/) {
		$v = $1;
	} elsif (/Write the value (\d)/) {
		$config{$s}->{$v}->{write} = $1;
	} elsif (/Move one slot to the (\w+)/) {
		$config{$s}->{$v}->{dir} = $1 eq 'left' ? -1 : 1;
	} elsif (/Continue with state (.)/) {
		$config{$s}->{$v}->{state} = $1;
	} elsif (/^$/) {
	} else { die }
}

my $pc = 0;
my %tape;

my $step = 0;
while ($step++ != $checksum_steps) {
	if ($step % 100_000 == 0) {
		print "$step: $pc $state\n";
	}
	my $tape = $tape{$pc} // 0;
	my $next = $config{$state}->{$tape};
	if ($tape and $next->{write} eq '0') { # keep only '1' on tape
		delete $tape{$pc};
	} elsif (not $tape and $next->{write} eq '1') {
		$tape{$pc} = 1;
	}
	$pc += $next->{dir};
	$state = $next->{state};
}

print "Tape checksum: " . scalar(keys %tape) . "\n";

__DATA__
Begin in state A.
Perform a diagnostic checksum after 12667664 steps.

In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state C.

In state B:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state A.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.

In state C:
  If the current value is 0:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state E.

In state D:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the right.
    - Continue with state B.

In state E:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state F.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the left.
    - Continue with state C.

In state F:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state D.
  If the current value is 1:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state A.
