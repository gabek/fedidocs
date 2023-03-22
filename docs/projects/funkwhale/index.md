---
id: funkwhale
title: Funkwhale
tags:
  - Audio
  - Podcasts
---

Funkwhale is a free, federated audio platform for listening to and publishing music and podcasts.

## What functionality does Funkwhale provide on the Fediverse?

- Allows users to create music or podcast channels that other Fediverse users can follow.

## What interoperability does Funkwhale support on the Fediverse?

:::note
Funkwhale doesn't currently support following actors from other services.
:::

* Users of microblogging platforms such as Mastodon and Pleroma can follow Funkwhale channels to see published work in their feed.
* Funkwhale users can search for other Fediverse accounts and render basic information about them.
* Funkwhale channels are compatible with Reel2Bits.

## What Objects does Funkwhale federate?

### Outbound

- [Notes](create/note) with attachments.

### Inbound

- [Likes](like)
- [Follows](activities/follow)
- [Shares](announce)
