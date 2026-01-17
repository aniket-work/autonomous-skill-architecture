import sys
from agents import MarketAnalyst, SkillGapAnalyzer, CurriculumArchitect, ResourceScout
from viz import generate_skill_radar_chart, generate_market_bar_chart
import time

def main():
    print("="*60)
    print("🚀 INITIALIZING AUTONOMOUS SKILL-ARCHITECTURE AGENT")
    print("="*60)
    time.sleep(1)

    target_role = "AI Engineer"
    current_skills = ["Python", "SQL", "Git", "FastAPI"]

    print(f"Targeting Transition to: {target_role}")
    print(f"Current Skill Set: {', '.join(current_skills)}")
    print("-"*60)

    # 1. Market Analysis
    analyst = MarketAnalyst()
    required_skills = analyst.analyze(target_role)

    # 2. Skill Gap Analysis
    gap_finder = SkillGapAnalyzer()
    gaps, proficiency = gap_finder.calculate_gaps(current_skills, required_skills)

    # 3. Curriculum Design
    architect = CurriculumArchitect()
    roadmap = architect.design_roadmap(gaps)

    # 4. Resource Scouting
    scout = ResourceScout()
    resources = scout.fetch_resources(roadmap)

    # 5. Visualization
    print("\n📈 Generating data visualizations...")
    generate_market_bar_chart("images/market_demand.png")
    generate_skill_radar_chart(proficiency, "images/skill_radar.png")
    print("✅ Visualizations saved to 'images/' directory.")

    # 6. Final Report (ASCII Table)
    print("\n" + "="*80)
    print(f"{'PHASE':<25} | {'SKILLS TO MASTER':<30} | {'RESOURCE LINK'}")
    print("-"*80)
    for phase, skills in roadmap.items():
        for skill in skills:
            link = resources[phase].get(skill, "N/A")
            print(f"{phase:<25} | {skill:<30} | {link}")
    print("="*80)
    print("\n🎯 Mission Accomplished. Career Roadmap Generated.")

if __name__ == "__main__":
    main()
