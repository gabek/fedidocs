---
id: artist
title: Artist
sidebar_label: Artist
sidebar_position: 1
tags:
  - artist
---

An `Artist` is a custom object used to store musical artist and podcast creator information.

## Properties

| Property         | Data type     | Description                                                    |
| ---------------- | ------------- | -------------------------------------------------------------- |
| `type`\*         | String        | The object type (`Artist`)                                     |
| `id`\*           | String (URI)  | The URI that identifies the artist over federation             |
| `name`\*         | String        | The artist's name                                              |
| `published`\*    | Datetime      | The date on which the artist was published over the federation |
| `musicbrainzId`? | String (UUID) | The MusicBrainz ID associated with the artist                  |

## Example

```json
{
  "type": "Artist",
  "id": "https://awesome.music/federation/music/artists/73c32807-a199-4682-8068-e967f734a320",
  "name": "Metallica",
  "published": "2018-04-08T12:19:05.920415+00:00",
  "musicbrainzId": "65f4f0c5-ef9e-490c-aee3-909e7ae6b2ab"
}
```
