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
https://github.com/paulhendricks/gym-inventory/blob/master/gym_inventory/envs/inventory_env.py

## Trading Environment
https://github.com/AminHP/gym-anytrading/blob/master/gym_anytrading/envs/trading_env.py
