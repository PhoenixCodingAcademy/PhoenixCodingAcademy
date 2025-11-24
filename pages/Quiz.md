# Overview
 
This application generates quizzes. See [Exam Report](/examreport) for statistics.

**USE CASES:** Students can use it for testing one's knowledge. Teachers might use it to evaluate a students understanding of a subject, or to give out "extra" credit to ambitious students. 

**CREATING:** Anyone can create a quiz. It is just a YAML file of one or more questions. 

**USAGE:** The generator will randomly select questions that total up to the "Max Points", where each question does not exceed the "Max difficult question" value. The answers are randomly ordered so all tests are different. All questions are multiple choices so you need to read all answers. Many questions have one answer, but you still get a list of checkboxes - not radio buttons. Every question has "None of the above" at the bottom. All questions must be answered before you can press "Grade Quiz". You can "Try Again" as many times as you want.

There is a general point system assigned to every question, but understand that a Ph.D. expert in one subject might be a beginner in another subject.
There are 8 year-old kids that are experts in Chess for instance, or piano. The point system is simple a prompt for AI to help generate questions.


The student can choose the maximum hard question

# Points

Questions are assigned to this general point system:

| Proficiency Level | Point Value | Suggested Grade-Level Band | Rationale for Progression |
| --- | --- | --- | --- |
| Beginner | 1 | Elementary (Grades 5-6) | Basic introduction to the subject; foundational concepts. |
| Beginner-Intermediate | 2 | Middle School (Grades 7-8) | Solid grasp of basics; can handle simple, multi-step problems. |
| Transitioning | 3 | High School Freshman (Grade 9) | Navigating higher-level conceptual organization and complexity. |
| Intermediate | 4 | High School Sophomore (Grade 10) | Mastery of core curriculum; comfortable with standard analysis. |
|  | 5 | Early High School Advanced | Beginning to apply concepts creatively; minor synthesis required. |
|  | 6 | Mid-High School Advanced | Consistent performance in challenging material; strong application. |
| Intermediate-Advanced | 7 | High School Junior (Grade 11) | Ready for AP/IB level introductory content; capable of independent thought. |
|  | 8 | High School Senior (Grade 12) | Proficient in complex synthesis; ready for college-level critical thinking. |
|  | 9 | Advanced High School | Demonstrated readiness for first-year college coursework (e.g., successful AP exam score). |
|  | 10 | College Freshman | Successfully navigating college-level assignments; strong foundational research skills. |
| Advanced | 11 | College Sophomore | Comfortable with subject-specific theory; deeper analytical capacity. |
|  | 12 | College Junior | Mastery of disciplinary methods; ready for advanced elective topics. |
|  | 13 | Upper-Level College | Excels in specialized coursework; capable of independent project management. |
|  | 14 | High-Level College | Demonstrates potential for original academic work or advanced problem-solving. |
|  | 15 | Entry-Level Graduate | Possesses necessary knowledge to begin specialized research or intense study. |
|  | 16 | Graduate Level I | Can critically evaluate current literature; strong contribution to discussion. |
|  | 17 | Graduate Level II | Capable of designing and executing small-scale original research projects. |
|  | 18 | Pre-Expert/Specialist | Deep, comprehensive understanding of a sub-discipline; near-professional capacity. |
|  | 19 | Near-Expert | Recognition as highly competent specialist; capable of mentoring others. |
| Expert | 20 | Graduate/Professional | World-class knowledge; capable of leading original research or defining industry best practices. |

# Reports

All tests are stored in the /reports/quizlog.yaml file as a list of objects.

Example of an object.
```yaml
- history:
  - 12:46:37 PM - Random Seed changed
  maxDifficulty: 3
  maxPoints: 3
  name: Rob Howard
  questions:
  - answers:
    - answer: false
      correct: true
      isRight: false
      selected: false
    - answer: true
      correct: true
      isRight: true
      selected: true
    - answer: None of the above
      correct: true
      isRight: false
      selected: false
    points: 1
    question: Is an orange orange?
    right: true
  - answers:
    - answer: Cat
      correct: true
      isRight: false
      selected: false
    - answer: Green
      correct: true
      isRight: true
      selected: true
    - answer: Red
      correct: true
      isRight: true
      selected: true
    - answer: Fish
      correct: false
      isRight: false
      selected: true
    - answer: Car
      correct: true
      isRight: false
      selected: false
    - answer: None of the above
      correct: true
      isRight: false
      selected: false
    points: 2
    question: Which of the following are colors?
    right: false
```

