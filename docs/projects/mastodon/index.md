---
id: mastodon
title: Mastodon
tags:
  - Microblogging
---

Mastodon is a Fediverse microblogging platform.

## Official documentation

Mastodon has quite detailed documentation of their use of ActivityPub at [docs.joinmastodon.org](https://docs.joinmastodon.org/spec/activitypub/). For additional information visit there.

## Overview

Mastodon stores little or no ActivityPub information directly in its databases. Incoming [Activities](/category/activities-5) are converted into Mastodon-specific data structures like `Status` and `Account`. ActivityPub Activities (primarily [Note](note.md)) are converted into a `Status` and an Actor is represented by an `Account`. An ActivityPub `Question` is converted into a special kind of poll `Status`.

Mastodon does not support the ActivityPub client to server (C2S) API. It uses a Mastodon-specific API for client access and administration.

### Inbox

Activities may be posted to the Mastodon inbox network endpoint, but not read from it. There is no actual inbox data structure in the Mastodon implementation. Mastodon represents this type of data as *timelines*, which are conceptually similar to the ActivityPub `OrderedCollection`.

Actor-specific inbox endpoints are supported and there is a instance-level shared inbox. Posts to the inbox are authenticated using HTTP Signatures.

### Outbox

A partial list of an Actor's Activities can be read from the outbox network endpoint. The outbox is read-only. When read, the outbox contents will be filtered according to the credentials of the requester and will only contain Activities Mastodon is able to reconstruct from its internal data.

