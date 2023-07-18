---
id: follow
title: Follow
sidebar_label: Follow
sidebar_position: 4
tags:
  - follow
---

## Follow

The `Follow` activity enables actors to access and retrieve content from other actors as soon as it updates.

### Request

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox) |
| Object    | Communecter object or ActivityPub actor                           |
| ID        | A unique Follow request IRI                                        |

### Internal Logic

When Communecter receives a follow activity on an object, it performs the following actions:

- Sends a notification to the followed actor.
- The followed actor can choose to accept or ignore the follow request.
- If the request is accepted, the follower will receive updates from the followed actor in their activity feed.

### Example

In this example, **Alice** sends a follow activity to follow **Bob** on Communecter:

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "type": "Follow",
  "object": "https://communecter.org/api/activitypub/users/u/Bob",
  "id": "https://communecter.org/api/activitypub/activity/id/Follow123",
  "actor": "https://communecter.org/api/activitypub/users/u/oceatoon"
}
