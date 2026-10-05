# The Unofficial Guide

Uyen Doan

Corpus: City Guides

---

# Unit 1

## What This Does

This is a question-answering system built on a corpus of city and town guides for one region — Brightwater, Halden Bay, Kestrelford, Corry Vale, Pellew Sands, and a handful of others — plus cross-cutting guides on eating, walking, seasons, transport, and accessibility. It answers specific, factual questions about the region: what to see somewhere in a given amount of time, where and what to eat, when to visit, and which places are hard to get around. Questions outside that scope, like general trivia unrelated to the region, are refused instead of guessed at.

## Chunking Strategy

**Chunk size:** 100

**Overlap:** 20

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — `source`: guide_accessibility.md#0  |  `produced by`: chunker.py::split_documents

```
An honest assessment rather than a promotional one. Some of these places are difficult and it is better to know in advance.
```

**Chunk 2** — `source`: guide_corry_vale.md#5  |  `produced by`: chunker.py::split_documents

```
Corry Vale Where to stay

Perhaps thirty beds in the entire valley, spread across two pubs and a handful of farmhouse rooms. In summer these are booked months ahead. Camping is permitted on two marked fields and nowhere else.
```

**Chunk 3** — `source`: guide_givens_mill.md#2  |  `produced by`: chunker.py::split_documents

```
Kestrelford What to see

The market square on a Saturday morning is the main event and has run continuously since the 1400s. The parish church has a 13th-century tower you can climb for £2. The old trackbed walk runs six miles to the next village along an easy gradient and is the best half-day here.
```

**Chunk 4** — `source`: guide_kestrelford.md#4  |  `produced by`: chunker.py::split_documents

```
Kestrelford What to see

The market square on a Saturday morning is the main event and has run continuously since the 1400s. The parish church has a 13th-century tower you can climb for £2. The old trackbed walk runs six miles to the next village along an easy gradient and is the best half-day here.
```

**Chunk 5** — `source`: guide_pellew_sands.md#6  |  `produced by`: chunker.py::split_documents

```
Pellew Sands When to go

June and September for the beach without the crowds. July and August are busy and the town is at its most itself, for better and worse. Winter is bleak, largely closed, and has a following among people who like that sort of thing.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question:** 

What to see under 2 hours in Brightwater?

**Answer:**

```
Based on the provided documents (`guide_brightwater.md`), the sights that take under two hours to see are:

* **The mill museum:** This takes about 90 minutes.
* **The 14th-century cathedral:** This takes about 20 minutes. 

*(Note: The river walk runs four miles upstream, but a specific time duration is not listed for it.)*

Sources retrieved: guide_brightwater.md
```

**My relevance cutoff:**

THRESHOLD = 0.6. The five in-corpus questions came back with distances between 0.3350 and 0.6042; the five OUT_OF_SCOPE questions came back between 0.8110 and 0.9991. That's a clear gap from about 0.60 to 0.81, and 0.6 sits right at its near edge — close enough that one in-corpus question ("Where in the region has difficult accessibility?", 0.6042) lands just barely on the wrong side of it. A cutoff nearer the middle of the gap, around 0.65–0.7, would keep that question in-scope while still refusing every OUT_OF_SCOPE question with room to spare.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
|---|---|---|
| Where can people find good cooking in this region? | Yes | 0.5999 |
| What to see under 2 hours in Brightwater? | Yes | 0.3975 |
| Where should students visit during the summer? | Yes | 0.4656 |
| What should students eat when visiting Halden Bay? | Yes | 0.3350 |
| Where in the region has difficult accessibility? | Yes | 0.6042 |
| What is the capital of Mongolia? | No | 0.8110 |
| How do I change the oil in a diesel engine? | No | 0.8797 |
| Who won the 1994 World Cup? | No | 0.9991 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8409 |
| How do I write a for loop in Rust? | No | 0.8776 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1.** I asked Claude to help guide me through the `split_documents` part since I did not know where to start. I wrote me 3 TODOs and I filled them in as I went, which are:
- Use regex to split in between \n##
- Consider whether I should keep or append the guide title and description so the system knows which context it is pulling from
- Consider any safety guards

**2.** I asked Claude to run the questions for me and compare different thresholds, top-k, and other specs so I did not have to run them manually.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 2. Every answer names a source | 5 of 5 | 4 of 5 | 5 of 5 | 5 of 5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 4. Chunk boundaries fall on sentence breaks | 4 of 5 sampled chunks | 5 of 5 | 5 of 5 | 5 of 5 | MET |
| 5. Sources point at the right guide | 4 of 5 town-specific questions | 1 of 2 | 1 of 2 | 1 of 2 | MISSED |

Criteria 1, 4, and 5 don't vary run to run — retrieval and chunking are
deterministic, so the same chunk comes back and the same source is closest
every time, regardless of what the model writes. Only criterion 2 (does the
*generated* answer name a source) can actually change between runs, and it
did: Run 1's answer to the Halden Bay eating question is a bare refusal with
no source. Criterion 5's denominator is also off — only 2 of my 5 QUESTIONS
are town-specific (Brightwater, Halden Bay), not 5, so "1 of 2" is the real
count behind that row.

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer | MET | I read the actual retrieved chunks for all 5 questions instead of trusting `scorer.py` alone — its literal substring check only catches 2 of 5 because it demands exact wording. By reading them: the cooking and summer chunks match the expected text verbatim; Brightwater's chunk has two of three facts word-for-word and the third (90 minutes at the mill) in substance, just phrased as "Allow 90 minutes"; the accessibility chunk names all three towns; and the Halden Bay chunk says the kitchens close "by 9pm," the same fact as "arrive before 9pm," just framed as a closing time. 5 of 5 clears the 4-of-5 target. |
| 2 | Every answer names a source | MISSED | Run 1's answer to "What should students eat when visiting Halden Bay?" is a bare refusal sentence with zero source citation, so that run was 4 of 5, not 5 of 5. Runs 2 and 3 were both clean. The target was *every* answer, every time, and one run dropping to 4 is a miss even though two of three runs were perfect. |
| 3 | Gate stops out-of-corpus questions | MET | 5 of 5 OUT_OF_SCOPE questions were refused, and the closest of them (0.811) still has a comfortable margin over the 0.6 cutoff. This check is deterministic — one pass, not three — so there's no run-to-run variance to second-guess. |
| 4 | Chunk boundaries fall on sentence breaks | MET | Pulled a random sample of 5 chunks from the current `split_documents` output and checked both ends of each. All 5 start right after a `##` heading and end on a sentence-final period — the rewritten chunker splits on heading boundaries instead of a fixed character count, so there's no longer a mechanism that could land mid-word. 5 of 5 clears the target comfortably. |
| 5 | Sources point at the right guide | MISSED | Only 2 of my 5 QUESTIONS are actually town-specific (Brightwater, Halden Bay) — not the 5 this criterion assumes, so "4 of 5" can't really be tested here. Of the 2 I have, Brightwater's top-cited source is correctly `guide_brightwater.md`, but Halden Bay's closest retrieved chunk (distance 0.335) comes from `guide_eating.md`, not `guide_halden_bay.md` (0.372) — the exact failure mode this criterion was written to catch. 1 of 2 misses the target no matter how thin the sample is. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

