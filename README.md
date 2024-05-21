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
# Description
This repository contains the evaluation scripts to evaluate CNER models and the official outputs of the CNER system, which can be used to reproduce paper results. We also release:
- Our silver training and gold evaluation data on [Huggingface](https://huggingface.co/Babelscape/cner).
- A [Concept and Named Entity Recognition model](https://huggingface.co/Babelscape/cner-base) trained on CNER-silver and on HugginFace🤗 Models (see the [Tutorial Notebook](CNER_HuggingFace.ipynb)). Specifically, we fine-tuned a plain DeBERTa-base for token classification model on our dataset.


# Evaluate CNER models
Using the official data, it is possible to train a cner model on CNER-silver.

To evaluate a CNER model, it is possible to run the following:
    ```
    python scripts/evaluate.py --predictions_path path_to_predictions
    
    )
    ```
    
where `path_to_predictions` is a file with CNER prediction over the cner-gold dataset split.
Supported formats: .jsonl
    ```
{"sentence_id": "55705165.21", "tokens": ["Commander", "Donald", "S.", "Jones", ",", "who", "would", "later", "command", "the", "United", "States", "Third", "Fleet", ",", "piloted", "Helicopter", "66", "during", "its", "inaugural", "astronaut", "recovery", "mission", "following", "Apollo", "8", ",", "and", "again", "during", "the", "Apollo", "11", "recovery", "of", "command", "module", "Columbia", "."], "pos": ["PROPN", "PROPN", "PROPN", "PROPN", "PUNCT", "PRON", "AUX", "ADV", "VERB", "DET", "VERB", "PROPN", "ADJ", "PROPN", "PUNCT", "VERB", "PROPN", "NUM", "ADP", "PRON", "ADJ", "NOUN", "NOUN", "NOUN", "VERB", "PROPN", "NUM", "PUNCT", "CCONJ", "ADV", "ADP", "DET", "PROPN", "NUM", "NOUN", "ADP", "NOUN", "NOUN", "PROPN", "PUNCT"], "c_vs_ne": ["O", "NE", "NE", "NE", "O", "O", "O", "O", "O", "O", "NE", "NE", "NE", "NE", "O", "O", "NE", "NE", "O", "O", "O", "C", "C", "C", "O", "NE", "NE", "O", "O", "O", "O", "O", "NE", "NE", "C", "O", "C", "NE", "NE", "O"], "predictions": ["B-PER", "I-PER", "I-PER", "I-PER", "O", "O", "O", "O", "O", "O", "B-ORG", "I-ORG", "I-ORG", "I-ORG", "O", "O", "B-ARTIFACT", "I-ARTIFACT", "O", "O", "O", "B-PER", "B-EVENT", "I-EVENT", "O", "B-ARTIFACT", "I-ARTIFACT", "O", "O", "O", "O", "O", "B-ARTIFACT", "I-ARTIFACT", "I-ARTIFACT", "O", "B-STRUCT", "B-ARTIFACT", "B-LOC", "O"]}

    ```
    
Supported formats: .tsv

| Sentence_id | Tokens | predictions |
| :------------- | -------------: | -------------: |
| "123..."	| ['Commander', 'Donald', 'S.', ... '.'] | ['B-PER', 'I-PER', ... 'O'] |


# Reproduce Paper Results
cner_output.jsonl are the official outputs of our cner system
To produce CNER results, it is possible to run the following:
    ```
    bash test.sh
    ```
    


