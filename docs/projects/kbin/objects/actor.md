---
id: actor
title: Actor
sidebar_label: Actor
sidebar_position: 3
tags:
  - actor
---

The `Actor` is an object that represents an individual user.

## Properties

| Property | Data type | Description |
|----------|-----------|-------------|
| `type`\* | String    | Person      |

## Example

```json
{
  "@context": [
    "https://www.w3.org/ns/activitystreams",
    "https://w3id.org/security/v1",
    {
      "manuallyApprovesFollowers": "as:manuallyApprovesFollowers",
      "schema": "http://schema.org#",
      "PropertyValue": "schema:PropertyValue",
      "value": "schema:value"
    }
  ],
  "id": "https://lab.kbin.pub/u/eee",
  "type": "Person",
  "name": "eee",
  "preferredUsername": "eee",
  "inbox": "https://lab.kbin.pub/u/eee/inbox",
  "outbox": "https://lab.kbin.pub/u/eee/outbox",
  "url": "https://lab.kbin.pub/u/eee",
  "manuallyApprovesFollowers": false,
  "published": "2022-12-23T16:21:13+00:00",
  "following": "https://lab.kbin.pub/u/eee/following",
  "followers": "https://lab.kbin.pub/u/eee/followers",
  "publicKey": {
    "owner": "https://lab.kbin.pub/u/eee",
    "id": "https://lab.kbin.pub/u/eee#main-key",
    "publicKeyPem": "-----BEGIN PUBLIC KEY-----"
  },
  "endpoints": {
    "sharedInbox": "https://lab.kbin.pub/f/inbox"
  }
}
```