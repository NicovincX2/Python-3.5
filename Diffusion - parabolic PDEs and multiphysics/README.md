# Diffusion - parabolic PDEs and multiphysics

#### Liens à consulter:

>> - [Diffusion](https://en.wikipedia.org/wiki/Diffusion)
>> - [Diffusion equation](https://en.wikipedia.org/wiki/Diffusion_equation)

>> - [Parabolic partial differential equation](https://en.wikipedia.org/wiki/Parabolic_partial_differential_equation)

>> - [Discretization](https://en.wikipedia.org/wiki/Discretization)

#### Time-explicit diffusion on a cell-centered grid: 

>> *diffexplicit.py*
     
#### Backward-difference (implicit) diffusion: 

>> *diffimplicit.py*

#### Crank-Nicolson differenced diffusion (direct solve): 

>> *diffCNimplicit.py*

#### Multigrid solution of diffusion (C-N discretization): 

>> *diffMG.py*

>> - [Crank–Nicolson method](https://en.wikipedia.org/wiki/Crank%E2%80%93Nicolson_method)
>> - [Méthode de Crank-Nicolson](https://fr.wikipedia.org/wiki/M%C3%A9thode_de_Crank-Nicolson)

#### Diffusion-reaction equation, using Strang-splitting (this can be thought of as a model for a flame): 

>> *diffreact.py*

>> - [Strang splitting](https://en.wikipedia.org/wiki/Strang_splitting)

#### Viscous burgers equation (2nd-order piecewise linear f-v method for advection + 2nd-order implicit method for diffusion): 

>> *burgervisc.py*