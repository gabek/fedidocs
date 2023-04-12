---
id: hashtags
title: Hashtags
sidebar_position: 3
tags:
  - Hashtags
---

## Example:

```json
{
  "object": {
    "id": "https://app.localhost/m/random/p/95113",
    "type": "Note",
    "attributedTo": "https://app.localhost/u/ernest",
    "inReplyTo": null,
    "to": [
      "https://app.localhost/m/random",
      "https://www.w3.org/ns/activitystreams#Public"
    ],
    "cc": [
      "https://app.localhost/u/ernest/followers"
    ],
    "sensitive": false,
    "content": "<p>Tag example usage <a href=\"https://app.localhost/tag/test\" class=\"hashtag tag\" rel=\"tag\">#test</a> <a href=\"https://app.localhost/tag/fediverse\" class=\"hashtag tag\" rel=\"tag\">#fediverse</a></p>\n",
    "mediaType": "text/html",
    "url": "https://app.localhost/m/random/p/95113",
    "tag": [
      {
        "type": "Hashtag",
        "href": "https://app.localhost/tag/test",
        "tag": "#test"
      },
      {
        "type": "Hashtag",
        "href": "https://app.localhost/tag/fediverse",
        "tag": "#fediverse"
      }
    ],
    "commentsEnabled": true,
    "published": "2023-04-12T09:09:39+00:00"
  }
}
```
