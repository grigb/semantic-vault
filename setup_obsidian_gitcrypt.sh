#!/bin/bash
# setup_obsidian_gitcrypt.sh
# One-command setup script for encrypted Obsidian vault using git-crypt + GitHub

set -e

# === CONFIGURATION ===
VAULT_DIR="$1"
REPO_URL="$2"
GPG_KEY_EMAIL="$3"

if [[ -z "$VAULT_DIR" || -z "$REPO_URL" || -z "$GPG_KEY_EMAIL" ]]; then
  echo "Usage: $0 /path/to/vault git@github.com:user/repo.git you@example.com"
  exit 1
fi

# === CREATE VAULT DIRECTORY ===
mkdir -p "$VAULT_DIR"
cd "$VAULT_DIR"

# === INIT GIT ===
git init

echo "*.md filter=git-crypt diff=git-crypt" > .gitattributes
echo "*.canvas filter=git-crypt diff=git-crypt" >> .gitattributes
echo "*.csv filter=git-crypt diff=git-crypt" >> .gitattributes

git add .gitattributes
git commit -m "Add git-crypt encryption rules"

# === INIT GIT-CRYPT ===
git-crypt init
git-crypt add-gpg-user "$GPG_KEY_EMAIL"

# === ADD REMOTE AND PUSH ===
git remote add origin "$REPO_URL"
git branch -M main
git push -u origin main

# === SUCCESS MESSAGE ===
echo "✅ Obsidian vault is initialized, encrypted with git-crypt, and pushed to $REPO_URL"
echo "Next: copy your Obsidian files into $VAULT_DIR, then use 'git add . && git commit -m \"...\" && git push'"
echo "🔐 Remember to back up your private GPG key (see private-key.asc)"

# === OPTIONAL: Export private key for 1Password backup ===
echo "\nExporting GPG private key to private-key.asc (for 1Password backup)"
gpg --armor --export-secret-keys "$GPG_KEY_EMAIL" > "$VAULT_DIR/private-key.asc"
echo "💾 Saved GPG private key to: $VAULT_DIR/private-key.asc"

