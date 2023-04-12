---
id: update
title: Update
sidebar_label: Update
sidebar_position: 2
tags:
  - update
---

The `Update` activity is used to edit existing [`Note`](../objects/note) or [`Page`](../objects/page) objects.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Update](https://www.w3.org/TR/activitypub/#update-activity-inbox) |
| Object    | `Note` or `Page`                                                   |

## Example

In this example, **bob** edit content and sends a message to its followers.

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
  "id": "https://lab.kbin.pub/f/object/15d1b2c2-50e0-4cd8-801c-6cedb405360c",
  "type": "Update",
  "actor": "https://lab.kbin.pub/u/bob",
  "published": "2023-04-12T06:10:40+00:00",
  "to": [
    "https://lab.kbin.pub/m/rust",
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": ["https://lab.kbin.pub/u/bob/followers"],
  "object": {}
}
```
