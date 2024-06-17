<div align="center">

# CNER: Concept and Named Entity Recognition


[![Conference](https://img.shields.io/badge/NAACL-2024-red)](https://2024.naacl.org/)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-green.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Hugging Face Datasets](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20dataset-cner-blue)](https://huggingface.co/datasets/Babelscape/cner)
[![Hugging Face Models](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face%20model-cner%20base-yellow)](https://huggingface.co/Babelscape/cner-base)

</div>


This is the official repository for [*CNER: Concept and Named Entity Recognition*](https://aclanthology.org/2024.eacl-long.135/).  

## Citation
This work has been published at NAACL 2024 (main conference). If you use any part, please consider citing our paper as follows:
```bibtex
@inproceedings{martinelli-etal-2024-cner,
    title = "{CNER}: Concept and Named Entity Recognition",
    author = "Martinelli, Giuliano  and
      Molfese, Francesco  and
      Tedeschi, Simone  and
      Fern{\'a}ndez-Castro, Alberte  and
      Navigli, Roberto",
    editor = "Duh, Kevin  and
      Gomez, Helena  and
      Bethard, Steven",
    booktitle = "Proceedings of the 2024 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1: Long Papers)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.naacl-long.461",
    pages = "8329--8344",
}
```
# Description
This repository contains the evaluation scripts to evaluate CNER models and the official outputs of the CNER system, which can be used to reproduce paper results. We also release:
- Our silver training and gold evaluation data on [Huggingface](https://huggingface.co/Babelscape/cner).
- A [Concept and Named Entity Recognition model](https://huggingface.co/Babelscape/cner-base) trained on CNER-silver on the HugginFace🤗 Models hub. Specifically, we fine-tuned a pretrained DeBERTa-v3-base for token classification using the default hyperparameters, optimizer and architecture of huggingface (see the [Tutorial Notebook](CNER_HuggingFace.ipynb)) therefore the results of this model may differ from the ones presented in the paper.

# Setup

1. Clone the repository:
    ```
    git clone https://github.com/Babelscape/cner.git
    ```
2. Create a conda environment: 
    ```
    conda create -n env-name python==3.9
    ```
3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

# Evaluate CNER models

To evaluate a CNER model, run the following script:
    ```
    python scripts/evaluate.py --predictions_path path_to_predictions
    ```
    
where `path_to_predictions` is a file with CNER predictions over the CNER-gold dataset split.

Supported formats:

- .jsonl
    ```
  {"sentence_id": "55705165.21", "tokens": ["Commander", ..., "."],  "predictions": ["B-PER", ... , "O"]}
    ```
    
- .tsv

  | Sentence_id | Tokens | predictions |
  | ------------- | ------------- | ------------- |
  | "55705165.21"	| ['Commander', 'Donald', 'S.', ... '.'] | ['B-PER', 'I-PER', ... 'O'] |


# Reproduce Paper Results
At `outputs/cner_output.jsonl` you can find the official outputs of our CNER system.
To reproduce our CNER results, run the following script:
    ```
    python scripts/evaluate.py --predictions_path outputs/cner_output.jsonl
    ```
    

