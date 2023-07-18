---
title: Webfinger sample files
description: A selection of Webfinger files as produced by common Fediverse apps
---

As of 2023-06-01 20:52:22 UTC. To regenerate, run `make`
in directory `scripts`.

## App: Mastodon, handle `@gargron@mastodon.social`

Endpoint: https://mastodon.social/.well-known/webfinger?resource=acct%3agargron@mastodon.social

```js
{
  "subject": "acct:Gargron@mastodon.social",
  "aliases": [
    "https://mastodon.social/@Gargron",
    "https://mastodon.social/users/Gargron"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://mastodon.social/@Gargron"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://mastodon.social/users/Gargron"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://mastodon.social/authorize_interaction?uri={uri}"
    }
  ]
}
```

## App: PeerTube, handle `@peertube@framapiaf.org`

Endpoint: https://framapiaf.org/.well-known/webfinger?resource=acct%3apeertube@framapiaf.org

```js
{
  "subject": "acct:peertube@framapiaf.org",
  "aliases": [
    "https://framapiaf.org/@peertube",
    "https://framapiaf.org/users/peertube"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://framapiaf.org/@peertube"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://framapiaf.org/users/peertube"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://framapiaf.org/authorize_interaction?uri={uri}"
    }
  ]
}
```

## App: Calckey, handle `@kainoa@calckey.social`

Endpoint: https://calckey.social/.well-known/webfinger?resource=acct%3akainoa@calckey.social

```js
{
  "subject": "acct:kainoa@calckey.social",
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://calckey.social/users/9aprgabaeb"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://calckey.social/@kainoa"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://calckey.social/authorize-follow?acct={uri}"
    }
  ]
}
```

## App: Misskey, handle `https://misskey.io/@syuilo`

Endpoint: https://misskey.io/.well-known/webfinger?resource=https://misskey.io/@syuilo

```js
{
  "subject": "acct:syuilo@misskey.io",
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://misskey.io/users/7rkrarq81i"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://misskey.io/@syuilo"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://misskey.io/authorize-follow?acct={uri}"
    }
  ]
}
```

## App: Streams, handle `@mike@macgirvin.com`

Endpoint: https://macgirvin.com/.well-known/webfinger?resource=acct%3amike@macgirvin.com

```js
{
  "subject": "acct:mike@macgirvin.com",
  "aliases": [
    "https://macgirvin.com/channel/mike",
    "https://macgirvin.com/~mike",
    "https://macgirvin.com/@mike"
  ],
  "properties": {
    "http://webfinger.net/ns/name": "mike",
    "http://xmlns.com/foaf/0.1/name": "mike",
    "https://w3id.org/security/v1#publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAoaTPG5iYKsHJ1cK5CJUy\niN2y6B7aI4JkKMjjZO0gy8+6oa5kx6H5w7qED937a/SvwuYxh1A5yO9nwoEarM5s\nPoYZ+Z+GGbAcvzdWURtDDdRMNgktAayDiOvEdiEbgPVx8f39YnpX39ngM8ukob16\nS8eNwjWG6uwBs6rxSA409fkWjjbQwbe8fNOpynFWoG8jrB+dK6huryYqkyf9S18u\n01IAJOo1ErtaUNkSzkeudXSWokRbN/P77N8LQXorwPF9U6ODblX9QXCWl6EnQ0CX\nfcC/3NM6uXfda2KTn83G1+mo5QgGYBjGzE9K1VngoyX4J8AqvQxoXkqV20vwFSqW\nccB13F5kqRQ4BoQm2v2/e65YzjrHwkUecj7tS8TVXu8z4mdbDDbso/UrS14JmrJh\njnbwPOYpHX/6p2SdYDTF/vUWUmeSatS7sHK92eTRukuONig+PNvx8GUtxgMWPIgH\njIupGnR5lZxFMP+iaAmfxOSbVNeLn/Nka7+UfkDThApfhesBA6P8jAdStTCyqAYB\nY3rTTwplcaKKnNv+pLqBqyhYEghmGvv2EC2UGsL6rFit1RaZgSXWCIcLzdRZo4Ak\nznvz8+juMjyPLp7DdSHhKss9kV9HDxZXjrstDxOR61j0vifaMh6bUVrOAMm0Ffs+\n41v+D6pSA5p0OI2aqNJzLZ8CAwEAAQ==\n-----END PUBLIC KEY-----\n"
  },
  "links": [
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "self",
      "type": "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\"",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/jpeg",
      "href": "https://macgirvin.com/photo/profile/l/5"
    },
    {
      "rel": "http://webfinger.net/rel/blog",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://purl.org/nomad",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://purl.org/openwebauth/v1",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/owa"
    },
    {
      "rel": "http://purl.org/openwebauth/v1#redirect",
      "type": "application/x-nomad+json",
      "href": "https://macgirvin.com/magic"
    },
    {
      "rel": "http://purl.org/zot/protocol/6.0",
      "type": "application/x-zot+json",
      "href": "https://macgirvin.com/channel/mike"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://macgirvin.com/follow?url={uri}"
    }
  ]
}
```

