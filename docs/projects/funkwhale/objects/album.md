---
id: album
title: Album
sidebar_label: Album
sidebar_position: 2
tags:
  - album
---

An `Album` is a custom object used to store album and podcast series information.

## Properties

| Property         | Data type                                                                   | Description                                                     |
| ---------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------- |
| `type`\*         | String                                                                      | The object type (`Album`)                                       |
| `id`\*           | String (URI)                                                                | A URI that identifies the album over federation                 |
| `name`\*         | String                                                                      | The album's title                                               |
| `artists`?       | Array of strings                                                            | A list of [`Artist` objects](artist) associated with the albums |
| `published`\*    | Datetime                                                                    | The date on which the artist was published over the federation  |
| `released`?      | Datetime                                                                    | The date on which the album was released                        |
| `musicbrainzId`? | String (UUID)                                                               | The MusicBrainz release ID                                      |
| `cover`?         | [`Link` object](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link) | A `Link` object representing the album cover                    |

## Example

```json
{
  "type": "Album",
  "id": "https://awesome.music/federation/music/albums/69d488b5-fdf6-4803-b47c-9bb7098ea57e",
  "name": "Ride the Lightning",
  "released": "1984-01-01",
  "published": "2018-10-02T19:49:17.412546+00:00",
  "musicbrainzId": "589ff96d-0be8-3f82-bdd2-299592e51b40",
  "cover": {
    "href": "https://awesome.music/media/albums/covers/2018/10/02/b69d398b5-fdf6-4803-b47c-9bb7098ea57e.jpg",
    "type": "Link",
    "mediaType": "image/jpeg"
  },
  "artists": [{}]
}
```
