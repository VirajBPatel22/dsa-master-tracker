# 🚀 Striver A2Z DSA Master Trackers (60-Day Sprint & 75-Day Pro Edition)

> **The ultimate interview-ready DSA curriculum based on the Striver A2Z Sheet.**  
> Curated to eliminate repetitive syntax drills (star patterns & elementary math loops) and focus 100% on high-yield, interview-defining algorithmic patterns asked at FAANG, Tier-1 product startups, and top tech companies.

---

## 📂 Repository Structure

```
.
├── 📁 dsa-60-day/
│   ├── README.md                     # Phase-by-phase roadmap & syllabus for the 60-day sprint
│   ├── notion_dsa_60day_planner.csv  # 1-Click CSV for instant Notion import (260 questions)
│   └── dsa_60day_database.json       # JSON dataset of the 60-day plan
│
├── 📁 dsa-75-day/
│   ├── README.md                     # Comprehensive roadmap & study schedule (315 questions)
│   ├── notion_dsa_75day_planner.csv  # 1-Click CSV for instant Notion import (315 questions)
│   └── dsa_75day_database.json       # JSON dataset of the 75-day plan
│
├── 📁 scripts/
│   ├── sync_to_notion.py             # Secure, automated Notion API sync script (zero hardcoded keys)
│   ├── build_database.py             # Dataset generation and topic allocator script
│   └── requirements.txt              # Python dependencies (`requests`)
│
├── .env.example                      # Template for Notion API credentials
├── .gitignore                        # Standard ignore rules (prevents committing secrets/cache)
└── README.md                         # Main repository guide
```

---

## ⚖️ Which Plan Should You Choose?

| Feature | ⚡ 60-Day Sprint | 🏆 75-Day Pro Master Plan |
| :--- | :--- | :--- |
| **Total Problems** | **260 Questions** | **315 Questions** |
| **Pacing** | ~4.3 Problems / Day | ~4.2 Problems / Day |
| **Best For** | Short deadlines (placements in 2–3 months) | Complete mastery (6–12 months timeline) |
| **Trees & BST** | 35 Problems | **41 Problems** (Adds Burning Tree, Children Sum, Max Sum BST) |
| **Graph Theory** | 35 Problems | **40 Problems** (Adds Number of Islands, Grid Dijkstra, Word Ladder II) |
| **Dynamic Programming** | 45 Problems | **50 Problems** (Adds Maximal Rectangle, Triangular DP, Stock IV) |
| **Omitted Content** | Star patterns & trivial syntax | Star patterns & trivial syntax |

---

## 🛠️ How to Import into Notion

You and your friends can set this up in Notion in **two ways**:

### 🎯 Option A: Instant 1-Click CSV Import (Recommended — No Code Needed!)

This is the fastest method (takes **10 seconds**):

1. **Open Notion** and create a new blank page named `DSA Master Tracker`.
2. In the top right corner of Notion, click the **`...`** (three dots) menu and select **`Import`**.
3. Choose **CSV** from the list of import options.
4. Select either:
   * [`dsa-60-day/notion_dsa_60day_planner.csv`](dsa-60-day/notion_dsa_60day_planner.csv) (for the 60-day sprint)
   * [`dsa-75-day/notion_dsa_75day_planner.csv`](dsa-75-day/notion_dsa_75day_planner.csv) (for the 75-day master plan)
5. Notion will instantly create a beautiful table database with all columns:
   * **Question Name** (Title)
   * **Day** & **Week** tags
   * **Phase**, **Topic**, and **Pattern**
   * **Difficulty** (Easy, Medium, Hard)
   * **Status** & **Confidence** dropdowns
   * **Practice Link**, **Striver Article**, and **YouTube Video** URLs
   * **Notes & Edge Cases**
6. **Set up Views:**
   * Click **Sort** ➔ Sort by `Day` (Ascending).
   * Optional: Click **Group** ➔ Group by `Phase` or `Day` for clean toggles.

---

### 🤖 Option B: Automated Python API Sync

If you want the script to automatically build the Notion database via Notion's official API:

1. **Install dependencies:**
   ```bash
   pip install -r scripts/requirements.txt
   ```

2. **Get your Notion Integration Token:**
   * Go to [https://www.notion.so/my-integrations](https://www.notion.so/my-integrations) and click **New integration**.
   * Copy the **Internal Integration Secret** (starts with `secret_...` or `ntn_...`).

3. **Connect your Notion Page:**
   * Open the Notion page where you want the planner.
   * Click the **`...`** (top right) ➔ **Connect to** ➔ Select your integration name.
   * Copy the URL of your Notion page.

4. **Run the Synchronizer:**
   ```bash
   # Sync the 75-Day Plan (Default):
   python3 scripts/sync_to_notion.py --plan 75

   # Or sync the 60-Day Sprint:
   python3 scripts/sync_to_notion.py --plan 60
   ```
   *The script will safely prompt you for your token and page URL, or you can configure them in a `.env` file (see `.env.example`).*

---

## 🧠 Best Practices for Maximum Retention

### 1. Cumulative Progress (Avoid the "Reset Trap")
A frequent mistake in algorithmic prep is resetting to Day 01 after every interruption. 
- When resuming from any break, never restart from the beginning.
- Review your Notion notes from the previous 2 days, then immediately continue from your next scheduled Day.

### 2. The Maintenance Routine
- During heavy workload periods or academic commitments, keep pattern recognition fresh with **1 review problem daily** (15–20 minutes) rather than pausing completely.

### 3. Spaced Repetition (The 1-3-7 Principle)
- Mark challenging problems with **"Needs Revision"** in your Notion tracker. Re-solve them on Day 3 and Day 7 to commit the underlying patterns to long-term memory.

---

## 🤝 Contributing & Community
Feel free to star ⭐ this repository, fork it, and share it with study groups or peers preparing for technical placements!
