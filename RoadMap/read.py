from fpdf import FPDF

# Create the PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Python to Kubernetes Automation Roadmap", ln=True, align="C")
pdf.ln(10)

pdf.set_font("Arial", "", 12)

content = """
This roadmap takes you from Python fundamentals to writing Kubernetes automation scripts and real-world DevOps projects.

------------------------------------------------------------
STAGE 1: Strengthen Core Python (2–3 weeks)
------------------------------------------------------------
Focus on building strong fundamentals:
• Data types (list, dict, tuple, set)
• Loops, conditionals, and functions
• File operations (read/write)
• Error handling and modules
• JSON/YAML handling
• Environment variables and datetime

Practice ideas:
• Parse a JSON file and print keys
• Modify YAML values and save them
• Write a script to read log files
Recommended: “Automate the Boring Stuff with Python”

------------------------------------------------------------
STAGE 2: Work with Files & APIs (2 weeks)
------------------------------------------------------------
Learn to manipulate YAML and call REST APIs.
• PyYAML – Read and write Kubernetes manifests
• requests – Send HTTP GET/POST requests
• subprocess – Run shell commands via Python

Example:
import yaml
with open('deployment.yaml') as f:
    data = yaml.safe_load(f)
data['spec']['replicas'] = 5
with open('updated.yaml', 'w') as f:
    yaml.dump(data, f)

------------------------------------------------------------
STAGE 3: Kubernetes API & Python Client (3–4 weeks)
------------------------------------------------------------
Install the client: pip install kubernetes
Learn API groups: CoreV1Api, AppsV1Api

Practice projects:
• List pods and namespaces
• Get logs from pods
• Create and scale deployments
• Patch deployments for rolling restarts

------------------------------------------------------------
STAGE 4: Build Mini Projects (4–6 weeks)
------------------------------------------------------------
Apply Python + Kubernetes together:
1. Namespace Cleaner – delete test namespaces older than 1 day
2. Pod Health Checker – alert if pods not Running
3. Deployment Generator – generate YAML from input
4. Custom Auto-Scaler – scale up/down via metrics

Each project should use argparse, logging, and version control (Git).

------------------------------------------------------------
STAGE 5: Combine with GCP (Advanced)
------------------------------------------------------------
Use Python SDKs for GCP:
• google-cloud-container – manage GKE clusters
• google-cloud-storage – store logs or manifests
• Automate GKE creation, IAM setup, and monitoring.

------------------------------------------------------------
SUGGESTED TIMELINE (Approx. 12 Weeks)
------------------------------------------------------------
Weeks 1–3: Python fundamentals
Weeks 4–5: File & API handling
Weeks 6–9: Kubernetes automation
Weeks 10–12: Projects & GCP integration

------------------------------------------------------------
LEARNING STRATEGY
------------------------------------------------------------
• Learn by doing small automations
• Use GitHub for your code portfolio
• Watch “TechWorld with Nana” or “DevOps Toolkit”
• Always understand WHY each line exists

------------------------------------------------------------
NEXT STEPS
------------------------------------------------------------
Build one complete project, e.g.:
“Kubernetes Deployment Manager” – a Python CLI to deploy, scale, and monitor workloads.
"""

pdf.multi_cell(0, 8, content)
pdf.output("Python_to_Kubernetes_Automation_Roadmap.pdf")

print("✅ PDF created: Python_to_Kubernetes_Automation_Roadmap.pdf")
