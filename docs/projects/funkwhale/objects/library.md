---
id: library
title: Library
sidebar_label: Library
sidebar_position: 4
tags:
  - library
---

A `Library` is a custom object used to store music collection information. It inherits its behavior and properties from ActivityPub's [`Actor`](https://www.w3.org/TR/activitypub/#actors) and [`Collection`](https://www.w3.org/TR/activitypub/#collections) objects.

## Properties

| Property       | Data type    | Description                                           |
| -------------- | ------------ | ----------------------------------------------------- |
| `type`\*       | String       | The object type (`Library`)                           |
| `id`\*         | String (URI) | A URI that identifies the library over federation     |
| `name`\*       | String       | The library's name                                    |
| `followers`\*  | String (URI) | The ID of the library's followers collection          |
| `totalItems`\* | Integer      | The number of [`Audio` objects](audio) in the library |
| `first`\*      | String (URI) | The URL of the library's first page                   |
| `last`\*       | String (URI) | The URL of the library's last page                    |
| `summary`?     | String       | The library's description                             |

## Example

```json
{
  "type": "Library",
  "id": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6",
  "attributedTo": "https://awesome.music/federation/actors/Alice",
  "name": "My awesome library",
  "followers": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6/followers",
  "summary": "This library is for restricted use only",
  "totalItems": 4234,
  "first": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6?page=1",
  "last": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6?page=56"
}
```
