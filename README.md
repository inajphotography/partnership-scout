# Partnership Scout

An open-source tool for pet photographers to find high-fit local businesses for gift-certificate partnerships.

Scrapes Google Maps for pet-related (Tier 1) and ideal-client-overlap (Tier 2) businesses in your service area, enriches each with website research, fit-scores them 0-10, and produces a ready-to-use Excel outreach file with email templates in your voice.

Built for my own pet photography business in Canberra, Australia. Adaptable to any city.

---

## What it finds

**Tier 1 — direct pet businesses** (their clients are dog parents by definition):
- Veterinary clinics
- Dog groomers (including mobile)
- Doggy daycares
- Dog boarding kennels
- Dog trainers and behaviourists
- Dog walkers
- Independent pet stores
- Pet-friendly accommodation

**Tier 2 — ideal-client overlap** (filtered ruthlessly to only businesses whose clients plausibly spend $2,000–$5,000 on custom pet artwork):
- Picture framers and custom framing
- Dog-friendly cafes in premium suburbs
- Independent real estate agents
- Interior designers
- Home stagers

Intentionally excluded: yoga studios, pilates studios, naturopaths, massage therapists, gift stores, jewellers, florists, generic hair salons, generic coffee shops, supermarkets, and chain pet stores. These don't have strong correlation with premium pet artwork spend.

---

## What you get

A 5-sheet Excel workbook:

1. **Businesses** — master list sorted by fit score with 28 columns (business name, suburb, email, phone, socials, Google rating, reviews count, year founded, milestone hook, fit-score reasons, relationship notes, pet-reference research, about-page snippet, your personal line, outreach status tracker).
2. **Outreach Emails** — one template per category, in your voice, with merge fields (`{{owner_first_name}}`, `{{business_name}}`, `{{personal_line}}`, `{{milestone_hook}}`, `{{category_specific_angle}}`).
3. **Client Letter Template** — the mail-merge letter the partner's clients receive, with your gift certificate mechanics.
4. **Follow-up Sequence** — Day 7 and Day 14 follow-up emails.
5. **Dropped (audit)** — everything that got filtered out, with reasons (for transparency and future tuning).

Plus a raw JSON cache so you can regenerate the Excel without re-paying the Apify scraper.

---

## Prerequisites

- **Python 3.10+**
- **Apify account** — free tier includes $5/month usage credit, which covers ~2,000 scraped places. Sign up at [apify.com](https://apify.com). A full run of this scout costs ~$1.70, so the free tier is plenty to experiment.
- (Optional) **Claude Code** on the web ([claude.ai/code](https://claude.ai/code)) or VS Code extension, if you want to run the agent interactively with AI assistance. Not required — the script runs standalone.

---

## Install

```bash
# Clone the repo
git clone https://github.com/YOUR-GITHUB-USERNAME/partnership-scout.git
cd partnership-scout

# Create a virtual environment (optional but recommended)
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy the config template
cp config.example.py config.py

# Copy the env template
cp .env.example .env
```

---

## Configure

### 1. Add your Apify API key

Open `.env` and paste your token:

```
APIFY_API_KEY=apify_api_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Get your token from [apify.com](https://apify.com) → Settings → Integrations → API tokens.

### 2. Edit `config.py`

Open `config.py` and work through the sections in order:

1. **YOUR BUSINESS** — name, email, website, base suburb, primary city
2. **YOUR GIFT CERTIFICATE OFFER** — session fee, print credit, deposit, artwork minimum
3. **YOUR GEOGRAPHY** — bounding-box polygon covering your service area. Use [geojson.io](https://geojson.io/) to draw your polygon and paste the coordinates
4. **YOUR WARM RELATIONSHIPS** — businesses you already know; these get flagged and score bonuses
5. **YOUR BLOCKLIST** — competitors, chains, and precincts to exclude
6. **WARM-INCLUDE OVERRIDES** — businesses you want as partners even though their Google category wouldn't qualify
7. **CATEGORIES TO SCRAPE** — Tier 1 and Tier 2 lists (defaults work for most)
8. **CATEGORY-SPECIFIC ANGLES** — one short sentence per category in YOUR voice explaining why their clients are your ideal clients. This is the most important section. Read each one aloud — does it sound like you?

The example values in `config.example.py` are written for Ina J Photography in Canberra. Rewrite them in your own voice.

---

## Run

```bash
# Test run: 3 categories, ~$0.13 Apify cost, ~3-5 minutes
python scripts/partnership_scout.py --test

# Full run: all categories, ~$1.70 Apify cost, ~10-15 minutes
python scripts/partnership_scout.py --full

# Custom categories
python scripts/partnership_scout.py --categories "veterinary clinic,dog groomer,picture framer"

# Regenerate Excel from cached raw data ($0 cost — use after iterating on your config or voice)
python scripts/partnership_scout.py --full --from-raw outputs/raw-YYYY-MM-DD.json
```

Output lands in `outputs/partnerships-YYYY-MM-DD.xlsx`.

---

## What to do with the Excel

1. Open `outputs/partnerships-YYYY-MM-DD.xlsx`
2. Sort by Fit Score (it's already sorted) and filter Email column to not-blank
3. Work through the top 20-30 first
4. For each, fill the **Your Personal Line** column using the Pet Reference and About Snippet research columns. Keep it to 1 short sentence. Never invent — only reference what you can see in the research.
5. Copy the email template from Sheet 2, fill in your merge fields, send.
6. Track in the Outreach Status column.
7. Follow up on Day 7 and Day 14 using Sheet 4 templates.

When a partner says yes:
1. Send them the voucher mockup and the client letter template (Sheet 3)
2. They send you a spreadsheet with first names + dog names
3. You mail-merge the letter, print, stamp, and deliver the envelopes ready to post

---

## Running via Claude Code (optional)

If you use Claude Code (web or VS Code extension), the `agents/partnership-scout.md` file registers a custom agent. Invoke it with:

```
/agents partnership-scout
```

and Claude will walk you through the config, run the script, and help you personalise the outreach.

If you don't use Claude Code, ignore the agents folder — the Python script works standalone.

---

## Cost

The Apify Google Maps scraper charges $2.10 per 1,000 scraped places. A typical run pulls ~800 places, so ~$1.70 per full run. The Apify free tier includes $5/month credit, so roughly 2-3 full runs per month for free.

The enrichment phase (website fetching, email extraction) is free — it's just Python making HTTP requests.

---

## Customising for your market

The defaults are tuned for Australia. If you're in the US, UK, or elsewhere:

- Change `"behaviourist"` → `"behaviorist"` in `TIER_1_CATEGORIES` if you're American
- Change Australian street address conventions in `BLOCKED_STREET_ADDRESSES` to match your format
- Change `CURRENCY_SYMBOL` if not AUD/USD
- Edit the `REAL_ESTATE_CHAINS_TO_EXCLUDE` list in `scripts/partnership_scout.py` to match your local chains
- Adjust `CATEGORY_ANGLES` for regional voice differences

Everything else is already market-agnostic.

---

## Credits

Built by Ina Jalil of [Ina J Photography](https://inajphotography.com.au) (Canberra, Australia) to find partnership opportunities for her Gift Certificate Program. Taught to the Consistent Bookings Mastermind community.

If this saves you time, a mention would be lovely but isn't required. If you find improvements, PRs welcome.

---

## Licence

MIT. Use it, modify it, share it.
