# START_VERSION_BLOCK
VERSION_MAJOR = 2
VERSION_MINOR = 2
VERSION_BUILD = 0
VERSION_ALPHA = 1
# END_VERSION_BLOCK

# Deprecations are removed at the next major bump. Derive the version from
# the block above so deprecation warnings can never drift out of date.
NEXT_MAJOR_VERSION = f"{VERSION_MAJOR + 1}.0.0"
