---
id: delete
title: Delete
sidebar_label: Delete
sidebar_position: 3
tags:
  - delete
---

The `Delete` activity removes an existing [`Note`](../objects/note) or [`Page`](../objects/page) objects.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Delete](https://www.w3.org/TR/activitypub/#delete-activity-inbox) |
| Object    | `Note` or `Page`                                                   |

## Example

In this example, **bob** remove content and sends a message to its followers.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/8076117d-58a1-4c73-b6e8-5041a68255d4",
  "type": "Delete",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": {
    "id": "https://lab.kbin.pub/m/rust/p/95110",
    "type": "Tombstone"
  },
  "to": [
    "https://lab.kbin.pub/m/rust",
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": ["https://lab.kbin.pub/u/bob/followers"]
}
```
