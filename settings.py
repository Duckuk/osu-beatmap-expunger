# Path to your osu song folder
# Windows default: %LOCALAPPDATA%/osu!/Songs
PATH_TO_SONG_FOLDER = "%LOCALAPPDATA%/osu!/Songs"

# Path to where filtered songs should be moved
PATH_TO_EXPUNGED_FOLDER = "%LOCALAPPDATA%/osu!/ExpungedSongs"

# Beatmap sets detected with any of these tags will be ignored
# Must be lowercase
TAGS_IGNORE = [
    "example_tag",
    "example_tag"
]

# Beatmap sets detected with any of these tags will be filtered
# Must be lowercase
ANY_TAGS_BLACKLIST = [
    "example_tag",
    "example_tag"
]

# Beatmap sets detected with all of the tags in any of the sub-lists will be filtered
# Must be lowercase
ALL_TAGS_BLACKLIST = [
    [
        "example_tag",
        "example_tag"
    ],
    [
        "example_tag",
        "example_tag"
    ]
]

# Only files with these file extensions will be scanned for tags
# Must be lowercase
SUFFIX_WHITELIST = [
    ".osu"
]

# What should be done to illegal beatmaps
# Options:
#  move (default)
#  copy
#  nothing
OPERATION = "move"

# Should multi-processing be used
# May or may not result in shorter execution time
# Disable this if any problems arise
MULTIPROCESSING = True