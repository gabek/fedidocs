---
id: follow
title: Follow
sidebar_label: Follow
sidebar_position: 1
tags:
  - follow
---

A `Follow` enables actors to access and retrieve content from other actors as soon as it updates.

## Request

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox) |
| Object    | A Funkwhale Library or ActivityPub actor                               |
| ID        | A unique Follow request IRI                                        |

## Internal logic

When Funkwhale receives a follow on a [library object](objects/library), it performs one of the following actions depending on the library's visibility:

- Automatically accept: If the library is public, Funkwhale automatically accepts the follow activity. Funkwhale sends a notification to the owner of the library and an [`Accept`](accept) activity to the actor who sent the follow
- Accept request: If the library isn't public, Funkwhale sends a notification to the library owner. If the owner approves the request, Funkwhale sends an [`Accept`](accept) activity to the actor who sent the follow

Funkwhale uses the library follow status to grant access to the actor who sent the follow request. If the library isn't public and the owner doesn't send an approval, the requesting actor can't access the library's content.

#### Example

In this example, **Alice** sends a follow activity for a [library object](objects/library) owned by **Bob**.

``` json
{
  "@context": [
      "https://www.w3.org/ns/activitystreams",
      "https://w3id.org/security/v1",
      {}
  ],
  "type": "Follow",
  "id": "https://music.rocks/federation/actors/Alice#follows/99fc40d7-9bc8-4c4a-add1-f637339e1ded",
  "actor": "https://music.rocks/federation/actors/Alice",
  "to": ["https://awesome.music/federation/actors/Bob"],
  "object": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6"
}
```
