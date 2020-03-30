## Setup

1. Launch docker environment
```
sh launch_docker.sh
```
2. Install custom gym environment
```
cd sph
# use the forked version with compat fixes
git clone https://github.com/ivallesp/gym-inventory.git
. /app/bin/activate
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
- Cost associated with purchasing A[t] items = K(if A[t] > 0) + c*A[t]
- Cost of holding inventory of size x = h * x
- Value of selling z units = p * z
- Note: p > h in order for there to be incentive to order new items
- M = maximum inventory size

Problem Setup:
- State: X[t], t >=0: the inventory size in evening of day t
- Action: A[t], t >=0: the number of items ordered in evening of day t
- Next state: X[t+1] = min(X[t] + A[t], M - D[t+1])
- Revenue on day t+1: R[t+1] = sale_value - (fixed_purchase_cost +  variable_purchase_cost + holding_cost)
  - sale_value = p*min(X[t]+A[t], M-X[t+1])
  - fixed_purchase_cost = K(if A[t] > 0)
  - variable_purchase_cost = c*min(X[t]+A[t], M-X[t])
  - holding_cost = h*X[t]
- (X[t+1], R[t+1]) is a function of (X[t], A[t], D[t+1])

## Trading Environment

Environment: https://github.com/AminHP/gym-anytrading/blob/master/gym_anytrading/envs/trading_env.py
