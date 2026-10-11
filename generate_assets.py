import os
from PIL import Image, ImageDraw, ImageFont
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')
IMG_DIR = os.path.join(STATIC_DIR, 'images')
DOC_DIR = os.path.join(STATIC_DIR, 'documents')

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(DOC_DIR, exist_ok=True)

def create_image(filename, width, height, title, subtitle, tag, bg_color, accent_color):
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Draw modern grid / background lines
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(bg_color[0]+8, bg_color[1]+8, bg_color[2]+10), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(bg_color[0]+8, bg_color[1]+8, bg_color[2]+10), width=1)

    # Accent decorative bar
    draw.rectangle([(60, 60), (width - 60, 68)], fill=accent_color)
    draw.rectangle([(60, height - 70), (width - 60, height - 66)], fill=(bg_color[0]+25, bg_color[1]+25, bg_color[2]+30))

    # Center box
    box_padding = 40
    box_rect = [60, 100, width - 60, height - 90]
    draw.rounded_rectangle(box_rect, radius=20, fill=(bg_color[0]+12, bg_color[1]+14, bg_color[2]+18), outline=accent_color, width=2)

    # Badge pill
    badge_rect = [100, 140, 360, 185]
    draw.rounded_rectangle(badge_rect, radius=22, fill=accent_color)
    
    # Try default or standard fonts
    try:
        font_large = ImageFont.truetype("arial.ttf", 36)
        font_mid = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 18)
        font_badge = ImageFont.truetype("arialbd.ttf", 18)
    except:
        font_large = font_mid = font_small = font_badge = ImageFont.load_default()

    # Draw text
    draw.text((120, 150), tag.upper(), fill=(255, 255, 255), font=font_badge)
    draw.text((100, 220), title, fill=(255, 255, 255), font=font_large)
    draw.text((100, 280), subtitle, fill=(180, 195, 215), font=font_mid)
    
    notice_text = "PLACEHOLDER ASSET - REPLACE WITH YOUR IMAGE AT: static/images/" + filename
    draw.text((100, height - 140), notice_text, fill=(140, 160, 185), font=font_small)

    filepath = os.path.join(IMG_DIR, filename)
    img.save(filepath, "JPEG", quality=92)
    print(f"Generated: {filepath}")

def create_profile_placeholder():
    # Profile placeholder specifically designed as a non-face professional monogram card
    width, height = 800, 960
    bg_color = (15, 23, 42) # Slate 900
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Subtle grid
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=(25, 35, 58), width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=(25, 35, 58), width=1)

    # Outer decorative ring
    center_x, center_y = width // 2, height // 2 - 60
    radius = 180
    draw.ellipse([(center_x - radius, center_y - radius), (center_x + radius, center_y + radius)], fill=(30, 41, 59), outline=(37, 99, 235), width=6)
    
    # Inner ring
    inner_rad = 140
    draw.ellipse([(center_x - inner_rad, center_y - inner_rad), (center_x + inner_rad, center_y + inner_rad)], fill=(37, 99, 235))

    try:
        font_ps = ImageFont.truetype("arialbd.ttf", 96)
        font_name = ImageFont.truetype("arialbd.ttf", 42)
        font_sub = ImageFont.truetype("arial.ttf", 24)
        font_note = ImageFont.truetype("arial.ttf", 18)
    except:
        font_ps = font_name = font_sub = font_note = ImageFont.load_default()

    draw.text((center_x - 68, center_y - 54), "PS", fill=(255, 255, 255), font=font_ps)
    draw.text((center_x - 145, height - 260), "PUJA SHARMA", fill=(255, 255, 255), font=font_name)
    draw.text((center_x - 170, height - 200), "SOFTWARE ENGINEER | R&D", fill=(147, 197, 253), font=font_sub)
    draw.text((center_x - 220, height - 110), "Place your photograph at: static/images/profile.jpg", fill=(148, 163, 184), font=font_note)

    filepath = os.path.join(IMG_DIR, "profile.jpg")
    img.save(filepath, "JPEG", quality=92)
    print(f"Generated: {filepath}")

