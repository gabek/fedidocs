---
id: follow
title: Follow
sidebar_label: Follow
sidebar_position: 2
tags:
  - Follow
  - Accept
---

Mastodon sends a `Follow` activity when an actor follows an external actor. It also accepts `Follow` activities send by external instances when one of their actors follows a Mastodon actor.

When the receiving actor accepts the follow, its instance is generally expected to send an [`Accept`](#accept) in response. Mastodon will not deliver an actor's activities to a new follower until that follower has accepted the follow.

Mastodon's `Follow` activity ids aren't fetchable via HTTP with `Accept: application/activity+json` content negotiation; they return HTTP 404 `{"error":"Not Found"}`.

## Request

| Reference              |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| Activity               | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox)                |
| Object                 | An ActivityPub Actor (IRI or inline)                                                                              |
| ID        | A unique Follow request IRI                                        |
| Official documentation | [docs.joinmastodon.org](https://docs.joinmastodon.org/spec/activitypub/#supported-activities-for-profiles) |

### Example Follow request

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://example.com/fce205fc-fced-4d81-9a7d-5485eec038a3",
  "type": "Follow",
  "actor": "https://example.com/users/123",
  "object": "https://other.example/users/456"
}
```


## Accept

The `Accept` activity is used to accept another activity that was previously received, usually a `Follow`.

Mastodon's `Accept` activity ids are based on their actor's ids, distinguished with a `#` fragment, which makes them not fetchable via HTTP with `Accept: application/activity+json` content negotiation. Attempting to fetch them returns the actor's AS2 object instead. [Background in this GitHub issue.](https://github.com/mastodon/mastodon/issues/13879)

| Reference              |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| Activity               | [Accept](https://www.w3.org/TR/activitypub/#accept-activity-inbox)                |
| Object                 | [Follow](https://www.w3.org/TR/activitypub/#follow-activity-inbox)                                                                              |
| Official documentation | [docs.joinmastodon.org](https://docs.joinmastodon.org/spec/activitypub/#supported-activities-for-profiles) |

### Example Accept request

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://other.example/users/456#accepts/follows/283636",
  "type": "Accept",
  "actor": "https://other.example/users/456",
  "object": {
    "id": "https://example.com/fce205fc-fced-4d81-9a7d-5485eec038a3",
    "type": "Follow",
    "actor": "https://example.com/users/123",
    "object": "https://other.example/users/456"
  }
}
```
