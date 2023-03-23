---
id: undo
title: Undo
sidebar_label: Undo
sidebar_position: 4
tags:
  - undo
---

The `Undo` activity reverses a referenced [`Follow`](follow) activity.

| Reference |                                                                |
| --------- | -------------------------------------------------------------- |
| Activity  | [Undo](https://www.w3.org/TR/activitypub/#undo-activity-inbox) |
| Object    | A `Follow` activity                                            |

## Internal logic

When Funkwhale receives an `Undo` activity, it deletes the corresponding [`Follow`](follow) from the database.

## Example

In this example, **Alice** notifies **Bob** that she's undoing her follow.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {}
  ],
  "type": "Undo",
  "id": "https://music.rocks/federation/actors/Alice#follows/99fc40d7-9bc8-4c4a-add1-f637339e1ded/accept",
  "to": ["https://awesome.music/federation/actors/Bob"],
  "actor": "https://music.rocks/federation/actors/Alice",
  "object": {
    "id": "https://music.rocks/federation/actors/Alice#follows/99fc40d7-9bc8-4c4a-add1-f637339e1ded",
    "type": "Follow",
    "actor": "https://music.rocks/federation/actors/Alice",
    "object": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6"
  }
}
```
