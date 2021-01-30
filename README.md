# ldif-decode
Decode base64 strings in OpenLDAP LDIF output.

## Features
- Takes input from LDIF file or stdin (standard input).
- Decodes single and multiline base64 encoded attributes.
- Prints error messages to stderr (standard error output).

## Usage
```
ldif-decode.py file.ldif
```
or
```
ldapsearch | ldif-decode.py
```
## Examples
```
$ ldapsearch -LLL givenName
...
givenName:: RMO2cnRl
...

$ ldapsearch -LLL givenName | ldif-decode.py
...
givenName:: Dörte
...
```
```
$ ldapsearch -LLL userPassword
...
userPassword:: e0NSWVBUfSQ2JHJvdW5kcz0yMDAwMDAwJEw0aFpTT3RoL2tpN0wkaDFXQ1Fxejl
 CWkV2cURRNVR2aGVoUU45L3BxL21zMEZnTzJqWEc5UlBWVnU4SVRjNVg3eE13MEJZSGNrOG1veFA1
 S2thVmhQOVhvQVBDQUIueGRkdjA=
...

$ ldapsearch -LLL userPassword | ldif-decode.py
...
userPassword:: {CRYPT}$6$rounds=2000000$L4hZSOth/ki7L$h1WCQqz9BZEvqDQ5TvhehQN9/pq/ms0FgO2jXG9RPVVu8ITc5X7xMw0BYHck8moxP5KkaVhP9XoAPCAB.xddv0
...
