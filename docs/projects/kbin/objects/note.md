---
id: note
title: Note
sidebar_label: Note
sidebar_position: 2
tags:
  - note
---

The `Note` is an object used to create comments, and posts in the microblog section.

## Properties

| Property         | Data type                                                                   | Description |
| ---------------- | --------------------------------------------------------------------------- |-------------|
| `type`\*         | String                                                                      | Note        |

## Example

Post:
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
  "id": "https://lab.kbin.pub/m/random/p/491",
  "type": "Note",
  "attributedTo": "https://lab.kbin.pub/u/eee",
  "inReplyTo": null,
  "to": [
    "https://lab.kbin.pub/m/random",
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": [
    "https://lab.kbin.pub/u/eee/followers"
  ],
  "sensitive": false,
  "content": "<p>Hello word</p>\n",
  "mediaType": "text/html",
  "url": "https://lab.kbin.pub/m/random/p/491",
  "tag": [],
  "commentsEnabled": true,
  "published": "2022-12-23T18:36:41+00:00"
}
```

Comment:
```json
{
  "type": "Note",
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1"
  ],
  "id": "https://lab.kbin.pub/m/fediverse/t/2917/-/comment/3567",
  "attributedTo": "https://lab.kbin.pub/u/eee",
  "inReplyTo": "https://lab.kbin.pub/m/fediverse/t/2917",
  "to": [
    "https://www.w3.org/ns/activitystreams#Public",
    "https://lab.kbin.pub/u/eee"
  ],
  "cc": [
    "https://lab.kbin.pub/m/fediverse",
    "https://lab.kbin.pub/u/eee/followers"
  ],
  "content": "<p>Lorem ipsum</p>\n",
  "mediaType": "text/html",
  "url": "https://lab.kbin.pub/m/fediverse/t/2917/-/comment/3567",
  "tag": [
    {
      "type": "Hashtag",
      "href": "https://lab.kbin.pub/tag/fediverse",
      "tag": "#fediverse"
    }
  ],
  "published": "2023-04-12T08:25:04+00:00"
}
```