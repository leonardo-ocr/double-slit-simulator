# Double Slit Simulator
Simulador feito em Python do Experimento da Dupla Fenda


Este projeto em Python utiliza Pygame para simular o famoso experimento da dupla fenda com fótons, revelando o padrão de interferência com alta fidelidade à distribuição real observada em experimentos físicos.
Fótons são emitidos em direção a uma barreira com duas fendas. Ao atingir uma tela de detecção, seus impactos seguem a distribuição probabilística da interferência quântica, acumulando-se gradualmente para formar franjas claras e escuras — o padrão de interferência.

A distribuição de probabilidade usada para simular os impactos é dada por:

I(y) ∝ cos²(π·d·y / (λ·L)) · sinc²(π·a·y / (λ·L))

Onde:
I(y) é a intensidade na posição y da tela, medida em W/m²

d é a distância entre as fendas, medida em metros(m)

a é a largura de cada fenda, medida em metros(m)

λ é o comprimento de onda, medido em metros(m)

L é a distância entre a barreira e a tela, medido em metros(m)

y é a posição vertical do impacto na tela, medido em metros(m).

Na simulação, usamos unidades arbitrárias, onde 1 pixel ≈ 1 unidade de comprimento. Isso permite visualizar o padrão sem se prender a uma escala física real, mas a equação e o comportamento seguem fielmente a física envolvida.


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This project in Python uses Pygame to simulate the famous double-slit experiment with photons, revealing the interference pattern with high fidelity to the real distribution observed in physical experiments. Photons are emitted toward a barrier with two slits. When they hit a detection screen, their impacts follow the probabilistic distribution of quantum interference, gradually accumulating to form light and dark fringes — the interference pattern.

The probability distribution used to simulate the impacts is given by:

I(y) ∝ cos²(π·d·y / (λ·L)) · sinc²(π·a·y / (λ·L))

Where:
I(y) is the intensity at the position y on the screen, measured in W/m²

d is the distance between the slits, measured in meters (m)

a is the width of each slit, measured in meters (m)

λ is the wavelength, measured in meters (m)

L is the distance between the barrier and the screen, measured in meters (m)

y is the vertical position of the impact on the screen, measured in meters (m).

In the simulation, we use arbitrary units, where 1 pixel ≈ 1 unit of length. This allows visualizing the pattern without focusing on a real physical scale, but the equation and behavior closely follow the involved physics.