**Criterion 2 — every answer names a source (MISSED). Stage: generation.**
Retrieval and the gate both did their job here: the best chunk for "What
should students eat when visiting Halden Bay?" passed the 0.6 cutoff with
room to spare (0.335–0.372), and it says outright, "Seafood, unsurprisingly,
and it is genuinely fresh... Everything closes by 9pm." All three runs still
answered "I do not have enough information" / "no mention," and Run 1
additionally cited nothing. `GROUNDING_INSTRUCTION` says "name the document
your answer came from" and separately "if the documents don't cover the
question, say you don't have enough information" — but nothing tells the
model to cite a source on the *refusal* branch specifically, since "name the
document" only reads as attached to giving an actual answer. Run 1 took the
refusal literally and dropped the citation; Runs 2 and 3 appended one anyway,
inconsistently. The missing instruction is the mechanism — but it's sitting
on top of a bigger problem, below.

**Criterion 5 — sources point at the right guide (MISSED). Stage: retrieval/embedding.**
`guide_halden_bay.md`'s own "Eat and drink" chunk and `guide_eating.md`'s
"Local specifics" chunk both describe the same thing — Halden Bay's seafood
and its 9pm closing time — because `guide_eating.md` was written to call out
each town by name. The embedding model scores the cross-cutting
`guide_eating.md` chunk at distance 0.335, fractionally closer than Halden
Bay's own chunk at 0.372, so the "top" source for a Halden Bay question
becomes the regional eating guide. Nothing in retrieval knows that one of
these documents is Halden Bay's canonical source and the other isn't; it only
measures text similarity, and here the regional doc's wording happens to
overlap with the query slightly more.

**The pattern:** both misses come from the *same* question. `guide_eating.md`
and `guide_halden_bay.md` say almost the same thing about the same town,
close enough in embedding space that retrieval can't reliably tell them
apart — that's criterion 5's failure directly. I think it's also why
generation got shaky on this question specifically: handed two chunks that
each half-own the fact instead of one chunk that clearly owns it, the model
treated the evidence as weaker than it was and refused. One overlapping pair
of documents is driving both misses, not two unrelated problems.

Worth saying plainly: criterion 2's "4 of 5" flatters this. Runs 2 and 3
technically pass it — a source got named — but the answer in all three runs
is still wrong: it says there's no information about Halden Bay eating when
the retrieved chunk states it outright. Criterion 2 only checks whether a
citation exists, not whether the answer is correct, so it can't see that this
question actually failed 3 of 3 times, not 1 of 3. If I were tightening a
criterion, it's this one — "names a source" is too easy to pass while still
getting the content wrong, and criterion 1 (chunks contain the answer, 5 of
5) shows the content was always sitting right there in retrieval.

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
