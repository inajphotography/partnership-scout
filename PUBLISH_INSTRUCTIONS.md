# Publishing the Partnership Scout to GitHub

This folder is ready to go up as a public GitHub repository. Two ways to publish — pick one.

---

## Option 1 — GitHub website (no command line)

1. Go to https://github.com/new
2. Sign in (create an account if you don't have one — username suggestion: `inajphotography` or `inajalil`)
3. Fill in:
   - **Repository name:** `partnership-scout`
   - **Description:** `An open-source tool for pet photographers to find high-fit local businesses for gift-certificate partnerships.`
   - **Public** (so anyone can download)
   - **Do NOT** tick "Add a README" — you already have one
   - **Do NOT** tick "Add .gitignore" — you already have one
   - **Do NOT** tick "Choose a license" — you already have LICENSE
4. Click **Create repository**
5. On the next page, click **uploading an existing file** (the blue link near the top)
6. In Finder, open `/Users/inajalil/Library/Mobile Documents/com~apple~CloudDocs/ClaudeProjects/partnership-scout-public/`
7. Select ALL files and folders inside (README.md, LICENSE, config.example.py, .env.example, .gitignore, requirements.txt, agents/, scripts/, outputs/, PUBLISH_INSTRUCTIONS.md) and drag them into the browser
8. At the bottom, commit message: `Initial commit — Partnership Scout v1`
9. Click **Commit changes**

Your repo is live at `https://github.com/YOUR-USERNAME/partnership-scout`.

---

## Option 2 — Command line (if you have git installed)

### 2a. If you don't have gh CLI yet (recommended install)

```bash
# macOS with Homebrew
brew install gh

# Log in
gh auth login
# Choose: GitHub.com → HTTPS → Login with browser → follow prompts
```

### 2b. Publish the repo

From the `partnership-scout-public` folder:

```bash
cd "/Users/inajalil/Library/Mobile Documents/com~apple~CloudDocs/ClaudeProjects/partnership-scout-public"

# Initialise git in this folder
git init
git add .
git commit -m "Initial commit — Partnership Scout v1"

# Create the public repo on GitHub and push
gh repo create partnership-scout \
  --public \
  --source=. \
  --description "An open-source tool for pet photographers to find high-fit local businesses for gift-certificate partnerships." \
  --push
```

Your repo is now live at `https://github.com/YOUR-USERNAME/partnership-scout`.

### 2c. Without gh CLI (plain git)

```bash
cd "/Users/inajalil/Library/Mobile Documents/com~apple~CloudDocs/ClaudeProjects/partnership-scout-public"

git init
git add .
git commit -m "Initial commit — Partnership Scout v1"
git branch -M main

# Create the repo on https://github.com/new first (as in Option 1), then:
git remote add origin https://github.com/YOUR-USERNAME/partnership-scout.git
git push -u origin main
```

---

## After publishing

1. **Test the flow yourself from scratch.** Download the ZIP from your own repo, unzip to a new folder, follow your own README. Catch any bugs before your clients do.

2. **Update the README's repo URL.** Open `README.md` and replace `YOUR-GITHUB-USERNAME` with your actual GitHub username. Commit the change.

3. **Update Guide 2.** In the Guide 2 HTML, replace the placeholder `https://github.com/YOUR-USERNAME/partnership-scout` with the real URL.

4. **Share with your mastermind.**
   - Share both guides (Guide 1 and Guide 2 HTML/PDF)
   - Share the repo URL
   - Let them know you're available in Voxer/office hours as they work through it

5. **(Optional) Post publicly.** Announce it on Instagram/Threads/Facebook as "the thing I built to solve my own outreach problem, free for any pet photographer." Good authority-building post.

---

## Apify referral (for your clients)

Apify has a referral program. When you're approved, edit the README:

- Find the section on Apify signup
- Replace `https://apify.com` with your referral link
- Every client who signs up through your link will give you credit toward your own Apify usage

---

## If you want to add updates later

Once the repo exists, updates are:

```bash
cd "/Users/inajalil/Library/Mobile Documents/com~apple~CloudDocs/ClaudeProjects/partnership-scout-public"
# edit files
git add .
git commit -m "Short description of the change"
git push
```

Or the equivalent through the GitHub website — just upload the new version.

---

## Don't commit these files

The `.gitignore` already excludes these, but just so you're aware:

- `.env` — contains your API key
- `config.py` — your personal business config
- `outputs/` — personal scout runs

The public repo only contains the TEMPLATES (`.env.example`, `config.example.py`) — never your personal data.
