---
id: track
title: Track
sidebar_label: Track
sidebar_position: 3
tags:
  - track
---

A `Track` is a custom object used to store track information.

## Properties

| Property         | Data type                           | Description                                                                      |
| ---------------- | ----------------------------------- | -------------------------------------------------------------------------------- | ------------------------- |
| `type`*         | String                              |                                                                                  | The object type (`Track`) |
| `id`*           | String (URI)                        | A URI that identifies the track over federation                                  |
| `name`*         | String                              | The track title                                                                  |
| `position`*     | Integer                             | The position of the track in the album                                           |
| `published`*    | Datetime                            | The date on which the track was published over the federation                    |
| `musicbrainzId`? | String (UUID)                       | The MusicBrainz recording ID                                                     |
| `album`?         | [`Album` object](album)             | The album that contains the track                                                |
| `artists`?       | Array of [`Artist` objects](artist) | A list of artists associated to the track. This can differ from the album artist |

## Example

```json
{
  "type": "Track",
  "id": "https://awesome.music/federation/music/tracks/82ece296-6397-4e26-be90-bac5f9990240",
  "name": "For Whom the Bell Tolls",
  "position": 3,
  "published": "2018-10-02T19:49:35.822537+00:00",
  "musicbrainzId": "771ab043-8821-44f9-b8e0-2733c3126c6d",
  "artists": [{}],
  "album": {}
}
```
