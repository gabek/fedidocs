---
id: owncast
title: Owncast
tags:
  - Video
---

Owncast is a live video streaming server that is designed to be self-hosted. Each instance of Owncast can enable a set of features that allow it to be a part of the Fediverse.

## What functionality does Owncast provide on the Fediverse?

- When a stream goes live a post to Followers with a preview of the stream is sent.
- When Likes, Shares or Follows take place those actions are surfaced in the chat.
- Chat participants can authenticate their chat identity with a process known as "FediAuth". Owncast sends a One Time Password (OTP) private message to the user's Fediverse account.

## What interoperability does Owncast support on the Fediverse?

Currently Owncast aims to be "microblog compatible" which means that it can federate with any platform that can send and receive a standard set of microblog related activities and objects.

## What Objects does Owncast federate?

### Outbound

- [Notes](create/note) with attachments.

### Inbound

- [Likes](like)
- [Follows](follow)
- [Shares](announce)
