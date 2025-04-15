---
title: "Best practices"
description: "How to work with Copiot by using diffrent prompting techniques"
category: prompts
platforms: [copilot, copilot-chat]
aliases:
  - /doc/prompts/best-practices
---

## Prompt Engineering

The concept of Natural Language Processing (NLP) involving integrating descriptions of tasks in input, to prompt the model to output the desired results.

### Basic Prompting

#### Single-Shot

One question with a clear statement what to do
Give me a summary of this website: <www.xyz.com>

Unclear question:
2. Generate a formular for calculating prime numbers
Missing information about the implementation, like Python code, for example

#### Few-/Multi-Shot

- Refine with examples with a simple UX

#### Chain of Thought

Is the process of breaking down a complex topic in multiple, smaller steps and asking the AI to refine its responses
It instructs the AI to articulate its reasoning step by step before delivering a response.
Explicitly structure the prompts to mirror expert thought processes, breaking down complex tasks for better performance.
For example, first prompt the AI to output numerous ideas and then asked it to refine and narrow down those ideas, explaining its reasoning at each step.

#### Purposeful Elicitation/Survey

Involves directing the AI to ask the user questions.
This technique has significant user experience implications:

1. It makes for a longer conversation, which can improve output. In some cases, direct the AI to ask the developer open-ended questions so that what might have been a short interaction turns into a longer conversation allowing the participant to guide output, provide more context, or redirect the conversation.
2. It helps the AI gather context.
3. It can create deliberate opportunities for developer input. Creating deliberate pause points in which the AI cannot proceed without gathering information from the developer provides an opportunity to add their judgment or expertise to the conversation

#### Personas & Role-Play

Personas involve assigning the AI a professional role (“you are an innovation specialist”) to provide context and shape how it analyzes problems and structures responses.
Role-Play extends beyI. ond persona to create interactive and dialogue-based simulations. The AI actively embodies a character (such as a simulated customer) and responds to questions, adapting its response based on the interaction.
It can do so realistically, even with just a prompt.
The AI’s ability to role-play creates a low-stakes environment for testing ideas, exploring perspectives, and following up on interesting responses that would be costly and hard to scale with real users.

#### Constrains

Constraints in prompts can serve as guardrails that keep the AI on track. These are not merely limitations but directives that help the AI achieve its goal.
We add constraints to  prompts to ensure consistency, draw out participant expertise, and to allow for natural dialogue.
For instance, we instruct the AI not to “provide a solution” in the framing prompt so that participants can spend time analyzing options; we instruct the AI to only ask “one question at a time” to allow a more natural flow to the conversation, and we instruct the AI to “Wait for the team to respond. Do not move on until the team responds” in the role-play prompt so that participants and not the AI pick a specific persona to interview.
Collectively, constraints can create more productive interactions, elicit participant expertise, and prevent the AI from defaulting to providing immediate solutions.

#### Specific Prompts

##### Ideation

Based on well-known ideation principles including generating many ideas before evaluation, using constraints to focus the problem space, and the integration of different perspectives. The prompts begin with explicit instructions for developers to share their problem statement, followed by a structured ideation using step-by-step prompting.
The prompt instructs the AI to generate many ideas and then evaluate these and modify and finally to develop each into a detailed concept.
Developers can see the ideas being developed, observe evaluations, and intervene or redirect at any point.

##### Framing

Built on problem-framing techniques that allow developers to view challenges from multiple perspectives.
The Alternative Structuring of the Problem prompt establishes a persona (an innovation specialist) who guides developers through the process but whose role is constrained (analyze, but do not provide a solution).
Using a few-shot approach provide examples of different frameworks without constraining the possible perspectives. The prompt should be explicitly structured to create a collaborative analysis process, beginning with an introduction, an explanation of the value of reframing, and an offer to help developers view the problem from multiple perspectives.

##### Simulated Interview

For interviews, combining traditional research in the form of a participant interview with the AI’s capacity to role-play different personas simultaneously and quickly create numerous opportunities for simulated interviews.
This structured prompt moves through distinct phases: persona creation, question development, interview, and post-interview analysis.
The prompt establishes the AI as both a psychologist (facilitator or guide) and a developer (interviewee) with clear rules about role adherence.
Creating a deliberate pause points requiring developers input and turn-taking and instruct the AI to encourage iteration (“do this several times with different participants”) and reflection.

