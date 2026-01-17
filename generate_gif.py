import os
import time
from PIL import Image, ImageDraw, ImageFont

def create_terminal_frame(text_lines, frame_num, total_frames):
    # Mac-style terminal dimensions
    width, height = 800, 500
    bg_color = (30, 30, 30)
    title_bar_color = (60, 60, 60)
    text_color = (255, 255, 255)
    
    image = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(image)
    
    # Draw Title Bar
    draw.rectangle([0, 0, width, 30], fill=title_bar_color)
    # Window Controls
    draw.ellipse([10, 8, 22, 20], fill=(255, 95, 87)) # Red
    draw.ellipse([30, 8, 42, 20], fill=(255, 189, 46)) # Yellow
    draw.ellipse([50, 8, 62, 20], fill=(39, 201, 63)) # Green
    
    # Content
    y_offset = 50
    line_height = 25
    for i, line in enumerate(text_lines):
        draw.text((20, y_offset + i*line_height), line, fill=text_color)
        
    return image

def generate_animation():
    print("Generating terminal + UI animation GIF...")
    frames = []
    
    # Part 1: Terminal Typing Phase
    commands = [
        "$ python main.py",
        "🚀 INITIALIZING AUTONOMOUS SKILL-ARCHITECTURE AGENT",
        "Targeting Transition to: AI Engineer",
        "------------------------------------------------------------",
        "[Market Pulse]: Top 5 required skills identified.",
        "[Gap Finder]: Found 3 critical skill gaps.",
        "[Roadmap Maker]: Learning path structured into 3 phases.",
        "================================================================================",
        "PHASE                     | SKILLS TO MASTER               | RESOURCE LINK ",
        "--------------------------------------------------------------------------------",
        "Phase 1: Foundations      | RAG                            | https://...  ",
        "Phase 2: Core Deep-Dive   | LLM Fine-tuning                | https://...  ",
        "================================================================================",
        "🎯 Mission Accomplished."
    ]
    
    current_lines = []
    for line in commands:
        current_lines.append(line)
        # Create a few frames per line for "scrolling" effect
        for _ in range(5):
            frames.append(create_terminal_frame(current_lines[-15:], len(frames), 50))

    # Part 2: Transition / UI Frames (Statistical Charts)
    # For now, we'll just repeat the last frame a bit or add a "UI LOADING" overlay
    last_frame = frames[-1].copy()
    draw = ImageDraw.Draw(last_frame)
    draw.rectangle([200, 150, 600, 350], fill=(74, 144, 226), outline=(255, 255, 255))
    draw.text((250, 230), "GRAPHICAL UI GENERATED", fill=(255, 255, 255))
    for _ in range(15):
        frames.append(last_frame)

    # Save as GIF
    os.makedirs("images", exist_ok=True)
    save_path = "images/title-animation.gif"
    
    # Quantize frames to prevent flickering
    optimized_frames = [frame.convert('P', palette=Image.ADAPTIVE) for frame in frames]
    
    optimized_frames[0].save(
        save_path,
        save_all=True,
        append_images=optimized_frames[1:],
        duration=100,
        loop=0,
        optimize=True
    )
    print(f"✅ GIF saved to {save_path}")

if __name__ == "__main__":
    generate_animation()
