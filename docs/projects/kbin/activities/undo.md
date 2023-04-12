---
id: undo
title: Undo
sidebar_label: Undo
sidebar_position: 9
tags:
  - undo
---

When Kbin receives an Undo activity, it deletes the corresponding object from the database. Activity is used
with [`Follow`](./follow) or [`Like`](./like) objects.

| Reference |                                                                |
|-----------|----------------------------------------------------------------|
| Activity  | [Undo](https://www.w3.org/TR/activitypub/#undo-activity-inbox) |
| Object    | `Follow` or `Like`                                             |

## Example

In this example, **bob** undo follow **alice**.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/accept",
  "type": "Undo",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": {
    "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/accept",
    "type": "Follow",
    "actor": "https://lab.kbin.pub/u/bob",
    "object": "https://mastodon.social/users/alice"
  }
}
```
