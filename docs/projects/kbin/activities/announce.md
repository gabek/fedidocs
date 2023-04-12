---
id: announce
title: Announce
sidebar_label: Announce
sidebar_position: 4
tags:
  - announce
---

The `Announce` activity is effectively what is known as "sharing", "reposting", or "boosting" in other social networks.
Activity is used with [`Note`](../objects/note) or [`Page`](../objects/page) objects.

| Reference |                                                                        |
|-----------|------------------------------------------------------------------------|
| Activity  | [Announce](https://www.w3.org/TR/activitypub/#announce-activity-inbox) |
| Object    | `Note` or `Page`                                                       |

## Internal logic

When Kbin receives an `Announce` activity, it is the equivalent of adding a plus to a thread or comment. Content then
moves to the top of the listings sorted by "active", and receives points that give it a higher position in the `hot`
and `top` sorting.

## Example

In this example, **bob** boost post from other instance.

```json
{
  "@context": "https://www.w3.org/ns/activitystreams",
  "id": "https://lab.kbin.pub/f/object/1cde2c49-3bfd-44d7-91c0-7ca11eaf8052",
  "type": "Announce",
  "actor": "https://lab.kbin.pub/u/bob",
  "object": "https://mastodon.social/users/alice/statuses/109748348495832857",
  "to": [
    "https://www.w3.org/ns/activitystreams#Public",
    "https://mastodon.social/users/alice"
  ],
  "cc": [],
  "published": "2023-04-12T07:06:46+00:00"
}
```
