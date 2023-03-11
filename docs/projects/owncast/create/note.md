---
id: note
title: Create Note
sidebar_label: Note
tags:
  - Create
  - Note
  - Microblogging
  - Attachments
---

Owncast sends out a note with an attachment to the inbox of each follower each time the stream goes live. Streamers can also compose and send out posts to their followers manually. It also utilizes private messages to an ActivityPub actor for use in authenticating to chat.

| Reference |                                                                    |
| --------- | ------------------------------------------------------------------ |
| Activity  | [Create](https://www.w3.org/TR/activitypub/#create-activity-inbox) |
| Object    | Note                                                               |

## Outbound

Outbound note objects from Owncast aim to be compatible with all microblogging style platforms.

## Inbound

Inbound note objects received by Owncast are not handled and silently discarded.

## Example automated "Go live" message

```json
Example TODO
```

## Example "FediAuth" message

```json
Example TODO
```
