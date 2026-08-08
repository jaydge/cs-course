#!/usr/bin/env bash
# One-command GitHub setup using the GitHub CLI (gh).
# Run this from inside the extracted cs-course folder.
#
# Prerequisite: install and sign in to the GitHub CLI once:
#   gh auth login
#
# Usage:
#   ./setup-github.sh              # creates a private repo named "cs-course"
#   ./setup-github.sh my-repo-name # creates a private repo with your name
set -euo pipefail

REPO_NAME="${1:-cs-course}"

# Initialize git if this folder is not already a repo.
if [ ! -d .git ]; then
  git init -b main
  git add .
  git commit -m "Initial commit: computer science course materials"
fi

# Create the GitHub repo from this folder and push.
gh repo create "$REPO_NAME" \
  --private \
  --source=. \
  --remote=origin \
  --description "High school computer science course materials" \
  --push

echo "Done. Your repo is created and pushed: $REPO_NAME"
