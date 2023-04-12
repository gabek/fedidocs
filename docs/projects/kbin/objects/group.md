---
id: group
title: Group
sidebar_label: Group
sidebar_position: 4
tags:
  - group
---

The `Group` is an object that represents an individual magazine / community.

## Properties

| Property | Data type | Description |
|----------|-----------|-------------|
| `type`\* | String    | Group       |

## Example

```json
{
  "type": "Group",
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1"
  ],
  "id": "https://lab.kbin.pub/m/fediverse",
  "name": "Fediverse",
  "preferredUsername": "fediverse",
  "inbox": "https://lab.kbin.pub/m/fediverse/inbox",
  "outbox": "https://lab.kbin.pub/m/fediverse/outbox",
  "followers": "https://lab.kbin.pub/m/fediverse/followers",
  "url": "https://lab.kbin.pub/m/fediverse",
  "publicKey": {
    "owner": "https://lab.kbin.pub/m/fediverse",
    "id": "https://lab.kbin.pub/m/fediverse#main-key",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----"
  },
  "summary": "Hello word",
  "sensitive": false,
  "moderators": "https://lab.kbin.pub/m/fediverse/moderators",
  "postingRestrictedToMods": false,
  "endpoints": {
    "sharedInbox": "https://lab.kbin.pub/f/inbox"
  },
  "published": "2023-04-11T18:47:56+00:00",
  "updated": "2023-04-12T08:25:04+00:00",
  "icon": {
    "type": "Image",
    "url": "https://devmedia.karab.in/79/ae/79ae0db57f949e51ddd3825632a2f0496a319db6527699b3c000ecf1f4857680.png"
  }
}
```