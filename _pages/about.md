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

Dr. Jiahao Wang is currently a senior research engineer in **AI safety and governance** at 2012 Lab of [Huawei Technologies Co., Ltd](https://www.huawei.com/eu/). He received his PhD and B.S. degrees in Computer Science from Beihang University in 2022 and 2017 respectively. He also worked as a research intern in Meituan in 2021.   
Supervised by Prof. [Yunhong Wang](https://scholar.google.com/citations?user=0ez7lA0AAAAJ) at [IRIP Lab](https://irip.buaa.edu.cn/), Dr. Wang's major research interest during PhD was computer vision and video understanding, where he focused on how to utilize **few-shot, unsupervised** and other representation learning methods to facilitate AI **understanding human behaviors accurately and reliably.** It was also from then he has begun to look into the trustworthiness and safety issues of AI. After joining Huawei, he started in-depth research in AI safety and governance, with a particular focus on **AI alignment, hallucination mitigation** and other cutting-edge areas like AI transparency, data governance, etc.


# 🔥 News
- *2025.01*: &nbsp;📚👉 We are recruiting **AI safety research interns and full-time researchers**. Research interests include AI value alignment, hallucination mitigation and other safety issues. You can contact me or apply through our [official website](https://career.huawei.com/reccampportal/portal5/campus-recruitment-detail.html?jobId=12597&dataSource=1&jobType=0&recruitType=CR&sourceType=001).
- *2024.12*: &nbsp;🎯🏆 We have released a [technical challenge](https://www.chaspark.com/#/questions/1081973535022497792?sub=1081986006777053184&lang=en) on [Huawei Chaspark](https://www.chaspark.com/#/home) regarding **AI value alignment evaluation**. Interested academic teams are welcomed to reveal this challenge and collaborate with us!
- *2024.05*: &nbsp;🎉🎉 Our work **EvCap: Element-Aware Video Captioning** was accepted by IEEE TCSVT.
- *2022.07*: &nbsp;🎉🎉 Our unsupervised video segmentation method **PACE** was accepted by IJCAI 2024.

# 📝 Selected Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IJCAI 2022</div><img src='images/IJCAI 2022.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PACE: Predictive and Contrastive Embedding for Unsupervised Action](https://www.ijcai.org/proceedings/2022/0198.pdf)

**Jiahao Wang**, Jie Qin, Yunhong Wang, Annan Li, **IJCAI 2022**

- We are the first to exploit both predictability and similarity information for unsupervised action segmentation. By leveraging their complementarity, we overcome the limitations of existing clustering- and prediction-based methods.
- We design a unified framework to simultaneously learn predictive and contrastive embeddings, based on which accurate action boundaries are detected.
- Extensive experiments on three challenging benchmarks demonstrate the superiority of PACE, with up to 26.9% improvements in F1-score over the state of the art.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2021</div><img src='images/ACM MM 21.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Few-shot Fine-grained Action Recognition via Bidirectional Attention and Contrastive Meta-learning](https://dl.acm.org/doi/10.1145/3474085.3475216)

**Jiahao Wang**, Yunhong Wang, Sheng Liu, Annan Li, **ACM Multimedia 2021**

[**Project**](https://github.com/acewjh/FSFG) <strong><span class='show_paper_citations' data='DhtAFkwAAAAJ:ALROH1vI_8AC'></span></strong>
- We propose the few-shot fine-grained action recognition problem, which is spawned from real-world demands. A novel framework is devised to accurately recognize unseen f ine-grained actions with few support samples. 
- We combine task-driven and saliency-supervised signals to capture subtle action details, simulating the top-down and bottom-up attention mechanism of human vision. 
- To generate discriminative representations for low interclass variance data, we propose contrastive meta-learning, making full use of potential contrastive pairs.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TMM 2022</div><img src='images/TMM 2022.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Bidirectional Maximum Entropy Training with Word Co-occurrence for Video Captioning](https://ieeexplore.ieee.org/document/9780231)

Sheng Liu, Annan Li, **Jiahao Wang**, Yunhong Wang, **IEEE TMM**

- We are the first to introduce the maximum entropy RL theory and probability distribution optimization into the video captioning task. The proposed BME method, which can be employed in a plug-and-play manner, enlarges the search space for RL algorithms and maximizes the relative entropy between neighboring words to increase the diversity of descriptions.
- To the best of our knowledge, this is the first work to exploit word co-occurrence in the training process of video captioning. It enables the model to pay different attention to neighboring word distributions at the phrase level, resulting in more human-like captions.
- Extensive experiments on MSVD and MSR-VTT demonstrate the effectiveness of our approach, by achieving competitive results in different metrics. Further studies show that our method significantly increases the diversity of descriptions compared with the baseline models.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TCSVT 2024</div><img src='images/TCSVT 2024.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EvCap: Element-Aware Video Captioning](https://ieeexplore.ieee.org/document/10529278)

Sheng Liu, Annan Li, Yuwei Zhao, **Jiahao Wang**, Yunhong Wang, **IEEE TCSVT**

- We propose the idea of the element-aware usage of linguistic features in video captioning models which previously rely on the only visual representation which results in the caption that is easily polluted by hallucinations.
- We design an EvCap framework that consists of a multimodal multi-branch encoder-decoder framework and a postoperation fusion strategy to flexibly insert and aggregate additional element-related features besides visual representations.
- We conduct extensive experiments with CNNs, ViT and CLIP as the encoder on four representative datasets. The results demonstrate that EvCap can surpass most state-of-theart methods without training encoders, e.g. MSVD+10.9%, MSR-VTT+1.5%, VATEX+18.9% and TVC+4.7% on CIDEr score under ViT architectures. Furthermore, we also explore the performance of the multi-modal multi-feature framework w.r.t. the types and number of features adopted, e.g. visual and linguistic features, hoping to provide some insights for future model design.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TOMM</div><img src='images/ACM TOMM 21.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Will You Ever Become Popular? Learning to Predict Virality of Dance Clips](https://dl.acm.org/doi/abs/10.1145/3477533)

**Jiahao Wang**, Yunhong Wang, Nina Weng, Tianrui Chai, Annan Li, Faxi Zhang, Sansi Yu, **ACM TOMM**

- We first study virality prediction from dance challenges using visual cues, which has great commercial value. To facilitate the research, we release VDV dataset, a large-scale multi-modal dance virality prediction benchmark.
- A multi-modal framework modeling both body movements and appearance dynamics is developed. For skeleton-based prediction, we devise a pyramidal skeleton graph convolutional network (PSGCN). For appearance-based prediction, relational temporal convolutional networks (RTCN) are proposed. An attentive modality fusion approach is introduced to aggregate predictions from multiple streams.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICIP 2019</div><img src='images/ICIP 2019.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Atrous Temporal Convolutional Network for Video Action Segmentation](https://ieeexplore.ieee.org/document/8803088)

**Jiahao Wang**, Zhengyin Du, Annan Li, Yunhong Wang, **ICIP 2019**

- A novel encoder-decoder fully convolutional network that utilizes atrous temporal convolutions to explicitly extract contextual and local features for accurate temporal action segmentation.
- We propose atrous temporal pyramid pooling (ATPP), an effective and efficient way to capture multiscale action dependencies. To our best knowledge, this is the first work that introduces atrous temporal convolutions to tackle the action segmentation problem in a multiscale manner.
- Experimental results demonstrate that our model achieves improvements over the state of the art on 50 Salads, JIGSAWS and GTEA datasets.
</div>
</div>

# 📝 Publication List
- EvCap: Element-Aware Video Captioning. IEEE TCSVT. 2024  
Sheng Liu, Annan Li, Yuwei Zhao, **Jiahao Wang**, Yunhong Wang
- PACE: Predictive and Contrastive Embedding for Unsupervised Action Segmentation. IJCAI. 2022  
**Jiahao Wang**, Jie Qin, Yunhong Wang, Annan Li
- Bidirectional Maximum Entropy Training with Word Co-occurrence for Video Captioning. IEEE TMM. 2022  
Sheng Liu, Annan Li, **Jiahao Wang**, Yunhong Wang
- Will You Ever Become Popular? Learning to Predict Virality of Dance Clips. ACM TOMM. 2021  
**Jiahao Wang**, Yunhong Wang, Nina Weng, Tianrui Chai, Annan Li, Faxi Zhang, Sansi Yu
- Few-shot Fine-grained Action Recognition via Bidirectional Attention and Contrastive Meta-learning. ACM Multimedia. 2021  
**Jiahao Wang**, Yunhong Wang, Sheng Liu, Annan Li
- Two-stream Temporal Convolutional Network for Dynamic Facial Attractiveness Prediction. IEEE ICRP. 2021  
Nina Weng, **Jiahao Wang**, Annan Li, Yunhong Wang
- Assessing Action Quality via Attentive Spatio-Temporal Convolutional Networks. PRCV. 2020  
**Jiahao Wang**, Zhengyin Du, Annan Li, Yunhong Wang
- Atrous Temporal Convolutional Network for Video Action Segmentation. IEEE ICIP. 2019  
**Jiahao Wang**, Zhengyin Du, Annan Li, Yunhong Wang

# 🎖 Honors and Awards
- *2023* Huawei Rising Star Award
- *2022* Outstanding Doctoral Graduate Award of Beihang University
- *2017* Doctoral Scholarship of Beihang University
- *2017* Outstanding Undergraduate Graduate Award of Beijing
- *2016* Meritorious Winner of MCM/ICM
- *2016* Social Work Scholarship of Beihang University
- *2016* Silver Medal of the 26th Feng Ru Competition of Beihang University

# 📖 Educations
- *2017.09 - 2022.07*, PhD in Computer Science, Beihang University, Beijing, China (Supervised by Prof. [Yunhong Wang](https://scholar.google.com/citations?user=0ez7lA0AAAAJ) at [IRIP Lab](https://irip.buaa.edu.cn/))
- *2015.09 - 2019.06*, B.E. in Computer Science and Technology, Beihang University, Beijing, China

# 💻 Internships
- *2021.05 - 2021.10*, Visual Intelligence Center, Meituan, Beijing, China.