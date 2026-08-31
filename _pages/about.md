---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Dr. Jiahao Wang is a Principal Research Engineer at the Central Research Institute of Huawei 2012 Laboratories. His current research focuses on **multimodal foundation models** and **Computer-Using Agents (CUA)**, including GUI/CLI agents, OS/mobile navigation, visual coding, scalable agent data flywheels, and pre-training/post-training techniques for agentic multimodal models.

Before moving to multimodal agent research, he worked on **AI safety and trustworthy foundation models**, with a focus on LLM value alignment, hallucination evaluation, factuality alignment, and frontier AI governance. His earlier Ph.D. research at [IRIP Lab](https://irip.buaa.edu.cn/), Beihang University, supervised by Prof. [Yunhong Wang](https://scholar.google.com/citations?user=0ez7lA0AAAAJ), focused on trustworthy multimodal learning and fine-grained video understanding.

I am interested in research collaborations and strong candidates in multimodal agents, GUI agents, CUA training, agentic RL, AI alignment, and trustworthy foundation models.

<span class='anchor' id='research-agenda'></span>
# Research Agenda

- **Computer-Using Agents**: GUI grounding, GUI/CLI navigation, OS/mobile/web agents, visual coding, and unified action spaces across interfaces and tools.
- **Agent Data Flywheels**: scalable data generation, trajectory quality control, verifiable task expansion, evaluation-to-training loops, and data mixture design for pre-training and SFT.
- **Agentic Training**: post-training, reinforcement learning infrastructure, process reward modeling, on-policy distillation, and long-horizon task optimization.
- **Trustworthy Foundation Models**: value alignment, hallucination and factuality evaluation, pluralistic alignment, safety evaluation, and governance-oriented model assessment.

<!-- <span class='anchor' id='selected-projects'></span>
# Selected Projects

**Multimodal Agent Data Flywheel**  
Built scalable data production pipelines for GUI grounding, navigation, and visual coding. The pipeline produced 13M pre-training samples and 500K SFT samples for multimodal foundation model training, improving GUI grounding accuracy by 21% and average navigation success rate by 16% on internal and public benchmarks.

**OS-Level GUI Navigation**  
Designed a goal-space-constrained GUI task expansion method that jointly generates executable instructions and verifiers. This improves the diversity and verifiability of OS-level agent trajectories and led to a 13% success-rate gain on OSWorld-style evaluation.

**Ethical Reasoning for Value Alignment**  
Proposed an ethical-reasoning paradigm for LLM value alignment, including fact gathering, norm identification, response strategy generation, ethical impact analysis, and reflection. The work achieved strong results on SafeWorld and was accepted as an oral paper at AIES 2025.

**Fine-Grained Hallucination Evaluation**  
Developed scalable benchmark construction and evaluation methods for hallucination detection in text and multimodal large models, covering factuality and faithfulness failure modes. Related work was accepted by ACM Multimedia 2025 and CIKM 2025. -->

<span class='anchor' id='news'></span>
# News

- *2026.04*: We are recruiting outstanding interns and full-time researchers in multimodal agentic models, GUI agents, and CUA training. Master's and Ph.D. candidates are welcome to connect.
- *2025.10*: Our work **Diverse Human Value Alignment for Large Language Models via Ethical Reasoning** was accepted as an [oral paper](https://ojs.aaai.org/index.php/AIES/article/download/36744/38882) by AIES 2025.
- *2025.08*: Our work **SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs** was accepted by ACM Multimedia 2025.
- *2025.08*: Our work **C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation** was accepted by CIKM 2025.
- *2024.12*: We released a [technical challenge](https://www.chaspark.com/#/questions/1081973535022497792?sub=1081986006777053184&lang=en) on [Huawei Chaspark](https://www.chaspark.com/#/home) about **AI value alignment evaluation**.
- *2024.05*: Our work **EvCap: Element-Aware Video Captioning** was accepted by IEEE TCSVT.
- *2022.07*: Our unsupervised video segmentation method **PACE** was accepted by IJCAI 2022.

<span class='anchor' id='selected-publications'></span>
# Selected Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AIES 2025</div><img src='images/AIES 2025.png' alt="AIES 2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Diverse Human Value Alignment for Large Language Models via Ethical Reasoning](https://arxiv.org/abs/2511.00379)

**Jiahao Wang**, Songkai Xue, Jinghui Li, Xiaozhen Wang, **AIES 2025 Oral**

[Paper](https://arxiv.org/pdf/2511.00379) / [Oral Presentation](https://www.youtube.com/live/ixl7piZoU5k?si=uvnY4nZ_IrDit1kQ)
- Built an ethical-reasoning paradigm for LLM value alignment from interdisciplinary ethical decision-making models.
- Integrated four complementary ethical theories for multi-lens ethical impact analysis and diverse human value alignment.
- Improved social norm inference and cultural sensitivity on SafeWorld-style value alignment evaluation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='images/ACM MM 2025.png' alt="ACM MM 2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs](https://arxiv.org/abs/2508.09584)

Bei Yan, Zhiyuan Chen, Yuecong Min, Jie Zhang, **Jiahao Wang**, Xiaozhen Wang, Shiguang Shan, **ACM Multimedia 2025**

[Paper](https://arxiv.org/pdf/2508.09584) / [ACM DL](https://dl.acm.org/doi/abs/10.1145/3746027.3758308)
- Built a scalable hallucination benchmark with controllable image-instruction pairs and fine-grained ground-truth answers.
- Covered diverse hallucination types, tasks, and scenarios with over 30K image-instruction pairs.
- Evaluated over 20 representative LVLMs and revealed factuality hallucination and semantic perturbation sensitivity.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">CIKM 2025</div><img src='images/CIKM 2025.png' alt="CIKM 2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation](https://arxiv.org/abs/2504.10167)

Xu Zhang, Zhifei Liu, **Jiahao Wang**, Huixuan Zhang, Fan Xu, Junzhe Zhang, Xiaojun Wan, **CIKM 2025**

[Paper](https://arxiv.org/pdf/2504.10167)
- Built a Chinese fine-grained benchmark for automated hallucination evaluation.
- Supports more precise assessment of factual consistency and hallucination failure modes in Chinese LLM outputs.
- Complements multimodal hallucination evaluation with a text-centric factuality benchmark.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2022</div><img src='images/IJCAI 2022.png' alt="IJCAI 2022" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PACE: Predictive and Contrastive Embedding for Unsupervised Action Segmentation](https://www.ijcai.org/proceedings/2022/0198.pdf)

**Jiahao Wang**, Jie Qin, Yunhong Wang, Annan Li, **IJCAI 2022**

- Proposed a unified framework that exploits both predictability and similarity information for unsupervised action segmentation.
- Learned predictive and contrastive embeddings for accurate action boundary detection.
- Achieved up to 26.9% F1-score improvement over prior state-of-the-art methods.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2021</div><img src='images/ACM MM 21.png' alt="ACM MM 2021" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Few-shot Fine-grained Action Recognition via Bidirectional Attention and Contrastive Meta-learning](https://dl.acm.org/doi/10.1145/3474085.3475216)

**Jiahao Wang**, Yunhong Wang, Sheng Liu, Annan Li, **ACM Multimedia 2021**

[Project](https://github.com/acewjh/FSFG)
- Proposed the few-shot fine-grained action recognition problem and a framework for recognizing unseen fine-grained actions with few support samples.
- Combined task-driven and saliency-supervised signals to capture subtle action details.
- Introduced contrastive meta-learning for discriminative representation learning in low inter-class variance scenarios.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCSVT 2024</div><img src='images/TCSVT 2024.png' alt="TCSVT 2024" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EvCap: Element-Aware Video Captioning](https://ieeexplore.ieee.org/document/10529278)

Sheng Liu, Annan Li, Yuwei Zhao, **Jiahao Wang**, Yunhong Wang, **IEEE TCSVT 2024**

- Proposed element-aware usage of linguistic features to reduce video-captioning hallucinations.
- Designed a multimodal multi-branch encoder-decoder framework with flexible feature fusion.
- Achieved strong CIDEr improvements across MSVD, MSR-VTT, VATEX, and TVC.
</div>
</div>

<span class='anchor' id='publication-list'></span>
# Publication List

- Diverse Human Value Alignment for Large Language Models via Ethical Reasoning. AIES 2025 Oral.  
**Jiahao Wang**, Songkai Xue, Jinghui Li, Xiaozhen Wang
- SHALE: A Scalable Benchmark for Fine-grained Hallucination Evaluation in LVLMs. ACM Multimedia 2025.  
Bei Yan, Zhiyuan Chen, Yuecong Min, Jie Zhang, **Jiahao Wang**, Xiaozhen Wang, Shiguang Shan
- C-FAITH: A Chinese Fine-Grained Benchmark for Automated Hallucination Evaluation. CIKM 2025.  
Xu Zhang, Zhifei Liu, **Jiahao Wang**, Huixuan Zhang, Fan Xu, Junzhe Zhang, Xiaojun Wan
- VAPO: ValueCoT-Enhanced Search-Based Prompt Optimization for Human Value Alignment. Preprint.  
Xuening Feng, **Jiahao Wang** et al.
- EvCap: Element-Aware Video Captioning. IEEE TCSVT 2024.  
Sheng Liu, Annan Li, Yuwei Zhao, **Jiahao Wang**, Yunhong Wang
- PACE: Predictive and Contrastive Embedding for Unsupervised Action Segmentation. IJCAI 2022.  
**Jiahao Wang**, Jie Qin, Yunhong Wang, Annan Li
- Bidirectional Maximum Entropy Training with Word Co-occurrence for Video Captioning. IEEE TMM 2022.  
Sheng Liu, Annan Li, **Jiahao Wang**, Yunhong Wang
- Few-Shot Fine-Grained Action Recognition via Bidirectional Attention and Contrastive Meta-Learning. ACM Multimedia 2021.  
**Jiahao Wang**, Yunhong Wang, Sheng Liu, Annan Li
- Will You Ever Become Popular? Learning to Predict Virality of Dance Clips. ACM TOMM 2021.  
**Jiahao Wang**, Yunhong Wang, Nina Weng, Tianrui Chai, Faxi Zhang, Sansi Yu, Annan Li
- Two-Stream Temporal Convolutional Network for Dynamic Facial Attractiveness Prediction. IEEE ICPR 2020.  
Nina Weng, **Jiahao Wang**, Annan Li, Yunhong Wang
- Assessing Action Quality via Attentive Spatio-Temporal Convolutional Networks. PRCV 2020.  
**Jiahao Wang**, Zhengyin Du, Annan Li, Yunhong Wang
- Atrous Temporal Convolutional Network for Video Action Segmentation. IEEE ICIP 2019.  
**Jiahao Wang**, Zhengyin Du, Annan Li, Yunhong Wang

<span class='anchor' id='honors-and-awards'></span>
# Honors and Awards

- *2024* Huawei Annual President's Individual Award
- *2024* Huawei Battlefield Hero Award
- *2022, 2023* Huawei Rising Star Award
- *2022* Outstanding Doctoral Graduate Award of Beihang University
- *2017* Doctoral Scholarship of Beihang University
- *2017* Outstanding Undergraduate Graduate Award of Beijing
- *2016* Meritorious Winner of MCM/ICM
- *2016* Silver Medal of the 26th Feng Ru Competition of Beihang University

<span class='anchor' id='education'></span>
# Education

- *2017.09 - 2022.07*, Ph.D. in Computer Science and Technology, Beihang University, Beijing, China. Supervised by Prof. [Yunhong Wang](https://scholar.google.com/citations?user=0ez7lA0AAAAJ) at [IRIP Lab](https://irip.buaa.edu.cn/).
- *2013.09 - 2017.06*, B.E. in Computer Science and Technology, Beihang University, Beijing, China.

<span class='anchor' id='experience'></span>
# Experience

- *2025 - Present*, Central Research Institute / Foundation Model Lab, Huawei 2012 Laboratories, Shenzhen, China.
- *2022 - 2025*, AI Safety and Trustworthiness Research, Huawei 2012 Laboratories, Shenzhen, China.
- *2021.05 - 2021.10*, Visual Intelligence Center, Meituan, Beijing, China.
