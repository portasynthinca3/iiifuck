# iiifuck
A Brainfuck clone that uses only three characters: I, l and |. That is, uppercase `i`, lowercase `L` and a `|` pipe. A combination of two of these characters forms an instruction. Here's the mapping:
```
| iiifuck instruction | brainfuck instruction |
|---------------------|-----------------------|
|          II         |           >           |
|          Il         |           <           |
|          I|         |           +           |
|          lI         |           -           |
|          ll         |           .           |
|          l|         |           ,           |
|          |I         |           [           |
|          |l         |           ]           |
```

# usage
  - `python3 iiifuck.py filename.iiif` to run an iiifuck program
  - `python3 iiitransp.py transpile filename.bf` to convert a brainfuck program to an iiifuck one
  - `python3 iiitransp.py detranspile filename.iiif` to convert an iiifuck program to a brainfuck one

# example

```I|I|I|I|I|I|I|I|I|I||IIII|I|I|I|I|I|I|III|I|I|I|I|I|I|I|I|I|III|I|I|III|IlIlIlIllI|lIII|I|llIII|llI|I|I|I|I|I|I|llllI|I|I|llIII|I|llIlIlI|I|I|I|I|I|I|I|I|I|I|I|I|I|I|llIIllI|I|I|lllIlIlIlIlIlIlllIlIlIlIlIlIlIlIllIII|llIIll```

Prints `Hello, World!`