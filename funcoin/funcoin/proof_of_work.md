###### Proof Of Work - Explained with the email example

Hashed Method Authentication Code Protocol ( Email )

1. Alice and Bob both share a secret phrase S.
2. Alice then creates a hash H of the message M with the secret appended to the end of the message:
    H = hash(M + S).
3. Alice sends H and M to Bob (the message and the computed hash).
4. Bob checks the message integrity by calculating H himself to see if it’s the same as the hash Alice advertised.

The idea is to add constraints on the hash. This causes the sender of the email to do some amount of computational work before sending an email. So it becomes expensive for a spammer to send spam.

Constraint Example: HashCash - The hash must be lower than a certain number. This seems simple but since crytographic hash functions output a random number for a given input, we cannot ensure that an email body will be hashed to a certain number. The only thing we can do is to add/remove arbitrary data in the email body and keep trial & erroring until the hash satisfies the constraint.

This is proof of work. The work is proven by displaying a particular hash, and it can be easily verified. The pattern is -> something difficult to generate and easy to verify.