Good question! Let me explain the difference:

## `isRight` (Answer Property)
This is a **property of the answer itself** - whether the answer is inherently correct according to the question bank.

- Static, comes from the YAML file
- **Example**: For "What is 2+2?"
  - "4" has `isRight: true`
  - "5" has `isRight: false`

## `correct` (User Behavior)
This is whether the **USER correctly handled** this particular answer choice.

- Dynamic, based on user's selection
- **Logic**:
  - ✅ Answer is correct AND user selected it → `correct: true`
  - ✅ Answer is wrong AND user did NOT select it → `correct: true`
  - ❌ Answer is correct AND user did NOT select it → `correct: false` (missed it)
  - ❌ Answer is wrong AND user selected it → `correct: false` (wrong choice)

## Example:
Question: "Which are primary colors?"

- Answer: "Red" → `isRight: true`, user selected → `correct: true` ✅
- Answer: "Blue" → `isRight: true`, user didn't select → `correct: false` ❌ (missed)
- Answer: "Orange" → `isRight: false`, user didn't select → `correct: true` ✅
- Answer: "Purple" → `isRight: false`, user selected → `correct: false` ❌ (wrong)

**In summary**: `isRight` = "Is this answer objectively correct?" | `correct` = "Did the user handle this answer correctly?"


# Prompt
The following LLM prompt can be used to generate a quiz of 100 questions that can become a YAML file in this set.

```
SUBJECT = History - 20th Century (Senior High School)
CONSTRAINTS = For average high schoolers interested in the subject. Include questions pertinent to the minimal junior-level work environment or internship. 

You are an SUBJECT teacher. You wish to evaluate a new student to find out what level of knowledge the student knows about the subject so that you can recommend a course of studies.
Create 100 questions of various levels of difficulty; not esoteric or trivial questions but rather ones with market value and usefulness.
Create more questions if you think that the basic 1-point questions have not all been addressed.
Ensure that each question is not a conjunction of multiple unrelated questions. Keep them distinct. 
Example: What is Mercury and what is Pluto?
If it makes sense to ask multiple questions that are related in context, then do so.
Example: What is Haley's Comet and why is it dangerous?
But even that could be two questions: What is Haley's Comet? Why is Haley's Comet dangerous?
Still, if the context is more clear with two questions in one sentence, then do so.
Generate one or more "right" answer. There must be one but some questions might have multiple choice.
Generate 5 false answers that sound correct but truely wrong.

Consider some questions can be in the form "Which of the following are true statements?" or "Which of the following are false statements?" Then have multiple true answers mixed with false answers.

Look at the question and the answers. Determine the number of points (1 to 20) the question might be worth according to this table:

| Proficiency Level | Point Value | Suggested Grade-Level Band | Rationale for Progression |
| --- | --- | --- | --- |
| Beginner | 1 | Elementary (Grades 5-6) | Basic introduction to the subject; foundational concepts. |
| Beginner-Intermediate | 2 | Middle School (Grades 7-8) | Solid grasp of basics; can handle simple, multi-step problems. |
| Transitioning | 3 | High School Freshman (Grade 9) | Navigating higher-level conceptual organization and complexity. |
| Intermediate | 4 | High School Sophomore (Grade 10) | Mastery of core curriculum; comfortable with standard analysis. |
|  | 5 | Early High School Advanced | Beginning to apply concepts creatively; minor synthesis required. |
|  | 6 | Mid-High School Advanced | Consistent performance in challenging material; strong application. |
| Intermediate-Advanced | 7 | High School Junior (Grade 11) | Ready for AP/IB level introductory content; capable of independent thought. |
|  | 8 | High School Senior (Grade 12) | Proficient in complex synthesis; ready for college-level critical thinking. |
|  | 9 | Advanced High School | Demonstrated readiness for first-year college coursework (e.g., successful AP exam score). |
|  | 10 | College Freshman | Successfully navigating college-level assignments; strong foundational research skills. |
| Advanced | 11 | College Sophomore | Comfortable with subject-specific theory; deeper analytical capacity. |
|  | 12 | College Junior | Mastery of disciplinary methods; ready for advanced elective topics. |
|  | 13 | Upper-Level College | Excels in specialized coursework; capable of independent project management. |
|  | 14 | High-Level College | Demonstrates potential for original academic work or advanced problem-solving. |
|  | 15 | Entry-Level Graduate | Possesses necessary knowledge to begin specialized research or intense study. |
|  | 16 | Graduate Level I | Can critically evaluate current literature; strong contribution to discussion. |
|  | 17 | Graduate Level II | Capable of designing and executing small-scale original research projects. |
|  | 18 | Pre-Expert/Specialist | Deep, comprehensive understanding of a sub-discipline; near-professional capacity. |
|  | 19 | Near-Expert | Recognition as highly competent specialist; capable of mentoring others. |
| Expert | 20 | Graduate/Professional | World-class knowledge; capable of leading original research or defining industry best practices. |


Use the following YAML template to format the output.
Ensure that strings are properly escaped if words are double-quoted inside.
Ensure that the "reason" does not reveal or provide a hint to the answer but explains why it ws chosen or exists.
Ensure that if a question or answer has a double-quote in it, that the entire string is enclosed with a single-quote, and vice versa,

questions:
- question: Which of the following are nice letters?
  reason: It is important in the industry to know which letters are nice and which one's aren't because it shows you understand the markets.
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
```


