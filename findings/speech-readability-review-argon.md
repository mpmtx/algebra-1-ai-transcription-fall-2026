# Speech Readability Review (Argon)

Independent verification of `findings/speech-readability-review-claude.md` and full-corpus readability & punctuation review across all 19 lecture files (`content/step4-*.tex`, Weeks 1–10) at commit `97f36b5` (`content/` matching `e9c395c`), against the book's conventions and `C:\Users\miche\latex\prompt-engineering\speech-refinement\speech-refinement.md` ("Advanced Punctuation Reference", lines 433–555).

---

## Proof of Reading to the End (Week 10 Wednesday)

In `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex` (lines 1034–1038, `\begin{speech}[00:41:47 - 00:42:30]`), the final speech paragraph (line 1037) is:

```latex
And you can imagine there's a set of $p$-Sylow subgroups, they're all conjugate, so the group acts on that by conjugation. So, you should study the conjugation action on that. We can discuss it next time if you have any questions, but... I recommend really trying to prove this.
```

The **exact last speech sentence of Week 10 Wednesday** is:

> `We can discuss it next time if you have any questions, but... I recommend really trying to prove this.`

---

## Part I: Verification of Claude's Findings (`findings/speech-readability-review-claude.md`)

### Category A — Unnatural / Garbled Sentences

#### A1. `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex:1184` — **Confirmed**
- **Current (line 1184):**
  ```latex
  And the proof is just that: the proof is that this rotation of this cube --- this is a group --- and there's a homomorphism to the permutation group of the long diagonals, which is $S_4$ \inlinemetanote{writes: $\operatorname{Rot}(\square) \xrightarrow{\phi} S_4$}. And the claim is this: rotations go to permutations of the long diagonals \inlinemetanote{writes: $\phi \colon$ rotations $\to$ permutations of the long diagonals}. I say long diagonals all the time here, but I mean, you know, if you pick two points on the same face, then there's kind of a short diagonal that's on the side, but there's four... so, every time you rotate, you permute the long diagonals. And the claim is this is an isomorphism \inlinemetanote{writes: This is an iso.}.
  ```
- **Proposed (line 1184):**
  ```latex
  And the proof is just that: this rotation group of the cube is a group, and there's a homomorphism to the permutation group of the long diagonals, which is $S_4$ \inlinemetanote{writes: $\operatorname{Rot}(\square) \xrightarrow{\phi} S_4$}. And the claim is this: rotations go to permutations of the long diagonals \inlinemetanote{writes: $\phi \colon$ rotations $\to$ permutations of the long diagonals}. I say long diagonals all the time here, but I mean, you know, if you pick two points on the same face, then there's kind of a short diagonal that's on the side, but there's four... so, every time you rotate, you permute the long diagonals. And the claim is this is an isomorphism \inlinemetanote{writes: This is an iso.}.
  ```

#### A2. `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex:1562` — **Confirmed**
- **Current (line 1562):**
  ```latex
  And to read this, we can put everything explicit. So, this is the action, this is group multiplication \inlinemetanote{draws arrows downward from \qt{Grp.} to the dot in $g_2 \cdot g_1$ and from \qt{$\phi$} to the outer dot before $t$}. Here, this is the action and this is group multiplication \inlinemetanote{draws a downward arrow from \qt{$\phi$} to the inner dot of $g_1 \cdot t$, and an upward arrow from \qt{group} below to the outer dot after $g_2$, a slip for $\phi$ that he corrects after the student's question below}. Okay? So, does that make sense?
  ```
- **Proposed (line 1562):**
  ```latex
  And to read this, we can make everything explicit. So, this is the action, this is group multiplication \inlinemetanote{draws arrows downward from \qt{Grp.} to the dot in $g_2 \cdot g_1$ and from \qt{$\phi$} to the outer dot before $t$}. Here, this is the action and this is group multiplication \inlinemetanote{draws a downward arrow from \qt{$\phi$} to the inner dot of $g_1 \cdot t$, and an upward arrow from \qt{group} below to the outer dot after $g_2$, a slip for $\phi$ that he corrects after the student's question below}. Okay? So, does that make sense?
  ```

#### A3. `content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:1478` — **Confirmed (with punctuation adjustment)**
- **Note:** Claude's first suggestion (`otherwise it would divide; so long division says ...`) violates `speech-refinement.md` §2 (semicolons in `speech` are for complex lists only, never between independent clauses) and §3 (mandatory comma after introductory `So,`). Splitting with a period (`... otherwise it would divide. So, long division says ...`) or using Claude's second suggestion (`so, the division algorithm says ...`) satisfies the punctuation rules.
- **Current (line 1478):**
  ```latex
  It's not here, so, we can't have zero, because otherwise it would be divisible, right? So, this $r$ is strictly between zero and $n$. That's the logic: we say \qt{suppose not}, and we use the division algorithm. It can't be zero, because otherwise it would divide, so, long division says $r$ is between zero and $n$. But then $r$ is a lesser positive integer in $I$, which is a contradiction: \inlinemetanote{writes \qt{but $r$ is a less pos. int. in $I$ (contradiction)}}.
  ```
- **Proposed (line 1478):**
  ```latex
  It's not here, so, we can't have zero, because otherwise it would be divisible, right? So, this $r$ is strictly between zero and $n$. That's the logic: we say \qt{suppose not}, and we use the division algorithm. It can't be zero, because otherwise it would divide. So, long division says $r$ is between zero and $n$. But then $r$ is a lesser positive integer in $I$, which is a contradiction: \inlinemetanote{writes \qt{but $r$ is a less pos. int. in $I$ (contradiction)}}.
  ```

#### A4. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:307` — **Confirmed (plus post-dash repetition trim per §5)**
- **Note:** In addition to `the ways ... is:` $\to$ `the way ... is:`, the post-dash repetition `--- $f$ non-zero,` directly violates `speech-refinement.md` §5 (*"Trimming Repetitions Around Em-Dash Interruptions"*).
- **Current (line 307):**
  ```latex
  And the ways we think about this is: given any $f$ --- always, you know, non-zero \inlinemetanote{writes: $f \in R[x], \; f \neq 0$} --- $f$ non-zero, then we can write $f$ is equal to the content, where we just pull out the $\operatorname{GCD}$ \inlinemetanote{writes: $\implies f = C(f)$}, and then we multiply by what's left, and this is what's called primitive \inlinemetanote{writes \qt{$\cdot f^*$} and draws an arrow from $f^*$ up to \qt{primitive}}. And the definition of the term primitive was: the content is equal to $1$ up to a unit \inlinemetanote{draws an arrow from $f^*$ down to \qt{$C(f^*) \stackrel{u}{=} 1$}}.
  ```
- **Proposed (line 307):**
  ```latex
  And the way we think about this is: given any $f$ --- always, you know, non-zero \inlinemetanote{writes: $f \in R[x], \; f \neq 0$} --- then we can write $f$ is equal to the content, where we just pull out the $\operatorname{GCD}$ \inlinemetanote{writes: $\implies f = C(f)$}, and then we multiply by what's left, and this is what's called primitive \inlinemetanote{writes \qt{$\cdot f^*$} and draws an arrow from $f^*$ up to \qt{primitive}}. And the definition of the term primitive was: the content is equal to $1$ up to a unit \inlinemetanote{draws an arrow from $f^*$ down to \qt{$C(f^*) \stackrel{u}{=} 1$}}.
  ```

#### A5. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:556` — **Confirmed**
- **Current (line 556):**
  ```latex
  And the only problem here --- so, this is a polynomial with coefficients in $Q[x]$ (i.e., $Q$) --- so this has some, you know, some $c_6 x^6 + c_5 x^5 + \dots + c_0$ \inlinemetanote{writes: $\hat{q} = c_6 x^6 + c_5 x^5 + \dots + c_0$}. Now, all of these coefficients are in the field of fractions of $R$ \inlinemetanote{writes: $c_i \in Q(R)$}. So, I can write them instead as elements in $R$: $\frac{a_6}{b_6}$, $\frac{a_5}{b_5}$ --- this is kind of explicit --- $\frac{a_0}{b_0}$, where all of these $a_i, b_i$ are in $R$ and moreover the denominators are not zero \inlinemetanote{writes \qt{$\frac{a_6}{b_6}, \frac{a_5}{b_5}, \dots, \frac{a_0}{b_0}$} above $c_6, c_5, \dots, c_0$ and writes \qt{$a_i, b_i \in R, \; b_i \neq 0$}}, right? So, I can just write it like this.
  ```
- **Proposed (line 556):**
  ```latex
  And the only problem here --- so, this is a polynomial with coefficients in $Q[x]$ (i.e., $Q$) --- is that this has some, you know, some $c_6 x^6 + c_5 x^5 + \dots + c_0$ \inlinemetanote{writes: $\hat{q} = c_6 x^6 + c_5 x^5 + \dots + c_0$}. Now, all of these coefficients are in the field of fractions of $R$ \inlinemetanote{writes: $c_i \in Q(R)$}. So, I can write them instead as elements in $R$: $\frac{a_6}{b_6}$, $\frac{a_5}{b_5}$ --- this is kind of explicit --- $\frac{a_0}{b_0}$, where all of these $a_i, b_i$ are in $R$ and moreover the denominators are not zero \inlinemetanote{writes \qt{$\frac{a_6}{b_6}, \frac{a_5}{b_5}, \dots, \frac{a_0}{b_0}$} above $c_6, c_5, \dots, c_0$ and writes \qt{$a_i, b_i \in R, \; b_i \neq 0$}}, right? So, I can just write it like this.
  ```

#### A6. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:1789` — **Confirmed**
- **Current (line 1789):**
  ```latex
  All right, and I just consider all of these: $x^4, x^5$, and eventually there'll be some $x^{17}$, and eventually $x^{691}$, and so on \inlinemetanote{writes: $x^4, x^5, \dots, x^{17}, \dots, x^{691}, \dots$}. And you'll see that there are infinitely many elements in this list, but $G$ is a finite group. So, two of them have to be... there must be that some of these are coincident; these cannot all be distinct \inlinemetanote{writes \qt{Can not all be distinct} with a brief note underneath regarding $G$}. They can't all be distinct, because $G$ is finite and this list is infinite. I hope you view that as a solid argument. Sometimes this is called something like the pigeonhole principle, or something like that; that seems like a fancy word for it.
  ```
- **Proposed (line 1789):**
  ```latex
  All right, and I just consider all of these: $x^4, x^5$, and eventually there'll be some $x^{17}$, and eventually $x^{691}$, and so on \inlinemetanote{writes: $x^4, x^5, \dots, x^{17}, \dots, x^{691}, \dots$}. And you'll see that there are infinitely many elements in this list, but $G$ is a finite group. So, two of them have to be... some of these must be coincident; these cannot all be distinct \inlinemetanote{writes \qt{Can not all be distinct} with a brief note underneath regarding $G$}. They can't all be distinct, because $G$ is finite and this list is infinite. I hope you view that as a solid argument. Sometimes this is called something like the pigeonhole principle, or something like that; that seems like a fancy word for it.
  ```

