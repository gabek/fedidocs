---
id: like
title: Like
sidebar_label: Like
sidebar_position: 5
tags:
  - like
---

The `Like` activity is effectively what is known as "like", "favourite". Activity is used with [`Note`](../objects/note)
or [`Page`](../objects/page) objects.

| Reference |                                                                |
|-----------|----------------------------------------------------------------|
| Activity  | [Like](https://www.w3.org/TR/activitypub/#like-activity-inbox) |
| Object    | `Note` or `Page`                                               |

## Internal logic

When Kbin receives a Like activity, it is the equivalent of adding a thread or comment to favorites. Content receives
points that give it a higher position in the "hot" sorting

## Example

In this example, **bob** add to favourites post from other instance.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/81f06acf-dcda-4960-9110-5c1241c012f4",
  "type": "Like",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": "https://mastodon.social/users/alice/statuses/109748348495832857"
}
```
