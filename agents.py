import time

class Agent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal

    def report(self, message):
        print(f"[{self.name} - {self.role}]: {message}")
        time.sleep(0.5)

class MarketAnalyst(Agent):
    def __init__(self):
        super().__init__("Market Pulse", "Market Research Analyst", "Identify trending skills for a specific target role.")

    def analyze(self, target_role):
        self.report(f"Analyzing global market trends for '{target_role}'...")
        # Mocking market data
        trends = {
            "AI Engineer": ["PyTorch", "TensorFlow", "RAG", "LLM Fine-tuning", "System Design"],
            "Cloud Architect": ["AWS", "Azure", "Terraform", "Kubernetes", "Microservices Design"],
            "Data Scientist": ["SQL", "Python", "Statistical Modeling", "PowerBI", "Machine Learning"]
        }
        result = trends.get(target_role, ["Python", "SQL", "Cloud Basics", "System Design", "Agile"])
        self.report(f"Top 5 required skills for '{target_role}' identified.")
        return result

class SkillGapAnalyzer(Agent):
    def __init__(self):
        super().__init__("Gap Finder", "Technical Skill Evaluator", "Compare current user skills against market requirements.")

    def calculate_gaps(self, current_skills, required_skills):
        self.report("Cross-referencing user profile with market requirements...")
        gaps = []
        for skill in required_skills:
            if skill not in current_skills:
                gaps.append(skill)
        
        # Simulating proficiency score (0-100)
        proficiency = {}
        for skill in required_skills:
            if skill in current_skills:
                proficiency[skill] = 85
            else:
                proficiency[skill] = 10
        
        self.report(f"Found {len(gaps)} critical skill gaps.")
        return gaps, proficiency

class CurriculumArchitect(Agent):
    def __init__(self):
        super().__init__("Roadmap Maker", "Lead Learning Path Designer", "Design a strategic learning roadmap based on identified gaps.")

    def design_roadmap(self, gaps):
        self.report("Architecting a personalized learning curriculum...")
        roadmap = {
            "Phase 1: Foundations": gaps[:2] if len(gaps) >= 2 else gaps,
            "Phase 2: Core Deep-Dive": gaps[2:4] if len(gaps) >= 4 else gaps[2:],
            "Phase 3: Advanced Projects": gaps[4:] if len(gaps) >= 4 else []
        }
        self.report("Learning path successfully structured into 3 technical phases.")
        return roadmap

class ResourceScout(Agent):
    def __init__(self):
        super().__init__("Source Finder", "Learning Resource Specialist", "Identify high-quality resources for the curriculum.")

    def fetch_resources(self, roadmap):
        self.report("Searching for top-tier learning materials (Coursera, Udemy, GitHub)...")
        resources = {}
        for phase, skills in roadmap.items():
            resources[phase] = {skill: f"https://learning-nexus.io/courses/{skill.lower().replace(' ', '-')}" for skill in skills}
        self.report("Strategic resources mapped to all curriculum phases.")
        return resources