#### A7. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:1429` — **Confirmed**
- **Current (line 1429):**
  ```latex
  I mean, most elements will work; there's some... if you're unlucky, you'll pick the wrong one. Well, it'd be bad to take $(1\,2)$, but if you take anything else, like $(1\,3)$ --- the inverse of $(1\,3)$ is $(1\,3)$ \inlinemetanote{writes: $(1\,3)(1\,2)(1\,3)$} --- so this is $x$ \inlinemetanote{points at the first $(1\,3)$} and that's $x$ inverse \inlinemetanote{points at the second $(1\,3)$}. And if you multiply this out, you get: $1$ goes to $3$, $3$ goes to $1$, so $1$ is fixed here; $2$ goes to $1$, $1$ goes to $3$, so this is $(2\,3)$ \inlinemetanote{writes: $= (2\,3)$}. Okay?
  ```
- **Proposed (line 1429):**
  ```latex
  I mean, most elements will work; there's some... if you're unlucky, you'll pick the wrong one. Well, it'd be bad to take $(1\,2)$, but you can take anything else, like $(1\,3)$ --- the inverse of $(1\,3)$ is $(1\,3)$ \inlinemetanote{writes: $(1\,3)(1\,2)(1\,3)$} --- so this is $x$ \inlinemetanote{points at the first $(1\,3)$} and that's $x$ inverse \inlinemetanote{points at the second $(1\,3)$}. And if you multiply this out, you get: $1$ goes to $3$, $3$ goes to $1$, so $1$ is fixed here; $2$ goes to $1$, $1$ goes to $3$, so this is $(2\,3)$ \inlinemetanote{writes: $= (2\,3)$}. Okay?
  ```

#### A8. `content/step4-2026-09-23-wednesday-week2-algebra-1-offset-final.tex:1095` — **Confirmed**
- **Current (line 1095):**
  ```latex
  This great 20th-century Hungarian mathematician (i.e., Paul Erd\H{o}s) said that if numbers aren't beautiful, I don't know what is. That's kind of the mathematical perspective on numbers.
  ```
- **Proposed (line 1095):**
  ```latex
  This great 20th-century Hungarian mathematician said that if numbers aren't beautiful, I don't know what is. That's kind of the mathematical perspective on numbers.
  ```

#### A9. `content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:2017-2019` — **Confirmed (with structural note)**
- **Current (lines 2017–2019):**
  ```latex
  \begin{speech}[01:11:29 - 01:12:07]
  \inlinemetanote{erases the graph of $\sin(1/x)$ and thoroughly cleans the lower blackboard to prepare for the category axioms}
  \end{speech}
  ```
- **Proposed:** Because a `content` block (`1965–2015`) separates this from the preceding speech block (`1953–1963`, `[01:11:01 - 01:11:29]`) and a `hidden` block + `\subsection` separate it from the next speech block (`2031`, `[01:12:07 - 01:14:06]`), delete lines `2017–2019`, change line `1953` to `\begin{speech}[01:11:01 - 01:12:07]`, and append the metanote to line `1962`:
  ```latex
  Okay, let's see... All right, so, let me state these properties carefully. \inlinemetanote{erases the graph of $\sin(1/x)$ and thoroughly cleans the lower blackboard to prepare for the category axioms}
  ```

---

### Category B — Convention & Consistency Issues

#### B1. `content/step4-2026-10-06-tuesday-week4-algebra-1-offset-final.tex:1773, 1779, 1825, 1827, 1910` — **Confirmed**
- Keep line `1773` as `(i.e., Gaussian rationals $\mathbb{Q}[i]$)` on first occurrence; shorten the four subsequent occurrences on lines `1779`, `1825`, `1827`, and `1910` to `(i.e., $\mathbb{Q}[i]$)`:
- **Current (line 1779):**
  ```latex
  That says that $\mathbb{Q}[x] \bmod$ the kernel of $f$ is isomorphic to the image of $f$, which is the Gaussian integers (i.e., Gaussian rationals $\mathbb{Q}[i]$), which, by the way, is a field! \inlinemetanote{writes: $\faktor{\mathbb{Q}[x]}{\ker(f)} \cong \operatorname{Im}(f) = \mathbb{Q}[i]$} It's a domain, and it's a field. 
  ```
- **Proposed (line 1779):**
  ```latex
  That says that $\mathbb{Q}[x] \bmod$ the kernel of $f$ is isomorphic to the image of $f$, which is the Gaussian integers (i.e., $\mathbb{Q}[i]$), which, by the way, is a field! \inlinemetanote{writes: $\faktor{\mathbb{Q}[x]}{\ker(f)} \cong \operatorname{Im}(f) = \mathbb{Q}[i]$} It's a domain, and it's a field. 
  ```
- **Current (line 1825):**
  ```latex
  Okay? If the answer is yes, then I've answered that question! Because here it is, it's $\mathbb{Q}[x] \bmod$... and spoiler: it's going to be yes. If it were yes, then I will have answered this question, because I've computed the kernel here, and I've showed it's isomorphic to the ring of Gaussian integers (i.e., Gaussian rationals $\mathbb{Q}[i]$). 
  ```
- **Proposed (line 1825):**
  ```latex
  Okay? If the answer is yes, then I've answered that question! Because here it is, it's $\mathbb{Q}[x] \bmod$... and spoiler: it's going to be yes. If it were yes, then I will have answered this question, because I've computed the kernel here, and I've showed it's isomorphic to the ring of Gaussian integers (i.e., $\mathbb{Q}[i]$). 
  ```
- **Current (line 1827):**
  ```latex
  Actually, that is a way of writing the ring of Gaussian integers (i.e., Gaussian rationals $\mathbb{Q}[i]$) in slightly hidden form. All I have to do is prove this thing is the kernel.
  ```
- **Proposed (line 1827):**
  ```latex
  Actually, that is a way of writing the ring of Gaussian integers (i.e., $\mathbb{Q}[i]$) in slightly hidden form. All I have to do is prove this thing is the kernel.
  ```
- **Current (line 1910):**
  ```latex
  And the final conclusion, using the First Isomorphism Theorem, is this: $\mathbb{Q}[x] \bmod (x^2 + 1)$ is isomorphic to this ring of Gaussian integers (i.e., Gaussian rationals $\mathbb{Q}[i]$). \inlinemetanote{writes: $\faktor{\mathbb{Q}[x]}{(x^2+1)} \cong \mathbb{Q}[i]$} 
  ```
- **Proposed (line 1910):**
  ```latex
  And the final conclusion, using the First Isomorphism Theorem, is this: $\mathbb{Q}[x] \bmod (x^2 + 1)$ is isomorphic to this ring of Gaussian integers (i.e., $\mathbb{Q}[i]$). \inlinemetanote{writes: $\faktor{\mathbb{Q}[x]}{(x^2+1)} \cong \mathbb{Q}[i]$} 
  ```

#### B2. `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:1425, 1731` — **Confirmed**
- **Current (line 1425):**
  ```latex
  And then I write down my equation, which says that the size of $T$ is equal to the sum over all of these $x_i$, and then the size of the orbit \inlinemetanote{writes \qt{$|T| = \sum_{x_i} |\operatorname{Orb}(x_i)|$} and writes \qt{$\binom{n}{p^k}$} underneath $|T|$}. So, this is an entirely uncontroversial statement: I've just taken this $T$ (spoken as \qt{$P$}, i.e., $T$) and I've cut it up into the orbits. And now I want to apply the Orbit-Stabilizer theorem for each one of these --- remember, this is $n$, $p^k$ --- so to each one of these I apply the Orbit-Stabilizer theorem.
  ```
- **Proposed (line 1425):**
  ```latex
  And then I write down my equation, which says that the size of $T$ is equal to the sum over all of these $x_i$, and then the size of the orbit \inlinemetanote{writes \qt{$|T| = \sum_{x_i} |\operatorname{Orb}(x_i)|$} and writes \qt{$\binom{n}{p^k}$} underneath $|T|$}. So, this is an entirely uncontroversial statement: I've just taken this $P$ (i.e., $T$) and I've cut it up into the orbits. And now I want to apply the Orbit-Stabilizer theorem for each one of these --- remember, this is $n$, $p^k$ --- so to each one of these I apply the Orbit-Stabilizer theorem.
  ```
- **Current (line 1731):**
  ```latex
  But that's not the set we're interested in. We're interested in this set $T$, which is the $p^k$-element subsets of $\widehat{T}$ (spoken as \qt{$T$}, i.e., $\widehat{T}$) \inlinemetanote{writes: $T = \{ p^k\text{-elmt subsets of } \widehat{T} \}$}. And on the top board, what we're really interested in: we must understand the $\mathbb{Z} \bmod p$ to the $k$ $\mathbb{Z}$ fixed points on this set $T$ \inlinemetanote{writes: We must understand the $\faktor{\mathbb{Z}}{p^k\mathbb{Z}}$-fixed pts on $T$}.
  ```
- **Proposed (line 1731):**
  ```latex
  But that's not the set we're interested in. We're interested in this set $T$, which is the $p^k$-element subsets of $T$ (i.e., $\widehat{T}$) \inlinemetanote{writes: $T = \{ p^k\text{-elmt subsets of } \widehat{T} \}$}. And on the top board, what we're really interested in: we must understand the $\mathbb{Z} \bmod p$ to the $k$ $\mathbb{Z}$ fixed points on this set $T$ \inlinemetanote{writes: We must understand the $\faktor{\mathbb{Z}}{p^k\mathbb{Z}}$-fixed pts on $T$}.
  ```

#### B3. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:516` — **Confirmed**
- **Current (line 516):**
  ```latex
  Theorem B, for tomorrow, \inlinemetanote{writes: Thm B:} is that if $R$ is a PID (i.e., a UFD), then the polynomial ring is a U... Sorry, screwed up. \inlinemetanote{erases \qt{PID} and writes: UFD} Is a UFD, then the polynomial ring is a UFD. \inlinemetanote{writes: then the $R[x]$ is a UFD.} Then the polynomial ring is a UFD.
  ```
- **Proposed (line 516):**
  ```latex
  Theorem B, for tomorrow, \inlinemetanote{writes: Thm B:} is that if $R$ is a PID, then the polynomial ring is a U... Sorry, screwed up. \inlinemetanote{erases \qt{PID} and writes: UFD} Is a UFD, then the polynomial ring is a UFD. \inlinemetanote{writes: then the $R[x]$ is a UFD.}
  ```

#### B4. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:746` — **Confirmed**
- **Current (line 746):**
  ```latex
  So, this is called $A_n$, and $A_n$ is for \newterm{alternating group}: $A_n$ inside of $S_n$, and this $A_n$ is by definition the kernel of the sign homomorphism \inlinemetanote{writes: $A_n \stackrel{\text{def}}{=} \ker(\operatorname{Sign})$}. In other words, equivalently, $A_n$ is equal to the subgroup of even permutations \inlinemetanote{writes \qt{$A_n =$ the subgrp of even permutations}}. Because the even ones are $+1$ (speaker says \qt{one}), that's in the kernel. So, that's another way to think about it.
  ```
