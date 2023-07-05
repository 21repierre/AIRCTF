# Le Quad

## Description

- Code source: oui
- Tourne en local
- Difficulté: simple

## Solve

On doit fournir 8 nombres: $a_i, i \in \{0,...,7\}$
Le script vérifie alors que pour $i \in \{0,2,4,6\}$:

$$
\DeclareMathOperator{\tr}{tr}
\begin{align}
    & \begin{cases}
        \begin{vmatrix}
        a_i & 0 \\
        0 & a_{i+1} \\
        \end{vmatrix} & =u_i \\
        \tr{
        \begin{pmatrix}
        a_i & 0 \\
        0 & a_{i+1} \\
        \end{pmatrix}
        } & =v_i \\
        a_i > a_{i+1}
    \end{cases} \\
    \Leftrightarrow 
    & \begin{cases}
        a_i a_{i+1} & = u_i \\
        a_i + a_{i+1} & = v_i \\
        a_i > a_{i+1}
    \end{cases}
\end{align}
$$

Ce qui revient à résoudre l'équation **quad**ratique suivante: $x^2 - v_i x + u_i = 0$.