#!/usr/bin/env python3
"""
Universal Notion Synchronizer for Striver A2Z DSA Roadmaps (60-Day & 75-Day)
Syncs curated DSA problem databases directly to your Notion workspace.

Security: ZERO hardcoded credentials. Reads from environment variables, CLI flags, or interactive prompt.
"""

import sys
import os
import json
import time
import argparse
import requests
import re
from pathlib import Path

NOTION_API_VERSION = "2022-06-28"
NOTION_BASE_URL = "https://api.notion.com/v1"

def clean_id(raw_id: str) -> str:
    """Extract 32-character UUID from a Notion URL or raw ID."""
    if not raw_id:
        return ""
    match = re.search(r'([0-9a-fA-F]{8})-?([0-9a-fA-F]{4})-?([0-9a-fA-F]{4})-?([0-9a-fA-F]{4})-?([0-9a-fA-F]{12})', raw_id)
    if match:
        return f"{match.group(1)}-{match.group(2)}-{match.group(3)}-{match.group(4)}-{match.group(5)}"
    
    match_32 = re.search(r'([0-9a-fA-F]{32})', raw_id)
    if match_32:
        c = match_32.group(1)
        return f"{c[:8]}-{c[8:12]}-{c[12:16]}-{c[16:20]}-{c[20:]}"
    return raw_id

def create_headers(token: str):
    return {
        "Authorization": f"Bearer {token.strip()}",
        "Notion-Version": NOTION_API_VERSION,
        "Content-Type": "application/json"
    }

def create_notion_database(token: str, parent_page_id: str, title: str) -> tuple:
    """Creates a new structured database under the given parent page."""
    url = f"{NOTION_BASE_URL}/databases"
    headers = create_headers(token)
    
    schema = {
        "parent": {
            "type": "page_id",
            "page_id": clean_id(parent_page_id)
        },
        "icon": {
            "type": "emoji",
            "emoji": "🚀"
        },
        "title": [
            {
                "type": "text",
                "text": {
                    "content": title
                }
            }
        ],
        "properties": {
            "Question Name": {
                "title": {}
            },
            "Day": {
                "select": {}
            },
            "Week": {
                "select": {}
            },
            "Phase": {
                "select": {}
            },
            "Topic": {
                "select": {}
            },
            "Pattern": {
                "select": {}
            },
            "Difficulty": {
                "select": {
                    "options": [
                        {"name": "Easy", "color": "green"},
                        {"name": "Medium", "color": "yellow"},
                        {"name": "Hard", "color": "red"}
                    ]
                }
            },
            "Status": {
                "select": {
                    "options": [
                        {"name": "Not Started", "color": "gray"},
                        {"name": "In Progress", "color": "blue"},
                        {"name": "Done", "color": "green"},
                        {"name": "Needs Revision", "color": "orange"}
                    ]
                }
            },
            "Confidence": {
                "select": {
                    "options": [
                        {"name": "⭐ Needs Practice", "color": "red"},
                        {"name": "⭐⭐ Confident", "color": "yellow"},
                        {"name": "⭐⭐⭐ Mastered", "color": "green"}
                    ]
                }
            },
            "Practice Link": {
                "url": {}
            },
            "Striver Article": {
                "url": {}
            },
            "Striver Video": {
                "url": {}
            },
            "Notes & Edge Cases": {
                "rich_text": {}
            },
            "Review Date": {
                "date": {}
            }
        }
    }
    
    response = requests.post(url, headers=headers, json=schema)
    if response.status_code != 200:
        print(f"❌ Error creating database in Notion: {response.status_code}")
        print(response.text)
        sys.exit(1)
        
    res_data = response.json()
    db_id = res_data["id"]
    db_url = res_data.get("url", f"https://www.notion.so/{db_id.replace('-', '')}")
    print(f"✅ Successfully created Notion Database: '{title}'")
    print(f"🔗 Database URL: {db_url}")
    return db_id, db_url

