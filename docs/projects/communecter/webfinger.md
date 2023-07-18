---
id: webfinger
title: Webfinger
sidebar_position: 3
tags:
  - Webfinger
---

Funkwhale supports the [Webfinger](https://tools.ietf.org/html/rfc7033) protocol for discovering the ActivityPub location of a user.

## Example request:

The following request queries for `ArmelWanes@communecter.org`.

```
GET https://communecter.org/.well-known/webfinger?resource=acct:ArmelWanes@communecter.org
```

## Example response:

```json
{
  "subject": "acct:ArmelWanes@communecter.org",
  "links": [
    {
      "rel": "self",
      "href": "https://communecter.org/api/activitypub/users/u/ArmelWanes",
      "type": "application/activity+json"
    }
  ],
  "aliases": ["https://communecter.org/api/activitypub/users/u/ArmelWanes"]
}
```
