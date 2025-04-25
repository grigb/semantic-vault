# Obsidian Vault Setup with Git-Crypt and GitHub

A full guide to encrypting your Obsidian vault using `git-crypt`, storing your GPG key in 1Password, and syncing safely with GitHub.

---

## 🛠️ Prerequisites

### 1. Install Required Tools (macOS)

```bash
brew install git
brew install git-crypt
brew install gnupg
```

### 2. Generate Your GPG Key (If You Don’t Have One)

```bash
gpg --full-generate-key
```

- Type: RSA and RSA
    
- Key size: 4096
    
- Expiry: 0 (never expires)
    
- Name/Email: Use your actual info
    

Then verify it:

```bash
gpg --list-secret-keys --keyid-format LONG
```

### 3. Create Your GitHub Repo

- Go to [https://github.com/new](https://github.com/new)
    
- Name it `obsidian-vault`
    
- Set to **private**
    
- Leave README/license unchecked
    

### 4. (Optional) Trust Your Key Locally

```bash
gpg --edit-key your@email.com
trust
5 (ultimate)
quit
```

---

## 🚀 Run the Script

```bash
bash setup_obsidian_gitcrypt.sh /path/to/obsidian-vault git@github.com:yourusername/obsidian-vault.git you@email.com
```

It will:

- Initialize Git
    
- Set up `.gitattributes` with encrypted extensions
    
- Init `git-crypt`
    
- Add your GPG user
    
- Push to GitHub
    
- Export your private key for backup
    

---

## 📝 Script: setup_obsidian_gitcrypt.sh

```bash
#!/bin/bash
set -e

VAULT_DIR="$1"
REPO_URL="$2"
GPG_KEY_EMAIL="$3"

if [[ -z "$VAULT_DIR" || -z "$REPO_URL" || -z "$GPG_KEY_EMAIL" ]]; then
  echo "Usage: $0 /path/to/vault git@github.com:user/repo.git you@example.com"
  exit 1
fi

mkdir -p "$VAULT_DIR"
cd "$VAULT_DIR"

git init

echo "*.md filter=git-crypt diff=git-crypt" > .gitattributes
echo "*.canvas filter=git-crypt diff=git-crypt" >> .gitattributes
echo "*.csv filter=git-crypt diff=git-crypt" >> .gitattributes

git add .gitattributes
git commit -m "Add git-crypt encryption rules"

git-crypt init
git-crypt add-gpg-user "$GPG_KEY_EMAIL"

git remote add origin "$REPO_URL"
git branch -M main
git push -u origin main

echo "Exporting GPG private key to private-key.asc (for 1Password backup)"
gpg --armor --export-secret-keys "$GPG_KEY_EMAIL" > "$VAULT_DIR/private-key.asc"
echo "Saved GPG private key to: $VAULT_DIR/private-key.asc"
```

---

## 🛠 After Running Script

1. Copy your Obsidian content into your vault:
    

```bash
cp -R /original/notes/* /path/to/obsidian-vault/
```

2. Commit and push:
    

```bash
cd /path/to/obsidian-vault
git add .
git commit -m "Add notes"
git push
```

3. Upload `private-key.asc` to **1Password** as a secure note or file.
    

---

## 🧼 Fixing Upstream Branch Errors

If you see:

```
fatal: The current branch main has multiple upstream branches
```

Fix with:

```bash
git remote remove origin
git remote add origin git@github.com:yourusername/obsidian-vault.git
git branch -M main
git push -u origin main --force
```

---

## ✅ Next Step: Selective Notion Sync

Pending... this section will guide you to sync only select notes from your encrypted vault to Notion for publishing or mobile composition.