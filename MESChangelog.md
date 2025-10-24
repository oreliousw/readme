# 📘 Market Emotion Strategy (MES) — CHANGELOG.md
**Author:** Mr O  
**Version:** v1.6  
**Date:** 2025-10-23  
**Type:** Strategy / Visualizer (Pine Script v5)  
**Purpose:** Multi-Timeframe Market Emotion Mapping for Sentiment Learning & Reversal Recognition  

---

## 🧩 Overview
**MES v1.6** transforms the earlier single-timeframe “Market Emotion Strategy” into a complete **multi-timeframe (MTF)** emotional analysis tool.  
It reads and visualizes trader sentiment (*Fear, Capitulation, Hope, Confidence, Greed, Indecision, Neutral*) on **15 M / 1 H / 4 H** charts, providing a live emotional map of the market.

This version focuses on **clarity, clean compile, and learning utility** — no SSI yet, but with stable MTF sentiment logic and dock visualization.

---

## 🧭 Purpose
- To turn price + volume + range data into readable **emotional context**.  
- To help traders recognize how **sentiment transitions** form short-term reversals or longer-term conviction shifts.  
- To build a **training chart** for pattern recognition — not a signal-only system.  
- To visualize emotional alignment across multiple time horizons for deeper learning.

---

## ⚙️ Core Additions & Improvements
| Category | Description |
|-----------|--------------|
| **✅ Multi-Timeframe Data** | Added `request.security()` for **15 M**, **1 H**, and **4 H** candles. Each timeframe computes its own volume, range, and candle-body ratios. |
| **📊 Smoothed Ratios** | Introduced EMA-smoothed `volRatioSm` and `rngRatioSm` to reduce mood flicker on volatile pairs. |
| **🧠 Strength Weighting** | Implemented `strength = bodyRatio × volRatio` so that only emotionally strong candles trigger defined moods. |
| **🎨 Dock Panel Redesign** | New 4-row dock summary: **Chart / 15 M / 1 H / 4 H** with arrows, colors, and ratio readouts for instant multi-TF sentiment view. |
| **🔔 Emotion Alerts** | Added built-in alerts for **Extreme Greed** and **Capitulation** to catch high-emotion extremes. |
| **🧹 Clean Compile & Refactor** | Fixed scope errors (`bgcolor` / `plot` in local scope), standardized variables, and added the `bnz()` helper for NA-safe bool checks. |
| **⚙️ MTF Toggle** | Added `useMTF` input to enable or disable multi-timeframe logic for simplified testing or faster loading. |

---

## 🧠 Learning Framework
| Timeframe | Role | What You Learn |
|------------|------|----------------|
| **4 H** | Institutional Mood | Spot macro conviction, accumulation, or absorption zones. |
| **1 H** | Trend Filter | Recognize when intraday sentiment supports or conflicts with higher-timeframe trend. |
| **15 M** | Tactical Mood | Identify early emotional flips that often precede reversals. |
| **All TFs** | Sentiment Alignment | Understand how emotions cascade → *Fear → Hope → Greed* or *Greed → Fear → Capitulation*. |

---

## 📈 Visual Output
- **Background Colors:** show dominant mood on the active chart.  
- **Labels:** display mood transitions (`Fear → Hope`, `Confidence → Indecision`, etc.).  
- **Volume Columns:** color-coded to the detected emotion.  
- **Dock Panel:** compact summary of each timeframe’s sentiment and strength ratios.  
- **Alerts:** notify when extreme emotions occur.

---

## 🧰 Developer Notes
- Designed for Pine Script v5 (TradingView).  
- Strategy engine included for optional entry/exit backtesting.  
- `initial_capital = 620 USD` to match real-account testing baseline.  
- MTF calls optimized for stability; 3-EMA smoothing ensures consistent visuals.  
- SSI block intentionally omitted (reserved for v1.7 update).  

---

## 🪄 Summary
**MES v1.6** is a **clean-compiled, multi-timeframe emotion map** that teaches how price + volume behavior translates into crowd psychology.  
It helps traders *see* how emotional tone shifts between the 15 M, 1 H, and 4 H layers — perfect for learning when a “mood reversal” truly reflects a structural change versus a short-term reaction.

---

*© Mr O — “Read emotion, not noise.”*