- **Proposed (line 746):**
  ```latex
  So, this is called $A_n$, and $A_n$ is for \newterm{alternating group}: $A_n$ inside of $S_n$, and this $A_n$ is by definition the kernel of the sign homomorphism \inlinemetanote{writes: $A_n \stackrel{\text{def}}{=} \ker(\operatorname{Sign})$}. In other words, equivalently, $A_n$ is equal to the subgroup of even permutations \inlinemetanote{writes \qt{$A_n =$ the subgrp of even permutations}}. Because the even ones are $1$, that's in the kernel. So, that's another way to think about it.
  ```

#### B5. `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex:1217` — **Confirmed (plus missing subject `it` after ellipsis)**
- **Current (line 1217):**
  ```latex
  Of course, if it's finite-dimensional, of course it has a basis. And this issue is about whether, if you have some massively infinite-dimensional field (i.e., vector space)... has a basis. And the traditional way to do this is an implication (application?) of Zorn's lemma, which is related to the axiom of choice in logic --- not my favorite direction to think about, but we will say a little bit about it. But...
  ```
- **Proposed (line 1217):**
  ```latex
  Of course, if it's finite-dimensional, it has a basis. And this issue is about whether, if you have some massively infinite-dimensional field (i.e., vector space)... it has a basis. And the traditional way to do this is an implication (i.e., application) of Zorn's lemma, which is related to the axiom of choice in logic --- not my favorite direction to think about, but we will say a little bit about it. But...
  ```

#### B6. `content/step4-2026-09-23-wednesday-week2-algebra-1-offset-final.tex:538` — **Confirmed (optional: natural board-writing echo)**
- **Current (line 538):**
  ```latex
  Yeah, $m$ is prime. $m$ is prime. \inlinemetanote{writes \qt{$\mathbb{Z}/m\mathbb{Z}$ is a domain $\iff m$ is prime}}
  ```
- **Proposed (line 538, if trimmed):**
  ```latex
  Yeah, $m$ is prime. \inlinemetanote{writes \qt{$\mathbb{Z}/m\mathbb{Z}$ is a domain $\iff m$ is prime}}
  ```

#### B7. `content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex:248` — **Confirmed**
- **Current (line 248):**
  ```latex
  I am not saying the other way around. If I have an ideal here, I can also take the image of that ideal. I'm not saying that's an ideal, and it may not be an ideal. An example, for example: if you take $\mathbb{Z}$ goes to $\mathbb{Q}$ \inlinemetanote{writes: $\mathbb{Z} \hookrightarrow \mathbb{Q}$}, and I take the ideal $2\mathbb{Z}$ \inlinemetanote{writes: $2\mathbb{Z}$}, that's an ideal here. If I view it here --- this is an injection, this is still $2\mathbb{Z}$, so to speak \inlinemetanote{writes: $2\mathbb{Z}$} --- that's not an ideal here. Is that clear?
  ```
- **Proposed (line 248):**
  ```latex
  I am not saying the other way around. If I have an ideal here, I can also take the image of that ideal. I'm not saying that's an ideal, and it may not be an ideal. For example: if you take $\mathbb{Z}$ goes to $\mathbb{Q}$ \inlinemetanote{writes: $\mathbb{Z} \hookrightarrow \mathbb{Q}$}, and I take the ideal $2\mathbb{Z}$ \inlinemetanote{writes: $2\mathbb{Z}$}, that's an ideal here. If I view it here --- this is an injection, this is still $2\mathbb{Z}$, so to speak \inlinemetanote{writes: $2\mathbb{Z}$} --- that's not an ideal here. Is that clear?
  ```

#### B8. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:289` — **Confirmed**
- **Current (line 289):**
  ```latex
  And so, this means that $z$ is in $I$ and $z$ is in $J$ \inlinemetanote{writes \qt{$z \in I$} and \qt{$z \in J$}}. That's how that's how you're zero $\bmod I$ and $J$.
  ```
- **Proposed (line 289):**
  ```latex
  And so, this means that $z$ is in $I$ and $z$ is in $J$ \inlinemetanote{writes \qt{$z \in I$} and \qt{$z \in J$}}. That's how you're zero $\bmod I$ and $J$.
  ```

#### B9. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:1600` — **Confirmed**
- **Current (line 1600):**
  ```latex
  Of course, the inverse of $e$ is, of course, $e$, right \inlinemetanote{draws an arrow from $e$ to $e$}? Neutral element. What's the inverse of this element \inlinemetanote{points at $(1\,2)$}? \inlinemetanote{inaudible answer from a student} Yeah. Itself \inlinemetanote{draws an arrow from $(1\,2)$ to $(1\,2)$}.
  ```
- **Proposed (line 1600):**
  ```latex
  Of course, the inverse of $e$ is $e$, right \inlinemetanote{draws an arrow from $e$ to $e$}? Neutral element. What's the inverse of this element \inlinemetanote{points at $(1\,2)$}? \inlinemetanote{inaudible answer from a student} Yeah. Itself \inlinemetanote{draws an arrow from $(1\,2)$ to $(1\,2)$}.
  ```

#### B10. `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex:317` — **Confirmed**
- **Current (line 317):**
  ```latex
  So, anyway, in this case we find that the order of the elements divides the order of the group, so one can wonder: is this always the case \inlinemetanote{writes: Is this always true?}? So, specifically, if $x$ is an element of $G$, a finite group, does the order of $x$ divide the order of $G$ \inlinemetanote{writes: If $x \in G$ finite group, does $\operatorname{Ord}(x) \mid |G|$?}? That's a very specific question, and the answer is going to be yes \inlinemetanote{writes: YES}. And actually, the proof is that actually a much more general property holds, and that's the main topic of today's lecture...
  ```
- **Proposed (line 317):**
  ```latex
  So, anyway, in this case we find that the order of the elements divides the order of the group, so one can wonder: is this always the case \inlinemetanote{writes: Is this always true?}? So, specifically, if $x$ is an element of $G$, a finite group, does the order of $x$ divide the order of $G$ \inlinemetanote{writes: If $x \in G$ finite group, does $\operatorname{Ord}(x) \mid |G|$?}? That's a very specific question, and the answer is going to be yes \inlinemetanote{writes: YES}. And actually, the proof is that a much more general property holds, and that's the main topic of today's lecture...
  ```

#### B11. `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex:755` — **Confirmed**
- **Current (line 755):**
  ```latex
  And then we take this stuff out and we go with the points that are remaining, again. Now we start with $2$: $2$ has to go, and has to be a cycle, and has to come back to $2$, and it can never interfere with the cycle here because of the bijective property. So, you just take out another cycle. You do that, and now you get the cycle decomposition. Associated to the cycle decomposition... so, let's pretend here $2$ goes to $3$ and comes back, then this would be $(2\,3)$ \inlinemetanote{draws arrows between $2$ and $3$ and writes: $(2\,3)$}. And what's left? $7$ by himself \inlinemetanote{draws a loop at $7$ and writes: $(7)$}, all right? So, that would be in this case, but that's how you visually see it.
  ```
- **Proposed (line 755):**
  ```latex
  And then we take this stuff out and we go with the points that are remaining, again. Now we start with $2$: $2$ has to go, and has to be a cycle, and has to come back to $2$, and it can never interfere with the cycle here because of the bijective property. So, you just take out another cycle. You do that, and now you get the cycle decomposition. So, let's pretend here $2$ goes to $3$ and comes back, then this would be $(2\,3)$ \inlinemetanote{draws arrows between $2$ and $3$ and writes: $(2\,3)$}. And what's left? $7$ by himself \inlinemetanote{draws a loop at $7$ and writes: $(7)$}, all right? So, that would be in this case, but that's how you visually see it.
  ```

#### B12. `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:757` — **Confirmed**
- **Current (line 757):**
  ```latex
  The next idea is that we let $T$ --- that's the one we're going to actually play with with the actions --- be the set of $p^k$-element subsets of $\widehat{T}$ \inlinemetanote{writes: $T = \text{set of } p^k\text{-element subsets of } \widehat{T}$}. Okay? Surely I'm allowed to do this also.
  ```
- **Proposed (line 757):**
  ```latex
  The next idea is that we let $T$ --- that's the one we're going to actually play with for the actions --- be the set of $p^k$-element subsets of $\widehat{T}$ \inlinemetanote{writes: $T = \text{set of } p^k\text{-element subsets of } \widehat{T}$}. Okay? Surely I'm allowed to do this also.
  ```

#### B13. Remaining `uh` / `um` Fillers (1 in `speech`, 9 in `student`) — **Confirmed (plus 3 extra grammar/stutter fixes in the same student lines)**
1. **`content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:534`** (`speech`):
   - **Current:** `Uh, but it's a confusing formula, like you might think... okay, so, this is the part that I view as perhaps related to things that may have been in school.`
   - **Proposed:** `But it's a confusing formula, like you might think... okay, so, this is the part that I view as perhaps related to things that may have been in school.`
2. **`content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:454`** (`student` — also fixes doubled `if`):
   - **Current:** `No, because we run into a problem for $-1$, because, um, if we had if $f(-1)$...`
   - **Proposed:** `No, because we run into a problem for $-1$, because if we had $f(-1)$...`
3. **`content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:462`** (`student`):
   - **Current:** `So, $f$ goes from, uh, $\mathbb{R}^*$ to $\mathbb{R}^*_{>0}$.`
   - **Proposed:** `So, $f$ goes from $\mathbb{R}^*$ to $\mathbb{R}^*_{>0}$.`
4. **`content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:486`** (`student` — also fixes `its times itself` $\to$ `it times itself`):
   - **Current:** `$f(-1) \cdot f(-1)$ will be $1$, so the only positive number such that, uh, its times itself is $1$ would be $1$. So, $f(-1)$ has to be $1$. So, $f(1) = f(-1)$, and then it's not bijective.`
   - **Proposed:** `$f(-1) \cdot f(-1)$ will be $1$, so the only positive number such that it times itself is $1$ would be $1$. So, $f(-1)$ has to be $1$. So, $f(1) = f(-1)$, and then it's not bijective.`
5. **`content/step4-2026-09-29-tuesday-week3-algebra-1-offset-final.tex:560`** (`student`):
   - **Current:** `Because $F$ is a field and we chose, um... $y \ne 0$.`
   - **Proposed:** `Because $F$ is a field and we chose... $y \ne 0$.`
6. **`content/step4-2026-10-13-tuesday-week5-algebra-1-offset-final.tex:1736`** (`student`):
   - **Current:** `Uh, $2 \cdot 5 - 3 \cdot 3$...`
   - **Proposed:** `$2 \cdot 5 - 3 \cdot 3$...`
