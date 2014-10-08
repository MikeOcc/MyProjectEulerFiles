#
#
#  Euler problem 66 - minimual Diophantine
#  D <= 1000
#
#
from math import sqrt
maxx=0;maxd=0;maxy=0
Dlist=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 158, 159, 160, 161, 162, 163, 164, 165, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 269, 270, 272, 273, 274, 275, 276, 278, 279, 280, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 302, 303, 304, 305, 306, 307, 308, 310, 311, 312, 314, 315, 316, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 354, 355, 356, 357, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 380, 381, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 395, 396, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 413, 414, 415, 416, 417, 418, 420, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 434, 435, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 450, 451, 452, 453, 455, 456, 458, 459, 460, 462, 464, 465, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 479, 480, 482, 483, 484, 485, 486, 487, 488, 489, 490, 492, 494, 495, 496, 497, 498, 499, 500, 503, 504, 505, 506, 507, 510, 512, 513, 514, 515, 516, 518, 519, 520, 522, 524, 525, 527, 528, 529, 530, 531, 532, 533, 534, 535, 536, 537, 539, 540, 542, 543, 544, 545, 546, 548, 550, 551, 552, 555, 557, 558, 560, 561, 562, 563, 564, 566, 567, 568, 570, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 590, 591, 592, 594, 595, 598, 600, 602, 603, 605, 606, 608, 609, 611, 612, 615, 616, 618, 620, 621, 623, 624, 625, 626, 627, 628, 629, 630, 632, 635, 636, 638, 639, 640, 642, 644, 645, 646, 647, 648, 650, 651, 654, 656, 657, 658, 659, 660, 663, 665, 666, 667, 668, 670, 671, 672, 674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 684, 687, 688, 689, 690, 692, 693, 695, 696, 697, 698, 699, 700, 702, 703, 704, 705, 706, 707, 708, 710, 711, 712, 713, 714, 715, 717, 720, 722, 723, 725, 726, 727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 740, 741, 742, 743, 744, 745, 747, 748, 750, 752, 755, 756, 759, 760, 761, 762, 765, 767, 768, 770, 774, 775, 776, 777, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 791, 792, 793, 795, 798, 799, 800, 803, 804, 806, 807, 808, 810, 812, 813, 815, 816, 817, 818, 819, 820, 822, 824, 825, 827, 828, 830, 831, 832, 833, 836, 837, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 850, 851, 852, 854, 855, 858, 860, 864, 866, 867, 868, 870, 872, 873, 874, 875, 876, 878, 879, 880, 882, 884, 885, 887, 888, 890, 891, 892, 894, 895, 896, 897, 898, 899, 900, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 914, 915, 916, 918, 920, 923, 924, 925, 927, 930, 933, 934, 935, 936, 938, 939, 940, 942, 943, 944, 945, 948, 950, 951, 952, 954, 957, 959, 960, 961, 962, 963, 964, 965, 966, 968, 969, 973, 975, 978, 979, 980, 982, 983, 984, 985, 986, 987, 990, 992, 993, 994, 995, 996, 999, 1000]



strt, endr = 6000000,10000000 #5000000,6000000 #4000000,5000000
print "Start to end",strt, endr

for i in xrange(1000,9,-1):
  if i in Dlist:continue
  D=i
  #if int(sqrt(i))**2 == i:
  #  if not i in Dlist:
  #    Dlist.append(i)
  #  continue

   
  
  for y in xrange(strt, endr):
    x2 = 1 + D * y * y
  
    x = int(round(sqrt(x2),6))  #int(x2**.5)
  
    if x*x == x2:
      if x>maxx:maxx=x;maxd=i;maxy=y
      print "Found min x at y:D",x,y,D
      if not D in Dlist:Dlist.append(D)
      break
  #print "min not found for D:",D 
  
print
print "Max X is ",maxx,maxd,maxy
print
print
Dlist = sorted(Dlist)
print Dlist
print "Length of Dlist is", len(Dlist)
print 
print "remaining Ds in Dlist"
for u in range(1,1001):
  if not u in Dlist: print u,