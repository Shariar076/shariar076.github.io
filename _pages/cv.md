---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% include base_path %}

<style>
.cv-logo-list > ul { list-style: none; padding-left: 0; }
.cv-logo-list > ul > li { margin-bottom: 0.8em; display: flow-root; }
.cv-logo-list > ul > li > img { float: left; margin-top: -0.4em; }
.cv-logo-list > ul > li > ul { clear: both; }
</style>

A PDF version of my CV is available [here](https://drive.google.com/file/d/1PgpbyadoiLizuEldiPbLEYyajZAsMr6z/view?usp=drive_link).

Education
======
<div class="cv-logo-list" markdown="1">
* <img src="/images/BUET.png" alt="BUET" style="width:3em; height:2.2em; object-fit:contain; vertical-align:bottom; margin-bottom:0.6em;"> M.Sc. in Computer Science and Engineering, Bangladesh University of Engineering and Technology (BUET), 2026
  * GPA: 3.74
  * Thesis: *Dynamic Resource Allocation for Workloads in Serverless Architecture using Collaborative Filtering*, supervised by Prof. Muhammad Abdullah Adnan
* <img src="/images/BUET.png" alt="BUET" style="width:3em; height:2.2em; object-fit:contain; vertical-align:center; margin-bottom:0.6em;"> B.Sc. in Computer Science and Engineering, Bangladesh University of Engineering and Technology (BUET), 2019
  * GPA: 3.53
  * Thesis: *Active Learning on Big Data*, supervised by Prof. Muhammad Abdullah Adnan
</div>

Experience
======
<div class="cv-logo-list" markdown="1">
* <img src="/images/SPAR.png" alt="SPAR" style="width:3em; height:2.2em; object-fit:contain; vertical-align:center; margin-bottom:0.6em;"> **Research Mentee**, Supervised Program for Alignment Research ([SPAR](https://sparai.org/)). Feb 2026 – May 2026
  * **Mentored by [Sriram Balasubramanian](https://www.sriram.live/) (University of Maryland, College Park)**
  * Project: [Automated Circuit Analysis for Real-time Internal Monitoring](https://sparai.org/projects/sp26/reccTI7zHJarXZ9oG). [Report](https://drive.google.com/file/d/1U-XkHeH6XfvY2D8KiuqdTK15dsXoLqt3/view?usp=drive_link).
  * Building automated agents for analyzing large and complex attribution graphs from neural networks.
  * Fully authored the task based on finding spurious correlation for validating the system and detecting failure modes.
  * Extending the system over more realistic tasks like secret knowledge elicitation and misreporting tool calls.

* <img src="/images/UCR.png" alt="UCR" style="width:4em; height:2.2em; object-fit:contain; vertical-align:center; margin-bottom:0.6em;"> **Research Intern**, UCR NLP Lab. Jan 2025 – Dec 2025
  * **Advised by Prof. [Yue Dong](https://yuedong.us/)**
  * Understanding LLMs' response instability over longer context and prompt manipulation.
  * Using mech-interp to understand LLMs behavior over subjective domains e.g., socio-political reasoning.
  * LLMs' social epistemology using Bayesian statistics to model belief depth and opinion dynamics in LLMs.

* <img src="/images/celloscope.svg" alt="Celloscope" style="width:4em; height:2.5em; object-fit:contain; vertical-align:center; margin-right:0.6em;"> **AI Research & Engineering**, Celloscope Limited. Sep 2020 – 2026
  * R&D (Sep 2020 – Jun 2021) → AI SWE (Jul 2021 – Dec 2023) → **Lead AI Research Engineer** (Jan 2024 – 2026)
  * Led a team of six research engineers building production-grade NLP and computer vision systems.
  * Directed key projects: Exercise Monitoring System for LG Nova, a RAG-based Resume Shortlister, and a vision-based Drawing Checker for engineering drawings.

* <img src="/images/MedAI.svg" alt="MedAI" style="width:4em; height:2.2em; object-fit:contain; vertical-align:center; margin-right:0.4em;"> **NLP and Data Scientist**, MedAI Pvt. Limited. Aug 2021 – Nov 2024 (Part Time)
  * Conversational AI chatbot for Bengali mental health support.
  * Synthetic patient generator reflecting local demography.
  * Voice-based patient symptom collector and audio data collection portal.

* <img src="/images/GRP.svg" alt="GRP" style="width:3em; height:2.2em; object-fit:contain; vertical-align:center; margin-bottom:0.6em;"> **DevOps Engineer**, GRP, ICT Division. May 2019 – Aug 2020
  * Automation scripts for deploying web apps and micro-services in Docker.
  * Gateway configuration using NGINX reverse proxy.
</div>

Skills
======
* Machine Learning, Deep Learning, NLP, Large Language Models
* Mechanistic Interpretability, Model Quantization, Computer Vision
* Data Analysis, Data Mining, Big Data, Distributed & Serverless Computing
* DevOps Engineering
* Languages: Python, Java, Scala, C/C++, JavaScript, SQL, Shell, LaTeX
* Frameworks & Libraries: PyTorch, TensorFlow, Transformers, Scikit-learn, LangChain, RASA, Flask, FastAPI, Spark
* Tools: Docker, Kubernetes, Ansible, AWS (EC2/Lambda/Cognito), Hugging Face, PostgreSQL, Grafana

Publications
======
  <ul>{% for post in site.publications reversed %}
    {% include archive-single-cv.html %}
  {% endfor %}</ul>

Talks
======
  <ul>{% for post in site.talks reversed %}
    {% include archive-single-talk-cv.html %}
  {% endfor %}</ul>

Awards & Achievements
======
* **2025** — Industry Coding Assessment (CodeSignal ICA): 510/600 (≈ 722/850 equivalent GCA, top 15%)
* **2024** — Global Health Equity Challenge Award, MIT Solve — *AmarDoctor* selected as one of six solvers out of 2200+ participants worldwide