7. **`content/step4-2026-11-04-wednesday-week8-algebra-1-offset-final.tex:263`** (`student`):
   - **Current:** `Yeah, sorry, I meant, uh, to the... map it to something in the image of $f$, so...`
   - **Proposed:** `Yeah, sorry, I meant to the... map it to something in the image of $f$, so...`
8. **`content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex:1248`** (`student`):
   - **Current:** `Um, $\mathbb{Z}$ is still generated by $1$...`
   - **Proposed:** `$\mathbb{Z}$ is still generated by $1$...`
9. **`content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:1405`** (`student`):
   - **Current:** `Um, how do we know a $p^k$-element subset necessarily maps to a $p^k$-element subset?`
   - **Proposed:** `How do we know a $p^k$-element subset necessarily maps to a $p^k$-element subset?`
10. **`content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:2125`** (`student` — also fixes `it's, uh, does not` $\to$ `it does not`):
    - **Current:** `It's the one that has the determinant $1$... it's, uh, does not...`
    - **Proposed:** `It's the one that has the determinant $1$... it does not...`

---

### Category C — Spoken Slips & Audio-Verification Candidates

#### C1. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:201` — **Keep as is**
- **Current (line 201):**
  ```latex
  So, consider $f(x^{-1})$, and what equation do we have? The equation, the homomorphism property equation, is $f(x) \cdot f(x^{-1})$ (i.e., $f(x \cdot x^{-1})$) is equal to $f(x)$ times $f(x^{-1})$, that's the hom property \inlinemetanote{writes \qt{$f(x \cdot x^{-1}) = f(x) \cdot f(x^{-1})$ hom. prop.}}.
  ```
- **Verdict:** Already properly annotated with `(i.e., $f(x \cdot x^{-1})$)` per the book's spoken-slip convention.

#### C2. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:305` — **Keep as is**
- **Current (line 305):**
  ```latex
  So, again, when you read this, you have to understand how to read this. This is the homomorphism, it eats an element of the symmetric group, this whole thing is therefore a matrix, and so I can act on this basis vector, okay? And in order to tell what this matrix is, I only have to tell you what its actions are on the matrix vectors (i.e., basis vectors); that's some linear algebra.
  ```
- **Verdict:** Already properly annotated with `(i.e., basis vectors)`.

#### C3. `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex:44` — **Keep as is**
- **Current (line 44):**
  ```latex
  So, what's the analogue here? What are the units, what are the invertible elements in here? Well, of course, there's still $\pm 1$, but there's also $\pm i$ \inlinemetanote{writes: $\{\pm 1, \pm i\}$}. These are also invertible, because $i^2 = -1$, and then you can multiply it by $1$ (i.e., $(-i) \cdot i = 1$).
  ```
- **Verdict:** Already properly annotated with `(i.e., $(-i) \cdot i = 1$)`.

#### C4. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:628` — **Confirmed**
- **Current (line 628):**
  ```latex
  And that makes sense, because a polynomial is just some list of these coefficients. You find the highest one that's not zero, you look at the $d$ index, and that's the degree. So, this is the degree of this polynomial. Another way to write it informally: the degree of $f$ is equal to this $d$ \inlinemetanote{writes: $\deg(f) = d$}, where $d$ is the coefficient of the highest not zero. Okay, is that clear?
  ```
- **Proposed (line 628):**
  ```latex
  And that makes sense, because a polynomial is just some list of these coefficients. You find the highest one that's not zero, you look at the $d$ index, and that's the degree. So, this is the degree of this polynomial. Another way to write it informally: the degree of $f$ is equal to this $d$ \inlinemetanote{writes: $\deg(f) = d$}, where $d$ is the coefficient (i.e., exponent) of the highest not zero. Okay, is that clear?
  ```

#### C5. `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex:2463` — **Confirmed (audio check whether `sorry` already corrected to $g_1 h g_1^{-1}$)**
- **Current (line 2463):**
  ```latex
  And then you have to check that if I do $g_1$ of $h$ and then $g_2$: this one by definition is $g_1^{-1}$ --- sorry, $g h g_1^{-1}$ (i.e., $g_1 h g_1^{-1}$), and then I do that one, that's $g_2 g_1 h g_1^{-1} g_2^{-1}$, that's this side \inlinemetanote{writes \qt{$\mathbf{(ii)}$ $\phi(g_2, \phi(g_1, h)) =$}, \qt{$g_2 g_1 h g_1^{-1}$}, and \qt{$g_2^{-1}$}}. And you have to check that that equals $g_2 g_1$ acting on $h$ \inlinemetanote{writes: $\phi(g_2 g_1, h) =$}. And then you need to know that this is $g_2 g_1 h$, and then the question's: what's the inverse of $g_2 g_1$ \inlinemetanote{writes \qt{$g_2 g_1 h$} and \qt{$(g_2 g_1)^{-1}$}}? And that's that \inlinemetanote{points between $g_2 g_1 h g_1^{-1} g_2^{-1}$ and $g_2 g_1 h (g_2 g_1)^{-1}$}. Okay?
  ```
- **Proposed (line 2463, if he said $g_1 h g_1^{-1}$ after `sorry`):**
  ```latex
  And then you have to check that if I do $g_1$ of $h$ and then $g_2$: this one by definition is $g_1^{-1}$ --- sorry, $g_1 h g_1^{-1}$, and then I do that one, that's $g_2 g_1 h g_1^{-1} g_2^{-1}$, that's this side \inlinemetanote{writes \qt{$\mathbf{(ii)}$ $\phi(g_2, \phi(g_1, h)) =$}, \qt{$g_2 g_1 h g_1^{-1}$}, and \qt{$g_2^{-1}$}}. And you have to check that that equals $g_2 g_1$ acting on $h$ \inlinemetanote{writes: $\phi(g_2 g_1, h) =$}. And then you need to know that this is $g_2 g_1 h$, and then the question's: what's the inverse of $g_2 g_1$ \inlinemetanote{writes \qt{$g_2 g_1 h$} and \qt{$(g_2 g_1)^{-1}$}}? And that's that \inlinemetanote{points between $g_2 g_1 h g_1^{-1} g_2^{-1}$ and $g_2 g_1 h (g_2 g_1)^{-1}$}. Okay?
  ```
  *(If he literally said `$g h g_1^{-1}$` after `sorry`, the current line with `(i.e., $g_1 h g_1^{-1}$)` is already right.)*

#### C6. `content/step4-2026-10-06-tuesday-week4-algebra-1-offset-final.tex:560` — **Confirmed**
- **Current (line 560):**
  ```latex
  Okay, so, if I have this ring homomorphism... so, these are both rings now, so, I try to make the parallel here: $R$ and $S$ are rings, \inlinemetanote{writes: $f \colon R \to S$, $R, S$ are rings} and I remind you, they're commutative rings with unit, and $f$ always takes unit... I don't remind you of all the definitions, but it's consistent with our previous... $f$ takes the $1$ to $1$, that's the definition of a ring (Recall: \cref{def:ring-homomorphism}). And $f$ is a homomorphism. \inlinemetanote{writes: $f$ hom} So, we just want to complete that board.
  ```
- **Proposed (line 560):**
  ```latex
  Okay, so, if I have this ring homomorphism... so, these are both rings now, so, I try to make the parallel here: $R$ and $S$ are rings, \inlinemetanote{writes: $f \colon R \to S$, $R, S$ are rings} and I remind you, they're commutative rings with unit, and $f$ always takes unit... I don't remind you of all the definitions, but it's consistent with our previous... $f$ takes the $1$ to $1$, that's the definition of a ring (i.e., ring homomorphism; Recall: \cref{def:ring-homomorphism}). And $f$ is a homomorphism. \inlinemetanote{writes: $f$ hom} So, we just want to complete that board.
  ```

#### C7. `content/step4-2026-10-06-tuesday-week4-algebra-1-offset-final.tex:1457` — **Confirmed**
- **Current (line 1457):**
  ```latex
  So, the kernel of $f$ may not be zero, but when I consider the kernel of $\bar{f}$ in the quotient ring, it's zero. And the way to think about that is kind of --- and we'll discuss this more tomorrow --- is that you can write this kernel of $\bar{f}$ as kind of whatever was in the kernel before, but now we quotient out by $f$, and then that's just the zero group. \inlinemetanote{writes: $\ker(\bar{f}) = \faktor{\ker(f)}{\ker(f)} = 0$} 
  ```
- **Proposed (line 1457):**
  ```latex
  So, the kernel of $f$ may not be zero, but when I consider the kernel of $\bar{f}$ in the quotient ring, it's zero. And the way to think about that is kind of --- and we'll discuss this more tomorrow --- is that you can write this kernel of $\bar{f}$ as kind of whatever was in the kernel before, but now we quotient out by $f$ (i.e., $\ker(f)$), and then that's just the zero group. \inlinemetanote{writes: $\ker(\bar{f}) = \faktor{\ker(f)}{\ker(f)} = 0$} 
  ```

#### C8. `content/step4-2026-09-29-tuesday-week3-algebra-1-offset-final.tex:300` — **Confirmed**
- **Current (line 300):**
  ```latex
  And so, I wanted to do another... there were various people asking me some questions, so, let's try this: $10\mathbb{Z}$, just to say a little bit.
  ```
- **Proposed (line 300):**
  ```latex
  And so, I wanted to do another... there were various people asking me some questions, so, let's try this: $10\mathbb{Z}$ (i.e., $\faktor{\mathbb{Z}}{10\mathbb{Z}}$), just to say a little bit.
  ```

#### C9. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:1025` — **Confirmed**
- **Current (line 1025):**
  ```latex
  All right, so, this is the standard one that's not principal. And the reason, as I said, you take something from the $\mathbb{Z}$ side and something from the two side. And so, this should be an exercise for you: prove it's not principal \inlinemetanote{writes: Prove not principal}.
  ```
- **Proposed (line 1025):**
  ```latex
  All right, so, this is the standard one that's not principal. And the reason, as I said, you take something from the $\mathbb{Z}$ side and something from the two (i.e., $x$) side. And so, this should be an exercise for you: prove it's not principal \inlinemetanote{writes: Prove not principal}.
  ```

#### C10. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:702` — **Confirmed (note: line 702, not 703)**
- **Current (line 702):**
  ```latex
  So, is polynomial long division \inlinemetanote{writes: Poly long div}.
  ```
- **Proposed (line 702):**
  ```latex
  So, this is polynomial long division \inlinemetanote{writes: Poly long div}.
  ```

#### C11. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:188` — **Keep as is (or audio-check `(4)` vs `for`)**
- **Current (line 188):**
  ```latex
  And this thing maps, by that map on the board, to $\mathbb{Z} \bmod 4$ --- so, what's this for? --- and $\mathbb{Z} \bmod 6$ \inlinemetanote{writes: $\xrightarrow{\phi} \faktor{\mathbb{Z}}{(4)} \times \faktor{\mathbb{Z}}{(6)}$}. Sorry. So, sometimes we write this $(4)$ as $4\mathbb{Z}$, it just means the same thing; it depends on your mood. Here I write it in this... these are different ways of writing an ideal, right? Today we're writing it like that.
  ```
