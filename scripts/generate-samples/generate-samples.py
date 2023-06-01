#!/usr/bin/python
#
# Generate documentation pages with samples of webfinger and actor files
# from various Fediverse servers/apps
#
# (C) 2023 Johannes Ernst, BSD 3-clause license
#

import argparse
import json
import re
from time import gmtime, strftime
import urllib.request


def readAccountsFile( fileName ) :
    with open( fileName, 'r' ) as fd :
        sampleAccountsContent = fd.read()

    return json.loads( sampleAccountsContent )


def emitHeader( title, description, outFd ) :
    outFd.write( f"""---
title: {title}
description: {description}
---

As of { strftime("%Y-%m-%d %H:%M:%S UTC", gmtime()) }. To regenerate, run `make`
in directory `scripts`.

""" )


def emitWebfinger( app, handle, outFd ) :
    try :
        outFd.write( f"## App: {app}, handle ``{handle}``\n" )
        wfUrl = handleToWebfingerEndpoint( handle )
        wfContent = urllib.request.urlopen( urllib.request.Request( wfUrl, headers={ 'User-Agent' : '' } )).read()
        # The default python user agent produces HTTP 403 on misskey.io -- no idea why
        wfJson = json.loads( wfContent.decode( 'utf-8' ))

        outFd.write( "\n")
        outFd.write( f"Endpoint: {wfUrl}\n" )
        outFd.write( "\n")
        outFd.write( "```js\n" )
        outFd.write( json.dumps( wfJson, indent=2 ))
        outFd.write( "\n")
        outFd.write( "```\n" )
        outFd.write( "\n")

    except Exception as e:
        print( f"ERROR when attempting to get webfinger data for {handle} at {wfUrl}. Skipping: {e}")


def emitActor( app, handle, outFd ) :
    try :
        outFd.write( f"## App: {app}, handle ``{handle}``\n" )
        wfUrl = handleToWebfingerEndpoint( handle )
        wfContent = urllib.request.urlopen( urllib.request.Request( wfUrl, headers={ 'User-Agent' : '' } )).read()
        # The default python user agent produces HTTP 403 on misskey.io -- no idea why
        wfJson = json.loads( wfContent.decode( 'utf-8' ))

    except Exception as e:
        print( f"ERROR when attempting to get webfinger data for {handle} at {wfUrl}. Skipping: {e}")
        return

    try :
        actorUrl = None
        for wfLinkJson in wfJson['links'] :
            if 'type' in wfLinkJson and wfLinkJson['type'] == 'application/activity+json' :
                actorUrl = wfLinkJson['href']
                break

        if actorUrl :
            actorContent = urllib.request.urlopen( urllib.request.Request( actorUrl, headers={ 'Accept' : 'application/activity+json', 'User-Agent' : '' } )).read()
            # The default python user agent produces HTTP 403 on misskey.io -- no idea why
            actorJson = json.loads( actorContent.decode( 'utf-8' ))

            outFd.write( "\n")
            outFd.write( f"Endpoint: {actorUrl}\n" )
            outFd.write( "\n")
            outFd.write( "```js\n" )
            outFd.write( json.dumps( actorJson, indent=2 ))
            outFd.write( "\n")
            outFd.write( "```\n" )
            outFd.write( "\n")

        else :
            outFd.write( "Actor JSON not found.\n" )
            outFd.write( "\n")

    except Exception as e:
        print( f"ERROR when attempting to get actor data for {handle} at {wfUrl}. Skipping: {e}")


def emitFooter( outFd ) :
    pass


def handleToWebfingerEndpoint( handle ) :
    match = re.match( "@([^@]+)@([^@]+)", handle )
    if match :
        ret = f"https://{ match.group(2) }/.well-known/webfinger?resource=acct%3a{ match.group(1) }@{ match.group(2) }"
        return ret

    match = re.match( "https://([^/]+)/", handle )
    if match :
        ret = f"https://{ match.group(1) }/.well-known/webfinger?resource={ handle }"
        return ret

    raise ValueError( 'Cannot parse: ' + handle )


parser = argparse.ArgumentParser( description='Generate webfinger samples for the docs' )
parser.add_argument( '--account-file', help='Name of a JSON file that contains the sample accounts')
parser.add_argument( '--type', choices=['webfinger', 'actor'], required=True, help='Generate webfinger samples or actor file samples')
parser.add_argument( '-o', '--out', help='Name of the output file' )

args = parser.parse_args()

sampleAccountsJson = readAccountsFile( args.account_file )

with open( args.out, 'w' ) as outFd :
    if args.type == 'webfinger' :
        emitHeader( 'Webfinger sample files', 'A selection of Webfinger files as produced by common Fediverse apps', outFd )
    else :
        emitHeader( 'Actor sample files', 'A selection of Actor files as produced by common Fediverse apps', outFd )

    for app in sampleAccountsJson :
        for handle in sampleAccountsJson[app] :
            if 'disabled' in sampleAccountsJson[app][handle] :
                print( f"Skipping {handle}: disabled" )
            else :
                print( f"Working on: {handle}" )
                if args.type == 'webfinger' :
                    emitWebfinger( app, handle, outFd )
                else :
                    emitActor( app, handle, outFd )

    emitFooter( outFd )
