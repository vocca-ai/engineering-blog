---
title: "Agents reason about what exists, which is why we hire for taste, agency and seniority"
slug: what-the-context-cannot-hold
summary: "An agent solves problems inside its context, and its context only ever contains the present, so the reasons behind past decisions and the shape of what does not exist yet stay out of reach, which is exactly the work we hire people to do."
team: Product
author: hugo-danet
date: 2026-11-04
cover: images/what-the-context-cannot-hold/cover.png
cover_alt: "Diagram of a context window holding what exists, with the past and the future outside it"
featured: false
status: published
---

Every agent harness, however elaborate, works the same way underneath, since it gathers files, tickets, logs and instructions into a context window and then reasons over what it has gathered, which makes it remarkably good at anything whose answer can be found in material that already exists and structurally weak at anything whose answer lies in material that was never written down or does not exist yet.

That limit matters little while agents execute, because execution is mostly a question of applying what is already known to a new case, but it becomes the central question once agents are asked to plan, to prioritize or to direct other agents, which is where most of the industry is now heading.

## The past that left no trace

Code records what was decided and almost never why, so the retry that looks redundant, the timeout that looks arbitrary and the feature that was built and then removed after a customer pilot all appear in the context either as unexplained details or not at all, and the attempts that were abandoned, which carry most of what a team has learned, leave no trace in the repository whatsoever.

A recent study measured this directly by giving coding agents tasks whose instructions conflicted with the conventions already present in a repository, and found that agents followed nearby existing code far more reliably than either their own defaults or the new intent, to the point that when all existing code contradicted the requested direction and nothing else was provided, none of sixty attempts succeeded, while a single written rule stating the intended priority brought success to fifty-nine out of sixty ([Precedent or Intent?](https://arxiv.org/html/2610.38244)), which means that the existing code prevails over any new intention that has not been stated explicitly somewhere the agent will read it.

## The future that has no trace yet

The opposite limit is less discussed and probably more important, since a product direction that nobody has formulated cannot be retrieved from any document, and an agent asked where a product should go next will reconstruct a direction from what the context contains, meaning the current features, the open tickets and the most frequent requests, which produces a careful extension of the present rather than a decision about the future.

Research on creative tasks points the same way, finding that models produce ideas that are individually competent but collectively far more similar to each other than human ideas, both within one model and across models from different labs ([PNAS Nexus, via TechXplore](https://techxplore.com/news/2026-03-llms-creativity-ai-responses-variety.html), [Are LLMs becoming similarly creative?](https://arxiv.org/pdf/2608.19437)), and work on teams of agents shows that they can deliver correct designs while exploring only a small part of the space of possible designs, with the injected context narrowing that exploration further ([When Context Hurts](https://arxiv.org/pdf/2605.04361)).

## Why agents directing agents drift towards the incremental

Put these two limits together and an organization in which agents plan the work of other agents converges, quite naturally, on a slightly better version of what it already does, because every step reasons from precedent and every proposal stays close to the most probable continuation of the present, which is a reasonable outcome for maintenance and a poor one for a company whose reason to exist is to build something that was not there before.

![Diagram of agents directing agents advancing in small steps along what exists, while a single chosen direction leaps far above](images/what-the-context-cannot-hold/drift.png)

Nothing about this is a failure of the models, and larger context windows do not change it, since the missing material is not too long to fit but simply absent, so the question for a team is not whether to rely on agents, which we do for most of our implementation, but who brings what the context cannot hold.

## Taste brings the future

Taste, in the sense we use when hiring, is the ability to recognize that something is good before there is any precedent proving it, and to reject something that is consistent with everything around it but does not deserve to exist, which is precisely the judgment an agent cannot borrow from its context because the reference it would need has not been built yet. Someone with taste looks at a technically correct proposal that extends the current product in the most obvious way and can explain why the customer would be better served by a different product altogether.

## Agency acts on what nobody asked for

An agent acts on the task it was given, while most of the decisions that change a company are ones nobody assigned, such as noticing that a process everyone works around should not exist, that a customer request hides a more general problem, or that a direction the team agreed on months ago no longer holds, so we look for people who take those decisions without waiting for permission and who then write them down as explicit rules, since a written rule is what lets an intention override the precedent agents would otherwise follow.

## Seniority carries the past

We value seniority for the memory it carries rather than for the technical depth it once implied, because knowledge of a framework is now available on demand to anyone who knows what to ask, whereas the memory of why a migration that looked routine turned out to be irreversible, or of why a shortcut failed in production at another company, exists only in the people who lived through it, and it is what lets someone stop an agent that is about to remove a fence whose purpose nobody wrote down.

## How we work with this

In practice we ask every decision of consequence to carry its reason next to it, so that the next person or agent reading it inherits the why and not only the what, we state product intentions as explicit rules in the instructions our agents read rather than hoping they will be inferred from examples, and we keep the work of setting direction with people while agents take on a growing share of the execution, which makes the quality of that direction the main thing a team like ours is judged on.

We are hiring product engineers and product managers who bring taste, agency and the memory of their own past decisions to problems where the stakes are real, through [our careers page](https://www.vocca.com/careers).
