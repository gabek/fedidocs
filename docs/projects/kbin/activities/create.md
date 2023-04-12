---
id: create
title: Create
sidebar_label: Create
sidebar_position: 1
tags:
  - create
---

The `Create` activity is used to create new [`Note`](../objects/note) or [`Page`](../objects/page) objects.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Create](https://www.w3.org/TR/activitypub/#create-activity-inbox) |
| Object    | `Note` or `Page`                                                   |

## Example

In this example, **bob** creates new content in **rust** magazine and sends a message to its followers.

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "ostatus": "http://ostatus.org#",
      "sensitive": "as:sensitive",
      "votersCount": "toot:votersCount"
    }
  ],
  "id": "https://lab.kbin.pub/m/rust/p/95109",
  "type": "Create",
  "actor": "https://lab.kbin.pub/u/bob",
  "published": "2023-04-12T06:09:01+00:00",
  "to": [
    "https://lab.kbin.pub/m/rust",
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": ["https://lab.kbin.pub/u/bob/followers"],
  "object": {}
}
```
