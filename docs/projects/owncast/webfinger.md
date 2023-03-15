---
id: webfinger
title: Webfinger
sidebar_position: 10
tags:
  - Webfinger
---

Owncast supports the [Webfinger](https://tools.ietf.org/html/rfc7033) protocol for discovering the ActivityPub location of a user.

## Example request:

The following request queries for `goodnight@nightly.owncast.tv`.

```
GET https://nightly.owncast.tv/.well-known/webfinger?resource=acct%3Agoodnight%40nightly.owncast.tv
```

## Example response:

```json
{
  "subject": "acct:goodnight@nightly.owncast.tv",
  "aliases": ["https://nightly.owncast.tv/federation/user/goodnight"],
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://nightly.owncast.tv/federation/user/goodnight"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://nightly.owncast.tv/federation/user/goodnight"
    }
  ]
}
```
