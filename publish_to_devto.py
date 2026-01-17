import os
import requests
import json

def publish_to_devto():
    api_key = os.getenv("DEVTO_API_KEY")
    if not api_key:
        print("❌ DEVTO_API_KEY not found in environment.")
        return

    # Load article content
    with open("../generated_article.md", "r") as f:
        content = f.read()

    # Extract frontmatter (simple split)
    parts = content.split("---")
    if len(parts) < 3:
        print("❌ Article frontmatter missing or malformed.")
        return
    
    # Extract metadata manually (for cleaner API payload)
    title = "Building an Autonomous Skill-Architecture Agent for Rapid Career Transition"
    subtitle = "How I Orchestrated Multi-Agent Systems to Automate Market Analysis and Personalized Curriculum Design"
    tags = ["ai", "python", "agents", "edtech"]
    
    # The body is everything after the second '---'
    body_markdown = "---".join(parts[2:]).strip()

    payload = {
        "article": {
            "title": title,
            "description": subtitle,
            "body_markdown": body_markdown,
            "published": True,
            "tags": tags,
            "main_image": "https://raw.githubusercontent.com/aniket-work/autonomous-skill-architecture/main/images/title-animation.gif"
        }
    }

    url = "https://dev.to/api/articles"
    headers = {
        "Content-Type": "application/json",
        "api-key": api_key
    }

    print(f"Publishing article: '{title}'...")
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 201:
        data = response.json()
        print(f"✅ Article successfully published to Dev.to!")
        print(f"🔗 URL: {data['url']}")
    else:
        print(f"❌ Failed to publish. Status: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    publish_to_devto()
