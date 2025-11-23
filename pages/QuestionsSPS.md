<!--
DESCRIPTION: Requirements for the quiz engine.
-->
[TOC]

From the "data/questions" folder, read all YAML file names that do not begin with an underscore.
Create a dropdown list of these file names. 
Under that list create these controls:
* Name: a text box with place holder "Your full name; e.g. John Smith"
* Max Points: a numeric text box with values 1 to 200 with default 50.
* Max difficult question: a numeric text box with values 1 to 20 with default 7.
* A "Start Exam" button.

When the "Start Exam" button is pressed, read the corresponding YAML file.
It will contain many questions.
Begin with a "history" list of strings.
Randomize the questions.
Choose a number of questions that equal the Max Points, or be one question over.
At the top of the quiz:
  Print the student's name.
  Print the current date and time YYYY-MM-DD.
  Print the string "{N} questions for a total of {P} points".
  For each row in the history list, print the row.

For each question, choose randomly 5 answers (right or wrong). The set of answers can be all wrong answers.
Randomize the answers.
Print the question as H2 heading.
For each answer print one row that begins with a checkbox, the answer, and the number of points for the question in parenthesis, e.g. " (10 pts)".

Begin with the scroll bar at the top.
We will need some method to mark each answer with a unique id that when submitted can be determined by the server if the answer represents a right answer or not.
To do so, we make a string that is a hidden key constant. To that append the answer, then append "RIGHT" or "WRONG" to the string. The id is the question number, followed by a "dash", followed by the xxhash of the string, and becomes the id (or name) of the checkbox.

At the end of the quiz, create a button called "Grade Quiz", which submits the entire form of answers to endpoint "/gradeexam".





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

REQUIREMENT: Assuming that some questions were answered wrong, when the "Grade Quiz" button is pressed, highlight all questions (not the answers) in red to show that are wrong. Then change the "Grade Quiz" button to read "Try Again", and add a button "Show Answers" to the right. When the "Try Again" button is pressed, the test is re-evaluated. When the "Show Answers" button is pressed then Reveal All Answers, which means mark all incorrect answers in RED. Also show the explanation for all answers below each answer in a smaller font.
At any point, if all questions were answered correctly, then then "Reveal All Answers.

REQUIREMENT: When the "Grade Quiz", "Try Again", or "Show Answers" button is pressed, then record that event in the history list with the number of questions missed and the number of points scored. Always show the history at the top.

REQUIREMENT: The "Question set" dropdown list should have the ability to type a string to filter the list. Typing each character invokes the filter. The string filters by matching any part of the string.

REQUIREMENT: If the user changes the "Random seed" then mark that in the history as "Random Seed changed". Only add it one time if changed.

REQUIREMENT: When a quiz is graded, create or append to the file "quizlog.yaml
---

SUBJECT = History - Basic Colonial America and the Revolution
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

