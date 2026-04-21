"""Partnership Scout configuration.

Copy this file to config.py (`cp config.example.py config.py`) and edit for
your photography business. Everything here is yours to customise — the script
imports from config.py, not this file.

Sections:
  1. YOUR BUSINESS
  2. YOUR GIFT CERTIFICATE OFFER
  3. YOUR GEOGRAPHY
  4. YOUR WARM RELATIONSHIPS
  5. YOUR BLOCKLIST
  6. WARM-INCLUDE OVERRIDES
  7. CATEGORIES TO SCRAPE
  8. CATEGORY-SPECIFIC ANGLES (in your voice)

Example values below reflect Ina J Photography in Canberra. Replace them.
"""
from __future__ import annotations


# ============================================================================
# 1. YOUR BUSINESS
# ============================================================================

BUSINESS_NAME = "Your Photography Business"
PHOTOGRAPHER_FIRST_NAME = "YourFirstName"
PHOTOGRAPHER_BASE = "YourSuburb"                 # Your home base suburb
PHOTOGRAPHER_CITY = "YourCity"                   # City you serve
PHOTOGRAPHER_EMAIL = "you@yourdomain.com"
PHOTOGRAPHER_WEBSITE = "yourwebsite.com"
PHOTOGRAPHER_INSTAGRAM = "@yourinstagram"


# ============================================================================
# 2. YOUR GIFT CERTIFICATE OFFER
# ============================================================================
# These values populate the outreach email, gift cert card, and client letter.

CURRENCY_SYMBOL = "$"
GIFT_CERT_TOTAL_VALUE = 490                       # Session fee + print credit
GIFT_CERT_SESSION_FEE = 190                       # Session fee alone
GIFT_CERT_PRINT_CREDIT = 300                      # Print credit alone
GIFT_CERT_CLIENT_MINIMUM_SPEND = 990              # Your artwork minimum
GIFT_CERT_CLIENT_TYPICAL_SPEND = "from $1,000 to $3,000 all up"
GIFT_CERT_OPTIONS_FROM = 300                      # "Options start at $X"
CONSULTATION_DEPOSIT = 100                        # Deposit at consultation
GIFT_CERT_REGISTER_BY_DAYS = 30                   # Register-by window
GIFT_CERT_CLIENTS_PER_PARTNER = 10                # How many vouchers per partner


# ============================================================================
# 3. YOUR GEOGRAPHY
# ============================================================================
# Bounding-box polygon covering the area you serve. Use https://geojson.io/ to
# draw it and paste the coordinates below. Coordinates are [longitude, latitude].
#
# Example below covers Canberra ACT + surrounding NSW towns. Replace with your
# service area.

SERVICE_AREA_POLYGON = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [148.75, -35.95],
            [149.55, -35.95],
            [149.55, -35.05],
            [148.75, -35.05],
            [148.75, -35.95],
        ]],
    },
}

# Short text appended to Google Maps search queries (e.g. "dog groomer Canberra").
# Use your primary city name.
LOCATION_SEARCH_HINT = "YourCity"

# Premium suburbs in your service area — used to filter Tier 2 businesses
# (real estate agents, dog-friendly cafes) to keep only the ones whose clients
# fit your ideal client. Lowercase names.
PREMIUM_SUBURBS = {
    # "suburb_1", "suburb_2", "suburb_3",
}


# ============================================================================
# 4. YOUR WARM RELATIONSHIPS
# ============================================================================
# Businesses you already know. Key: lowercase substring of the business name.
# Value: note describing the connection. These get +2 fit score and appear in
# the Relationship Note column of the output Excel.

RELATIONSHIP_NOTES: dict[str, str] = {
    # "example cafe": "Owner Sarah is a friend. Reach out personally.",
    # "jane smith realty": "Jane photographed my home in 2024.",
}


# ============================================================================
# 5. YOUR BLOCKLIST
# ============================================================================
# Business titles containing these substrings will be dropped. Include:
#   - Direct competitors (other pet photographers)
#   - Marketplaces that aren't a single business (e.g. Mad Paws)
#   - Supermarkets, big chains
#   - Chain pet stores
#
# Case-insensitive substring match.

BLOCKLIST = [
    # "name of competing photographer",
    # "name of chain to exclude",
    # "supermarket",
    # "petco", "petsmart",
]

# Street addresses to exclude (useful for precincts where a competitor has
# exclusivity with local businesses). Example: if a competitor handles
# photography for all businesses on "Main Street", add that here.
BLOCKED_STREET_ADDRESSES: list[str] = [
    # "main street, exampletown",
]