## App: Hubzilla, handle `@contribute@hubzilla.org`

Endpoint: https://hubzilla.org/.well-known/webfinger?resource=acct%3acontribute@hubzilla.org

```js
{
  "subject": "acct:contribute@hubzilla.org",
  "aliases": [
    "https://hubzilla.org/channel/contribute",
    "https://hubzilla.org/~contribute",
    "https://hubzilla.org/@contribute",
    "acct:contribute@zotlabs.org"
  ],
  "properties": {
    "http://webfinger.net/ns/name": "Hubzilla | Contribute",
    "http://xmlns.com/foaf/0.1/name": "Hubzilla | Contribute",
    "https://w3id.org/security/v1#publicKeyPem": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAvgz86rVOBlnDaYOfPzpC\nUxIproAWLPrGVFHUJ5r3WDkZv8CTgVLMJB4lzgMaLjkHwaFDA0I4Ax7Qdk5Li8ZK\na+DNGGlP8c1nusPhbSMFC8hqY73Vxz7rxMvtHPEpyXLiivBkRDwtXvrz87ALQ13C\nXX0FlV5rV0mzf3W3mny9WKRaYoSqC8tZ9LeRdP2YPMr656BivJxQg3UQZTihkhd2\n/rsEs8T+C8dQdOjN8ON7X1afdO28jkMwdkmOnEkuY/RY15VBt0cS3w+h+lyP0SYO\n+Xj8lh6XJgsBKNU0cKYR7DKL+uCcRwPB9cxgPIIdUX1iqBGXSGnbFU/GHLsvNfxD\nlYRRZoyC2zBkJJE0TAeF6mCVFczBAl1+ECENnbvbrE2JE/jkwZx8dOJ1EAGQFqpC\ntrBywvKqKv5TVvwjuWyt6lluLdTp1+I+Xlt1YoqYqiJESFyCZaOHwQiq/RzWek5s\nntFPmIfbIJcd7tEf2NzQRVhfvxDWIL7XxLUZDazjuIy8lnPngTFf6YJ2Rox3JTaX\nPwu3jVumK0LFp8l1U8ohFHxvQsvHXQWIVvQyogPTvWLe1N2V2HENUfvADgsvCFMd\n8nwUmKhD0IjRKyKGoywQQpgLNSTVLb19JPOUm+Y8OsJLgOo3F3/cwWcEUunuHVUm\nOzhTSexpTaN49YsBkA2l6TUCAwEAAQ==\n-----END PUBLIC KEY-----\n",
    "http://purl.org/zot/federation": "zot6"
  },
  "links": [
    {
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/png",
      "href": "https://hubzilla.org/photo/profile/l/17"
    },
    {
      "rel": "http://microformats.org/profile/hcard",
      "type": "text/html",
      "href": "https://hubzilla.org/hcard/contribute"
    },
    {
      "rel": "http://openid.net/specs/connect/1.0/issuer",
      "href": "https://hubzilla.org"
    },
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://hubzilla.org/profile/contribute"
    },
    {
      "rel": "http://webfinger.net/rel/blog",
      "href": "https://hubzilla.org/channel/contribute"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://hubzilla.org/follow?f=&url={uri}"
    },
    {
      "rel": "http://purl.org/zot/protocol/6.0",
      "type": "application/x-zot+json",
      "href": "https://hubzilla.org/channel/contribute"
    },
    {
      "rel": "http://purl.org/openwebauth/v1",
      "type": "application/x-zot+json",
      "href": "https://hubzilla.org/owa"
    },
    {
      "rel": "magic-public-key",
      "href": "data:application/magic-public-key,RSA.vgz86rVOBlnDaYOfPzpCUxIproAWLPrGVFHUJ5r3WDkZv8CTgVLMJB4lzgMaLjkHwaFDA0I4Ax7Qdk5Li8ZKa-DNGGlP8c1nusPhbSMFC8hqY73Vxz7rxMvtHPEpyXLiivBkRDwtXvrz87ALQ13CXX0FlV5rV0mzf3W3mny9WKRaYoSqC8tZ9LeRdP2YPMr656BivJxQg3UQZTihkhd2_rsEs8T-C8dQdOjN8ON7X1afdO28jkMwdkmOnEkuY_RY15VBt0cS3w-h-lyP0SYO-Xj8lh6XJgsBKNU0cKYR7DKL-uCcRwPB9cxgPIIdUX1iqBGXSGnbFU_GHLsvNfxDlYRRZoyC2zBkJJE0TAeF6mCVFczBAl1-ECENnbvbrE2JE_jkwZx8dOJ1EAGQFqpCtrBywvKqKv5TVvwjuWyt6lluLdTp1-I-Xlt1YoqYqiJESFyCZaOHwQiq_RzWek5sntFPmIfbIJcd7tEf2NzQRVhfvxDWIL7XxLUZDazjuIy8lnPngTFf6YJ2Rox3JTaXPwu3jVumK0LFp8l1U8ohFHxvQsvHXQWIVvQyogPTvWLe1N2V2HENUfvADgsvCFMd8nwUmKhD0IjRKyKGoywQQpgLNSTVLb19JPOUm-Y8OsJLgOo3F3_cwWcEUunuHVUmOzhTSexpTaN49YsBkA2l6TU.AQAB"
    }
  ]
}
```

