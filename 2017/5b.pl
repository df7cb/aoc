#!/usr/bin/perl

use strict;
use warnings;

undef $/;
my @tape = split /\n/, <DATA>;

my $cnt = 0;
my $pc = 0;
while ($pc >= 0 and $pc < @tape) {
	$cnt++;
	my $off = $tape[$pc];
	if ($off >= 3) {
		$tape[$pc]--;
	} else {
		$tape[$pc]++;
	}
	print "round $cnt pc $pc off $off\n" if ($cnt % 10000 == 0);
	$pc += $off;
}

print "exit at $pc after $cnt rounds\n";

__DATA__
2
2
0
0
-2
-1
-3
0
0
-3
-5
-5
1
-10
-8
-1
-8
-5
-12
-5
1
-6
-18
-17
-9
-12
-24
-16
-6
-12
-14
-15
-28
-1
-10
-2
-2
0
-16
-4
-22
-33
-34
-28
-41
-11
-16
-12
-25
-13
-12
-14
-17
-24
-48
-54
-7
-10
-8
-49
-24
-49
-39
-8
-53
2
-65
-55
-52
1
-54
-3
-60
-28
-3
-33
-41
-66
-70
-46
-68
-26
-22
0
-82
-72
-82
-61
-33
-15
-9
-19
-83
-46
-21
-92
-47
-72
-86
-7
-2
-65
-4
-64
-52
-30
-34
-50
-46
-107
-20
-61
-49
-82
-18
-108
-59
-7
-97
-66
-78
-31
-49
-89
-16
-27
-107
-120
-87
-74
-50
-11
-53
-14
-128
-124
-99
-42
-73
-129
-112
-85
-52
-23
-120
-22
-82
-65
-51
-118
-37
-59
-105
-59
-152
-6
-61
-96
-30
-126
-83
-65
-144
-106
0
-156
-79
-22
-15
-132
0
-144
-132
-119
-20
-92
-96
-21
-110
-124
-59
-23
-128
-67
-48
1
-185
-175
-70
-103
-71
-40
-76
-96
-85
1
-96
-165
-94
-129
-104
-165
-127
-135
-83
-103
-77
-61
-115
-33
-203
-174
-82
-81
-22
-86
-172
-143
-197
-70
-126
-193
-152
-213
-129
-176
-182
-9
-51
-108
-132
-28
-106
-163
-201
-128
-49
-48
-90
-163
-217
-146
-117
-122
-96
-40
-23
-125
-46
-121
-127
-50
-193
-40
-220
-253
-224
-86
-252
-129
-188
-154
-103
-110
-66
-205
-138
-256
-134
-39
-233
-90
-95
-76
-179
-27
-245
-242
-6
-124
-137
-275
-75
-99
-62
1
-15
-175
-9
-193
-22
-128
-140
-290
-119
-127
-271
-137
-188
-21
-82
-143
-210
-246
-94
-188
-238
-2
-10
-185
-142
-73
-213
-170
-150
-238
-23
-69
-13
-186
-56
-22
-297
-258
0
-302
-287
-209
-288
-280
-257
-164
0
-158
-197
-313
-229
-249
-240
-218
-169
-126
-186
-22
-105
-176
-270
-337
-129
-260
-100
-43
-301
-281
-258
-82
-110
-144
-193
-253
-115
-117
-230
-261
-299
-63
-118
-257
-17
-364
-214
-223
-182
-329
-299
1
-116
-306
-198
-34
-121
-132
-76
-27
-103
-118
-262
-383
-195
-323
-142
-279
-162
-318
-15
-362
-272
-291
-397
-49
-309
-158
-368
-215
-301
-168
-317
-24
-247
-33
-193
-309
-90
0
-104
-335
-42
-149
-241
-35
-397
-235
-10
-206
-45
-21
-80
-215
-411
-16
-338
-253
-169
-278
-339
-50
-321
-189
-72
-91
-411
-257
-139
-270
-253
-82
-139
-168
-195
-76
-125
-230
-194
-386
-216
-242
-407
-238
-173
-15
-424
-72
-363
-66
-462
-412
-171
-349
-342
-109
-358
-285
-196
-178
-268
-464
-410
-344
-374
-193
-156
-170
-157
-362
-473
-329
-96
-30
-26
-157
-434
-406
-349
-463
-156
-166
-423
-61
-268
-182
-66
-155
-426
-396
-207
-210
-129
-454
-277
-324
1
-76
-247
-9
-147
-155
-318
-494
-325
-348
-507
-391
-209
-481
-112
-236
-157
-515
-3
-245
-447
-521
-349
-429
-271
-93
-29
-482
-4
-174
-390
-278
-240
-208
-317
-331
-175
-319
-438
-337
-91
-26
-460
-479
-321
-464
-216
-379
-75
-215
-109
-465
-280
-189
-439
-345
-170
-250
-59
-257
-525
-475
-547
-504
-101
-238
-394
-501
-265
-426
-469
-68
-252
-216
-234
-395
-89
-353
-287
-559
-371
-400
-377
-385
-504
-159
-22
-378
-515
-133
-286
-414
-478
-205
-489
-37
-64
-556
-171
-366
-49
-540
-474
-501
-51
-457
-174
-231
-96
-365
-475
-385
-257
-271
-129
-616
-474
-127
-389
-407
-557
-448
-49
-324
-143
-271
-363
-82
-311
-593
-303
-355
-91
-181
-462
-453
-548
-171
-96
-110
-475
-412
-49
-379
-294
-294
-324
-382
-327
-233
-482
-209
-28
-375
-236
-538
-7
-427
-424
-169
-152
-421
-503
-17
-390
-615
-113
-45
-113
-150
-329
-111
-9
-649
-647
-652
0
-610
-127
-286
-405
-38
-225
-595
-195
-509
-61
-651
-279
-270
-54
-110
-324
-220
-630
-490
-313
-672
-591
-379
-27
-599
-232
-593
-463
-243
-375
-414
-476
-324
-269
-103
-65
-576
-452
-591
-7
-402
-696
-383
-498
-622
-690
-33
-660
-83
-393
-70
-197
-522
-616
-716
-342
-142
-374
-412
-241
-155
-22
-593
-691
-28
-150
-26
-681
-290
-688
-369
-552
-601
-231
-120
-484
-342
-497
-412
-342
-728
-600
-275
-88
-341
-752
-602
-41
-519
-663
-578
-758
-658
-69
-710
-567
-278
-299
-658
-363
-651
-138
-394
-403
-771
-569
-234
-230
-268
-130
-104
-507
-148
-400
-473
-699
-506
-497
-110
-279
-470
-776
-21
-10
-412
-419
-6
-488
-19
-86
-70
-386
-263
-59
-813
-776
-494
-644
-67
-450
-384
-232
-552
-227
-480
-599
-412
-190
-87
-483
-446
-153
-309
-729
-14
-163
-698
-27
-404
-656
-571
-686
-333
-49
-829
-541
-812
-782
-614
-534
-399
-100
-560
-547
-258
-808
-754
-543
-581
-785
-581
-500
-210
-709
-774
-263
-124
-469
-840
-374
-695
-747
-439
-260
-119
-792
-554
-310
-177
-749
-292
-617
-112
-303
-207
-785
-457
-608
-628
-654
-107
-510
-522
-701
-171
-102
-303
-804
-60
-771
-51
-570
-76
-440
-746
-704
-135
-738
-377
-23
-452
-732
-169
-262
-689
-271
-676
-503
-543
-529
-158
-547
-413
-898
-448
-810
-637
-440
-251
-798
-161
-334
-512
-214
-912
-571
-80
-192
-777
-298
-403
-909
-244
2
-377
-291
-86
-742
-71
-88
-137
-455
-671
-689
-243
-760
-229
-183
-516
-789
-205
-710
-607
-866
-634
-913
-105
-648
-895
-576
-165
-667
-89
-890
-481
-258
-434
-788
-417
-608
-855
-642
-152
-621
-558
-65
-259
-742
-195
-451
-85
-310
-402
-586
-508
-201
-775
-466
-80
-402
-565
-574
-351
-891
-704
-411
-266
-830
-1012
-712
-749
-842
-175
-927
-1003
-484
-723
-677
-607
-338
-367
-488
-618
-189
-109
-181
-547
-852
