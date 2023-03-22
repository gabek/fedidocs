---
id: service-actor
title: Service actor
sidebar_position: 4
tags:
  - Service actor
---

Funkwhale uses a dedicated service actor to send messages or authenticate fetches. This actor isn't associated to a user.

You can query a pod's nodeinfo endpoint to return the ID of the service actor in the `metadata > actorId` field. See the [API explorer](https://docs.funkwhale.audio/swagger/) for more information about this endpoint.

Funkwhale considers a pod's service actor to be an authoritative source for activities associated with **all** objects on its pod's domain. If the service actor sends an activity linked to an object on its domain, remote pods will recognize its authority.