- **Verdict:** Immediately after `--- so, what's this for? ---`, he says `Sorry. So, sometimes we write this (4) as 4\mathbb{Z}`. He likely asked `"so, what's this (4)?"` as he wrote `\faktor{\mathbb{Z}}{(4)}` instead of `\faktor{\mathbb{Z}}{4\mathbb{Z}}`. If audio confirms he meant the ideal `(4)`, propose:
  ```latex
  And this thing maps, by that map on the board, to $\mathbb{Z} \bmod 4$ --- so, what's this $(4)$? --- and $\mathbb{Z} \bmod 6$ \inlinemetanote{writes: $\xrightarrow{\phi} \faktor{\mathbb{Z}}{(4)} \times \faktor{\mathbb{Z}}{(6)}$}. Sorry. So, sometimes we write this $(4)$ as $4\mathbb{Z}$, it just means the same thing; it depends on your mood. Here I write it in this... these are different ways of writing an ideal, right? Today we're writing it like that.
  ```

#### C12. `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex:921` — **Keep as is (unless audio says `wilder` / `weirder`)**
- **Current (line 921):**
  ```latex
  That's a wider property. These are the linear properties --- we'll say more about them in a moment --- but this property is about the multiplication. It says that if I take an element of the kernel, I can then go pick any element of the ring and multiply it, and it'll be in the kernel. So, it's a more interesting property. You can see that here: if you have an element of the kernel, it's $n$ times something. If I multiply it by any integer, it's still $n$ times something.
  ```
- **Verdict:** `"wider property"` makes sense in context (absorption by the *entire* ring $R$, not just closure inside $\ker(f)$), though worth a 5-second audio check against `"wilder"` / `"weirder"`.

#### C13. `content/step4-2026-09-16-wednesday-week1-algebra-1-offset-final.tex:42` — **Reject change (Keep as is)**
- **Current (line 42):**
  ```latex
  The first thing is: what are... for $\mathbb{Z}$ \inlinemetanote{writes: $\mathbb{Z}$}, there were the units, that's $\pm 1$ \inlinemetanote{writes: $\{\pm 1\}$}. And those confused our multiplication always, because you could always put in as many $-1$'s and $+1$'s as you want.
  ```
- **Verdict:** Keep as is. Six lines later (line 48: `It means if you write down any multiplication, like any unique factorization into primes...`), the lecturer explicitly uses `"multiplication"` to mean a multiplicative decomposition into factors.

#### C14. `content/step4-2026-09-22-tuesday-week2-algebra-1-offset-final.tex:117` — **Reject doubt (Keep as is)**
- **Current (line 117):**
  ```latex
  Another course hack is that if you look at this Metaphor page: in $2018$ \inlinemetanote{writes \qt{Metaphor 2018} on the board} it was the last time I taught this course. That Metaphor page is there. This course is going to follow roughly the same path. In fact, the topics and homework --- I mean, there's maybe some slight switching order of lectures --- but you can find all the information there. In particular, all the problem sets that Lycka will eventually upload, you can already look at them now if you want to get ahead. And also, there are all the answers to all the problem sets; you can also look at them if you want. But in the modern world, it's easy to find answers to these questions, so, I don't see there's any reason to hide them from you. You can find everything there.
  ```
- **Verdict:** Keep as is. **Metaphor** (`metaphor.ethz.ch`) is the official ETH Zurich D-MATH course website system, and he writes `"Metaphor 2018"` on the board.

#### C15. `content/step4-2026-09-23-wednesday-week2-algebra-1-offset-final.tex:784, 816, 178` — **Keep 784 and 178 as is; minor optional tweak on 816**
- **Line 784:** `So, the inertia of language: \qt{The units} \inlinemetanote{writes \qt{The units:}} --- if I say \qt{the units} here, that means all of them: $\{1, -1\}$ \inlinemetanote{writes \qt{$\{1, -1\}$}}. The units.` — Keep as is (natural Pandharipande phrasing following line 780: `English is a language I know, which means that I actually speak it without thinking`).
- **Line 178:** `So, the identity doesn't change the... We just discussed this last time, so, I wanted to say.` — Keep as is (natural trailing conversational closer).
- **Current (line 816):**
  ```latex
  This is an exercise: Prove the units of the Gaussian integers are $\pm 1, \pm i$. You need an argument for that, and that argument comes from the norm in complex analysis so that you prove it.
  ```
- **Proposed (line 816, if smoothed):**
  ```latex
  This is an exercise: Prove the units of the Gaussian integers are $\pm 1, \pm i$. You need an argument for that, and that argument comes from the norm in complex analysis to prove it.
  ```

#### C16. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:1593` — **Keep as is (aborted false start)**
- **Current (line 1593):**
  ```latex
  And this has to do with the problem about names which I've discussed several times, because every equivalence class has many names when I use the bar notation. I could transfer $x$... And for this to be a definition, when I change the names here \inlinemetanote{points at $\bar{x} \cdot \bar{y}$}, I have to be someone in the same equivalence class. And that's really the heart of the matter, and this is where all the action is in this definition.
  ```
- **Verdict:** `I could transfer $x$...` is an aborted false start immediately replaced by `when I change the names here`. It can either be kept as a natural self-interruption with `...` or trimmed.

#### C17. `content/step4-2026-11-17-tuesday-week10-algebra-1-offset-final.tex:492, 496` — **Keep `"take this flight by $C$"` and retire the `% [WORD-SUSPECT]` comment!**
- **Current (line 496):**
  ```latex
  Then we can do two things: we can either take this coset and apply the $G$-action, and then take this flight by $C$ to get to the orbit space, or we can apply $C$ first, and then apply the group action. So, this is the question about \qt{respects}, so the definition is: this is always true \inlinemetanote{writes and boxes: $C(g \cdot \gamma \operatorname{Stab}(x)) = g \cdot C(\gamma \operatorname{Stab}(x))$}. Okay, this box.
  ```
- **Verdict:** **Cross-lecture proof that `"take this flight by $C$"` is genuine!** In `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:492`, the lecturer uses the exact same aviation metaphor for following an arrow across a diagram:
  > `and if I put them together all the way --- the direct flight here --- this is $\hat{\Phi}_{\text{mat}}$`
  So `"take this flight by $C$"` at `W10 Tue:496` is 100% authentic Pandharipande idiom, and the `% [WORD-SUSPECT: "take this flight by C" ...]` comment at line 492 can be retired.

---

### Categories D & E — Structural Observations & Intentional Preservations
- **D1 (`W4 Wed:133–156`) & D2 (`W9 Wed:13–67`):** Confirmed as intentional verbatim captures of live classroom events (microphone troubleshooting and fire alarm), though `W4 Wed:135` has a minor grammar glitch (`yesterday: is that` $\to$ `yesterday: that` or `yesterday: we take`, listed in Part II.B item 3 below).
- **D3 (`W10 Tue:1139–1140`):**
  - **Current (line 1140):**
    ```latex
    \inlinemetanote{faint, partly inaudible answer from a student} Yeah. If the stabilizer's the whole thing, then it's $1$. You know, $1$ is a divisor of $p^k$, but it's not divisible by $p$. So, it's always divisible by $p$ except when the stabilizer of $x$ is equal to the whole thing \inlinemetanote{writes \qt{except when $\operatorname{Stab}(x) = \faktor{\mathbb{Z}}{p^k\mathbb{Z}}$}}. Okay?
    ```
  - **Verdict:** Matches the established convention for inaudible student responses elsewhere in the book (e.g., `W7 Tue:1599, 1605, 1863, 1867`). Keep as is.
- **D4 (`W3 Wed:862–866`):** Confirmed that the `"nought"` joke is self-explanatory in context (`a_0 b_0` read aloud as `"a nought b nought"`).
- **Category E:** Confirmed that all items listed by Claude in Category E are genuine lecturer voice or documented in `% [WORD-CHECKED]` comments and should remain untouched.

---

## Part II: Argon's Additional Findings (Missed by Claude)

### Section II.A — Punctuation Conventions (`speech-refinement.md:433–555`)

1. **Em-Dash Cap (§4 — Maximum 2 `---` per sentence):**
   - Verified across all 19 `content/step4-*.tex` files: **0 sentences** contain 3 or more em-dashes.
2. **Trimming Post-Dash Repetitions (§5 — `"Never repeat the pre-dash word or phrase after the closing ---"`):**
   - Found **2 violations**:
     - **`W6 Tue:220`** (`$R$ is a Noetherian ring --- this is also on the order of a hundred years ago --- Noetherian ring.` — see Item 10 in Section II.B below).
     - **`W7 Tue:307`** (`given any $f$ --- always, you know, non-zero \inlinemetanote{...} --- $f$ non-zero, then` — included in A4 above).
3. **Commas After Compound Connectors (§3 — `"Always place a comma after so (or then) when the connector introduces a clause: Okay, so, / All right, so,"`):**
   - While Weeks 1–9 and Week 10 Tuesday follow `Okay, so,` and `All right, so,` systematically (with one corrupted `Okay, so, far,` in `W7 Tue:1455` where `so far` was mistakenly split by a comma, and one valid `Okay, so far,` in `W10 Tue:862`), **Week 10 Wednesday (`content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex`) is missing the comma after `so` in 14 occurrences** of `Okay, so` / `All right, so`:

#### P1. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:1455` (Intruding comma inside `so far`)
- **Current (line 1455):**
  ```latex
  Okay, so, far, the question is: how are we going to talk about these elements of the symmetric group? And there's a standard way, which is about the \newterm{cycle decomposition}, so I'll try to write it, and it's really useful notation.
  ```
- **Proposed (line 1455):**
  ```latex
  Okay, so far, the question is: how are we going to talk about these elements of the symmetric group? And there's a standard way, which is about the \newterm{cycle decomposition}, so I'll try to write it, and it's really useful notation.
  ```

#### P2–P15. 14 Missing Commas After `Okay, so` / `All right, so` in `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex`

- **P2 (`W10 Wed:109`):**
  - **Current:** `Okay, so we start, and the topic today is Sylow \inlinemetanote{writes: Sylow:}.`
  - **Proposed:** `Okay, so, we start, and the topic today is Sylow \inlinemetanote{writes: Sylow:}.`
- **P3 (`W10 Wed:165`):**
  - **Current:** `So, the full converse to Lagrange is impossible because of this example. Sylow gives you a partial converse. It says at least if you take the biggest $p$-th power, you can find a subgroup there. Is that clear? All right, so we're going to prove this.`
  - **Proposed:** `So, the full converse to Lagrange is impossible because of this example. Sylow gives you a partial converse. It says at least if you take the biggest $p$-th power, you can find a subgroup there. Is that clear? All right, so, we're going to prove this.`
