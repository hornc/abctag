# abctag
Experimental Arithmetic-Bitwise-Cyclic-Tag-over-HTTP server.

This is an arithmetic implementation of the low-level Turing complete esoteric programming language [Bitwise Cyclic Tag](https://esolangs.org/wiki/Bitwise_Cyclic_Tag)

It works as a webserver which redirects (303) between `/<program>/<datastring>/` states. When/if the data string is empty, it returns a 200.

Additionally, it provides UTF-8 output in response JSON and collects all output in cookies when the datastring ever contains `STX` `ETX` delimited bytes with correct start/stop bits.

## Start the server

    ./abct-web 8080

## Example usage

Browsers tend to complain about too many redirects when used with most programs.

The following is a `curl` command demonstrating how to disable redirect limits, and view cookie output for the "Hello, World!" example:

    curl -sLc- --max-redirs -1 localhost:8080/5814709794364855124394590463104036274829130886495847474077938692059840777884347510099960415045708498000107405098735286987994946170377558/2

There is also a `/b/` path that will redirect raw binary BCT data to the corresponding program Gödel number, 
which is done by converting all `1` to `2`s and `0` to `1`s, and interpreting the resulting string of `1` and `2` as a [Bijective base-2](https://en.wikipedia.org/wiki/Bijective_numeration) numeral.

e.g.

    localhost:8080/b/011/0

will redirect to

     localhost:8080/13/0

Note, this implementation uses a slightly different Gödel numbering from the one described at [esolangs.org](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#G.C3.B6del_numbering). Here both program and data use the same reversed notation.
(I'm sure there was a reason for this...)

## CLI version

There is also a command line utility for testing

    ./abct-cli $(cat examples/hello-world.abct) 2
    
`2` is the initial data value representing a binary `1`

`1` represents binary `0`

`0` represents the empty datastring, or null, and is the halt condtion.

Arithmetic BCT programs require an initial starting input of at least `2` to perform any active computation.
