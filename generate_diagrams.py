import base64
import requests
import os

def generate_diagram(name, code):
    print(f"Generating diagram: {name}...")
    encoded = base64.b64encode(code.encode()).decode()
    url = f"https://mermaid.ink/img/{encoded}"
    try:
        response = requests.get(url, timeout=30)
        if response.status_code == 200:
            os.makedirs("images", exist_ok=True)
            path = f"images/{name}.png"
            with open(path, 'wb') as f:
                f.write(response.content)
            print(f"✅ Successfully saved to {path}")
            return True
        else:
            print(f"❌ Failed to generate diagram {name}. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error generating diagram {name}: {str(e)}")
        return False

diagrams = {
    "title_diagram": """
graph TD
    Title["Autonomous Skill-Architecture Agent"]
    Sub["AI-Powered Career Transition & Upskilling"]
    Title --- Sub
    style Title fill:#2C3E50,stroke:#34495E,stroke-width:2px,color:#fff
    style Sub fill:#ECF0F1,stroke:#BDC317,stroke-width:1px,color:#2C3E50
    """,
    "architecture_diagram": """
graph LR
    User([User Profile]) --> SA[Skill Analyzer]
    MD[(Market Data)] --> MA[Market Analyst]
    MA --> SA
    SA --> CA[Curriculum Architect]
    CA --> RS[Resource Scout]
    RS --> Result[Personalized Roadmap]
    
    style SA fill:#3498DB,color:#fff
    style MA fill:#E74C3C,color:#fff
    style CA fill:#2ECC71,color:#fff
    style RS fill:#F1C40F,color:#333
    """,
    "sequence_diagram": """
sequenceDiagram
    participant U as User
    participant MA as Market Analyst
    participant SA as Skill Analyzer
    participant CA as Curriculum Architect
    participant RS as Resource Scout

    U->>MA: Request Career Path
    MA->>MA: Analyze Demand
    MA->>SA: Trend Data
    SA->>SA: Identify Gaps
    SA->>CA: Gap Report
    CA->>CA: Structure Roadmap
    CA->>RS: Curriculum
    RS->>RS: Curate Sources
    RS->>U: Final Roadmap & Resources
    """,
    "flow_diagram": """
flowchart TD
    Start([Start Mission]) --> Analyze[Analyze Job Market]
    Analyze --> Identify[Identify Role Skills]
    Identify --> Compare{Compare to User}
    Compare --> Found[Gap Found?]
    Found -- Yes --> Design[Design Roadmap]
    Design --> Scout[Scout Resources]
    Scout --> End([Deliver Plan])
    Found -- No --> End
    """
}

def main():
    success_count = 0
    for name, code in diagrams.items():
        if generate_diagram(name, code):
            success_count += 1
    
    print(f"\nTotal diagrams generated: {success_count}/{len(diagrams)}")
    if success_count < len(diagrams):
        print("⚠️ Warning: Some diagrams failed to generate!")

if __name__ == "__main__":
    main()
