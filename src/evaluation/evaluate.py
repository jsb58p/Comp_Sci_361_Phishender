import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import csv
import json
import time
from pipeline import analyze_protected

SAMPLE_SIZE = 20
RESULTS_FILE = "evaluation_results.jsonl"

def load_samples(n: int) -> list[dict]:
    print("Loading dataset...")
    phishing = []
    legitimate = []

    with open("email.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            label = row.get("Category", "")
            text  = row.get("Message", "")
            if not text.strip():
                continue
            if label == "spam" and len(phishing) < n // 2:
                phishing.append({"text": text, "expected": "PHISHING"})
            elif label == "ham" and len(legitimate) < n // 2:
                legitimate.append({"text": text, "expected": "LEGITIMATE"})
            if len(phishing) >= n // 2 and len(legitimate) >= n // 2:
                break

    print(f"Loaded {len(phishing)} phishing and {len(legitimate)} legitimate samples")
    return phishing + legitimate

#results printed to terminal and saved to evaluation_results.jsonl, reports precision, recall, f1 and accuracy
def run_evaluation():
    samples = load_samples(SAMPLE_SIZE)

    tp = fp = tn = fn = 0
    results = []

    print(f"\nRunning {len(samples)} samples through pipeline...\n")
    print(f"{'#':<5} {'Expected':<12} {'Got':<12} {'Correct'}")
    print("-" * 40)

    for i, sample in enumerate(samples):
        try:
            result = analyze_protected(sample["text"])
            verdict = result["verdict"].upper()

            #normalize
            if verdict == "UNCERTAIN":
                verdict = "PHISHING"

            expected = sample["expected"]
            correct = verdict == expected

            #confusion matrix
            if expected == "PHISHING" and verdict == "PHISHING":
                tp += 1
            elif expected == "LEGITIMATE" and verdict == "PHISHING":
                fp += 1
            elif expected == "LEGITIMATE" and verdict == "LEGITIMATE":
                tn += 1
            elif expected == "PHISHING" and verdict == "LEGITIMATE":
                fn += 1

            print(f"{i+1:<5} {expected:<12} {verdict:<12} {'yes' if correct else 'no'}")

            results.append({
                "index": i + 1,
                "expected": expected,
                "got": verdict,
                "correct": correct,
                "injection_detected": result.get("injection_detected", False),
            })

            time.sleep(0.5)

        except Exception as e:
            print(f"{i+1:<5} ERROR: {e}")
            results.append({"index": i + 1, "error": str(e)})

    #calculate metrics
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall    = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1        = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    accuracy  = (tp + tn) / len(samples) if samples else 0

    print("\n" + "=" * 40)
    print("EVALUATION RESULTS")
    print("=" * 40)
    print(f"Total samples : {len(samples)}")
    print(f"True Positives: {tp}  (phishing correctly flagged)")
    print(f"True Negatives: {tn}  (legitimate correctly cleared)")
    print(f"False Positives:{fp}  (legitimate flagged as phishing)")
    print(f"False Negatives:{fn}  (phishing missed)")
    print(f"Accuracy  : {accuracy:.2%}")
    print(f"Precision : {precision:.2%}")
    print(f"Recall    : {recall:.2%}")
    print(f"F1 Score  : {f1:.2%}")
    print("=" * 40)

    #save results
    with open(RESULTS_FILE, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
        f.write(json.dumps({
            "summary": {
                "total": len(samples),
                "tp": tp, "tn": tn, "fp": fp, "fn": fn,
                "accuracy": round(accuracy, 4),
                "precision": round(precision, 4),
                "recall": round(recall, 4),
                "f1": round(f1, 4),
            }
        }) + "\n")

    print(f"\nResults saved to {RESULTS_FILE}")

if __name__ == "__main__":
    run_evaluation()