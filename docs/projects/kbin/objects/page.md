---
id: page
title: Page
sidebar_label: Page
sidebar_position: 1
tags:
  - page
---

The `Page` is an object used for add more relevant links and articles displayed on the homepage of the platform.

## Properties

| Property | Data type | Description |
|----------|-----------|-------------|
| `type`\* | String    | Page        |

## Example

```bash
curl -H "Accept: application/activity+json, application/ld+json" https://dev.karab.in/m/fediverse/t/2917
```

```
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
  "id": "https://lab.kbin.pub/m/fediverse/t/2917",
  "type": "Page",
  "attributedTo": "https://lab.kbin.pub/u/eee",
  "inReplyTo": null,
  "to": [
    "https://lab.kbin.pub/m/fediverse",
    "https://www.w3.org/ns/activitystreams#Public"
  ],
  "cc": [
    "https://lab.kbin.pub/u/eee/followers"
  ],
  "name": "Fediverse Developer Network",
  "content": "<p>A community for developers building the existing projects that make up the Fediverse.</p>\n",
  "summary": "A community for developers building the existing projects that make up the Fediverse. #fediverse",
  "mediaType": "text/html",
  "url": "https://fedidevs.org/",
  "tag": [
    {
      "type": "Hashtag",
      "href": "https://lab.kbin.pub/tag/fediverse",
      "tag": "#fediverse"
    }
  ],
  "commentsEnabled": true,
  "sensitive": false,
  "stickied": false,
  "published": "2023-04-11T18:58:03+00:00",
  "attachment": [],
  "source": "https://fedidevs.org/"
}
```