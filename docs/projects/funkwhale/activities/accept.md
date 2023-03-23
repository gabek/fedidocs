---
id: accept
title: Accept
sidebar_label: Accept
sidebar_position: 3
tags:
  - accept
---

The `Accept` activity sends a positive response, such as confirming a [`Follow` activity](follow).

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox) |
| Object    | An ActivityPub Actor (IRI or inline)                               |
| ID        | The initial Follow activity request ID                             |

## Internal logic

When Funkwhale receives an `Accept` activity related to a [`Follow`](follow) activity, it marks the `Follow` as accepted in the database. If the `Follow` activity relates to a [`Library` object](../objects/library), the requester receives future activities associated with the library. This includes [`Create`](create) and [`Delete`](delete) activities as well as  [`Audio` objects](../objects/audio). They can also browse and download the library's audio files.

## Example

In this example, **Bob** accepts a follow request from **Alice**.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {}
  ],
  "type": "Accept",
  "id": "https://music.rocks/federation/actors/Alice#follows/99fc40d7-9bc8-4c4a-add1-f637339e1ded/accept",
  "to": ["https://music.rocks/federation/actors/Alice"],
  "actor": "https://awesome.music/federation/actors/Bob",
  "object": {
    "id": "https://music.rocks/federation/actors/Alice#follows/99fc40d7-9bc8-4c4a-add1-f637339e1ded",
    "type": "Follow",
    "actor": "https://music.rocks/federation/actors/Alice",
    "object": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6"
  }
}
```
