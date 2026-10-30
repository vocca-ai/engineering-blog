---
title: "Building product when building is no longer the constraint"
slug: building-when-building-is-cheap
summary: "Product management grew up around the assumption that software is expensive to produce, and now that agents have made production cheap, the work that remains is judgment, validation and attention, which changes how a product team should plan, review and decide."
team: Product
author: hugo-danet
date: 2026-10-30
cover: images/building-when-building-is-cheap/cover.png
cover_alt: "Diagram comparing the share of building and deciding before and now"
featured: true
status: draft
---

For most of its history, product management rested on a single founding premise, which is that building software is expensive and that someone therefore has to decide what gets built and in what order, and nearly every framework, ritual and best practice of the discipline, from roadmaps and prioritization matrices to sprint planning and estimation, follows from that one assumption about the cost of production.

That premise has been quietly failing for a couple of years, because coding agents now turn a prototype that used to take weeks into something a single engineer can put in front of users within days, and a team that keeps organizing itself as if production were the scarce resource ends up coordinating a process that barely needs coordinating while neglecting the parts of the work that have become the real bottleneck. This article describes how we think about product building at Vocca under that new condition, and what it changes in the way we plan, review, validate and decide.

## The constraint moved from execution to judgment

When production was expensive, adding engineers was the most direct way to ship more, and the main job of product people was to protect that capacity from being spent on the wrong things. Today a small team of engineers working with agents routinely produces more than a much larger team working the traditional way, so the limiting factor is no longer how much can be built but how well the team can tell which things deserve to be built, which of them are working once they ship, and which decisions it will not be able to take back.

This shift is easy to underestimate, because the visible signs of activity, such as pull requests, demos and prototypes, multiply very quickly once production becomes cheap, and a team can feel more productive than ever while the quality of its decisions stays exactly where it was, so the discipline we try to keep is to measure ourselves by the problems that actually went away for the people using the product rather than by the volume of things we managed to produce.

## Planning describes outcomes rather than tasks

Traditional planning breaks work into implementable pieces, such as building an authentication flow, adding retry logic or writing a set of validation tests, because those pieces used to be the expensive part and therefore the part worth coordinating. When an agent can propose an implementation in minutes, the more useful thing for a plan to contain is a precise description of what must be true once the work is done and of the failures that would be unacceptable along the way, so that the people and the agents doing the work can choose the implementation themselves and be judged against something that matters.

Writing a plan in that form turns out to be harder than writing a list of tasks, since it forces the team to agree on what success means before anything is built, but it is also the only form of plan that still holds when the cost of trying three different implementations has dropped close to zero.

## Reversible and irreversible decisions deserve different speeds

Once building becomes cheap, the only cost left that deserves careful management is the cost of what cannot be undone, which is why the judgment we value most in product people is the ability to tell a reversible decision from an irreversible one and to give each the speed it deserves. A change to the wording of a screen, a new internal tool or an experiment exposed to a small share of traffic can be rolled back in minutes and should move as fast as the team can manage, whereas a change to how data is stored, a commitment made to a customer or an action an agent takes on behalf of a practice may have consequences that no rollback will repair.

![Diagram of a reversible door crossed in both directions and an irreversible door with a gate](images/building-when-building-is-cheap/doors.png)

In a regulated domain such as healthcare the second category is larger than in most consumer software, so a large part of our product thinking goes into designing the gates that sit in front of irreversible actions, such as a verification step before an agent writes into a calendar or an explicit rule that a certain kind of request always reaches a human, while keeping everything else as light and as fast as possible.

## Validation is the new ceiling

There is a principle in systems optimization known as Amdahl's law, which says that the overall improvement obtained by speeding up one part of a system is limited by how much that part contributes to the whole, and applied to software delivery it means that making the writing of code dramatically faster only speeds up the full cycle by a modest amount when specification, review, validation and release keep taking as long as they did before.

![Diagram of a delivery pipeline where code has become narrow and validation has become the widest step](images/building-when-building-is-cheap/amdahl.png)