## App: GNU Social, handle `@administrator@gnusocial.net`

Endpoint: https://gnusocial.net/.well-known/webfinger?resource=acct%3aadministrator@gnusocial.net

```js
{
  "subject": "acct:administrator@gnusocial.net",
  "aliases": [
    "https://gnusocial.net/index.php/user/1",
    "https://gnusocial.net/administrator",
    "https://gnusocial.net/user/1",
    "https://gnusocial.net/index.php/administrator"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "http://gmpg.org/xfn/11",
      "type": "text/html",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "describedby",
      "type": "application/rdf+xml",
      "href": "https://gnusocial.net/administrator/foaf"
    },
    {
      "rel": "http://apinamespace.org/atom",
      "type": "application/atomsvc+xml",
      "href": "https://gnusocial.net/api/statusnet/app/service/administrator.xml"
    },
    {
      "rel": "http://apinamespace.org/twitter",
      "href": "https://gnusocial.net/api/"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "type": "application/atom+xml",
      "href": "https://gnusocial.net/api/statuses/user_timeline/1.atom"
    },
    {
      "rel": "magic-public-key",
      "href": "data:application/magic-public-key,RSA.lrWlx-ufdZ3OgBuV1ZKHQ1T4Rx99QcThod8Bpn1jhmpOufts8oQ1CV7YK0SKTCHLFU6ZQSjm8f3aftoHnW6W51WxqCFD6VFFpQYO6ur8Vf0rYRIpgLVKKS1dl5OdVdQ0Rtj1fsUC2QMD9f7r4tEJQmHnjM8t7twjlN_x83gxwis=.AQAB"
    },
    {
      "rel": "diaspora-public-key",
      "type": "RSA",
      "href": "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tDQpNSUdKQW9HQkFKYTFwY2ZybjNXZHpvQWJsZFdTaDBOVStFY2ZmVUhFNGFIZkFhWjlZNFpxVHJuN2JQS0VOUWxlDQoyQ3RFaWt3aHl4Vk9tVUVvNXZIOTJuN2FCNTF1bHVkVnNhZ2hRK2xSUmFVR0R1cnEvRlg5SzJFU0tZQzFTaWt0DQpYWmVUblZYVU5FYlk5WDdGQXRrREEvWCs2K0xSQ1VKaDU0elBMZTdjSTVUZjhmTjRNY0lyQWdNQkFBRT0NCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0="
    },
    {
      "rel": "http://joindiaspora.com/guid",
      "href": "a7ea2e0f4f4b270d6a1b59638171309d5d1225b0a8dfd2473e375ded45bd4982"
    },
    {
      "rel": "salmon",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://salmon-protocol.org/ns/salmon-replies",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://salmon-protocol.org/ns/salmon-mention",
      "href": "https://gnusocial.net/main/salmon/user/1"
    },
    {
      "rel": "http://specs.openid.net/auth/2.0/provider",
      "href": "https://gnusocial.net/administrator"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://gnusocial.net/main/remotefollowsub?profile={uri}"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://gnusocial.net/index.php/user/1"
    }
  ]
}
```

