---
id: audio
title: Audio
sidebar_label: Audio
sidebar_position: 5
tags:
  - audio
---

An `Audio` object is a custom object used to store upload information. It extends the [ActivityStreams Audio object](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-audio) with custom attributes.

## Properties

| Property      | Data type                                                                   | Description                                                                                         |
| ------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `type`\*      | String                                                                      | The object type (`Audio`)                                                                           |
| `id`\*        | String (URI)                                                                | A URI that identifies the audio over federation                                                     |
| `name`\*      | String                                                                      | A readable title for the order. Funkwhale concatenates the track name, album title, and artist name |
| `size`\*      | Integer                                                                     | The size of the audio in bytes                                                                      |
| `bitrate`\*   | Integer                                                                     | The bitrate of the audio in bytes/s                                                                 |
| `duration`\*  | Integer                                                                     | The duration of the audio in seconds                                                                |
| `library`\*   | String (URI)                                                                | The ID of the audio's containing [`Library` object](library)                                        |
| `published`\* | Datetime                                                                    | The date on which the audio was published over the federation                                       |
| `updated`\*   | Datetime                                                                    | The date on which the audio was last updated over the federation                                    |
| `url`\*       | [`Link` object](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-link) | A `Link` object object containing the download location of the audio file                           |
| `track`?      | [`Track` object](track)                                                     | The track associated with the audio file                                                            |

## Example

```json
{
  "type": "Audio",
  "id": "https://awesome.music/federation/music/uploads/88f0bc20-d7fd-461d-a641-dd9ac485e096",
  "name": "For Whom the Bell Tolls - Ride the Lightning - Metallica",
  "size": 8656581,
  "bitrate": 320000,
  "duration": 213,
  "library": "https://awesome.music/federation/music/libraries/dc702491-f6ce-441b-9da0-cecbed08bcc6",
  "updated": "2018-10-02T19:49:35.646372+00:00",
  "published": "2018-10-02T19:49:35.646359+00:00",
  "track": {},
  "url": {
    "href": "https://awesome.music/api/v1/listen/82ece296-6397-4e26-be90-bac5f9990240/?upload=88f0bc20-d7fd-461d-a641-dd9ac485e096",
    "type": "Link",
    "mediaType": "audio/mpeg"
  }
}
```

## Audio fetching on restricted libraries

Audio objects are subject to the following access rules:

- Audio items in public libraries can be accessed by actors without restriction
- Audio items in restricted libraries can only be accessed if the HTTP request is signed by an actor who has an associated **approved** [`Follow` activity](../activities/follow)