# Bruce Campbell
Let me tell you a story. When I was in High School, our computer science/physics teacher (Bruce Campbell, at Villa Park HS) did a similar thing, but he had all the questions and answers in a text file on his protected account on an [HP3000 mainframe computer](https://en.wikipedia.org/wiki/HP_3000) at Santa Ana College. Yes, I'm aging myself. We all had user accounts and could run the test-taking practice exams, where it would ask us 20 random questions, and score us at the end. Campbell said that our final physics exam would be 20 random questions from a set of 500. Everyone would get a random different test, so you should run this practice test many times to see what you know.

One question might be "Who discovered the electron? ANSWERS: (A) Albert Einstein (B) Henri Becquerel (C) J. J. Thomson (D) Wilhelm Röntgen (E) All of the above (F) None of the above.

All questions had the same (E) and (F) answers, but (A), (B), (C), and (D) would be random for all students.

As young hackers, we thought we could do better than run practice exams all day long. So one of us distracted the teacher for help with some home work problem, and while Campbell stepped away from his logged-in terminal (a [DecWriter](https://en.wikipedia.org/wiki/DECwriter)), another person dumped out the entire text file of questions (while still logged onto his account) and quickly scurried the fan-fold paper out of the lab. We then had all 500 questions printed out with the answers. So we memorized all the answers.

Come test day, all the students got perfect answers on the test. And here's what Campbell said the next day.

> This is the best day of my life! Everyone got an "A+" on this final exam. I feel like I'm the best Physics teacher of all time. Those tests were random so I know there was no cheating; copying your neighbors answers [*students are secretly snickering and winking to each other*]. Forgive me kids, I'm all choked up. Let me have a minute [*more students snickering*]. I let you all believe that you pulled a fast one on me. Do you really think that I would ever leave my terminal unlocked and walk away from it accidentally? I remember hearing the Decwriter printing in the background while I was helping that decoy student. But I just pretended not to notice. I got the entire class to memorize all 500 answers to great physics questions, like "What year did Max Plank win the Nobel Prize in Physics?" If I had printed out those questions and given them to you last week, I would have seen worse grades. But if you think you're pulling a fast one on me, then you'll study! I am definitely the best High School teacher ever!

Well, let's just say that the snickering stopped and was instantly replaced with awesome respect.

This strategy of making the test answers available to everyone up front is honoring the spirit of Bruce Campbell.
