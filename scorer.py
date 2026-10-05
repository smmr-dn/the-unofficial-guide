"""
scorer.py — judge whether retrieval actually found the answer.

    judge(question, expects, answer, results) -> bool

Criterion 1 is about RETRIEVAL, not generation: "the retrieved chunks include
one that contains the answer." So this checks the chunks in `results`, not
the model's `answer` — that's why judge() takes `results` at all.

Either way it's a substring test: does `expects` show up in the text? That's
wrong in both directions — a chunk can say the same thing in different words
and get missed (false negative), or contain the substring without actually
being the passage that answers the question (false positive). Good enough to
start; we come back to how to do better later.
"""

import re


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def judge(question: str, expects: str, answer: str, results: list) -> bool:
    if not expects:
        return False

    needle = _normalize(expects)
    return any(needle in _normalize(r.text) for r in results)


def main():
    import config
    import questions as qs
    from store import search
    import gate
    from generate import answer_from_chunks

    items = qs.answered()
    if not items:
        print("questions.py has no questions in it yet.")
        return

    passed_count = 0
    for item in items:
        question = item["question"]
        expects = item.get("expects", "")

        results = search(question, top_k=config.TOP_K, corpus=config.CORPUS, variant="default")
        decision = gate.check(results, threshold=config.THRESHOLD)
        answer = answer_from_chunks(question, results) if decision.passed else gate.REFUSAL

        passed = judge(question, expects, answer, results)
        passed_count += passed
        print(f"{'PASS' if passed else 'FAIL'}  {question}")

    print(f"\n{passed_count} of {len(items)} passed")


if __name__ == "__main__":
    main()
