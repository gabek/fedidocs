---
id: webfinger
title: Webfinger
sidebar_position: 6
tags:
  - Webfinger
---

Kbin supports the [Webfinger](https://tools.ietf.org/html/rfc7033) protocol for discovering the ActivityPub location of a user.

## Example request:

The following request queries for `eee@dev.karab.in`.

```
GET https://dev.karab.in/.well-known/webfinger?resource=acct:eee@dev.karab.in
```

## Example response:

### Person

```json
{
  "subject": "acct:eee@dev.karab.in",
  "aliases": ["https://dev.karab.in/u/eee"],
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

### Group

```json
{
  "subject": "acct:fediverse@dev.karab.in",
  "aliases": ["https://dev.karab.in/m/fediverse"],
  "links": [
    {
      "rel": "self",
      "href": "https://dev.karab.in/m/fediverse",
      "type": "application/activity+json"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://dev.karab.in/m/fediverse",
      "type": "text/html"
    }
  ]
}
```
