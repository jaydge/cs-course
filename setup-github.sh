#!/usr/bin/env bash
# One-command GitHub setup using the GitHub CLI (gh).
# Run this from inside the extracted cs-course folder.
# Prerequisite: gh auth login  (as your personal account)
# Usage: ./setup-github.sh [repo-name]   (default: cs-course)
set -euo pipefail
REPO_NAME="${1:-cs-course}"
if [ ! -d .git ]; then
  git init -b main
  git add .
  git commit -m "Initial commit: computer science course materials"
fi
gh repo create "$REPO_NAME" --private --source=. --remote=origin \
  --description "High school computer science course materials" --push
echo "Done: $REPO_NAME"
