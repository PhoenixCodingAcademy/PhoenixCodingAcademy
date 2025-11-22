<!--
DESCRIPTION: Requirements for the quiz engine.
-->
[TOC]

* Create an exam from a list of subjects, courses, or assignments. This is resolved into a set of item ids.
* Pick a random seed number, perhaps based on the student's id and exam number.
* For each id in ids:
  * Under the `data/questions` folder find file "{id}.yaml".
  * If the file is not found: continue
  * Add all the questions to a set Q1
* Q2 = 20 random questions from Q1
* For each Q in Q2:
  * Create a list of all right and wrong answers.
  * Pick 5 random answers A
  * Print the question
  * Print each answer in A as a checkbox choice
  * Add check box "None of the above"
  * The student makes the selection
  * If any boxes checks except last one, then the last one gets unchecked.
  * At least one checkbox must be checked for the SUBMIT button to become enabled.
  * The student clicks SUBMIT.
  * If in practice mode, if any are incorrect, the page says so, and the student must try another combination.
  * If in test mode, nothing is shown.

* The exam is completed. The choices are recorded. A score is created.

---

SUBJECT = Large Language Models

You are an SUBJECT teacher. You wish to evaluate a new student to find out what level of knowledge the student knows about the subject so that you can recommend a course of studies.
Create 100 questions of various levels of difficulty.
Ensure that each question is not a conjunction of multiple unrelated questions. Keep them distinct. 
Example: What is Mercury and what is Pluto?
If it makes sense to ask multiple questions that are related in context, then do so.
Example: What is Haley's Comet and why is it dangerous?
But even that could be two questions: What is Haley's Comet? Why is Haley's Comet dangerous?
Still, if the context is more clear with two questions in one sentence, then do so.
Generate one or more "right" answer. There must be one but some questions might have multiple choice.
Generate 5 false answers that sound correct but truely wrong.

Look at the question and the answers. Determine the number of points (1 to 20) the question might be worth according to this table:
* Beginner - 1 point
* Beginner-Intermediate - 2 points
* Intermediate - 4 points
* Intermediate-Advanced - 7 points
* Advanced - 12 points
* Expert - 20 points

Use the following YAML template to format the output.

questions:
- question: Which of the following are nice letters?
  points: 12
  right:
  - answer: A
    explanation: Because I like A.
    links:
    - https://en.wikipedia.org/wiki/A
  - answer: B
    explanation: Because I like B.
  - answer: C
    explanation: Because I like C.
  - answer: D
    explanation: Because I like D.
  - answer: E
    explanation: Because I like E.
  wrong:
  - answer: F
    explanation: Because I don't like F.
  - answer: G
    explanation: Because I don't like G.
  - answer: H, I and J
    explanation: Because I don't like those letters either.
    links:
    - https://en.wikipedia.org/wiki/H
    - https://en.wikipedia.org/wiki/I
    - https://en.wikipedia.org/wiki/J

