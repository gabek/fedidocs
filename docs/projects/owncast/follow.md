---
id: follow
title: Follow Requests
sidebar_position: 1
sidebar_label: Follow
tags:
  - Follow
---

Owncast accepts inbound Follow requests from other ActivityPub Actors. When a Follow request is received Owncast will add the Actor to the list of Followers for the Owncast instance and display it in chat.

## Request

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox) |
| Object    | An ActivityPub Actor (IRI or inline)                               |
| ID        | A unique Follow request IRI                                        |


### Example expected inbound Follow request

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://example.com/activities/123",
  "type": "Follow",
  "actor": "https://example.com/users/123",
  "object": "https://example.com/users/456"
}
```

## Accept

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox) |
| Object    | An ActivityPub Actor (IRI or inline)                               |
| ID        | The initial Follow activity request ID                             |

### Example expected inbound Follow accept

```json
Example TODO
```