def create_resume_pdf():
    pdf_path = os.path.join(DOC_DIR, "resume.pdf")
    c = canvas.Canvas(pdf_path, pagesize=letter)
    width, height = letter

    # Header
    c.setFont("Helvetica-Bold", 24)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, height - 60, "PUJA SHARMA")

    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#2563eb"))
    c.drawString(50, height - 80, "Software Engineer | R&D | AI/ML | RAG | QA Automation")

    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor("#475569"))
    c.drawString(50, height - 100, "Tamil Nadu, India | pujasharmarps@gmail.com | linkedin.com/in/puja-sharma-a7178a242")

    # Divider
    c.setStrokeColor(colors.HexColor("#cbd5e1"))
    c.setLineWidth(1)
    c.line(50, height - 115, width - 50, height - 115)

    y = height - 140

    # Summary
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "PROFESSIONAL PROFILE")
    y -= 18
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor("#334155"))
    c.drawString(50, y, "Software Engineer building practical AI systems with a strong foundation in software quality and application engineering.")
    y -= 14
    c.drawString(50, y, "Experienced across Python development, RAG architectures, document OCR pipelines, and QA automation.")
    y -= 30

    # Experience
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "EXPERIENCE")
    y -= 20

    # Job 1
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "Developer - R&D Team | Ecrio Inc.")
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor("#64748b"))
    c.drawRightString(width - 50, y, "Jul 2025 - Present")
    y -= 16
    c.setFont("Helvetica", 9.5)
    c.setFillColor(colors.HexColor("#334155"))
    responsibilities_1 = [
        "- Develop Retrieval-Augmented Generation (RAG) solutions for industrial equipment and technical Q&A.",
        "- Build AI/ML solutions in Python and construct document parsing / OCR pipelines.",
        "- Research and experiment with Qualcomm SDK technologies for on-device edge AI.",
        "- Engineer anomaly detection models and contribute to real-world industrial deployments."
    ]
    for resp in responsibilities_1:
        c.drawString(60, y, resp)
        y -= 14

    y -= 10
    # Job 2
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "QA Intern | Ecrio Inc.")
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor("#64748b"))
    c.drawRightString(width - 50, y, "Sep 2024 - Jul 2025")
    y -= 16
    c.setFont("Helvetica", 9.5)
    c.setFillColor(colors.HexColor("#334155"))
    responsibilities_2 = [
        "- Executed manual and UI automation testing using Appium and Python across applications.",
        "- Conducted thorough REST API testing and endpoint response verification.",
        "- Performed structured test-case runs and managed end-to-end defect tracking lifecycle.",
        "- Collaborated closely with developer teams to reproduce and triage critical issues."
    ]
    for resp in responsibilities_2:
        c.drawString(60, y, resp)
        y -= 14

    y -= 20
    # Education
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "EDUCATION & HONORS")
    y -= 20
    c.setFont("Helvetica-Bold", 10.5)
    c.drawString(50, y, "M.Sc. Computer Science (Data Science) - Mother Teresa Women's University")
    c.setFont("Helvetica", 10)
    c.setFillColor(colors.HexColor("#64748b"))
    c.drawRightString(width - 50, y, "Aug 2020 - May 2025")
    y -= 16
    c.setFont("Helvetica-Bold", 9.5)
    c.setFillColor(colors.HexColor("#d97706"))
    c.drawString(60, y, "Gold Medalist & Top Performer of the Batch | CGPA: 8.6 / 10")
    y -= 30

    # Skills
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "TECHNICAL SKILLS")
    y -= 18
    skills = [
        ("Programming & Scripting:", "Python, SQL"),
        ("Applied AI & ML:", "RAG Systems, Vector Databases (ChromaDB), Machine Learning, Anomaly Detection"),
        ("Document Intelligence:", "OCR, PDF Processing, Document Parsing"),
        ("Testing & Quality:", "Manual Testing, Appium, Python Automation, API Testing, Regression Testing"),
        ("Edge AI / R&D:", "Qualcomm SDK, AI/ML on Qualcomm platforms"),
        ("Tools & Platforms:", "Git, GitHub, Postman, Microsoft Office Suite")
    ]
    for category, details in skills:
        c.setFont("Helvetica-Bold", 9.5)
        c.setFillColor(colors.HexColor("#0f172a"))
        c.drawString(60, y, category)
        c.setFont("Helvetica", 9.5)
        c.setFillColor(colors.HexColor("#334155"))
        c.drawString(210, y, details)
        y -= 15

    y -= 15
    # Certifications
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.HexColor("#0f172a"))
    c.drawString(50, y, "CERTIFICATIONS")
    y -= 18
    c.setFont("Helvetica", 9.5)
    c.setFillColor(colors.HexColor("#334155"))
    c.drawString(60, y, "MongoDB (ICT) | Artificial Intelligence (NoviTech) | MERN Stack (Ecrio Inc.)")

    c.showPage()
    c.save()
    print(f"Generated: {pdf_path}")

if __name__ == "__main__":
    create_profile_placeholder()
    create_image("project-rag.jpg", 1000, 650, "Industrial Q&A RAG System", "Semantic Retrieval & Context-Grounded LLM", "AI / RAG / Industrial", (15, 23, 42), (37, 99, 235))
    create_image("project-ocr.jpg", 1000, 650, "PDF Parsing & OCR Pipeline", "Automated Rasterization & Text Extraction", "AI / Document Intelligence", (17, 24, 39), (14, 165, 233))
    create_image("project-automation.jpg", 1000, 650, "Mobile Application Automation", "Appium, Python & End-to-End API Test Suites", "QA Automation", (24, 24, 27), (16, 185, 129))
    create_image("project-qualcomm.jpg", 1000, 650, "Qualcomm AI / SDK Exploration", "Edge AI Constraints & Hardware-Aware Runtime", "Edge AI / R&D", (23, 23, 23), (168, 85, 247))
    create_resume_pdf()
