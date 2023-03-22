---
id: webfinger
title: Webfinger
sidebar_position: 3
tags:
  - Webfinger
---

Funkwhale supports the [Webfinger](https://tools.ietf.org/html/rfc7033) protocol for discovering the ActivityPub location of a user.

## Example request:

The following request queries for `test_channel@open.audio`.

```
GET https://open.audio/.well-known/webfinger?resource=acct:test_channel%40open.audio
```

## Example response:

```json
{
   "subject": "acct:test_channel@open.audio",
   "links": [
      {
         "rel": "self",
         "href": "https://open.audio/federation/actors/test_channel",
         "type": "application/activity+json"
      }
   ],
   "aliases": [
      "https://open.audio/federation/actors/test_channel"
   ]
}
```