- **P4 (`W10 Wed:276`):**
  - **Current:** `Okay, so we're going to study this $G$-action on this set $T$ \inlinemetanote{writes: $G \curvearrowright T$}. And as I said, the confusing part of this proof is to keep track of all the actions. There's the pictures --- perhaps they could be more clear, but they couldn't be much more clear, it's relatively clear there.`
  - **Proposed:** `Okay, so, we're going to study this $G$-action on this set $T$ \inlinemetanote{writes: $G \curvearrowright T$}. And as I said, the confusing part of this proof is to keep track of all the actions. There's the pictures --- perhaps they could be more clear, but they couldn't be much more clear, it's relatively clear there.`
- **P5 (`W10 Wed:297`):**
  - **Current:** `All right, so first you have to accept what we're doing here. We pick some element in this set $T$. It is an element --- it's a subset of $G$ --- and since $G$ acts on $T$, I can contemplate the stabilizer of any element. I want the stabilizer of this one. Okay?`
  - **Proposed:** `All right, so, first you have to accept what we're doing here. We pick some element in this set $T$. It is an element --- it's a subset of $G$ --- and since $G$ acts on $T$, I can contemplate the stabilizer of any element. I want the stabilizer of this one. Okay?`
- **P6 (`W10 Wed:531`):**
  - **Current:** `All right, so now we use the Orbit--Stabilizer Theorem for that orbit \inlinemetanote{wipes a spot on the lower-right board and writes: Use Orb-Stab Thm}. So, use this Orbit--Stabilizer Theorem, and what does it say? It says the size of $G$ divided by the size of the stabilizer of that $X_j$ equals the size of this orbit \inlinemetanote{writes: $\frac{|G|}{|\operatorname{Stab}(X_j)|} = |\operatorname{Orb}(X_j)|$}. That's the Orbit--Stabilizer Theorem.`
  - **Proposed:** `All right, so, now we use the Orbit--Stabilizer Theorem for that orbit \inlinemetanote{wipes a spot on the lower-right board and writes: Use Orb-Stab Thm}. So, use this Orbit--Stabilizer Theorem, and what does it say? It says the size of $G$ divided by the size of the stabilizer of that $X_j$ equals the size of this orbit \inlinemetanote{writes: $\frac{|G|}{|\operatorname{Stab}(X_j)|} = |\operatorname{Orb}(X_j)|$}. That's the Orbit--Stabilizer Theorem.`
- **P7 (`W10 Wed:599`):**
  - **Current:** `Okay, so Sylow $2$ says something else. So, we're going to state Sylow $2$ \inlinemetanote{writes: Sylow II}. It's the same hypotheses. I don't write them again: we have $G$ is a group of order $n$, and we have $p$ to the $k$ is the biggest power of $p$ that divides $n$. Maybe I write it anyway, so we don't get confused \inlinemetanote{writes \qt{Let $H \subset G$} and \qt{$|G| = n = p^k m$, $(p, m) = 1$}}.`
  - **Proposed:** `Okay, so, Sylow $2$ says something else. So, we're going to state Sylow $2$ \inlinemetanote{writes: Sylow II}. It's the same hypotheses. I don't write them again: we have $G$ is a group of order $n$, and we have $p$ to the $k$ is the biggest power of $p$ that divides $n$. Maybe I write it anyway, so we don't get confused \inlinemetanote{writes \qt{Let $H \subset G$} and \qt{$|G| = n = p^k m$, $(p, m) = 1$}}.`
- **P8 (`W10 Wed:638`):**
  - **Current:** `All right, so we have to name one, so let's call it $P$. I'm going to give the proof now \inlinemetanote{writes: Proof.}.`
  - **Proposed:** `All right, so, we have to name one, so let's call it $P$. I'm going to give the proof now \inlinemetanote{writes: Proof.}.`
- **P9 (`W10 Wed:670`):**
  - **Current:** `So, this is the action we're going to take. Is this restriction clear? We already know how $G$ acts on left cosets. $H$ is a subgroup, so it just acts as if it were an element of $G$. Okay, so this is the action we'll consider: we consider this action in the proof \inlinemetanote{writes \qt{We consider this action} with an arrow to $H \times \faktor{G}{P} \to \faktor{G}{P}$}.`
  - **Proposed:** `So, this is the action we're going to take. Is this restriction clear? We already know how $G$ acts on left cosets. $H$ is a subgroup, so it just acts as if it were an element of $G$. Okay, so, this is the action we'll consider: we consider this action in the proof \inlinemetanote{writes \qt{We consider this action} with an arrow to $H \times \faktor{G}{P} \to \faktor{G}{P}$}.`
- **P10 (`W10 Wed:695`):**
  - **Current:** `Okay, so what are we going to do with this action? I'll try to make big $P$'s here so you don't get confused. What are we going to do with this action? Well, we'd like to know what is the size of this set \inlinemetanote{writes: $\left|\faktor{G}{P}\right|$}. And the answer is that we know this is $n$, and this is $p$ to the $k$, and so this is $m$ \inlinemetanote{writes: $= \frac{n}{p^k} = m$}. Because Lagrange says that the size of this is equal to the size of $G$, size of $P$ \inlinemetanote{writes $\frac{|G|}{|P|}$ below $\left|\faktor{G}{P}\right|$}, okay?`
  - **Proposed:** `Okay, so, what are we going to do with this action? I'll try to make big $P$'s here so you don't get confused. What are we going to do with this action? Well, we'd like to know what is the size of this set \inlinemetanote{writes: $\left|\faktor{G}{P}\right|$}. And the answer is that we know this is $n$, and this is $p$ to the $k$, and so this is $m$ \inlinemetanote{writes: $= \frac{n}{p^k} = m$}. Because Lagrange says that the size of this is equal to the size of $G$, size of $P$ \inlinemetanote{writes $\frac{|G|}{|P|}$ below $\left|\faktor{G}{P}\right|$}, okay?`
- **P11 (`W10 Wed:822`):**
  - **Current:** `All right, so we found one $z_i$. This $z_i$, this one that's a fixed point, is an element of this \inlinemetanote{writes \qt{$z_i \in \left|\faktor{G}{P}\right|$}, a slip for $z_i \in \faktor{G}{P}$}, right? So, it's a coset space, so we can write $z_i$ as some $x P$ \inlinemetanote{writes: $z_i = x P$}. That's the left coset of $x$, where $x$ is in $G$ \inlinemetanote{writes: $x \in G$}. So, this $z_i$ is an element of this coset space, and now I'm just writing it explicitly as a coset.`
  - **Proposed:** `All right, so, we found one $z_i$. This $z_i$, this one that's a fixed point, is an element of this \inlinemetanote{writes \qt{$z_i \in \left|\faktor{G}{P}\right|$}, a slip for $z_i \in \faktor{G}{P}$}, right? So, it's a coset space, so we can write $z_i$ as some $x P$ \inlinemetanote{writes: $z_i = x P$}. That's the left coset of $x$, where $x$ is in $G$ \inlinemetanote{writes: $x \in G$}. So, this $z_i$ is an element of this coset space, and now I'm just writing it explicitly as a coset.`
- **P12 (`W10 Wed:826`):**
  - **Current:** `All right, so we're going to look at this equation: what does it say \inlinemetanote{pushes the lower-right board up}? But the whole point of this analysis of this action of $H$ on the left coset space was to find this fixed point. That was the whole purpose of that analysis. Well, we found it now, and that fixed point has this property. \inlinemetanote{erases the lower-left board}`
  - **Proposed:** `All right, so, we're going to look at this equation: what does it say \inlinemetanote{pushes the lower-right board up}? But the whole point of this analysis of this action of $H$ on the left coset space was to find this fixed point. That was the whole purpose of that analysis. Well, we found it now, and that fixed point has this property. \inlinemetanote{erases the lower-left board}`
- **P13 (`W10 Wed:845`):**
  - **Current:** `And now we have the fixed-point equation \inlinemetanote{writes: Fixed point equation}. The fixed-point equation says --- I just repeat it --- for every $h$, if I take $h$ times this coset, I get back this coset \inlinemetanote{writes: $\forall h \in H$, $h x P = x P$}. All right, so I write here: $x P$ in $\faktor{G}{P}$ is $H$-fixed \inlinemetanote{writes: $x P \in \faktor{G}{P}$ is $H$-fixed}.`
  - **Proposed:** `And now we have the fixed-point equation \inlinemetanote{writes: Fixed point equation}. The fixed-point equation says --- I just repeat it --- for every $h$, if I take $h$ times this coset, I get back this coset \inlinemetanote{writes: $\forall h \in H$, $h x P = x P$}. All right, so, I write here: $x P$ in $\faktor{G}{P}$ is $H$-fixed \inlinemetanote{writes: $x P \in \faktor{G}{P}$ is $H$-fixed}.`
- **P14 (`W10 Wed:862`):**
  - **Current:** `Okay, so we need to think a little bit about what this means. When I write this \inlinemetanote{writes: $h x P$}, I hope you understand what this coset is, you know: $x$ is an element of $G$, $h$ is an element of $H$ inside $G$, so when I multiply $h$ times $x$, that's inside $G$, and this is the coset \inlinemetanote{writes \qt{$x \in G$} and \qt{$h \in H \subset G$}}.`
  - **Proposed:** `Okay, so, we need to think a little bit about what this means. When I write this \inlinemetanote{writes: $h x P$}, I hope you understand what this coset is, you know: $x$ is an element of $G$, $h$ is an element of $H$ inside $G$, so when I multiply $h$ times $x$, that's inside $G$, and this is the coset \inlinemetanote{writes \qt{$x \in G$} and \qt{$h \in H \subset G$}}.`
- **P15 (`W10 Wed:943`):**
  - **Current:** `All right, so Sylow $3$ says that all $p$-Sylow subgroups --- remember, $p$-Sylow means that you're a subgroup of the maximal $p$-size, meaning $P$ inside $G$ with $P$ (i.e., $|P|$) equal to $p$ to the $k$, the maximal $k$: if you say a subgroup is $p$-Sylow, it's not small $p$, it's the biggest $p$ you can have, that's the definition --- so all $p$-Sylow subgroups of $G$ are conjugate \inlinemetanote{writes \qt{Sylow III}, \qt{All $p$-Sylow subgroups}, \qt{($P \subset G$ with $|P| = p^k$)}, and \qt{of $G$ are conjugate}}.`
  - **Proposed:** `All right, so, Sylow $3$ says that all $p$-Sylow subgroups --- remember, $p$-Sylow means that you're a subgroup of the maximal $p$-size, meaning $P$ inside $G$ with $P$ (i.e., $|P|$) equal to $p$ to the $k$, the maximal $k$: if you say a subgroup is $p$-Sylow, it's not small $p$, it's the biggest $p$ you can have, that's the definition --- so all $p$-Sylow subgroups of $G$ are conjugate \inlinemetanote{writes \qt{Sylow III}, \qt{All $p$-Sylow subgroups}, \qt{($P \subset G$ with $|P| = p^k$)}, and \qt{of $G$ are conjugate}}.`

