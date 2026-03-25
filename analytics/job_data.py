JOB_ROLES = {

    "technology": {
        "frontend_developer": ["html", "css", "javascript", "react", "git", "responsive design"],
        "backend_developer": ["python", "django", "nodejs", "api", "mysql", "git"],
        "fullstack_developer": ["html", "css", "javascript", "react", "nodejs", "django", "mysql", "git"],
        "data_scientist": ["python", "machine learning", "pandas", "numpy", "data visualization"],
        "data_analyst": ["excel", "sql", "python", "power bi", "statistics"],
        "devops_engineer": ["docker", "kubernetes", "aws", "ci/cd", "linux", "git"],
        "mobile_app_developer": ["flutter", "react native", "android", "ios", "api"],
        "cybersecurity_analyst": ["network security", "ethical hacking", "firewalls", "cryptography"],
        "cloud_engineer": ["aws", "azure", "gcp", "cloud architecture", "linux"],
        "ai_engineer": ["python", "deep learning", "tensorflow", "nlp", "computer vision"],
        "software_engineer": ["java", "python", "dsa", "oop", "git"],
        "game_developer": ["unity", "c#", "game design", "graphics"],
        "qa_engineer": ["testing", "selenium", "automation", "bug tracking"],
        "blockchain_developer": ["solidity", "ethereum", "smart contracts"],
        "system_admin": ["linux", "networking", "servers", "troubleshooting"]
    },

    "finance": {
        "accountant": ["accounting", "tally", "gst", "taxation", "excel"],
        "financial_analyst": ["financial modeling", "excel", "valuation", "forecasting"],
        "investment_banker": ["finance", "valuation", "m&a", "pitching"],
        "auditor": ["audit", "compliance", "accounting standards"],
        "tax_consultant": ["tax laws", "gst", "income tax"],
        "risk_manager": ["risk analysis", "compliance", "finance"],
        "bank_manager": ["banking", "customer service", "loans"],
        "credit_analyst": ["credit analysis", "risk assessment"],
        "insurance_advisor": ["insurance", "sales", "client handling"],
        "stock_broker": ["stock market", "trading", "analysis"],
        "finance_manager": ["budgeting", "finance", "leadership"],
        "treasury_analyst": ["cash flow", "liquidity", "banking"],
        "portfolio_manager": ["investment", "portfolio", "analysis"]
    },

    "management": {
        "project_manager": ["project planning", "agile", "scrum", "leadership"],
        "hr_manager": ["recruitment", "employee relations", "hr policies"],
        "operations_manager": ["operations", "logistics", "process improvement"],
        "product_manager": ["product strategy", "roadmap", "user research"],
        "business_analyst": ["analysis", "requirements gathering", "documentation"],
        "marketing_manager": ["marketing", "branding", "campaigns"],
        "sales_manager": ["sales", "negotiation", "crm"],
        "supply_chain_manager": ["logistics", "inventory", "procurement"],
        "entrepreneur": ["business strategy", "innovation", "finance"],
        "consultant": ["problem solving", "analysis", "presentation"],
        "event_manager": ["event planning", "coordination", "budgeting"],
        "operations_executive": ["operations", "reporting", "coordination"]
    },

    "healthcare": {
        "doctor": ["diagnosis", "medical knowledge", "patient care"],
        "nurse": ["patient care", "clinical skills"],
        "pharmacist": ["medication", "pharmacy", "drug knowledge"],
        "lab_technician": ["lab tests", "equipment handling"],
        "physiotherapist": ["rehabilitation", "therapy"],
        "radiologist": ["imaging", "x-ray", "mri"],
        "medical_coder": ["coding", "medical records"],
        "healthcare_admin": ["hospital management", "operations"],
        "dentist": ["dental care", "oral health"],
        "nutritionist": ["diet planning", "health"],
        "surgeon": ["surgery", "precision"],
        "paramedic": ["emergency care", "first aid"]
    },

    "education": {
        "teacher": ["teaching", "subject knowledge", "communication"],
        "professor": ["research", "teaching"],
        "tutor": ["guidance", "subject expertise"],
        "principal": ["management", "leadership"],
        "counselor": ["guidance", "psychology"],
        "curriculum_developer": ["curriculum design", "education"],
        "librarian": ["library management"],
        "special_educator": ["special needs", "teaching"],
        "education_coordinator": ["planning", "coordination"],
        "online_instructor": ["e-learning", "content creation"]
    },

    "arts_design": {
        "graphic_designer": ["photoshop", "illustrator", "design"],
        "ui_ux_designer": ["figma", "user research", "wireframing"],
        "animator": ["animation", "after effects"],
        "fashion_designer": ["fashion", "creativity"],
        "interior_designer": ["interior", "space planning"],
        "video_editor": ["editing", "premiere pro"],
        "photographer": ["photography", "lighting"],
        "content_creator": ["creativity", "social media"],
        "illustrator": ["drawing", "digital art"],
        "art_director": ["design", "leadership"]
    },

    "retail": {
        "store_manager": ["management", "sales"],
        "sales_executive": ["sales", "customer service"],
        "cashier": ["billing", "transactions"],
        "inventory_manager": ["inventory", "stock"],
        "retail_buyer": ["purchasing", "analysis"],
        "merchandiser": ["display", "sales"],
        "customer_support": ["communication", "problem solving"],
        "retail_supervisor": ["supervision", "operations"],
        "warehouse_staff": ["storage", "logistics"]
    },

    "hospitality": {
        "hotel_manager": ["management", "operations"],
        "chef": ["cooking", "creativity"],
        "waiter": ["service", "communication"],
        "receptionist": ["front desk", "communication"],
        "housekeeping": ["cleanliness", "maintenance"],
        "event_coordinator": ["events", "planning"],
        "travel_agent": ["travel planning"],
        "tour_guide": ["guidance", "history"],
        "restaurant_manager": ["operations", "staff management"]
    },

    "law": {
        "lawyer": ["legal knowledge", "litigation"],
        "legal_advisor": ["consulting", "law"],
        "judge": ["judgment", "law"],
        "paralegal": ["documentation", "research"],
        "corporate_lawyer": ["corporate law", "contracts"],
        "criminal_lawyer": ["criminal law", "defense"],
        "legal_researcher": ["research", "analysis"],
        "compliance_officer": ["compliance", "regulations"]
    },

    "manufacturing": {
        "production_manager": ["production", "planning"],
        "quality_engineer": ["quality control", "testing"],
        "mechanical_engineer": ["mechanics", "design"],
        "electrical_engineer": ["electrical", "circuits"],
        "plant_manager": ["operations", "management"],
        "safety_officer": ["safety", "regulations"],
        "maintenance_engineer": ["maintenance", "repair"],
        "industrial_engineer": ["process optimization"],
        "supply_chain_executive": ["logistics", "inventory"]
    }
}


