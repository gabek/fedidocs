---
id: project
title: Project
sidebar_label: Project
sidebar_position: 1
---

A `Project` is an activity representing a specific project or initiative.

## Properties

| Property            | Data Type              | Description                                                    |
| ------------------- | ---------------------- | -------------------------------------------------------------- |
| `type`\*            | String                 | The object type (`Project`)                                    |
| `id`\*              | String (URI)           | The URI that identifies the project                            |
| `attachment`\*      | Array of Attachments   | Attachments associated with the project                         |
| `attributedTo`\*    | String (URI)           | The URI of the entity or user who created the project           |
| `content`\*         | String                 | The content or description of the project                       |
| `name`\*            | String                 | The name or title of the project                                |
| `startTime`         | String                 | The start time of the project (formatted as a date and time)    |
| `endTime`           | String                 | The end time of the project (formatted as a date and time)      |
| `location`          | Object (Place)         | The location of the project                                    |
| `published`\*       | String                 | The date and time when the project was published                |
| `url`               | String (URL)           | The URL of the project's website or landing page                |
| `uuid`              | String (UUID)          | The universally unique identifier (UUID) of the project         |
| `slug`              | String                 | The slug or identifier of the project                           |
| `email`             | String                 | The email address associated with the project                   |
| `shortDescription`  | String                 | A short description or summary of the project                   |
| `progress`          | String                 | The progress status of the project                              |

### Attachment Object

| Property         | Data Type    | Description                                     |
| ---------------- | ------------ | ----------------------------------------------- |
| `type`\*         | String       | The object type (`Document` or `Link`)           |
| `name`           | String       | The name or title of the attachment              |
| `url`\*          | String (URL) | The URL of the attachment                        |
| `mediaType`      | String       | The media type of the attachment (e.g., `image/png`, `text/html`) |
| `category`       | String       | The category or classification of the attachment |

### Place Object

| Property         | Data Type         | Description                                     |
| ---------------- | ----------------- | ----------------------------------------------- |
| `type`\*         | String            | The object type (`Place`)                       |
| `id`\*           | String (URI)      | The URI that identifies the place                |
| `name`           | String            | The name of the place                            |
| `address`        | Object (Address)  | The address details of the place                 |

### Address Object

| Property           | Data Type | Description                                     |
| ------------------ | --------- | ----------------------------------------------- |
| `type`\*           | String    | The object type (`PostalAddress`)               |
| `addressCountry`   | String    | The country of the address                       |
| `addressLocality`  | String    | The locality (city, town, etc.) of the address   |
| `addressRegion`    | String    | The region (state, province, etc.) of the address|
| `postalCode`       | String    | The postal code of the address                   |
| `streetAddress`    | String    | The street address of the place                  |

## Example

```json
{
  "type": "Project",
  "id": "https://communecter.org/api/activitypub/object/id/64a15d71d725c",
  "attachment": [
    {
      "type": "Document",
      "name": "Image",
      "url": "https://communecter.org/upload/communecter/projects/64a1594e603ab8a6ef0e605c/EcoSmart-Gold-Venue-2022.png",
      "mediaType": "image/png",
      "category": "image"
    },
    {
      "type": "Link",
      "name": "Website",
      "mediaType": "text/html",
      "category": "url",
      "url": "https://www.ecosmarthomesinitiative.com"
    },
    {
      "type": "Link",
      "name": "gitlab",
      "mediaType": "text/html",
      "category": "socialNetwork",
      "url": "https://gitlab.com/ecosmarthomesinitiative"
    },
    {
      "type": "Link",
      "name": "github",
      "mediaType": "text/html",
      "category": "socialNetwork",
      "url": "https://github.com/ecosmarthomesinitiatif"
    },
    {
      "type": "Link",
      "name": "facebook",
      "mediaType": "text/html",
      "category": "socialNetwork",
      "url": "https://www.facebook.com/ecosmarthomesinitiative"
    },
    {
      "type": "Link",
      "name": "twitter",
      "mediaType": "text/html",
      "category": "socialNetwork",
      "url": "https://twitter.com/ecosmarthomes"
    },
    {
      "type": "Document",
      "name": "Banner",
      "url": "https://communecter.org/upload/communecter/projects/64a1594e603ab8a6ef0e605c/banner/ecosmart-innovation.jpg",
      "mediaType": "image/jpg",
      "category": "image"
    }
  ],
  "attributedTo": "https://communecter.org/api/activitypub/users/u/Hajavololona",
  "content": "The EcoSmart Homes Initiative is a comprehensive program aimed at promoting sustainable and energy-efficient housing solutions...",
  "name": "EcoSmart Homes Initiative",
  "startTime": "2023-07-02T14:22:00Z",
  "endTime": "2024-07-31T14:21:00Z",
  "location": {
    "type": "Place",
    "id": "https://communecter.org/address/332566bc-fba0-4c82-8fc1-d86f1822c75f",
    "address": {
      "type": "PostalAddress",
      "addressCountry": "MG",
      "addressLocality": "Fianarantsoa",
      "addressRegion": "Madagascar",
      "streetAddress": "Antarandolo"
    }
  },
  "published": "2023-07-02T14:22:00Z",
  "url": "https://www.ecosmarthomesinitiative.com",
  "shortDescription": "Create a knowledge-sharing platform: Establish an online platform to share information and resources about sustainable housing...",
  "progress": "Ongoing"
}

