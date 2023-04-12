---
id: mentions
title: Mentions
sidebar_position: 4
tags:
  - Mentions
---

## Example:

```json
{
  "object": {
    "id": "https://lab.kbin.pub/m/random/p/95114",
    "type": "Note",
    "attributedTo": "https://lab.kbin.pub/u/ernest",
    "inReplyTo": null,
    "to": [
      "https://lab.kbin.pub/m/random",
      "https://www.w3.org/ns/activitystreams#Public",
      "https://dev.karab.in/u/eee",
      "https://101010.pl/users/ernest"
    ],
    "cc": [
      "https://lab.kbin.pub/u/ernest/followers"
    ],
    "sensitive": false,
    "content": "<p>Mentions example <a href=\"https://dev.karab.in/u/eee\" class=\"mention u-url\" title=\"@eee@dev.karab.in\" data-action=\"mouseover-&gt;kbin#mention\" data-kbin-username-param=\"eee@dev.karab.in\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">@eee</a> <a href=\"https://101010.pl/@ernest\" class=\"mention u-url\" title=\"@ernest@101010.pl\" data-action=\"mouseover-&gt;kbin#mention\" data-kbin-username-param=\"ernest@101010.pl\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">@ernest</a></p>\n",
    "mediaType": "text/html",
    "url": "https://lab.kbin.pub/m/random/p/95114",
    "tag": [
      {
        "type": "Mention",
        "href": "https://dev.karab.in/u/eee",
        "name": "@eee@dev.karab.in"
      },
      {
        "type": "Mention",
        "href": "https://101010.pl/users/ernest",
        "name": "@ernest@101010.pl"
      }
    ],
    "commentsEnabled": true,
    "published": "2023-04-12T09:13:14+00:00"
  }
}
```