## App: Pleroma, handle `@karolat@stereophonic.space`

Endpoint: https://stereophonic.space/.well-known/webfinger?resource=acct%3akarolat@stereophonic.space

```js
{
  "aliases": [
    "https://stereophonic.space/users/karolat"
  ],
  "links": [
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html"
    },
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "self",
      "type": "application/activity+json"
    },
    {
      "href": "https://stereophonic.space/users/karolat",
      "rel": "self",
      "type": "application/ld+json; profile=\"https://www.w3.org/ns/activitystreams\""
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://stereophonic.space/ostatus_subscribe?acct={uri}"
    }
  ],
  "subject": "acct:karolat@stereophonic.space"
}
```

## App: Pixelfed, handle `@dansup@pixelfed.social`

Endpoint: https://pixelfed.social/.well-known/webfinger?resource=acct%3adansup@pixelfed.social

```js
{
  "subject": "acct:dansup@pixelfed.social",
  "aliases": [
    "https://pixelfed.social/dansup",
    "https://pixelfed.social/users/dansup"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://pixelfed.social/dansup"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "type": "application/atom+xml",
      "href": "https://pixelfed.social/users/dansup.atom"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://pixelfed.social/users/dansup"
    }
  ]
}
```

## App: Friendica, handle `@tobias@friendi.ca`

Endpoint: https://friendi.ca/.well-known/webfinger?resource=acct%3atobias@friendi.ca

```js
{
  "subject": "acct:tobias@friendi.ca",
  "aliases": [
    "acct:tobias@friendi.ca",
    "https://friendi.ca/author/tobias/",
    "mailto:tobias.diekershoff@gmx.net"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://friendi.ca/author/tobias/",
      "type": "text/html"
    },
    {
      "rel": "http://webfinger.net/rel/avatar",
      "href": "https://secure.gravatar.com/avatar/7faf7abf39f117b7bb2cf8e08f4eded7?s=96&d=mm&r=g"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://friendi.ca/author/tobias/"
    }
  ]
}
```

## App: Funkwhale, handle `@Greensky@open.audio`

Endpoint: https://open.audio/.well-known/webfinger?resource=acct%3aGreensky@open.audio