COMMON_SKILLS = [

    # 🧠 Cognitive Skills
    "problem solving",
    "critical thinking",
    "analytical thinking",
    "decision making",
    "creativity",

    # 🗣️ Communication Skills
    "communication",
    "verbal communication",
    "written communication",
    "presentation skills",
    "active listening",

    # 👥 Interpersonal Skills
    "teamwork",
    "collaboration",
    "leadership",
    "conflict resolution",
    "emotional intelligence",

    # ⏱️ Work Ethics & Productivity
    "time management",
    "adaptability",
    "multitasking",
    "work ethic",
    "attention to detail",

    # 💼 Professional Skills
    "project management",
    "organizational skills",
    "client handling",
    "negotiation",
    "decision making",

    # 💻 Basic Technical Skills (used across industries)
    "ms excel",
    "ms word",
    "powerpoint",
    "internet research",
    "data entry",

    # 🌐 Digital Literacy
    "email communication",
    "social media",
    "online collaboration tools",
    "google workspace",

    # 📊 Business & Analytical Tools
    "data analysis",
    "reporting",
    "documentation",
    "basic accounting",

    # 🧩 Personality Traits (optional but useful)
    "self motivation",
    "responsibility",
    "adaptability",
    "punctuality"
]

CORE_WEIGHT = 0.7
COMMON_WEIGHT = 0.3