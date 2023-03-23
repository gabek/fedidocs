---
id: create
title: Create
sidebar_label: Create
sidebar_position: 1
tags:
  - create
---

The `Create` activity is used to create new [`Audio` objects](../objects/audio).

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Create](https://www.w3.org/TR/activitypub/#create-activity-inbox) |
| Object    | A Funkwhale `Audio` object                                         |

## Internal logic

When Funkwhale receives a `Create` activity with an [`Audio` object](../objects/audio), it persists a local upload in the database. It then associates the upload to related library and track information. If no track matches the audio metadata, Funkwhale creates on using the `metadata` attribute in the object.

Funkwhale ensures the activity actor and library owner are the same before handling the activity. If the associated library has no local followers, Funkwhale discards the activity.

## Example

In this example, **Bob** creates new content in his library and sends a message to its followers.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {}
  ],
  "to": [
    "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6/followers"
  ],
  "type": "Create",
  "actor": "https://awesome.music/federation/actors/Bob",
  "object": {}
}
```
