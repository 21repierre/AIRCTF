# La colline

## Description


Un de vos collegues vous explique qu'il bloque sur un code depuis le debut de semaine: «<br>
\- Nous avons intercepté cette communication sur *passioncollines.fr* mais je n'arrive toujours pas a comprendre comment la déchiffrer. 
Voici la transcription de la communication: »<br>

> ~h1ll045> Bravo~ *(supprimé)*
> h1ll045> l{3R0nh0 ThCZ0A7KArR,6gvm-cUikwbhXNfwb64Kb d

« - Nous avons quand meme réussi a récupérer le programme qu'il a utilisé, le voici: »

- Resources: [colline.sage](colline.sage)
- Difficulté: moyen/facile

## Fonctionnement

- Code source: oui
- Tourne en local (sans la clé ni le message original)
- Key: [[0, 48],[66, 70]]
- Message: `Bravo, le flag est AIRCTF{kN0Wn_pla1n_T3xt}`
- Encrypted: `l{3R0nh0 ThCZ0A7KArR,6gvm-cUikwbhXNfwb64Kb d`

## Writeup

On connait le debut du texte chiffre, ce qui nous permet de nous rammener a 2 systemes de 2 equations a 2 inconnnues pour retrouver la cle.

$$
\begin{align}
\begin{cases}
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
m_0 \\
m_1
\end{pmatrix} =
\begin{pmatrix}
e_0 \\
e_1
\end{pmatrix}
\end{cases}
& \iff
\begin{cases}
a * m_0 + b * m_1 = e_0 \\
c * m_0 + d * m_1 = e_1
\end{cases}\, \\
\end{align} \\
$$

Et

$$
\begin{align}
\begin{cases}
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix}
\begin{pmatrix}
m_2 \\
m_3
\end{pmatrix} =
\begin{pmatrix}
e_2 \\
e_3
\end{pmatrix}
\end{cases}
& \iff
\begin{cases}
a * m_2 + b * m_3 = e_2 \\
c * m_2 + d * m_3 = e_3
\end{cases}\, \\
\end{align} \\
$$

Ce qui nous donne:

$$
\begin{align}
& 
\begin{cases}
a * m_0 + b * m_1 = e_0 \\
a * m_2 + b * m_3 = e_2
\end{cases}\, \\
& 
\begin{cases}
c * m_0 + d * m_1 = e_1 \\
c * m_2 + d * m_3 = e_3
\end{cases}\, \\
\end{align} \\
$$

Qui peut se resoudre dans sage (tout est modulo 71) pour retrouver $a, b, c, d$
Voir [solve.sage](solve.sage).