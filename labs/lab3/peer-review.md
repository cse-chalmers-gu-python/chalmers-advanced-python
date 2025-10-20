# Peer-review guidelines for Lab 3

## Overview

For Lab 3, each group of students (hereinafter the _submitting group_) is expected to submit their solution to another group (hereinafter the _reviewing group_), which will have to assess whether the submission passes or fails.
The reviewing groups will be **selected by the teaching team** in order to reduce conflicts of interest.
The selections will be published directly after the first deadline for Lab 3.
The review process is not blind, i.e. the identities of the submitting and reviewing groups are known to each other.

## Assessment

Each reviewing group have to assess whether the submitted solution is acceptable or not as follows:

1. The submitting group should demonstrate their application running on their own machines during a live presentation (physical or online) to the reviewing group.
  (the reviewing group is not expected to run the code of the submitting group).
  From this presentation, the reviewing group can evaluate the **core functionality** of the application (see [Section 1](#section-1-core-functionality) below).
2. The reviewing group must also be given access to the submitting group's repository in order to see their code. From this they can evaluate the **code quality** of the project (see [Section 2](#section-2-code-quality) below)

## Report

The reviewing group must write a short report giving their assessment and motivating their decision according to the given criteria.

The report must been submitted as an **issue** opened on the submitting group's repository.
The name of the issue must clearly state the group number of the reviewing group.

The template for the report/issue is found below.
Note that all Sections are **mandatory** in the report.

---

### Section 1: Core functionality

1. Does the application run? (yes/no)
2. Does the application display the complete map of tram lines? (yes/no)
3. Is it possible to query shortest path between any two points? (yes/no)
4. Does the application deal with changes correctly? (yes/no)
5. Does the application show current traffic information? (yes/no)

### Section 2: Code quality

Make comments on the overall code quality of the submission, including whether:

1. code from lab 2 has been properly reused (i.e. in an efficient way without [boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code))
2. the `dijkstra()` function has been implemented and used as intended: there is just
  one definition of the function itself, and different distances are
  obtained by just changing the cost function

You may add any other comments about code quality you wish,
for example suggestions for code optimization and good practices of Object Oriented Programming.

<!--
JOHN: They have to run the code in order to produce screenshots!
### Section 3: Screenshots

Insert two screenshots:

- screenshot 1 must present the web application displaying a shortest path between two stops (similar to the one presented in the assignement [here](https://htmlpreview.github.io/?https://github.com/aarneranta/chalmers-advanced-python/blob/main/labs/lab3/examples/show_route.html) but with **different tram stops** than in the example)
- screenshot 2 must present the code of the function `show_shortest()` (the main function required in the core part of the assignment, see [here](https://github.com/aarneranta/chalmers-advanced-python/blob/main/labs/lab3/lab3.md#your-todo-continue-from-here)).
-->

---

## Deadlines

### Code

The deadline for the submission of your code is the end of study week 6, but you can submit beforehand.

### Report, demonstration, and self-registration

Demonstrations for reviewers are carried out in study week 7.
You can use any of the regular lab times and rooms scheduled for this course.
You can also agree to do your peer review remotely.

After the reviews, the reports are to be submitted on GitHub classroom, in the same repository as the lab3 solution itself. **You must submit both reports: the one you wrote about the other group, and the one they wrote about you**. This is of course redundant, but it will make the TAs' work much easier, because they only have to look at one repository to see both reports.

### Resubmission

A TA is ultimately responsible for the evalidation of the submission, and also has the responsibility to support the reviewing group in their endeavor (typically for edge cases).
Note that a solution will have to be resubmitted if it doesn't pass the peer-review process. A submitting group can apply for resubmission **once**.
The same reviewing group and TA are assigned for the resubmission.
A group reviewing a resubmission can simply add an addendum to their initial report.
The resubmission report must be written **within 1 day (24 hours)** after resubmission (as the structure should already be familiar to the reviewers).

We invite you to self-manage your resubmission on your private time, including a new demonstration.
