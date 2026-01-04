## What happens behind the scenes when you run "print("hello world")"

# Python reads the code (Lexing and Parsing)

a. Lexing (Tokenization)
 -- Python breaks the line of code into tokens 
 ---- print -> Identifier
 ---- ( -> Open parenthesis
 ---- "hello world" -> String literal
 ---- ) -> Close parenthesis

b. Parsing
 -- Python checks:
 ---- Is the syntax valid
 ---- Does this follow python grammar

 NB: If something is wrong, you get a syntax error

# Bytecode compilation 
-- The code is compiled into bytecode -- PVM
  eg: -- LOAD_NAME print
      -- LOAD_CONST "hello world"
      -- CALL_FUNCTION 1
      -- RETURN_VALUE 

  nb: Bytecode may be cached in __pycache__
  -- The PVM execute the code
   --- inside print if needed, __str__() will convert to string

 