---

### Section II.B — Additional Readability, False-Start, Repetition, and Slip Findings (W1 Wed – W10 Wed)

#### 1. `content/step4-2026-09-23-wednesday-week2-algebra-1-offset-final.tex:970` (Student block stutter `Only $1$, $1$ to $6$`)
- **Current (line 970):**
  ```latex
  Only $1$, $1$ to $6$ are the units.
  ```
- **Proposed (line 970):**
  ```latex
  Only $1$ to $6$ are the units.
  ```

#### 2. `content/step4-2026-09-29-tuesday-week3-algebra-1-offset-final.tex:1227` (Doubled `already` in same clause)
- **Current (line 1227):**
  ```latex
  And we've already done this kind of thing twice already in the lecture. If you just do it and follow your nose, you'll see it all unwinds. You just use the definition: you have to say formally that this result respects our definition of equivalence classes.
  ```
- **Proposed (line 1227):**
  ```latex
  And we've already done this kind of thing twice in the lecture. If you just do it and follow your nose, you'll see it all unwinds. You just use the definition: you have to say formally that this result respects our definition of equivalence classes.
  ```

#### 3. `content/step4-2026-10-07-wednesday-week4-algebra-1-offset-final.tex:135` (Extra `is` after colon: `what we did yesterday: is that`)
- **Current (line 135):**
  ```latex
  Anyway, so, that's another way of thinking about what we did yesterday: is that we take $R$, we have the set of equivalence classes, and we want to define a ring structure on it for which this quotient --- this map, $x$ goes to its equivalence class --- is a ring homomorphism. And we just define all the structure so it is. That's another way of thinking about what happened yesterday.
  ```
- **Proposed (line 135):**
  ```latex
  Anyway, so, that's another way of thinking about what we did yesterday: we take $R$, we have the set of equivalence classes, and we want to define a ring structure on it for which this quotient --- this map, $x$ goes to its equivalence class --- is a ring homomorphism. And we just define all the structure so it is. That's another way of thinking about what happened yesterday.
  ```

#### 4. `content/step4-2026-10-13-tuesday-week5-algebra-1-offset-final.tex:456` (Garbled false start `So, by this one, by the way:`)
- **Current (line 456):**
  ```latex
  Now let's do the other way. There's nothing to these proofs here; it's just somehow organizing the definitions in your head correctly. So, by this one, by the way: if you put this in your brain, you'll never forget it. It's too, too simple to forget. And I don't know what was in your linear algebra class, but there's an analogous thing in linear algebra. Did you prove that? No? All right, well... \inlinemetanote{takes sponge to clean the rightmost board panel}
  ```
- **Proposed (line 456):**
  ```latex
  Now let's do the other way. There's nothing to these proofs here; it's just somehow organizing the definitions in your head correctly. So, this one, by the way: if you put this in your brain, you'll never forget it. It's too, too simple to forget. And I don't know what was in your linear algebra class, but there's an analogous thing in linear algebra. Did you prove that? No? All right, well... \inlinemetanote{takes sponge to clean the rightmost board panel}
  ```

#### 5. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:345` (Garbled `where that you want`)
- **Current (line 345):**
  ```latex
  Surjective means we start: so, choose any $\bar{x} \in R \bmod I$ and $\bar{y} \in R \bmod J$ \inlinemetanote{writes: Choose any $\bar{x} \in \faktor{R}{I}, \bar{y} \in \faktor{R}{J}$}, right? Then we have to find... we have to construct a $\bar{z} \in R \bmod IJ$ such that \inlinemetanote{writes: We have to construct a $\bar{z} \in \faktor{R}{IJ}$ such that} $z$ is congruent to $x \bmod I$ and $z$ is congruent to $y \bmod J$ \inlinemetanote{writes \qt{$z \equiv x \bmod I$} and \qt{$z \equiv y \bmod J$}}. If I do that, that's surjectivity. That's the Chinese Remainder problem that we talked about at the beginning. So, you pick where that you want, and you have to find the $z$ that satisfies that.
  ```
- **Proposed (line 345):**
  ```latex
  Surjective means we start: so, choose any $\bar{x} \in R \bmod I$ and $\bar{y} \in R \bmod J$ \inlinemetanote{writes: Choose any $\bar{x} \in \faktor{R}{I}, \bar{y} \in \faktor{R}{J}$}, right? Then we have to find... we have to construct a $\bar{z} \in R \bmod IJ$ such that \inlinemetanote{writes: We have to construct a $\bar{z} \in \faktor{R}{IJ}$ such that} $z$ is congruent to $x \bmod I$ and $z$ is congruent to $y \bmod J$ \inlinemetanote{writes \qt{$z \equiv x \bmod I$} and \qt{$z \equiv y \bmod J$}}. If I do that, that's surjectivity. That's the Chinese Remainder problem that we talked about at the beginning. So, you pick whatever you want, and you have to find the $z$ that satisfies that.
  ```

#### 6. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:355` (Broken restart `this is congruent... it's to $x$`)
- **Current (line 355):**
  ```latex
  If I look at this term here, $jx$ \inlinemetanote{circles $jx$}, this is congruent to $x \bmod I$ \inlinemetanote{writes: $jx \equiv x \bmod I$}, because this equation says that if I look $\bmod I$, this is congruent... it's to $x$, okay? So, just this equation shows that $jx$ is congruent to $x \bmod I$. Is that clear?
  ```
- **Proposed (line 355):**
  ```latex
  If I look at this term here, $jx$ \inlinemetanote{circles $jx$}, this is congruent to $x \bmod I$ \inlinemetanote{writes: $jx \equiv x \bmod I$}, because this equation says that if I look $\bmod I$, this is congruent to $x$, okay? So, just this equation shows that $jx$ is congruent to $x \bmod I$. Is that clear?
  ```

#### 7. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:706` (Missing verb in `so when division,`)
- **Current (line 706):**
  ```latex
  And we're going to do division, so when division, you always have to assume somebody's not zero. This one's not zero \inlinemetanote{writes: $g \neq 0$}. You can't divide by zero.
  ```
- **Proposed (line 706):**
  ```latex
  And we're going to do division, so when doing division, you always have to assume somebody's not zero. This one's not zero \inlinemetanote{writes: $g \neq 0$}. You can't divide by zero.
  ```

#### 8. `content/step4-2026-10-14-wednesday-week5-algebra-1-offset-final.tex:882` (Doubled `again` in `then again we're happy again`)
- **Current (line 882):**
  ```latex
  Okay, so, what are the possibilities for the remainder? The remainder could be zero \inlinemetanote{writes: $r(x) = 0$}. That's good for us, because then again we're happy again, because then that means that $g$ is in \inlinemetanote{writes: $\implies g \in (f)$}... because if this is zero, that means $g$ is in the ideal generated by $f$. Okay?
  ```
- **Proposed (line 882):**
  ```latex
  Okay, so, what are the possibilities for the remainder? The remainder could be zero \inlinemetanote{writes: $r(x) = 0$}. That's good for us, because then we're happy again, because then that means that $g$ is in \inlinemetanote{writes: $\implies g \in (f)$}... because if this is zero, that means $g$ is in the ideal generated by $f$. Okay?
  ```

#### 9. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:126` (Looping restart `every ideal ... is of the form... an ideal... every ideal is of this form, where $f$ is just one element, is generated by one element`)
- **Current (line 126):**
  ```latex
  Last week we had $k$ is a field, \inlinemetanote{writes: $k$ field} and we proved, using the division algorithm (Recall: \cref{thm:poly-long-division}) --- so, this was from last week --- that if I take the polynomial ring, this is a PID, \inlinemetanote{writes: $\to k[x]$ is a PID} a principal ideal domain. And this means that \inlinemetanote{draws curved arrow} every ideal \inlinemetanote{writes: any ideal is of the form $(f) = I$} is of the form... an ideal... every ideal is of this form, where $f$ is just one element, is generated by one element.
  ```
- **Proposed (line 126):**
  ```latex
  Last week we had $k$ is a field, \inlinemetanote{writes: $k$ field} and we proved, using the division algorithm (Recall: \cref{thm:poly-long-division}) --- so, this was from last week --- that if I take the polynomial ring, this is a PID, \inlinemetanote{writes: $\to k[x]$ is a PID} a principal ideal domain. And this means that \inlinemetanote{draws curved arrow} every ideal \inlinemetanote{writes: any ideal is of the form $(f) = I$} is of this form, where $f$ is just one element --- it is generated by one element.
  ```

#### 10. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:220` (Post-dash repetition `Noetherian ring --- ... --- Noetherian ring.` violating `speech-refinement.md` §5)
- **Current (line 220):**
  ```latex
  And the definition \inlinemetanote{writes: Def: $R$ is a Noetherian Ring} is that $R$ is a Noetherian ring --- this is also on the order of a hundred years ago --- Noetherian ring. There are various ways to define it: if and only if every ideal \inlinemetanote{writes: Every $I \subset R$ is finitely gen.} is finitely generated, in the sense of David Hilbert.
  ```
- **Proposed (line 220):**
  ```latex
  And the definition \inlinemetanote{writes: Def: $R$ is a Noetherian Ring} is that $R$ is a Noetherian ring --- this is also on the order of a hundred years ago. There are various ways to define it: if and only if every ideal \inlinemetanote{writes: Every $I \subset R$ is finitely gen.} is finitely generated, in the sense of David Hilbert.
  ```

#### 11. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:325, 327` (Missing preposition `for` in line 325 + board-writing repetition `, whenever $x = y z$, then` in line 327)
- **Current (line 325):**
  ```latex
  All right. So, the first definition --- so, I have not defined UFD, I will eventually define it. The first definition here \inlinemetanote{writes: Def:} is: let $x$ \inlinemetanote{writes: let $x \in R$, $x \neq 0$, $x$ not unit} be an element of $R$ where $x$ is not zero and not a unit. So, it's going to be one of the elements we will consider factorization. We don't consider factorization of zero or the units.
  ```
- **Proposed (line 325):**
  ```latex
  All right. So, the first definition --- so, I have not defined UFD, I will eventually define it. The first definition here \inlinemetanote{writes: Def:} is: let $x$ \inlinemetanote{writes: let $x \in R$, $x \neq 0$, $x$ not unit} be an element of $R$ where $x$ is not zero and not a unit. So, it's going to be one of the elements we will consider for factorization. We don't consider factorization of zero or the units.
  ```
- **Current (line 327):**
  ```latex
  Then the definition: $x$ is irreducible \inlinemetanote{writes: $x$ is irreducible} --- so, this is the term that's being defined --- if and only if, \inlinemetanote{writes: $\iff$} whenever \inlinemetanote{writes: whenever} we have a factorization $x = y z$, \inlinemetanote{writes: $x = y z$} then \inlinemetanote{writes: then}, whenever $x = y z$, then either $y$ \inlinemetanote{writes: either $y$ is a unit} is a unit or $z$ \inlinemetanote{writes: or $z$ is a unit.} is a unit.
  ```
