# Simple data types can be combined into collections, which can have different structures
# The structure can matter a lot to efficiency and simplicity of use

# For example, we have seen lists, which are ordered collections of elements with a dynamic size and type
# Lists are very flexible, but not necessarily super efficient
participant_1_RTs = [713, 552, 473, 143, 638, 311, 668, 937, 621, 459]
participant_2_RTs = [287, 750, 411, 410, 351, 1040, 1124, 891, 924, 664]
participant_3_RTs = [342, 1063, 131, 485, 480, 159, 60, 389, 375, 653]

# Compare the RTs on the 4th trial
print(participant_1_RTs[3], participant_2_RTs[3], participant_3_RTs[3])

# Maybe a list of lists is slightly cleaner?
participants = [
    [713, 552, 473, 143, 638, 311, 668, 937, 621, 459],
    [287, 750, 411, 410, 351, 1040, 1124, 891, 924, 664],
    [342, 1063, 131, 485, 480, 159, 60, 389, 375, 653]
]

# It's cleaner, but still slightly cumbersome
for participant in participants:
    print(participant[3])

# So what's the difference between a list and an array?
# Mostly technical, so not much to worry about, but:
#  - Fixed size (no appending)
#  - Fixed type (everything of the same type)
#  - Bulk computations on arrays are much faster
import numpy as np  # noqa: E402

participants = np.array(participants)
print(participants[:, 3])  # It's so simple now!

# What about participant RT means and stdevs?
print(participants.mean(axis=1), participants.std(axis=1))

# ... or trial RT means?
print(participants.mean(axis=0))
