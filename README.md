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

    localhost:8080/b/011/0

will redirect to

     localhost:8080/13/0

## Bitstring to Gödel numbering

The numbering convention used in this arithmetic implementation of Bitwise Cyclic Tag is simply interpreting a bitstring as a [little-endian](https://en.wikipedia.org/wiki/Endianness) [bijective base-2](https://en.wikipedia.org/wiki/Bijective_numeration) numeral.

This can be accomplished as a two step process:

* Convert the bitstring to its arithmetic (place value index) order (i.e. reverse the string)
* Convert the symbols to bijective base-2 (`1` → `2`, `0` → `1`)

A BCT program bitstring is processed left-ro-right, as strings are generally read. For ease of arithmetic processing it is helpful to use this processing order index as the place value of each bit.
The left-most bit is treated as the least significant bit of the resulting numeral. This results in reversing the original bitstring from its LTR little-endian order to the conventional numeric positional notation (BE).
`01000` → `00010`

Now interpret this as a bijective base-2 numeral. This allows both symbols to be meaningful in the MSB position, unlike in binary where leftmost zeros do not affect the value.
`00010` → `11121`

`11121` as a bijective base-2 numeral represents 33.

This can be checked by passing the bitstring as a program with a null data string to the abct endpoint
https://abctag.herokuapp.com/b/01000/0 which will redirect to the arithmetic version: https://abctag.herokuapp.com/33/0/

```
{
  "program": "01000",
   "data": ""
}
```

| bitstring (LE) | bijective base-2 | value |
|:---------------|-----------------:|------:|
|           |                  | 0 |
| `0`       |  1               | 1 |
| `1`       |  2               | 2 |
| `00`      | 11               | 3 |
| `10`      | 12               | 4 |
| `01`      | 21               | 5 |
| `11`      | 22               | 6 |
| `000`     | 111              | 7 |
| `100`     | 112              | 8 |
| `010`     | 121              | 9 |
| `110`     | 122              | 10|


Note, the above is just one of many possible conventions for converting bitstrings into numeric values for arithmetic interpretation of Bitwise Cyclic Tag.
Other conventions will require different arithmetic equations, but the underlying cyclic tag concept and computation will be the same. This implementation uses a slightly different Gödel numbering from the one described at [esolangs.org](https://esolangs.org/wiki/Bitwise_Cyclic_Tag#Arithmetic_interpretation_of_BCT).
The program string numbering is identical (reverse the bitstring), but the esolangs' article uses a different system for the data string where the bitstring is *not* reversed. I didn't want to implent two bitstring conversions, so here program and data bitstrings are converted the same way.
For our data strings: data is appended as the MSB, and deletions occur at the LSB (i.e. bitshift right, or divde-by-2).

## CLI version

There is also a command line utility for testing:

    ./abct-cli $(<examples/hello-world.abct) 2
    
2 is the initial data value representing a binary bitstring `1`

1 represents binary bitstring `0`

0 represents the empty datastring, or `null`, and is the halt condtion.

Arithmetic BCT programs require an initial starting input of at least 2 to perform any active computation.

### Truth machine example usage

For the 'zero' case (BCT `10` = bijective base-2 `12` = input value `4`):

    ./abct-cli $(<examples/truth-machine.abct) 4 | grep OUTPUT

which gives a single output line:

    39217909666694773142903776444132544299164543308230190564477239295	3026142152962	11000000100100110000010000101001000000110	OUTPUT>>>	0

For the 'one' case (BCT `11` = bijective base-2 `22` = input value `6`):

    ./abct-cli $(<examples/truth-machine.abct) 6 | grep OUTPUT
 
 which repeats indefinitely:
 
    39217909666697766298257028305177290289800352374943150376712755052	12104570709002	1101000000100100110001010000101001000000110	OUTPUT>>>	1
 
 The CLI output columns represent:
 * PROGRAM VALUE
 * DATA VALUE
 * DATA as binary
 * The string "OUTPUT>>>" if any output was completed on this step
 * The encoded OUTPUT completed on this step, if any
