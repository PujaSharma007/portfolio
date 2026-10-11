import os
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'puja-sharma-portfolio-secret-key-2026')

# Helper to automatically resolve image extensions (.jpeg, .jpg, .png)
def resolve_image_path(base_name, default_ext="jpg"):
    images_dir = os.path.join(app.root_path, 'static', 'images')
    for ext in ['.jpeg', '.jpg', '.png', '.webp']:
        if os.path.exists(os.path.join(images_dir, f"{base_name}{ext}")):
            return f"images/{base_name}{ext}"
    return f"images/{base_name}.{default_ext}"

# Structured portfolio data for easy maintenance and clean presentation
PORTFOLIO_DATA = {
    "personal": {
        "name": "Puja Sharma",
        "title": "Software Engineer · R&D · AI/ML · RAG · QA Automation",
        "location": "Tamil Nadu, India",
        "email": "pujasharmarps@gmail.com",
        "linkedin": "https://linkedin.com/in/puja-sharma-a7178a242",
        "linkedin_display": "linkedin.com/in/puja-sharma-a7178a242",
        "github": "[ADD GITHUB URL]",
        "hero_statement": "Building reliable software and intelligent systems.",
        "hero_subtext": "Software Engineer with experience across AI/ML solution development, Retrieval-Augmented Generation, software quality assurance, and application automation. Currently focused on practical AI systems, industrial RAG, OCR/document processing, and Qualcomm technologies.",
        "brand_tagline": "Software Engineer building practical AI systems with a strong foundation in software quality and application engineering.",
        "about_story": "I started my professional journey in QA, where I learned to understand software from the perspective of quality, usability, application workflows and edge cases. I later moved into R&D and software development, where my focus expanded toward AI/ML, Retrieval-Augmented Generation, document processing and practical software solutions.",
        "about_highlight": "From testing how software works to building how intelligent systems work.",
        "profile_image": "images/profile.jpg"
    },
    "stats": [
        {
            "value": "2+",
            "label": "Years of Professional Experience",
            "detail": "QA Intern to Developer R&D at Ecrio Inc."
        },
        {
            "value": "2",
            "label": "Roles at Ecrio",
            "detail": "QA Intern & Developer – R&D Team"
        },
        {
            "value": "4+",
            "label": "Core Technical Areas",
            "detail": "AI/ML, RAG, Python Automation, Edge AI"
        },
        {
            "value": "8.6/10",
            "label": "M.Sc. CGPA",
            "detail": "Mother Teresa Women's University"
        },
        {
            "value": "Gold Medalist",
            "label": "Academic Achievement",
            "detail": "Top Performer of the Batch (Data Science)"
        }
    ],
    "process": [
        {
            "step": "01",
            "title": "Understand",
            "icon": "fa-regular fa-lightbulb",
            "description": "Understand the problem domain, requirements, users, and technical constraints before writing code."
        },
        {
            "step": "02",
            "title": "Build",
            "icon": "fa-solid fa-code",
            "description": "Design and implement clean, practical software solutions using robust Python and AI/ML architectures."
        },
        {
            "step": "03",
            "title": "Validate",
            "icon": "fa-solid fa-circle-check",
            "description": "Test functionality, APIs, workflows, and edge cases leveraging a deeply ingrained quality assurance mindset."
        },
        {
            "step": "04",
            "title": "Improve",
            "icon": "fa-solid fa-chart-line",
            "description": "Analyze results, debug bottlenecks, refine outputs, and continuously iterate for production reliability."
        }
    ],
    "experience": [
        {
            "year": "2025",
            "role": "Developer – R&D",
            "company": "Ecrio Inc.",
            "period": "Jul 2025 – Present",
            "status": "Current Position",
            "stage": "Development & Applied AI",
            "responsibilities": [
                "Develop Retrieval-Augmented Generation (RAG) solutions for industrial use cases.",
                "Build AI/ML solutions in Python and engineer document processing/OCR pipelines.",
                "Work on anomaly detection models for predictive use cases.",
                "Explore and work with Qualcomm SDK technologies for on-device edge AI.",
                "Contribute to AI-driven solutions for real-world industrial applications.",
                "Collaborate with cross-functional development teams."
            ]
        },
        {
            "year": "2024",
            "role": "QA Intern",
            "company": "Ecrio Inc.",
            "period": "Sep 2024 – Jul 2025",
            "status": "Foundation",
            "stage": "Quality Engineering & Automation",
            "responsibilities": [
                "Manual testing of applications and core workflows.",
                "UI automation using Appium and Python.",
                "API testing and payload validation.",
                "Structured test-case execution across environments.",
                "Defect tracking and end-to-end lifecycle management.",
                "Collaboration with development teams on issue reproduction."
            ]
        }
    ],
    "projects": [
        {
            "id": "project-rag",
            "title": "Industrial Q&A RAG System",
            "category": "AI / RAG / Industrial",
            "featured": True,
            "short_desc": "Built a Retrieval-Augmented Generation system for answering questions related to industrial equipment and technical information. The system combines document retrieval and context-based response generation for industrial use cases.",
            "image": "images/project-rag.jpg",
            "technologies": ["Python", "RAG", "Vector Database", "LLM", "Document Processing"],
            "repo_type": "Private / Demonstration",
            "case_study": {
                "problem": "Industrial equipment documentation and technical manuals are lengthy and challenging to search quickly during active operations. Traditional keyword queries failed to capture contextual relationships.",
                "approach": "Engineered a Retrieval-Augmented Generation (RAG) pipeline utilizing Python, vector embeddings, and chunked indexing. Designed semantic search retrieval over specialized equipment manuals, paired with prompt structures for grounded, hallucination-resistant answers.",
                "technologies": ["Python", "RAG Architecture", "Vector Embeddings", "ChromaDB", "LLM Integration", "Industrial Ingestion"],
                "contribution": "Constructed the ingestion and chunking workflow, established semantic indexing for technical manuals, integrated contextual retrieval mechanisms, and built response-generation logic tailored for industrial equipment questions.",
                "outcome_learning": "Engineering Focus: Gained hands-on expertise managing chunk granularity, prompt grounding, vector querying, and ensuring high answer relevance in mission-critical environments."
            }
        },
        {
            "id": "project-ocr",
            "title": "PDF Parsing & OCR Pipeline",
            "category": "AI / Document Processing / OCR",
            "featured": False,
            "short_desc": "Developed a document-processing pipeline that converts incoming PDFs into images and extracts text using OCR. The extracted information is processed and validated for downstream AI/ML applications.",
            "image": "images/project-ocr.jpg",
            "technologies": ["Python", "PDF Processing", "OCR", "Document Processing", "AI/ML"],
            "repo_type": "Private / Demonstration",
            "case_study": {
                "problem": "Enterprise documents and scanned multi-page PDF files contain vital records that cannot be directly queried by machine learning models or downstream automation tools.",
                "approach": "Built a multi-stage Python pipeline that decomposes incoming multi-page PDFs into high-resolution images, applies Optical Character Recognition (OCR), normalizes character encoding, and runs validation filters on extracted text.",
                "technologies": ["Python", "PDF Rasterization", "OCR Engines", "Text Cleaning", "Data Validation", "Downstream Pipeline"],
                "contribution": "Architected the document ingestion script, implemented image pre-processing stages to improve OCR clarity, designed text parsing algorithms to capture clean tokens, and connected outputs to AI/ML ingest channels.",
                "outcome_learning": "Key Learning: Handled noisy scanned inputs, resolved formatting edge cases, and implemented automated quality validation checks rooted in QA testing principles."
            }
        },
        {
            "id": "project-automation",
            "title": "Mobile Application Automation",
            "category": "QA Automation",
            "featured": False,
            "short_desc": "Built and executed UI automation test suites using Appium and Python, alongside manual and API testing, to improve test coverage and reduce repetitive testing effort.",
            "image": "images/project-automation.jpg",
            "technologies": ["Python", "Appium", "Android", "API Testing", "Automation Testing"],
            "repo_type": "Internal / Production Testing",
            "case_study": {
                "problem": "Manual regression testing across repetitive mobile workflows and frequent app releases led to high testing overhead and risk of regression misses across device builds.",
                "approach": "Constructed structured UI automation suites using Appium with Python bindings. Coupled UI end-to-end automation with systematic REST API verification to validate both frontend rendering and backend state changes.",
                "technologies": ["Python", "Appium Framework", "Android Mobile Testing", "Postman / REST APIs", "Pytest", "Defect Tracking"],
                "contribution": "Authored automated test scenarios for key user journeys, maintained device element locators, integrated API assertions into test workflows, and logged actionable defect reports with reproducible steps.",
                "outcome_learning": "Engineering Focus: Developed a deep understanding of application state management, network/API failure modes, edge cases, and how software fails—providing an invaluable foundation for building resilient software."
            }
        },
        {
            "id": "project-qualcomm",
            "title": "Qualcomm AI / SDK Exploration",
            "category": "Edge AI / R&D",
            "featured": False,
            "short_desc": "Exploring Qualcomm SDK technologies and understanding how AI/ML workloads can be developed and supported across Qualcomm platforms.",
            "image": "images/project-qualcomm.jpg",
            "technologies": ["Qualcomm SDK", "AI/ML", "Edge AI", "Python"],
            "repo_type": "R&D Exploration (Ongoing)",
            "case_study": {
                "problem": "Modern AI workloads are moving toward low-latency, privacy-preserving on-device edge execution, requiring specialized developer SDKs and hardware acceleration platforms.",
                "approach": "Engaging in hands-on exploration of Qualcomm SDKs and developer toolkits to study hardware-aware model compilation, edge inference constraints, and runtime execution pipelines.",
                "technologies": ["Qualcomm SDK Tools", "Edge AI Concepts", "Model Runtime Constraints", "Python", "Embedded / On-Device AI"],
                "contribution": "Setting up SDK environments, analyzing sample models, evaluating platform architectures, and studying optimization strategies for edge hardware deployment.",
                "outcome_learning": "Key Learning: Actively building foundational knowledge in edge AI compilation, quantization principles, and embedded compute constraints as part of ongoing R&D initiatives."
            }
        }
    ],
    "skills": {
        "Programming": ["Python", "SQL"],
        "AI / ML": ["RAG", "Machine Learning", "Anomaly Detection", "LLM Applications"],
        "Document Intelligence": ["OCR", "PDF Processing", "Document Parsing"],
        "Vector / Data": ["ChromaDB", "PostgreSQL", "pgvector"],
        "Testing": ["Manual Testing", "Appium", "Python Automation", "API Testing", "Regression Testing"],
        "Edge AI": ["Qualcomm SDK", "AI/ML on Qualcomm platforms"],
        "Tools": ["Git", "GitHub", "Postman", "Microsoft Office Suite"]
    },
    "education": {
        "degree": "M.Sc. Computer Science (Data Science)",
        "institution": "Mother Teresa Women's University",
        "location": "Kodaikanal, India",
        "period": "Aug 2020 – May 2025",
        "cgpa": "8.6 / 10",
        "honors": ["Gold Medalist", "Top Performer of the Batch"]
    },
    "certifications": [
        {"name": "MongoDB", "issuer": "ICT"},
        {"name": "Artificial Intelligence", "issuer": "NoviTech"},
        {"name": "MERN Stack", "issuer": "Ecrio Inc."}
    ],
    "currently_exploring": [
        "RAG Systems",
        "OCR & Document Intelligence",
        "AI/ML",
        "Qualcomm SDK Technologies",
        "Edge AI",
        "Software Engineering"
    ]
}

