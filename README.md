<div align="center">

# CNER: Concept and Named Entity Recognition


[![Conference](https://img.shields.io/badge/NAACL-2024-red)](https://2024.naacl.org/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-green.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Hugging Face Datasets](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20dataset-cner-blue)](https://huggingface.co/datasets/Babelscape/cner)
[![Hugging Face Models](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20model-cner%20base-yellow)](https://huggingface.co/datasets/Babelscape/cner)

</div>


This is the official repository for [*CNER: Concept and Named Entity Recognition*](https://aclanthology.org/2024.eacl-long.135/).  

## Citation
This work has been published at NAACL 2024 (main conference). If you use any part, please consider citing our paper as follows:
```bibtex
@inproceedings{martinelli-etal-2024-cner,
    title = "CNER: Concept and Named Entity Recognition",
    author = "Martinelli, Giuliano and
      Molfese, Francesco  and
      Tedeschi, Simone  and
      Fernàndez-Castro, Alberte  and
      Navigli, Roberto",}
```
# 
This repository contains-  The evaluation scripts to evaluate CNER models.
-  The log of our CNER system used to reproduce paper results.

# Data



# Pretrained Model on HuggingFace 🤗
We release a [Concept and Named Entity Recognition model](https://huggingface.co/Babelscape/cner-base) trained on CNER-silver and on HigginFace🤗 Models.
Specifically, we fine-tuned DeBERTa-base for token classification model on our dataset.


# Reproduce Paper Results
The official weights and training scripts used for the paper are not released in this repository and can be released upon request. 
To produce results for the 10 trained models, run:
    ```
    bash test.sh
    ```
    
    `test.sh` also contains more complex bash for loops that can produce results on multiple datasets / models at once.

<br>
For a stronger system (DeBERTa + Bi-LSTM + CRF) look at [Reproduce Paper Results](#reproduce-paper-results) Section.

https://user-images.githubusercontent.com/47241515/155128789-9bce46bb-598d-4bda-8f62-db43d47a7dfd.mp4


<br>

