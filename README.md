# Velmara

![make.fun](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539.svg)
![rank](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/JohnyKucel/velmara-poster/rank.svg)
![reward](https://make.fun/badge/the-poster-for-a-place-that-i-2-20261121-0539/JohnyKucel/velmara-poster/reward.svg)

A travel poster for Velmara, a lantern-lagoon island that does not exist.
At dusk, paper lanterns drift across the lagoon beneath the Lantern Spire,
a slender tower crowned by one giant lantern. A stone bridge arcs from the
islet to the shore, and a small boat carries one figure holding a lantern
toward the light.

Built for the make.fun bounty
[The Poster for a Place That Isn't There](https://make.fun/bounty/the-poster-for-a-place-that-i-2-20261121-0539).

## Run it

```sh
python3 main.py
```

This writes `out/entry.png` (1024x1024 PNG). The program uses only the
Python standard library and runs with no network. The poster pixels live
compressed in `assets/poster.rgb.z`; `main.py` decompresses them and encodes
a PNG. Running it twice produces byte-identical output.

Referral: jy3a6hm3
