---
id: webfinger
title: Webfinger
sidebar_position: 5
tags:
  - Webfinger
---

Kbin supports the [Webfinger](https://tools.ietf.org/html/rfc7033) protocol for discovering the ActivityPub location of a user.

## Example request:

The following request queries for `eee@dev.karab.in`.

```
GET https://eee@dev.karab.in/.well-known/webfinger?resource=acct%3Aeee%40dev.karab.in
```

## Example response:

```json
{
  "subject": "acct:eee@dev.karab.in",
  "aliases": [
    "https://dev.karab.in/u/eee"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://dev.karab.in/u/eee",
      "type": "text/html"
    },
    {
      "rel": "self",
      "href": "https://dev.karab.in/u/eee",
      "type": "application/activity+json"
    }
  ]
}
```