```js
{
  "subject": "acct:Greensky@open.audio",
  "links": [
    {
      "rel": "self",
      "href": "https://open.audio/federation/actors/Greensky",
      "type": "application/activity+json"
    }
  ],
  "aliases": [
    "https://open.audio/federation/actors/Greensky"
  ]
}
```

## App: WriteFreely, handle `@matt@write.as`

Endpoint: https://write.as/.well-known/webfinger?resource=acct%3amatt@write.as

```js
{
  "subject": "acct:matt@write.as",
  "aliases": [
    "https://write.as/matt/",
    "https://write.as/api/collections/matt"
  ],
  "links": [
    {
      "href": "https://write.as/matt/",
      "type": "text/html",
      "rel": "https://webfinger.net/rel/profile-page"
    },
    {
      "href": "https://write.as/api/collections/matt",
      "type": "application/activity+json",
      "rel": "self"
    }
  ]
}
```

## App: Plume, handle `@actapopuli@fediverse.blog`

Endpoint: https://fediverse.blog/.well-known/webfinger?resource=acct%3aactapopuli@fediverse.blog

```js
{
  "subject": "acct:actapopuli@fediverse.blog",
  "aliases": [
    "https://fediverse.blog/@/actapopuli/"
  ],
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "href": "https://fediverse.blog/@/actapopuli/",
      "type": "text/html"
    },
    {
      "rel": "http://schemas.google.com/g/2010#updates-from",
      "href": "https://fediverse.blog/@/actapopuli/feed.atom",
      "type": "application/atom+xml"
    },
    {
      "rel": "self",
      "href": "https://fediverse.blog/@/actapopuli/",
      "type": "application/activity+json"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://fediverse.blog/remote_interact?target={uri}"
    }
  ]
}
```

## App: Mobilizon, handle `@framasoft@mobilizon.fr`

Endpoint: https://mobilizon.fr/.well-known/webfinger?resource=acct%3aframasoft@mobilizon.fr

```js
{
  "aliases": [
    "https://mobilizon.fr/@framasoft"
  ],
  "links": [
    {
      "href": "https://mobilizon.fr/@framasoft",
      "rel": "self",
      "type": "application/activity+json"
    },
    {
      "rel": "http://ostatus.org/schema/1.0/subscribe",
      "template": "https://mobilizon.fr/interact?uri={uri}"
    },
    {
      "href": "https://mobilizon.fr/media/ff5b2d425fb73e17fcbb56a1a032359ee0b21453c11af59e103e783817a32fdf.png?name=framasoft%27s%20avatar.png",
      "rel": "http://webfinger.net/rel/avatar",
      "type": "image/png"
    },
    {
      "href": "https://mobilizon.fr/@framasoft",
      "rel": "http://webfinger.net/rel/profile-page/",
      "type": "text/html"
    }
  ],
  "subject": "acct:framasoft@mobilizon.fr"
}
```

## App: Lemmy, handle `@lemmy_support@lemmy.ml`

Endpoint: https://lemmy.ml/.well-known/webfinger?resource=acct%3alemmy_support@lemmy.ml

```js
{
  "subject": "acct:lemmy_support@lemmy.ml",
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://lemmy.ml/c/lemmy_support",
      "properties": {}
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://lemmy.ml/c/lemmy_support",
      "properties": {
        "https://www.w3.org/ns/activitystreams#type": "Group"
      }
    }
  ]
}
```

## App: Micro.blog, handle `@manton@manton.org`

Endpoint: https://manton.org/.well-known/webfinger?resource=acct%3amanton@manton.org

```js
{
  "subject": "acct:manton@manton.org",
  "links": [
    {
      "rel": "http://webfinger.net/rel/profile-page",
      "type": "text/html",
      "href": "https://manton.org/activitypub/manton"
    },
    {
      "rel": "self",
      "type": "application/activity+json",
      "href": "https://manton.org/activitypub/manton"
    }
  ]
}
```
