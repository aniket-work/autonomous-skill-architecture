import matplotlib.pyplot as plt
import numpy as np
import os

def generate_skill_radar_chart(proficiency_data, output_path):
    labels = list(proficiency_data.keys())
    values = list(proficiency_data.values())
    
    # Number of variables
    num_vars = len(labels)

    # Compute angle of each axis
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # The plot is a circle, so we need to "complete the loop"
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='#4A90E2', alpha=0.3)
    ax.plot(angles, values, color='#4A90E2', linewidth=2)

    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=10, fontweight='bold')

    plt.title("Personalized Skill Gap Analysis", size=15, pad=20, fontweight='bold', color='#2C3E50')
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_market_bar_chart(output_path):
    skills = ['PyTorch', 'LLMs', 'System Design', 'Cloud', 'RAG']
    demand = [95, 88, 75, 90, 82]
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(skills, demand, color=['#3498DB', '#E74C3C', '#2ECC71', '#F1C40F', '#9B59B6'])
    
    plt.xlabel('Technical Domain', fontweight='bold')
    plt.ylabel('Industry Demand (%)', fontweight='bold')
    plt.title('2026 Skill Demand Projection: AI Engineering', fontsize=14, fontweight='bold', color='#34495E')
    
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path, dpi=300)
    plt.close()
