## Setup

1. Launch docker environment
```
sh launch_docker.sh
```
2. Install custom gym environment
```
cd /code/pi-rl/sph
git clone https://github.com/paulhendricks/gym-inventory.git
pip3 install -e gym-inventory
```
3. Run script
```
python3 inventory.py
```

## Sparse Predictive Hierarchies
https://github.com/ogmacorp/OgmaNeo2/blob/master/SPH_Presentation.pdf

## PyOgmaNeo2 CartPole Example
https://github.com/ogmacorp/PyOgmaNeo2/blob/master/examples/CartPole.py

## Inventory Control Environment

Example 1.1 in [Algorithms for Reinforcement Learning by Csaba Szepesvari (2010)](https://sites.ualberta.ca/~szepesva/RLBook.html)

Environment: https://github.com/paulhendricks/gym-inventory/blob/master/gym_inventory/envs/inventory_env.py

### Summary

1. Evening: Inventory manager decides the quantity to be ordered for the next day.
2. Morning: Inventory is filled up with the ordered quantity.
3. During the day: Stochastic demand.

Goal: Maximise expected total future income.

Payoff at time step t:
- Cost associated with purchasing $A_t$ items = $K + c*A_t$
- Cost of holding inventory of size $x = h * x$
- Value of selling z units = $p * z$
- $p > h$ in order for there to be incentive to order new items

Problem Setup:
- State: $X_t$, t >=0: the inventory size in evening of day t
- Action: $A_t$, t >=0: the number of items ordered in evening of day t
- $M$: maximum inventory size
- Next State: $X_{t+1} = min(X_t + A_t, M - D_{t+1})$
- Revenue on day t+1: $R_{t+1} = -K - c min(

## Trading Environment

Environment: https://github.com/AminHP/gym-anytrading/blob/master/gym_anytrading/envs/trading_env.py
