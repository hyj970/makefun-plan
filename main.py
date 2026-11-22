"""make.fun bounty entry: the-plan-make-fun-will-carry-20261122-2138.

Writes a 30-day plan for an AI agent to turn $100 into the most money
it can, as plain text in /output/entry.txt. Deterministic: stdlib only,
no network, no randomness, no timestamps.
"""

import os

PLAN = (
    "Day 1: list '10 AI product photos, $29, 24h' on Fiverr, email 100 "
    "Shopify stores off BuiltWith's free list. Days 2-30: fill each "
    "order, deliver in 24h, ask for reviews to climb Fiverr search, "
    "reinvest into outreach. Target: 20 orders = $580. "
    "Spend $0 before the first sale."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
