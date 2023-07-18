---
title: HTTP Signatures
description: Tracking adoption of current drafts of HTTP Signatures across the Fediverse.
---

    	<p>Adoption of current drafts of HTTP Signatures across the Fediverse.</p>
    	<table class="theTable">
    		<tr>
    			<th rowspan="2">Service</th>
    			<th rowspan="2">Library</th>
    			<td rowspan="2" class="sep"></td>
    			<th colspan="3">Accepts</th>
    			<td rowspan="2" class="sep"></td>
    			<th colspan="3">Sends</th>
    		</tr>
    		<tr>
    			<th>algorithm="hs2019"</th>
    			<th>(created) &amp; (expires)</th>
    			<th>Signature-Input</th>
    			<th>algorithm</th>
    			<th>(created) &amp; (expires)</th>
    			<th>Signature-Input</th>
    		</tr>
    		<tr>
    			<td><a href="https://joinmastodon.org">Mastodon</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">Partial<sup>5</sup></td>
    			<td class="yes">Yes</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://pleroma.social">Pleroma</a></td>
    			<td><a href="https://git.pleroma.social/pleroma/elixir-libraries/http_signatures">pleroma/http_signatures</a></td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://joinpeertube.org">PeerTube</a></td>
    			<td><a href="https://www.npmjs.com/package/@peertube/http-signature">@peertube/http-signature</a></td>
    			<td />
    			<td class="yesish">
    				Partial<sup>7</sup>
    			</td>
    			<td class="yes">Yes</td>
    			<td class="no">No - <a href="https://github.com/joyent/node-http-signature/issues/118">Issue</a></td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://writefreely.org/">WriteFreely</a></td>
    			<td><a href="https://github.com/writeas/httpsig">writeas/httpsig</a></td>
    			<td />
    			<td class="no">No - <a href="https://github.com/spacemonkeygo/httpsig/issues/7">Issue</a></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://pixelfed.org/">Pixelfed</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://join.misskey.page/">Misskey</a></td>
    			<td><a href="https://www.npmjs.com/package/http-signature">http-signature</a></td>
    			<td />
    			<td class="no">
    				No - <a href="https://github.com/joyent/node-http-signature/issues/106">Issue</a>
    			</td>
    			<td class="yes">Yes</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://friendi.ca">Friendica</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">
    				Partial<sup>5</sup>
    			</td>
    			<td class="yes">
    				Yes
    			</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://zotlabs.org/page/hubzilla/hubzilla-project">Hubzilla</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">
    				Partial<sup>2</sup>
    			</td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://funkwhale.audio/">Funkwhale</a></td>
    			<td>
    				<a href="https://github.com/EliotBerriot/requests-http-signature/tree/signature-header-support">
    					EliotBerriot/requests-http-signature#signature-header-support
    				</a>
    				<sup>3</sup>
    			</td>
    			<td />
    			<td class="no">No</td>
    			<td class="no">No<sup>4</sup></td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://joinplu.me/">Plume</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://joinmobilizon.org">Mobilizon</a></td>
    			<td><a href="https://git.pleroma.social/pleroma/elixir-libraries/http_signatures">pleroma/http_signatures</a></td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://join-lemmy.org">Lemmy</a></td>
    			<td><a href="https://git.asonix.dog/asonix/http-signature-normalization">http-signature-normalization</a></td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="yes">Yes</td>
    			<td class="no">No</td>
    			<td />
    			<td class="yes">hs2019</td>
    			<td class="yes">Yes</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://gnusocial.network">GNU social</a></td>
    			<td>None</td>
    			<td />
    			<td class="yesish">Partial<sup>1</sup></td>
    			<td class="no">No</td>
    			<td class="no">No</td>
    			<td />
    			<td class="old">rsa-sha256</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    		<tr>
    			<td><a href="https://sr.ht/~vpzom/lotide/">lotide</a></td>
    			<td><a href="https://crates.io/crates/hancock">hancock</a></td>
    			<td />
    			<td class="yesish">Maybe<sup>6</sup></td>
    			<td class="yes">Yes</td>
    			<td class="no">No</td>
    			<td />
    			<td class="yes">hs2019</td>
    			<td class="old">No</td>
    			<td class="old">No</td>
    		</tr>
    	</table>
    	<ul>
    		<li><sup>1</sup> This implementation assumes all signatures use SHA256</li>
    		<li>
    			<sup>2</sup> This implementation uses the passed algorithm if known (not recommended by the spec),
    			but falls back to SHA256 if unrecognized, which technically works for current uses of hs2019
    		</li>
    		<li>
    			<sup>3</sup> Temporary fork, see
    			<a href="https://dev.funkwhale.audio/funkwhale/funkwhale/-/issues/876">this issue</a>
    		</li>
    		<li>
    			<sup>4</sup> Implemented in upstream library, but not released yet
    		</li>
    		<li>
    			<sup>5</sup> This implementation assumes "hs2019" is equivalent to "rsa-sha256", which is not
    			recommended but is technically compatible with current uses of hs2019
    		</li>
    		<li>
    			<sup>6</sup> This implementation technically supports signature algorithm derivation, but given that it's the only one, this is not a standard
    		</li>
    		<li>
    			<sup>7</sup> This implementation assumes "hs2019" is equivalent to "rsa-sha512"
    		</li>
    	</ul>

Graciously provided under CC0 from [this Github repo](https://github.com/vpzomtrrfrt/arewehs2019yet).