@app.route('/')
def index():
    # Dynamically ensure profile image uses whichever file exists (.jpeg or .jpg)
    data = PORTFOLIO_DATA.copy()
    data["personal"]["profile_image"] = resolve_image_path("profile", "jpg")
    return render_template('index.html', data=data)

@app.route('/static/documents/resume.pdf')
def get_resume():
    documents_dir = os.path.join(app.root_path, 'static', 'documents')
    resume_path = os.path.join(documents_dir, 'resume.pdf')
    if os.path.exists(resume_path):
        return send_from_directory(documents_dir, 'resume.pdf', as_attachment=False)
    else:
        return "Resume PDF is being finalized. Please contact pujasharmarps@gmail.com directly for the latest copy.", 404

@app.route('/api/contact', methods=['POST'])
def contact_form():
    try:
        data = request.get_json(silent=True) or request.form
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip() or 'Portfolio Contact'
        message = data.get('message', '').strip()

        if not name or not email or not message:
            return jsonify({
                "success": False,
                "message": "Please provide your name, email, and message."
            }), 400

        print(f"[CONTACT INQUIRY] From: {name} <{email}> | Subject: {subject} | Message: {message}")

        return jsonify({
            "success": True,
            "message": "Thank you for reaching out! Your message was received. You can also reach me directly at pujasharmarps@gmail.com."
        }), 200
    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"An error occurred: {str(e)}"
        }), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', data=PORTFOLIO_DATA), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
