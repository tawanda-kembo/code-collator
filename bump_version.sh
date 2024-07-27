#!/bin/bash
set -e

# Default bump type
DEFAULT_BUMP=${DEFAULT_BUMP:-minor}

# Get the current version
CURRENT_VERSION=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.0.0")

# Split the version into parts
IFS='.' read -r -a VERSION_PARTS <<< "$CURRENT_VERSION"
MAJOR="${VERSION_PARTS[0]}"
MINOR="${VERSION_PARTS[1]}"
PATCH="${VERSION_PARTS[2]}"

# Bump the version
case $DEFAULT_BUMP in
  major)
    MAJOR=$((MAJOR + 1))
    MINOR=0
    PATCH=0
    ;;
  minor)
    MINOR=$((MINOR + 1))
    PATCH=0
    ;;
  patch)
    PATCH=$((PATCH + 1))
    ;;
  *)
    echo "Unknown bump type: $DEFAULT_BUMP"
    exit 1
    ;;
esac

NEW_VERSION="$MAJOR.$MINOR.$PATCH"

# Create a new tag
git tag "v$NEW_VERSION"
git push origin "v$NEW_VERSION"