- **Proposed (line 327):**
  ```latex
  Then the definition: $x$ is irreducible \inlinemetanote{writes: $x$ is irreducible} --- so, this is the term that's being defined --- if and only if, \inlinemetanote{writes: $\iff$} whenever \inlinemetanote{writes: whenever} we have a factorization $x = y z$, \inlinemetanote{writes: $x = y z$} then \inlinemetanote{writes: then} either $y$ \inlinemetanote{writes: either $y$ is a unit} is a unit or $z$ \inlinemetanote{writes: or $z$ is a unit.} is a unit.
  ```

#### 12. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:946` (Garbled ending `using if two`)
- **Current (line 946):**
  ```latex
  The definition of prime is with two: if you have a product in the prime, then at least one of them has to be in the prime. But if I have a list, I can just keep separating them off one at a time using if two. So, one of them has to be in this prime.
  ```
- **Proposed (line 946):**
  ```latex
  The definition of prime is with two: if you have a product in the prime, then at least one of them has to be in the prime. But if I have a list, I can just keep separating them off one at a time using the case of two. So, one of them has to be in this prime.
  ```

#### 13. `content/step4-2026-10-20-tuesday-week6-algebra-1-offset-final.tex:1292` (Board-writing stutter `is just some element, is some element such that`)
- **Current (line 1292):**
  ```latex
  Is it okay for me to write this $\ell^{-1}$? Sometimes people get scared by that. $\ell^{-1}$ is just some element, is some element such that \inlinemetanote{writes: is some element such that $\ell^{-1} \ell = 1$} $\ell^{-1} \ell = 1$, because it's a unit. If it's a unit, that means there's somebody; it's traditional to call it $\ell^{-1}$, but sometimes people get confused by it. I could call it something else, you know, like $W$ or Fred or anything, doesn't really matter.
  ```
- **Proposed (line 1292):**
  ```latex
  Is it okay for me to write this $\ell^{-1}$? Sometimes people get scared by that. $\ell^{-1}$ is just some element such that \inlinemetanote{writes: is some element such that $\ell^{-1} \ell = 1$} $\ell^{-1} \ell = 1$, because it's a unit. If it's a unit, that means there's somebody; it's traditional to call it $\ell^{-1}$, but sometimes people get confused by it. I could call it something else, you know, like $W$ or Fred or anything, doesn't really matter.
  ```

#### 14. `content/step4-2026-10-21-wednesday-week6-algebra-1-offset-final.tex:200` (Board-writing echo `the non-zero coefficients \inlinemetanote{...}, non-zero coefficients,`)
- **Current (line 200):**
  ```latex
  So, this is how it's typically written, but what it means is you take $f$, you put here the non-zero coefficients \inlinemetanote{writes \qt{non-zero} under $a_0, a_1, \dots, a_n$}, non-zero coefficients, and then take their $\operatorname{GCD}$s, as we discussed yesterday (Recall: \cref{def:gcd-ufd}, \cref{thm:gcd-formula-ufd}).
  ```
- **Proposed (line 200):**
  ```latex
  So, this is how it's typically written, but what it means is you take $f$, you put here the non-zero coefficients \inlinemetanote{writes \qt{non-zero} under $a_0, a_1, \dots, a_n$}, and then take their $\operatorname{GCD}$s, as we discussed yesterday (Recall: \cref{def:gcd-ufd}, \cref{thm:gcd-formula-ufd}).
  ```

#### 15. `content/step4-2026-10-21-wednesday-week6-algebra-1-offset-final.tex:751` (Doubled `We already had shown ...: we already had shown`)
- **Current (line 751):**
  ```latex
  Step 2: prove uniqueness. \inlinemetanote{writes: Step. Prove (!)} We already had shown a method to prove uniqueness: we already had shown that if $p$ irreducible implies $p$ prime, then uniqueness holds. \inlinemetanote{writes \qt{We already have shown: If $p$ irr $\implies (p) \subset R[x]$ prime} and, on the next line, \qt{the uniqueness holds}} Because that was one of our steps yesterday (Recall: \cref{clm:step1-uniqueness}): if I have any ring where irreducible implies prime, then I get uniqueness.
  ```
- **Proposed (line 751):**
  ```latex
  Step 2: prove uniqueness. \inlinemetanote{writes: Step. Prove (!)} We already had shown that if $p$ irreducible implies $p$ prime, then uniqueness holds. \inlinemetanote{writes \qt{We already have shown: If $p$ irr $\implies (p) \subset R[x]$ prime} and, on the next line, \qt{the uniqueness holds}} Because that was one of our steps yesterday (Recall: \cref{clm:step1-uniqueness}): if I have any ring where irreducible implies prime, then I get uniqueness.
  ```

#### 16. `content/step4-2026-10-27-tuesday-week7-algebra-1-offset-final.tex:1861` (Spliced clause `you apply $e$ to the $1$ is $e$`)
- **Current (line 1861):**
  ```latex
  So, let us try to think about $S_3$ \inlinemetanote{writes and underlines: $S_3$}: what is the order of $e$ \inlinemetanote{writes: $e \to$}? Well, this order of $e$ is $1$, because you don't have to... you apply $e$ to the $1$ is $e$ (i.e., $e^1 = e$) \inlinemetanote{writes: $\operatorname{Ord}(e) = 1$}. It's kind of silly, all right, anyway.
  ```
- **Proposed (line 1861):**
  ```latex
  So, let us try to think about $S_3$ \inlinemetanote{writes and underlines: $S_3$}: what is the order of $e$ \inlinemetanote{writes: $e \to$}? Well, this order of $e$ is $1$, because you don't have to... $e$ to the $1$ is $e$ (i.e., $e^1 = e$) \inlinemetanote{writes: $\operatorname{Ord}(e) = 1$}. It's kind of silly, all right, anyway.
  ```

#### 17. `content/step4-2026-10-28-wednesday-week7-algebra-1-offset-final.tex:228` (Missing `to the` in `equal to $x$ $\operatorname{Ord}(x)$`)
- **Current (line 228):**
  ```latex
  But this times this is equal to $x$ $\operatorname{Ord}(x)$, which is $e$ \inlinemetanote{writes: $x^k \cdot x^{\operatorname{Ord}(x)-k} = x^{\operatorname{Ord}(x)} = e$}. So, that means the inverse is also in this list. Okay? So, all these three things are satisfied, and it is a fact that this construction --- if I take $x$ and I take the neutral element and I go all the way up to the order minus $1$ --- is a nice subset and it is a subgroup.
  ```
- **Proposed (line 228):**
  ```latex
  But this times this is equal to $x$ to the $\operatorname{Ord}(x)$, which is $e$ \inlinemetanote{writes: $x^k \cdot x^{\operatorname{Ord}(x)-k} = x^{\operatorname{Ord}(x)} = e$}. So, that means the inverse is also in this list. Okay? So, all these three things are satisfied, and it is a fact that this construction --- if I take $x$ and I take the neutral element and I go all the way up to the order minus $1$ --- is a nice subset and it is a subgroup.
  ```

#### 18. `content/step4-2026-11-03-tuesday-week8-algebra-1-offset-final.tex:431` (Missing subject after ellipsis `because it takes the first basis vector... should go to the second one`)
- **Current (line 431):**
  ```latex
  Yeah, $0, 1, 0$, because it takes the first basis vector... should go to the second one, and that's the matrix that does it \inlinemetanote{writes the first column $(0, 1, 0)^T$}. And then this one is that, and then it's that, all right \inlinemetanote{completes $\Phi_{\text{mat}}(1\,2)$}?
  ```
- **Proposed (line 431):**
  ```latex
  Yeah, $0, 1, 0$, because the first basis vector should go to the second one, and that's the matrix that does it \inlinemetanote{writes the first column $(0, 1, 0)^T$}. And then this one is that, and then it's that, all right \inlinemetanote{completes $\Phi_{\text{mat}}(1\,2)$}?
  ```

#### 19. `content/step4-2026-11-10-tuesday-week9-algebra-1-offset-final.tex:1597` (Garbled word order `no ever reason`)
- **Current (line 1597):**
  ```latex
  Okay? This is just a translation of that. So, in principle, there's no ever reason to be confused, because when you have a dot... when you consider group actions, there'll be two things, and there could be dots between them. And if the dot's between two group elements, that's group multiplication. If the dot's between a group element and an element of $T$, that's the action. There shouldn't be a confusion between those two things, because they eat different things, right?
  ```
- **Proposed (line 1597):**
  ```latex
  Okay? This is just a translation of that. So, in principle, there's never any reason to be confused, because when you have a dot... when you consider group actions, there'll be two things, and there could be dots between them. And if the dot's between two group elements, that's group multiplication. If the dot's between a group element and an element of $T$, that's the action. There shouldn't be a confusion between those two things, because they eat different things, right?
  ```

#### 20. `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex:325` (Spoken slip `"the stabilizer"` for `"the subset $X$"`, noted in `aiNote` at line 336 but missing inline `(i.e., ...)` in `speech`)
- **Current (line 325):**
  ```latex
  So, how are we going to do that? Well, the stabilizer has a particular element $a_1$ in it \inlinemetanote{points at $a_1$ in $X$}. I can pick any one I want. So, here's $a_1$, all right? This set has an $a_1$ in it. This is in $G$ \inlinemetanote{draws a contour labeled $G$ with a point $a_1$ inside}. This $a_1$ is, let's say, one of the elements of this set $X$. I just pick one.
  ```
- **Proposed (line 325):**
  ```latex
  So, how are we going to do that? Well, the stabilizer (i.e., the subset $X$) has a particular element $a_1$ in it \inlinemetanote{points at $a_1$ in $X$}. I can pick any one I want. So, here's $a_1$, all right? This set has an $a_1$ in it. This is in $G$ \inlinemetanote{draws a contour labeled $G$ with a point $a_1$ inside}. This $a_1$ is, let's say, one of the elements of this set $X$. I just pick one.
  ```

#### 21. `content/step4-2026-11-18-wednesday-week10-algebra-1-offset-final.tex:718` (Spoken slip `"divisible by"` for `"divisors of"`, noted in `aiNote` at line 729 but missing inline `(i.e., ...)` in `speech`)
- **Current (line 718):**
  ```latex
  I'll give you an argument for this, but it should not be a surprise. Well, I'll say it in words and I'll write it down clear, because we can divide this \inlinemetanote{points at $\faktor{G}{P}$} in terms of the orbits, right? And the orbits always have orders that are divisible by the order of $H$. That's by the Orbit--Stabilizer Theorem.
  ```
- **Proposed (line 718):**
  ```latex
  I'll give you an argument for this, but it should not be a surprise. Well, I'll say it in words and I'll write it down clear, because we can divide this \inlinemetanote{points at $\faktor{G}{P}$} in terms of the orbits, right? And the orbits always have orders that are divisible by (i.e., that divide) the order of $H$. That's by the Orbit--Stabilizer Theorem.
  ```