This is why we invested in monitoring, replay and fallback logic before we built many of our features, and why we treat the ability to validate a change at the same pace as we can produce it as the real measure of our speed. For software built on language models the problem is sharper still, because the behavior of an agent is a distribution over thousands of conversations rather than a property anyone can read in the code, so a consequential change is first checked offline against recorded conversations and then exposed to a fraction of live traffic in which its target metric has to move before it reaches everyone.

The same reasoning shapes how we evaluate reliability, since a workflow made of many steps succeeds only when every one of its steps succeeds, and an agent that is right ninety percent of the time on each step will complete a ten-step workflow correctly only about a third of the time, which leads us to evaluate complete sequences rather than isolated turns and to place verification gates inside long chains instead of trusting a good average.

![Chart of the probability that every step of a workflow succeeds, falling as the number of steps grows](images/building-when-building-is-cheap/passk.png)

## Review verifies intent, and documentation explains why

When engineers wrote every line themselves, code review spent much of its time on naming, style and the edge cases of individual functions, which made sense because those were the places where a human author was most likely to slip. With agents producing a growing share of the implementation, the more valuable questions in a review are whether the change actually solves the problem it was meant to solve, whether it quietly diverges from what the team intended, and whether it creates coordination costs that someone will have to pay later.

Documentation follows the same logic, because the code already shows how something works once an agent has written it, while the reasons behind a choice and the constraints that future changes must respect exist nowhere unless someone writes them down, which is also why we keep comments only where they capture a constraint the code cannot express, given that the next reader of a stale comment is increasingly another model that will take it at face value.

## Running our own use of AI in the open

Most companies use AI in private, in a browser tab or a personal conversation that nobody else will ever read, and we have moved a large part of ours into public channels where the agent answers in front of everyone who happens to be reading. The interesting effect is less about transparency than about product discovery, because a long private session in which someone reconciles two exports every week looks like productivity, whereas the same session held in public reveals a missing standard between two systems that the team is repairing by hand at the speed of a model.

![Diagram of a private session that stays closed and a public session that becomes product](images/building-when-building-is-cheap/public.png)

Nearly every long private session with an AI turns out to be work that has no owner yet, in the sense that it should either become part of the product, a rule or a feature that runs without anyone prompting it, or go back to the customer as something they can perfectly well do themselves, and running that work in the open is one of the most reliable sources of product ideas we have found.

## Why we hire for seniority, and what we mean by it

None of this reduces the importance of engineers or product people, but it does change what makes someone excellent at the job, since the scarce skills are now the ability to define precisely what success means, to recognize which decisions cannot be undone, to design the validation that lets a team move fast without breaking what matters, and to read a generated change for its intent rather than its syntax.

This is the main reason we look for experienced people, and it is worth being precise about what we expect that experience to bring, because it is not primarily technical depth. Knowledge of a framework, a language or a particular infrastructure used to take years to accumulate and used to separate senior engineers from everyone else, whereas today an agent can supply most of that knowledge on demand to anyone who knows what to ask, so the advantage that remains with people who have built and operated systems for a long time is the judgment that only comes from having lived with the consequences of their own decisions.

That judgment shows up in moments that rarely appear in a job description, such as sensing that a feature everyone agrees on solves the wrong problem, noticing that a migration presented as routine cannot actually be rolled back, recognizing in a generated change the kind of shortcut that worked in a demo and failed in production somewhere else, or deciding that a question deserves a week of measurement before anyone writes a line of code. People acquire that sense by having been wrong in ways that cost something, by having watched systems they designed fail at three in the morning, and by having seen which of their past certainties survived contact with real users, and none of it can be retrieved from a model the way an API reference can.

It also explains why we value the ability to step back as much as the ability to go fast, since a team in which production is nearly free can generate a great deal of motion in the wrong direction very quickly, and the person who slows down at the right moment to ask whether the work is worth doing at all often contributes more than the one who ships the most. When we interview, we therefore spend less time testing what candidates know and more time listening to how they reason about trade-offs, how they describe decisions they would make differently today, and how they tell a reversible choice from one that deserves caution.

We are hiring product engineers and product managers who want to work this way on problems where the stakes are real, and if that description sounds like the kind of team you would like to join, we would be glad to hear from you through [our careers page](https://www.vocca.com/careers).
