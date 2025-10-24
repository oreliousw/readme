from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

# Create PDF
pdf_path = "/mnt/data/AWS_Cloud_Trading_Environment_Guide.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter)
styles = getSampleStyleSheet()

content = []

# Title
content.append(Paragraph("<b>AWS Cloud-Native Trading & Development Environment</b>", styles["Title"]))
content.append(Spacer(1, 12))

# Section 1: Overview
content.append(Paragraph("<b>1. Overview</b>", styles["Heading2"]))
content.append(Paragraph(
    "This document provides a visual and step-by-step guide for setting up a fully cloud-based "
    "trading and development environment using AWS WorkSpaces, Lambda, EC2, Route 53, and GitHub. "
    "It allows for a hardware-free workflow that centralizes trading, video editing, and development "
    "activities entirely in the cloud.",
    styles["Normal"]
))
content.append(Spacer(1, 12))

# Section 2: System Layout
content.append(Paragraph("<b>2. System Layout (Architecture Diagram)</b>", styles["Heading2"]))
layout_text = """
GitHub (Code & Versioning)
   ↓
AWS Cloud Infrastructure:
   • Route 53 – DNS Management
   • Lambda – Event-based OANDA Automation
   • EC2/Lightsail – Web Servers & Bridge
   • S3 – Logs, Videos, and Backups
   • CloudWatch – Monitoring
   • WorkSpaces – Windows 11 Cloud PC
   ↓
User Access:
   • Laptop / Linux / iPad / Tesla Browser (via WorkSpaces Web)
"""
content.append(Paragraph(layout_text.replace("\n", "<br/>"), styles["Code"]))
content.append(Spacer(1, 12))

# Section 3: AWS Components Table
content.append(Paragraph("<b>3. AWS Component Overview</b>", styles["Heading2"]))
table_data = [
    ["Component", "Purpose", "Example Use"],
    ["GitHub", "Source Control & CI/CD", "Holds Pine + Python scripts for OANDA Bridge"],
    ["Lambda", "Serverless compute", "Executes trading triggers and webhooks"],
    ["EC2/Lightsail", "Persistent server", "Runs OANDA Bridge + Telegram Agent"],
    ["WorkSpaces", "Cloud PC", "Windows 11 dev, 1Password, Insta360 Studio"],
    ["S3", "Storage", "Stores 360 videos, logs, and backups"],
    ["Route 53", "DNS Service", "Manages execflightservices.com"],
    ["CloudWatch", "Monitoring", "Tracks performance and logs"]
]
table = Table(table_data, colWidths=[100, 150, 200])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
    ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
]))
content.append(table)
content.append(Spacer(1, 12))

# Section 4: WorkSpaces Setup Steps
content.append(Paragraph("<b>4. AWS WorkSpaces Setup Steps</b>", styles["Heading2"]))
steps = [
    "1. Sign in to AWS Console → WorkSpaces → 'Launch WorkSpace'.",
    "2. Choose region (e.g., us-west-2) and create a directory (Simple AD).",
    "3. Add user account (you).",
    "4. Select bundle type: Performance Plus or Graphics.g4dn (8 vCPU / 32 GB RAM + GPU).",
    "5. Configure networking: use same VPC as Lambda/EC2 and allow outbound 80/443.",
    "6. Enable browser-based access (WorkSpaces Web).",
    "7. Install essential tools (1Password, Insta360 Studio, VS Code, AWS CLI).",
    "8. Integrate GitHub & AWS CLI for deployments.",
    "9. Link 1Password secrets for secure CI/CD and OANDA credentials.",
    "10. Enable auto-stop timers for cost efficiency."
]
content.extend([Paragraph(s, styles["Normal"]) for s in steps])
content.append(Spacer(1, 12))

# Section 5: Example Cloud Workstation
content.append(Paragraph("<b>5. Recommended WorkSpace Specs</b>", styles["Heading2"]))
specs = """
• CPU: 8 vCPU (NVIDIA T4 GPU optional)<br/>
• RAM: 32 GB<br/>
• Storage: 512 GB SSD<br/>
• OS: Windows 11 Pro or Server GUI<br/>
• Network: Low-latency connection<br/>
• Software Stack: 1Password, Insta360 Studio, VS Code, AWS CLI, TradingView<br/>
"""
content.append(Paragraph(specs, styles["Normal"]))
content.append(Spacer(1, 12))

# Section 6: Optional Enhancements
content.append(Paragraph("<b>6. Optional Enhancements</b>", styles["Heading2"]))
enhancements = """
• S3 + Glacier for long-term 8K storage<br/>
• Amplify or Lightsail for web apps<br/>
• RDS / DynamoDB for trade & flight data<br/>
• QuickSight or Grafana for analytics<br/>
• 1Password Teams + IAM roles for security<br/>
"""
content.append(Paragraph(enhancements, styles["Normal"]))
content.append(Spacer(1, 12))

# Section 7: Summary
content.append(Paragraph("<b>7. Summary</b>", styles["Heading2"]))
summary_text = """
This setup enables a zero-hardware workflow, allowing you to develop, trade, and edit video entirely in the cloud.
Everything runs through AWS and GitHub, giving secure, scalable, and location-independent access.
"""
content.append(Paragraph(summary_text, styles["Normal"]))

# Build PDF
doc.build(content)
pdf_path
