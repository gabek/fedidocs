---
id: follow
title: Follow
sidebar_label: Follow
sidebar_position: 6
tags:
  - follow
---

A `Follow` enables actors to access and retrieve content from other actors as soon as it updates. Activity is used with [`Person`](../objects/person) or [`Group`](../objects/group) objects.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox) |
| Object    | `Person` or `Group`                                                |
| ID        | A unique Follow request IRI                                        |

## Example

In this example, **bob** follow **alice**.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814",
  "type": "Follow",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": "https://mastodon.social/users/alice"
}
```