## Copilot Prompt Examples

### Single-shot

- Give me an idication what this #gitHubrepo [Copilot-how-to](https://github.com/ralphke/Copilot-HowTo) is all about.

### Few/multi-shot

Which are the most relevant topics I need to learn when working with GitHub Copilot?

1. What keyboard shortcuts to use?
2. When to use chat vs inline prompting
3. What are potential bottlenecks?

Keep your answer short but relevant for the current context

### Chain-of-Thought prompt 1

Please provide at least 5 alternative ways to solve the following code issue.
Make sure to explain why you are choosing which solution
Provide a summary which of the proposed solutions might be the best for this issue

Developing a frontend application for order taking which can run on multiple devices

- Smartphones with  Android OS like Samsung S24, S24+
- Smartphones by Apple like iPhone 4s and iPhone 7x
- Laptop and Tablets with Windows 10 and 11 OS

The order taking process should be very easy for the user to accomplish
The application should be written in C# and dotnet core for optimal portability of the code
The database to store the data being processed should be a Microsoft SQL-Server.
A database schema for the given application would be helpful

#### Chain-of-Thought prompt 2

Would your solution be the same if online and offline capabilities are required?

#### Chain-of-Thought prompt 3

When considering .NET MAUI, what kind of database should be used?
Is the provided SQL-Server schema sufficient all aspects of such an app?

### Purposeful Elicitation/Survey

What other topics might be relevant in the context of developing this application?

- lets consider the paltform is .NET core aith C# as programming language
- MAUI is the UX library of choice
- SQLLite and SQL Server for rempte stoage will be used.

### Personas & Role-Play

Consider you are Joe, a professional frontend developer with over 10 years of experience in building responsive and user-friendly applications, who can solve multiple complex problems easily.
Your co-worker Bill is a backend specialist for Microsoft SQL-Server.

- **Joe's Responsibilities:**
  - Design and implement the frontend using .NET MAUI for a responsive and user-friendly interface.
  - Ensure cross-platform compatibility for smartphones, tablets, and laptops.
  - Collaborate with Bill to integrate frontend with backend APIs.

- **Bill's Responsibilities:**
  - Design and manage the database schema using Microsoft SQL-Server.
  - Develop and optimize backend APIs for seamless data exchange.
  - Ensure data security and scalability of the backend.

How would you structure the project for optimal collaboration and minimal conflicts?s?

### Constrains

Let's focus on the following tools and components:

- as Version Control system we want to use our on-prem GitHub system
- Docker will be our container system
- For collaboration we want to use Microsoft Teams and Azure DevOps
- The Testing should be basedfacilitated by NUnit
- Microsoft Sync framework should not be used due to recent security vulnerabilities detected

### Simulated Interview Prompt

What questions should be asked from Joe and Bill before even considering the start of the project?
Please create a conversation guideline in an interview style wbere Bill and Joe exchange their thougts.

### Ideation

Please create at least 10 relevant questions from a potential customer of the aplication?
Do it step by step and explain why this might be relevant for each person.

### Five Vectors

what addtional features might be useful for this application?
Consider these vectors:

1. uniqunes and value of the solution
2. superior code quality
3. great scalability
4. exceptionel performance
5. minimal maintenenace and operation efforts

### Constrained Ideation

Pick 4 random numbers between 1 and 11.
Then, for each number, look at the appropriate lines on the list below and use the constraint you find for that number to generate an additional 3 ideas that solve the question but adhere to the constraints.
Take the constraint literally. List:
Must use C# as programming language
Must be affordable
Must consist of OSS components onyl
Must be very complicatedeasy to maintain
Must be usable by an child
Must be usable by a blind
Must be have voice as interface
Must appeal to the CIO
Must be scarynot more that 500 lines per module
Must be related to the movie Starwars
Must be made by less that three developers

### Selection

Read all the ideas so far.
Select the ten ideas that combine feasibility, uniqueness, and the ability to drive a competitive advantage for the company the most and present a chart showing the ideas and how they rank.
For each idea in the chart, describe the main features and functionalities of the proposed solution and how we might drive category growth (i.e., # of users, usage occasions, premiumization).