# ============================================================================
# 6. WARM-INCLUDE OVERRIDES
# ============================================================================
# Businesses you want as partners even though their Google category wouldn't
# qualify as Tier 1 or Tier 2 (e.g. your gym, your yoga studio, your
# hairdresser — anywhere you have a personal connection that lets you skip
# cold outreach). Key: lowercase substring. Value: (label, tier).

FORCE_INCLUDE_AS_PARTNERSHIP: dict[str, tuple[str, int]] = {
    # "my gym business name": ("personal connection (non-standard partner)", 1),
}


# ============================================================================
# 7. CATEGORIES TO SCRAPE
# ============================================================================
# Tier 1 = direct pet businesses. Their clients ARE dog parents by definition.
# Keep this list as is unless your market has strong regional variations.

TIER_1_CATEGORIES = [
    "veterinary clinic",
    "dog groomer",
    "mobile dog groomer",
    "doggy daycare",
    "dog boarding kennel",
    "dog trainer",
    "dog behaviourist",
    "dog walker",
    "independent pet store",
    "pet-friendly accommodation",
]

# Tier 2 = businesses whose CLIENTS plausibly spend the same money as yours on
# custom pet artwork. Be ruthless. The test: would someone willing to spend
# $2,000–$5,000 on pet artwork be a regular here? If maybe/no, drop it.
#
# Kept: picture framers, custom framing, dog-friendly cafes, premium real
# estate agents, interior designers, home stagers.
#
# Dropped (intentionally): yoga studios, pilates studios, naturopaths, massage
# therapists, acupuncturists, gift stores, jewellers, florists, hair salons,
# generic coffee shops. None of these have strong correlation with $2K+ pet
# artwork spend.

TIER_2_CATEGORIES = [
    "picture framer",
    "custom framing",
    "dog-friendly cafe",
    "boutique real estate agent",
    "interior designer",
    "home stager",
]


# ============================================================================
# 8. CATEGORY-SPECIFIC ANGLES (your voice)
# ============================================================================
# For each category, one short sentence that explains WHY their clients fit
# your ideal client. This lands in the outreach email after your introduction.
#
# Voice tips:
#   - Speak as you would to a friend over coffee
#   - Be specific about the overlap (not generic flattery)
#   - Avoid salesy or corporate language
#   - Australian English if you're in Australia (colour, realise, organise)
#   - Read aloud — does it sound like YOU?
#
# The examples below are in Ina's voice. Rewrite in yours.

CATEGORY_ANGLES: dict[str, str] = {
    "veterinary clinic": "the dog parents who trust you with their dog's health are exactly the kind of people who treat their dog like family",
    "dog groomer": "dogs coming to you regularly usually have parents who love spoiling them, which is my sweet spot",
    "mobile dog groomer": "clients who book a mobile groomer prioritise their dog's experience, which is exactly my ideal client",
    "doggy daycare": "anyone who trusts you with their dog for the day is a dog parent who's all-in",
    "dog boarding kennel": "the pet parents who plan their dog's stay carefully are the ones who'd love what I do",
    "dog trainer": "your clients invest in their dog's experience, which is the same reason they'd love what I do",
    "dog behaviourist": "your clients care deeply about their dog's wellbeing, which tells me everything about who they are",
    "dog walker": "your regulars value their dog's quality of life, which tells me everything about who they are",
    "independent pet store": "your shoppers aren't buying supermarket kibble, they're invested in their dog's life, and that's my ideal client",
    "pet-friendly accommodation": "guests who travel with their dog treat them like family, which is the heart of what I do",
    "picture framer": "your clients already value custom artwork on their walls, and many of them would love a gallery piece of their dog",
    "custom framing": "your clients already value custom artwork on their walls, and many of them would love a gallery piece of their dog",
    "dog-friendly cafe": "your regulars who bring their dogs are exactly the pet parents I work with",
    "boutique real estate agent": "a new home is a milestone moment, and a lot of your buyers mark it with family photos, dog very much included",
    "interior designer": "your clients care about what goes on their walls, and a gallery piece of their dog is often on the list",
    "home stager": "your clients care about what goes on their walls, and a gallery piece of their dog is often on the list",
}


# ============================================================================
# 9. ADVANCED (leave as-is unless you know why you're changing them)
# ============================================================================

# Years in business that count as a "milestone" — triggers the milestone hook.
MILESTONE_YEARS: set[int] = {5, 10, 15, 20, 21, 25, 30, 35, 40, 50}

CURRENT_YEAR = 2026

# Chain businesses to auto-filter (applies in addition to BLOCKLIST).
CHAIN_KEYWORDS: list[str] = [
    "greencross", "petbarn", "petstock", "woolworths", "coles", "bunnings",
    "anytime fitness", "f45", "snap fitness", "jim's",
    "just cuts", "myer", "david jones", "bakers delight",
    "the coffee club", "gloria jean", "starbucks", "mcdonald", "kfc", "domino",
]
