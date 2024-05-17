from argparse import ArgumentParser
from datasets import load_dataset
import jsonlines
import csv
import ast
from sklearn.metrics import classification_report as token_level_report
from seqeval.metrics import classification_report as span_level_report

class CnerEvaluator:
    def __init__(self, predictions_path: str):
        self.predictions_path = predictions_path

    def prepare_data(self):
        test_dataset = load_dataset("Babelscape/cner")["test"]
        all_predictions = []
        all_test_labels = []

        ## Load the model predictions and test labels from a jsonl file.
        if self.predictions_path.endswith(".jsonl"):
            predictions_file = jsonlines.open(self.predictions_path, "r")
            for pred_line in predictions_file:
                all_predictions.extend(pred_line["predictions"])
            for test_line in test_dataset:
                all_test_labels.extend(test_line["cner_tags"])

        ## Load the model predictions and test labels from a tsv file.
        elif self.predictions_path.endswith(".tsv"):
            predictions_file = csv.reader(
                open(self.predictions_path, "r"), delimiter="\t"
            )
            next(predictions_file)  ## Skipping the header
            for pred_line in predictions_file:
                all_predictions.extend(ast.literal_eval(pred_line[4]))
            for test_line in test_dataset:
                all_test_labels.extend(test_line["cner_tags"])

        return all_predictions, all_test_labels

    def evaluate(self):
        ## Load all the token predictions and test labels.
        predictions, test_labels = self.prepare_data()

        ## Compute token level metrics (Micro and Macro F1 scores).
        token_level_metrics = token_level_report(
            y_pred=predictions, y_true=test_labels, output_dict=False, digits=4
        )
        print("Classification Report Micro F1 and Macro F1: \n")
        print(token_level_metrics)

        ## Compute span level metrics (Span F1 score).
        span_metrics = span_level_report(
            y_pred=[predictions], y_true=[test_labels], output_dict=False, digits=4
        )
        print("Classification Report Span F1: \n")
        print(span_metrics)


if __name__ == "__main__":
    parser = ArgumentParser(
        description="Script to evaluate a CNER model output on the official test set.",
        add_help=True,
    )
    parser.add_argument(
        "--predictions_path",
        type=str,
        help="Path to the model predictions file. Supported formats: .jsonl, .tsv.",
    )
    args = parser.parse_args()
    cner_evaluator = CnerEvaluator(args.predictions_path)
    cner_evaluator.evaluate()
