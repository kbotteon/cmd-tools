# timecard.py
#
# Generate a list of task allocation percentages from hours for my timecard
#
################################################################################
# Copyright 2022 Kyle Botteon
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
#!/usr/bin/env python3

import sys
import numpy

def timecard(hoursArr):

    # Split the input
    proHrs = hoursArr[0]
    taskHrsArr = hoursArr[1:]

    # Figure the total time worked, and the total direct time
    taskHrs = sum(taskHrsArr)
    totalHrs = taskHrs + proHrs

    # Of the total time, what percentage was each task?
    taskPctArr = []
    for taskHr in taskHrsArr:
        taskPctArr.append(taskHr/taskHrs)

    # Smear the prorated time based on the percentages from above
    proHrsArr = []
    for taskPct in taskPctArr:
        proHrsArr.append(taskPct * proHrs)

    # Sum the task and prorated hours to get total hours
    totalHrsArr = numpy.add(numpy.array(taskHrsArr), numpy.array(proHrsArr))

    # The percent value to bill is the task percentage of total time, plus the
    # subset of prorated time that will be allocated to each task
    tcPctArr = []
    for taskHr, proHr in zip(taskHrsArr, proHrsArr):
        tcPctArr.append((taskHr + proHr) / totalHrs)

    # Display results!
    for taskNo, tcPct in enumerate(tcPctArr):
        print("Task {} : {:.1f}, {:.1f}%".format(taskNo, totalHrsArr[taskNo], 100*tcPct))

    print(" Total : {:.1f} Hours".format(totalHrs))

if __name__ == "__main__":

    args = []
    for arg in sys.argv[1:]:
        args.append(float(arg))

    timecard(args)
