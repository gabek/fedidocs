---
id: note
title: Note
sidebar_label: Note (status)
tags:
  - Status
  - Note
  - Microblogging
  - Attachments
---

An ActivityPub Note object represents a single status post on Mastodon.

| Reference              |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| Object                 | Note                                                                              |
| Official documentation | [docs.joinmastodon.org](https://docs.joinmastodon.org/spec/activitypub/#payloads) |

## Common attachments

- Hashtags ([Hashtag](hashtag))
- Media attachments

## Things to be aware of

- Mastodon (as of last tested) requires tags ([Hashtags](hashtag) objects) to be an array. While ActivityPub supports specifying a single object for a property, Mastodon will silently discard your post if you do not specify this property as an array.

A Note object can be included in the following ActivityPub activities:

- [Create](activities/create)
- [Delete](activities/delete)
- [Like](activities/like)
- [Announce](activities/announce)
- [Flag](activities/flag)
- [Update](activities/update)
- [Undo](activities/undo)
