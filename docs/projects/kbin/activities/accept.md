---
id: accept
title: Accept
sidebar_label: Accept
sidebar_position: 7
tags:
  - accept
---

The `Accept` activity sends a positive response, such as confirming a [`Follow` activity](follow).

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox) |
| Object    | An ActivityPub Actor (IRI or inline)                               |

## Example

In this example, **bob** accept follow **alice**.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/accept",
  "type": "Accept",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": {
    "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/accept",
    "type": "Follow",
    "actor": "https://lab.kbin.pub/u/bob",
    "object": "https://mastodon.social/users/alice"
  }
}
```
