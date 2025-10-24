# 📘 Market Emotion Strategy (MES) — CHANGELOG.md
**Author:** Mr O  
**Version:** v1.6  
**Date:** 2025-10-23  
**Type:** Strategy Script (Pine Script v5)  
**Purpose:** Multi-Timeframe Market Emotion Mapping for Sentiment Learning and Reversal Recognition  

---

## 🧩 Overview
**MES v1.6** expands on the original single-timeframe Market Emotion Strategy by introducing a full **multi-timeframe (MTF) sentiment system**.  
It tracks market “moods” — *Fear, Capitulation, Hope, Confidence, Greed, Indecision, and Neutral* — across **15 M, 1 H, 4 H** timeframes and aligns them into a single, readable dashboard.

The goal is to help traders visually **understand emotional flow** across market layers and learn how short-term sentiment transitions forecast longer-term conviction.

---

## 🧭 Purpose
- To translate raw volume, range, and candle-body behavior into *emotional context*.  
- To show how sentiment evolves across **scales of participation**: retail (15 M), institutional (4 H), and structural trend (1 H).  
- To create a *training tool* for developing emotional pattern recognition — not just an entry system.  
- To support studying when emotions align (trend continuation) or diverge (pullbacks or reversals).

---

## ⚙️ Core Additions in v1.6
| Category | Description |
|-----------|--------------|
| **✅ Multi-Timeframe Data** | Added `request.security()` calls for **15 M, 1 H, 4 H** data streams. Each computes independent volume, range, and body ratios. |
| **📊 Smoothed Ratios** | Implemented EMA smoothing for `volRatio` and `rngRatio` → reduces flickering between moods. |
| **🧠 Strength Filter** | Added candle-body × volume weighting (`strength`) so weak emotions are filtered out. |
| **🎨 Dock Panel Redesign** | Dock now displays separate sentiment rows for each timeframe (native, 15 M, 1 H, 4 H). Uses color + arrow cues for instant emotional direction. |
| **🧮 Sentiment Sync Index (SSI)** | New optional indicator scoring alignment from **−3 (bearish)** → **+3 (bullish)**; displayed numerically and plotted for study. |
| **🔔 Alerts** | Added alert conditions for *Extreme Greed* and *Capitulation* to notify high-emotion events. |
| **🧹 Clean Compile** | Removed local-scope plot/bgcolor issues, unified variable naming, and improved NA-safety with helper function `bnz()`. |

---

## 🧠 Learning Framework
| Timeframe | Role | What You Learn |
|------------|------|----------------|
| **4 H** | Institutional Mood | Recognize macro conviction and absorption patterns. |
| **1 H** | Trend Filter | Train on emotional synchronization vs. divergence. |
| **15 M** | Tactical Mood | Detect first sentiment shifts before broader confirmation. |
| **All TFs Combined** | Emotional Alignment | Understand how emotions cascade: *Fear → Hope → Greed* (bull cycle) or *Greed → Fear → Capitulation* (bear cycle). |

---

## 📈 Reading the Output
- **Background Colors:** visualize the dominant emotion on your active chart.  
- **Labels:** mark mood transitions (`Fear → Hope`, `Confidence → Indecision`, etc.).  
- **Volume Columns:** color-coded to the active emotion.  
- **Dock Panel:** compact sentiment summary across all TFs for instant alignment check.  
- **Sentiment Sync Index (SSI):** numerical alignment gauge (−3 to +3).

---

## 🧰 Developer Notes
- Compatible with Pine Script v5+ (TradingView).  
- Strategy entries remain optional; main focus = sentiment visualization.  
- Code structured with global-scope visuals for performance stability.  
- Initial capital set to **620 USD** to match real trading test environment.  
- `useMTF` toggle allows running in single-TF mode for simplified study.

---

## 🪄 Summary
**MES v1.6** shifts the script from a simple emotional color map into a **learning instrument** —  
a real-time teaching chart for how *market psychology evolves* across layers of participation.  
It’s ideal for anyone studying how short-term emotion flips lead to, or fake out, major trend reversals.

---

*© Mr O — “Read emotion, not noise.”*
