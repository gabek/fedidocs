---
id: reject
title: Reject
sidebar_label: Reject
sidebar_position: 7
tags:
  - reject
---

The `Reject` activity sends a negative response to [`Follow` activity](follow).

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox) |
| Object    | An ActivityPub Actor (IRI or inline)                               |

## Example

In this example, **bob** reject follow request from **alice**.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/reject",
  "type": "Reject",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": {
    "id": "https://lab.kbin.pub/f/object/bf3848a8-15f6-42e1-a318-2cf1637d6814/accept",
    "type": "Follow",
    "actor": "https://lab.kbin.pub/u/bob",
    "object": "https://mastodon.social/users/alice"
  }
}
```
