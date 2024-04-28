#    Hugerandom number generator with averaging feature
#    Copyright (C) 2024  angrypig555

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random
import sys
stringminNumber = sys.argv[1]
stringmaxNumber = sys.argv[2]
stringtries = sys.argv[3]
stringaverage = sys.argv[4]
minNumber = int(stringminNumber)
maxNumber = int(stringmaxNumber)
tries = int(stringtries)
trieskept = int(stringtries)
average = int(stringaverage)
averagenumber = 0

while int(tries) > 0:
    randomNumber = random.randint(minNumber, maxNumber)
    if average == 1:
        averagenumber += randomNumber
        print(randomNumber)
    else:
        print(randomNumber)
    tries -=1

if average == 1:
    averagenumber = averagenumber / trieskept
    print("Average: ", averagenumber)
else:
    print("Average not calculated")