def insert_row(token: str, db_id: str, item: dict) -> bool:
    url = f"{NOTION_BASE_URL}/pages"
    headers = create_headers(token)
    
    properties = {
        "Question Name": {
            "title": [
                {
                    "text": {
                        "content": item["name"]
                    }
                }
            ]
        },
        "Day": {
            "select": {
                "name": f"Day {item['day']:02d}"
            }
        },
        "Week": {
            "select": {
                "name": f"Week {item['week']:02d}"
            }
        },
        "Phase": {
            "select": {
                "name": str(item["phase"]).replace(",", " &").strip()
            }
        },
        "Topic": {
            "select": {
                "name": str(item["topic"]).replace(",", " &").strip()
            }
        },
        "Pattern": {
            "select": {
                "name": str(item.get("pattern", "Core")).replace(",", " &").strip()
            }
        },
        "Difficulty": {
            "select": {
                "name": item.get("difficulty", "Medium")
            }
        },
        "Status": {
            "select": {
                "name": "Not Started"
            }
        },
        "Confidence": {
            "select": {
                "name": "⭐⭐ Confident"
            }
        },
        "Notes & Edge Cases": {
            "rich_text": [
                {
                    "text": {
                        "content": item.get("notes", "")[:2000]
                    }
                }
            ]
        }
    }
    
    if item.get("practice_url"):
        properties["Practice Link"] = {"url": item["practice_url"]}
    if item.get("article_url"):
        properties["Striver Article"] = {"url": item["article_url"]}
    if item.get("video_url"):
        properties["Striver Video"] = {"url": item["video_url"]}

    payload = {
        "parent": {
            "database_id": clean_id(db_id)
        },
        "properties": properties
    }
    
    retries = 3
    while retries > 0:
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=20)
            if response.status_code == 200:
                return True
            elif response.status_code == 429:
                retry_after = float(response.headers.get("Retry-After", "1.0"))
                time.sleep(retry_after)
                retries -= 1
            else:
                print(f"Failed '{item['name']}': {response.status_code} - {response.text}")
                return False
        except Exception as e:
            time.sleep(1.0)
            retries -= 1
    return False

def parse_args():
    parser = argparse.ArgumentParser(description="Sync Curated Striver A2Z DSA Plan to Notion")
    parser.add_argument("--plan", choices=["60", "75"], default="75", help="Choose plan: '60' or '75' (default: 75)")
    parser.add_argument("--token", type=str, help="Notion Internal Integration Token")
    parser.add_argument("--page-id", type=str, help="Parent Notion Page URL or ID")
    parser.add_argument("--database-id", type=str, help="Existing Notion Database ID (if updating existing)")
    return parser.parse_args()

def main():
    args = parse_args()
    
    # Locate data files
    base_dir = Path(__file__).resolve().parent.parent
    if args.plan == "60":
        json_file = base_dir / "dsa-60-day" / "dsa_60day_database.json"
        default_title = "Striver A2Z 60-Day Sprint DSA Planner"
    else:
        json_file = base_dir / "dsa-75-day" / "dsa_75day_database.json"
        default_title = "Striver A2Z 75-Day Pro DSA Master Plan"

    if not json_file.exists():
        print(f"❌ Could not find database file: {json_file}")
        sys.exit(1)

    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    print("=" * 65)
    print(f"🚀 Striver A2Z Notion Synchronizer ({args.plan}-Day Curriculum)")
    print(f"📦 Total Questions to Upload: {len(data)}")
    print("=" * 65)

    # Resolve Token
    token = args.token or os.environ.get("NOTION_TOKEN")
    if not token:
        print("\n🔑 Notion API Token is required:")
        print("1. Go to https://www.notion.so/my-integrations")
        print("2. Create a new integration and copy the 'Internal Integration Secret'.")
        token = input("👉 Enter your Notion Token: ").strip()

    if not token:
        print("❌ Token cannot be empty. Exiting.")
        sys.exit(1)

    # Resolve Database / Page ID
    db_id = args.database_id
    db_url = None
    if not db_id:
        page_id = args.page_id or os.environ.get("NOTION_PAGE_ID")
        if not page_id:
            print("\n📄 Parent Notion Page ID or URL is required:")
            print("1. Open the page in Notion where you want this database.")
            print("2. Click '...' (top-right) -> 'Connect to' -> Select your integration.")
            print("3. Copy the URL of your Notion page.")
            page_id = input("👉 Enter Notion Page URL: ").strip()

        if not page_id:
            print("❌ Page URL cannot be empty. Exiting.")
            sys.exit(1)

        db_id, db_url = create_notion_database(token, page_id, default_title)

    # Upload rows
    print(f"\n⏳ Uploading {len(data)} problems to Notion (at ~3 req/sec)...")
    success = 0
    total = len(data)
    for idx, item in enumerate(data, start=1):
        ok = insert_row(token, db_id, item)
        if ok:
            success += 1
            pct = int(idx / total * 100)
            print(f"[{idx:03d}/{total:03d} | {pct:02d}%] Day {item['day']:02d} - {item['name']}")
        else:
            print(f"[{idx:03d}/{total:03d}] ⚠️ Failed to insert: {item['name']}")
        time.sleep(0.35)

    print("\n" + "=" * 65)
    print(f"🎉 Synchronization Complete! {success}/{total} questions uploaded.")
    if db_url:
        print(f"🔗 View your new Notion Database: {db_url}")
    print("=" * 65)

if __name__ == "__main__":
    main()
