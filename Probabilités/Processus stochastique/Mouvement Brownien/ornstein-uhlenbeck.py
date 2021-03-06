# -*- coding: utf-8 -*-

import os
import parameters


def ornstein_uhlenbeck_levels(param):
    """
    This method returns the rate levels of a mean-reverting ornstein uhlenbeck process.
    :param param: the model parameters object
    :return: the interest rate levels for the Ornstein Uhlenbeck process
    """
    ou_levels = [param.all_r0]
    brownian_motion_returns = brownian_motion_log_returns(param)
    for i in range(1, param.all_time):
        drift = param.ou_a * (param.ou_mu - ou_levels[i - 1]) * param.all_delta
        randomness = brownian_motion_returns[i - 1]
        ou_levels.append(ou_levels[i - 1] + drift + randomness)
    return ou_levels

ou_examples = []
for i in range(paths):
    ou_examples.append(ornstein_uhlenbeck_levels(mp))
plot_stochastic_processes(ou_examples, "Ornstein Uhlenbeck")

os.system("pause")
