# Obsidian Gitcrypt Guide

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
    
---
