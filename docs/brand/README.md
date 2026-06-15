# Brand assets

- **`smt_logo.png`** — the SMT logo (480×480; navy / gold / teal; whale-fluke + candlestick
  breakout + circuit motif). Use for the BUIDL logo field, README header, dashboard, social avatar.

## Updating the logo (swap in the final version)
The committed `smt_logo.png` is a **working placeholder** generated from `/tmp/smt_logo.svg`. To
replace it with your final design:

- **GitHub web UI:** open `docs/brand/` → **Add file → Upload files** → drag your PNG **named
  `smt_logo.png`** → Commit (it overwrites). Keep it ≤2 MB, 480×480 recommended.
- **Locally:** save your PNG over `docs/brand/smt_logo.png` → `git add docs/brand/smt_logo.png` →
  commit → push.

Everything that references the logo (`README.md` header, etc.) points at this path, so a swap
updates them all at once.
